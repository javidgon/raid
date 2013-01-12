#! python

import subprocess
import urlparse
import sys
import os

from optparse import OptionParser
import utils


class Raid(object):
    """
    Raid, in some few words, is a HTTP's requests generator.
    It's pretty handy for testing high loads in development
    environments.
    
    Settings currently supported:
    
    -u, --url: Requests' target (Default: http://127.0.0.1:8000)
    -w, --workers: Number of workers in parallel (Default: 1)
    -r, --requests: Number of requests per worker (Default: 1)

    """

    def __call__(self, url, concurrency, requests_number):
        self.controller(url, concurrency, requests_number)

    def controller(self, url, concurrency, requests_number):
        """
        Create workers and verify whether the other methods do their
        job properly.

        :param url: Requests' target.
        :param concurrency: Number of workers in parallel. Define Concurrency.
        :param requests_number: Number of requests per worker. Define
                                sequentiality.
        """
        if self.validate_url(url):
            self.create_workers(url=url, concurrency=concurrency,
                               requests_number=requests_number)
        else:
            print "[Controller] Invalid URL"
            sys.exit(1)

    def create_workers(self, url, concurrency, requests_number):
        """
        Create workers and, therefore, concurrency. Exit when all the
        workers are done.
        
        :param url: Requests' target.
        :param concurrency: Number of workers in parallel. Define Concurrency.
        :param requests_number: Number of requests per worker. Define
                                sequentiality.
        """
        worker = 1
        workers = []
        while worker <= concurrency:
            workers.append(subprocess.Popen('python %s %s %s %s' %
                           (utils.get_file('worker.py'), worker, url, requests_number),
                            shell=True))
            worker += 1

        while True:
            if all([x.poll() for x in workers]):
                print "[Controller] Switching off workers..."
                sys.exit(1)

    def validate_url(self, url):
        """
        Simply validate the URL.
        
        :param url: Requests' target.
        """
        parts = urlparse.urlparse(url)
        return parts.scheme in ('http', 'https')


if __name__ == '__main__':
    parser = OptionParser()
    parser.add_option("-u", "--url", action="store", type="string",
                      default="http://127.0.0.1:8000",
                      help="Requests' target", dest="url")
    parser.add_option("-w", "--workers", action="store", type="int",
                      default=1, help="Number of workers in parallel", dest="workers")
    parser.add_option("-r", "--requests", action="store", type="int",
                      default=1, help="Number of requests per worker",
                      dest="requests_number")
    parser.add_option("-t", "--tests", action="store", type="string",
                      default=1, help="Trigger Test Suite",
                      dest="test_mode")

    (options, args) = parser.parse_args()
    if len(sys.argv) > 1:
        if sys.argv[1] == 'tests':
            print "Running tests..."
            os.system('python %s' %
                     (utils.get_file('run_tests.py')))
            sys.exit()

    raid = Raid()
    raid(options.url, options.workers, options.requests_number)
