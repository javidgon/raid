
import requests
import sys


class Worker(object):

    def __call__(self, worker_id, url, requests_number):
        self.make_request(worker_id, url, requests_number)

    def make_request(self, worker_id, url, requests_number):
        """
        It's the worker's job, make requests. It makes the
        requests sequentially.
        
        :param worker_id: Worker's id.
        :param url: Requests' target.
        :param requests_number: Number of requests per worker. Define
                                sequentiality.
        """
        for i in range(1, int(requests_number) + 1):
            print ('[Worker %s - %s time] Making the request to %s'
                   % (worker_id, i, url))
            try:
                result = requests.get(url)
            except requests.exceptions.ConnectionError as e:
                print '[Worker %s - %s time] Got %s!' % (worker_id, i, e)
                sys.exit(1)
            print ('[Worker %s - %s time] Request finalized with status %s'
                   % (worker_id, i, result.status_code))
        sys.exit(1)

if __name__ == '__main__':
    worker = Worker()
    worker(sys.argv[1], sys.argv[2], sys.argv[3])
