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
        self.driver.get("https://www.copart.com")
        cookie = {}
        # for x in self.driver.get_cookies():
        #     cookie[x["name"]]= x["value"]
        cookie = {x["name"]: x["value"] for x in self.driver.get_cookies()}

        compart_url = "https://www.copart.com/public/lots/search"
        my_fav_cars = []
        data = {
            "query": "toyota camry"
        }
        r = requests.post(compart_url,data,cookies=cookie)

        info = r.text
        print(info)

    if __name__ == '__main__':
     unittest.main()