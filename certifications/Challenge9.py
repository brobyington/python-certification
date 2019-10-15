import unittest
from certifications.BaseChallenge import BaseChallenge
from certifications.WebHelpers import WebHelpers
import requests
import json

class Challenge9(BaseChallenge):

    def test_challenge9(self):
        web_helpers = WebHelpers(self.driver)
        count = 0
        self.driver.get("https://www.copart.com")
        cookie = {x["name"]: x["value"] for x in self.driver.get_cookies()}
        data_types = [str, int, str, str, int, str, float, float, str, float, str, str, str, str, str, str, str, str,
                      int, float, int, str, float, bool, str, str, str, str, str, str, list, str, str, int, int, bool,
                      int, bool, str, str, float, str, str, str, str, str, str, str, str, bool, bool, str, bool, bool,
                      float, str]
        bools = []

        compart_url = "https://www.copart.com/public/lots/search"
        data = {"query": "lexus is 350"}

        r = requests.post(compart_url, data, cookies=cookie)

        rcode = r.status_code
        status_ok = web_helpers.validate_ok_status(rcode)
        self.assertTrue(status_ok,"Call not successful")

        info = r.text
        parsed_info = json.loads(info)
        car_info = parsed_info["data"]["results"]["content"][1].items()

        for key, value in car_info:
            print("Key: " + key + ", Value: " + str(value) + " is a " + str(type(value).__name__))
            actual_type = type(value)

            if actual_type == data_types[count]:
                print("Types match!")
                bools.append(True)
            else:
                print("Should be " + str(data_types[count].__name__) + " not a " + str(type(value).__name__))
                bools.append(False)

            count += 1

        self.assertTrue(all(bools), "There were types that didn't match!")











    if __name__ == '__main__':
     unittest.main()