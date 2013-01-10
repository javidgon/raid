import subprocess
import urlparse
import sys

from optparse import OptionParser


def controller(url, concurrency, requests_number):
    if validate_url(url):
        create_worker(url=url, concurrency=concurrency,
                      requests_number=requests_number)
    
def create_worker(url, concurrency, requests_number):
    worker = 1
    workers = []
    while worker <= concurrency:
        workers.append(subprocess.Popen('python worker.py %s %s %s' %
                                        (worker, url, requests_number), shell=True))
        worker += 1
        
    while True:
        if all([x.poll() for x in workers]):
            print "Switching off workers..."
            sys.exit(1)

def validate_url(url):
    return urlparse.urlparse(url)


if __name__ == '__main__':
    parser = OptionParser()
    parser.add_option("-u", "--url", action="store", type="string",
                      default="http://127.0.0.1:8000", help="Requests' target", dest="url")
    parser.add_option("-w", "--workers", action="store", type="int",
                      default=1, help="Number of workers", dest="workers")
    parser.add_option("-r", "--requests", action="store", type="int",
                      default=1, help="Number of requests per worker", dest="requests_number")
    (options, args) = parser.parse_args()
        
    controller(options.url, options.workers, options.requests_number)