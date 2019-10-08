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
        ok = '2'
        self.driver.get("https://www.copart.com")
        cookie = {}
        # for x in self.driver.get_cookies():
        #     cookie[x["name"]]= x["value"]
        cookie = {x["name"]: x["value"] for x in self.driver.get_cookies()}

        compart_url = "https://www.copart.com/public/lots/search"
        my_fav_cars = ["toyota camry", "nissan skyline", "lexus is 350", "audi r8", "lotus elise",
                       "lamborghini murcielago", "mitsubishi eclipse spyder", "mitsubishi lancer evolution",
                       "dodge viper", "bugatti veyron"]
        file = open("Log.txt", "a")

        for car in my_fav_cars:
            data = {"query": car}
            r = requests.post(compart_url,data,cookies=cookie)
            rcode = r.status_code
            str_rcode = str(rcode)
            self.assertEqual(ok,str_rcode[0],"Not successful")
            info = r.text
            print("Car: " + car + "\n" + info, file=file)
            parsed_info = json.loads(info)
            #print(json.dumps(parsed_info,indent=4))
            car_count = parsed_info["data"]["results"]["totalElements"]
            print(car + ": " + str(car_count))

        file.close()



    if __name__ == '__main__':
     unittest.main()