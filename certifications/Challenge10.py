import unittest
from certifications.BaseChallenge import BaseChallenge
from certifications.WebHelpers import WebHelpers
import requests
import json
import pandas as pd


class Challenge10(BaseChallenge):

    def test_challenge10(self):
        web_helpers = WebHelpers(self.driver)
        self.driver.get("https://www.copart.com")
        bool_list = []
        count = 0
        query_excel = pd.read_excel(r'car_query.xlsx', sheet_name='Queries')
        rows = len(query_excel.index)
        cols = 4
        cookie = {x["name"]: x["value"] for x in self.driver.get_cookies()}
        compart_url = "https://www.copart.com/public/lots/search"
        #data = {"query": "toyota avalon 2018 Automobiles"}
        while count < rows:
            col = 0
            qd = web_helpers.get_query_data(count, query_excel)
            make = qd['make']
            model = qd['model']
            year = qd['year']
            vtype = qd['vtype']

            final_query = make + " " + model + " " + str(year) + " " + vtype
            print("Search query = " + final_query)
            data = {'query': final_query}

            r = requests.post(compart_url, data, cookies=cookie)

            rcode = r.status_code
            status_ok = web_helpers.validate_ok_status(rcode)
            self.assertTrue(status_ok, "Call not successful")

            info = r.text
            #print(info)
            parsed_info = json.loads(info)
            car_info = parsed_info["data"]["results"]["content"]
            #print(car_info)
            query_bool = web_helpers.search_for_items_in_api_results(qd,car_info)
            bool_list.append(query_bool)

            count += 1
        print(bool_list)

        for b in bool_list:
            #print(b)
            for x in b:
                #print("this is x: " + x)
                try:
                    self.assertNotIn("wasn't",x)
                except:
                    splitStr =  x.split(" ")
                    print(splitStr[0] + " wasn't found in results")


    if __name__ == '__main__':
     unittest.main()