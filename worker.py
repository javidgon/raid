import requests
import sys


class Worker(object):

    def __call__(self, worker, url, requests_number):
        self.make_request(worker, url, requests_number)

    def make_request(self, worker, url, requests_number):
        """
        It's the worker's job, make requests. It makes the
        requests sequentially.
        """
        for i in range(1, int(requests_number) + 1):
            print ('[Worker %s - %s time] Making the request to %s'
                   % (worker, i, url))
            try:
                result = requests.get(url)
            except requests.exceptions.ConnectionError as e:
                print '[Worker %s - %s time] Got %s!' % (worker, i, e)
                sys.exit(1)
            print ('[Worker %s - %s time] Request finalized with status %s'
                   % (worker, i, result.status_code))
        sys.exit(1)

if __name__ == '__main__':
    worker = Worker()
    worker(sys.argv[1], sys.argv[2], sys.argv[3])
