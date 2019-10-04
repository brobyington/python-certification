import time
import unittest
from certifications.BaseChallenge import BaseChallenge
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from certifications.BaseChallenge import BaseChallenge
from certifications.WebHelpers import WebHelpers
import requests
import json

class Challenge8(BaseChallenge):

    def test_challenge8(self):
        web_helpers = WebHelpers(self.driver)

        compart_url = "https://www.copart.com/public/lots/search"
        query_str = 'toyota camry'
        url ="https://api.cquotient.com/v3/activities/bcpk-gamestop-us/viewSearch?clientId=522f0d29-60b5-4497-a06d-5fcacd6c8503"
        data = {
            'query': "toyota camry"
        }
        # gamestop = {
        #     'searchText': 'xbox'
        # }
        #data = json.dumps({"query":{"query":['toyota camry']}})
        r = requests.post(compart_url,data)
        #r = requests.post(url,gamestop)


        info = r.text
        print(info)


    if __name__ == '__main__':
     unittest.main()