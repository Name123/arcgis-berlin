import os
import sys
import unittest
import json

from tornado.testing import AsyncHTTPTestCase

sys.path.insert(1, os.path.join(sys.path[0], '..'))
sys.path.insert(1, os.path.join(sys.path[0], '..', 'lib'))

import app
import log
import config
   

class TestApp(AsyncHTTPTestCase):
    def get_app(self):
        log.init()
        return app.make_app(config.load())

    def test_buildings_by_zip_code(self):
        response = self.fetch('/buildings/by_zip_code/')
        self.assertEqual(response.code, 200)
        js = json.loads(response.body)
        self.assertTrue('status' in js)
        self.assertEqual(js['status'], 'ok')
        self.assertTrue('result' in js)
        self.assertTrue(len(js['result']) > 0)

    def test_buildings_by_add_year(self):
        response = self.fetch('/buildings/by_year/')
        self.assertEqual(response.code, 200)
        js = json.loads(response.body)
        self.assertTrue('status' in js)
        self.assertEqual(js['status'], 'ok')
        self.assertTrue('result' in js)
        self.assertTrue(len(js['result']) > 0)

 
 
if __name__ == '__main__':
    unittest.main()
