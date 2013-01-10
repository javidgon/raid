import subprocess
import urlparse
import sys

from optparse import OptionParser


class Raid(object):

    def __call__(self, url, concurrency, requests_number):
        self.controller(url, concurrency, requests_number)

    def controller(self, url, concurrency, requests_number):
        if self.validate_url(url):
            self.create_worker(url=url, concurrency=concurrency,
                               requests_number=requests_number)
        else:
            print "[Controller] Invalid URL"
            sys.exit(1)

    def create_worker(self, url, concurrency, requests_number):
        worker = 1
        workers = []
        while worker <= concurrency:
            workers.append(subprocess.Popen('python worker.py %s %s %s' %
                           (worker, url, requests_number),
                           shell=True))
            worker += 1

        while True:
            if all([x.poll() for x in workers]):
                print "[Controller] Switching off workers..."
                sys.exit(1)

    def validate_url(self, url):
        parts = urlparse.urlparse(url)
        return parts.scheme in ('http', 'https')


if __name__ == '__main__':
    parser = OptionParser()
    parser.add_option("-u", "--url", action="store", type="string",
                      default="http://127.0.0.1:8000",
                      help="Requests' target", dest="url")
    parser.add_option("-w", "--workers", action="store", type="int",
                      default=1, help="Number of workers", dest="workers")
    parser.add_option("-r", "--requests", action="store", type="int",
                      default=1, help="Number of requests per worker",
                      dest="requests_number")
    (options, args) = parser.parse_args()

    raid = Raid()
    raid(options.url, options.workers, options.requests_number)
