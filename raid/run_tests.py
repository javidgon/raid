#! python

import unittest2 as unittest
import commands

from raid import Raid
from worker import Worker


class RaidTestSuite(unittest.TestCase):
    
    def setUp(self):
        self.raid = Raid()
        self.worker = Worker()
        
    def test_invalid_url_request(self):
        url = 'nothing'
        workers = 1
        requests_number = 1
        
        output = commands.getstatusoutput('python raid.py -u %s -w %s -r %s' % (url, workers, requests_number))
        self.assertIn('Invalid URL', output[1])
        
    def test_connection_refused_request(self):
        url = 'http://127.0.0.1:8906'
        workers = 1
        requests_number = 1
        
        output = commands.getstatusoutput('python raid.py -u %s -w %s -r %s' % (url, workers, requests_number))
        self.assertIn('Connection refused', output[1])
        
    def test_successful_request(self):
        url = 'http://www.nostravia.com'
        workers = 1
        requests_number = 1
        
        output = commands.getstatusoutput('python raid.py -u %s -w %s -r %s' % (url, workers, requests_number))
        self.assertIn('Request finalized with status 200', output[1])  


if __name__=='__main__':
    unittest.main()