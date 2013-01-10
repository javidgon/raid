import requests
import sys

def make_request(worker, url, requests_number):
    for i in range(1, int(requests_number) + 1):
        print '[Worker %s - %s time] Making the request to %s' % (worker, i, url)
        try:
            result = requests.get(url)
        except requests.exceptions.ConnectionError as e:
            print '[Worker %s - %s time] Got %s!' % (worker, i, e)
            sys.exit(1)
        print '[Worker %s - %s time] Request finalized with status %s' % (worker, i, result.status_code)
    sys.exit(1)
        
if __name__ == '__main__':
    make_request(sys.argv[1], sys.argv[2], sys.argv[3])
