import unittest, requests
from config import hash, ts, apikey

class TestApi(unittest.TestCase):
    URL = "http://localhost:5000"
    API = f"https://gateway.marvel.com/v1/public/characters?ts={ts}&apikey={apikey}&hash={hash}&limit=100"
    
    def test_1_host(self):
        resp = requests.get(self.URL)
        self.assertEqual(resp.status_code, 200)
        print('Test 1 completed')

    def test_2_get_all(self):
        resp = requests.get(self.API)
        self.assertEqual(resp.status_code, 200)
        print('Test 2 completed')    

if __name__ == '__main__':
    tester = TestApi()
    tester.test_1_host()
    tester.test_2_get_all()