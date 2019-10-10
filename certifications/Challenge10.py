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
            print(final_query)
            data = {'query': final_query}

            r = requests.post(compart_url, data, cookies=cookie)

            rcode = r.status_code
            status_ok = web_helpers.validate_ok_status(rcode)
            self.assertTrue(status_ok, "Call not successful")

            info = r.text
            #print(info)
            parsed_info = json.loads(info)
            car_info = parsed_info["data"]["results"]["content"]

            for k,v in qd.items():
                print(v)
                if v in car_info:
                    bool_list.append(True)
                    print("is true")
                else:
                    bool_list.append(False)
                #self.assertIn(v,car_info,"" + v + " not found in results")
                #self.assertIn("matrim cothin",car_info,"matt not found")
                #print("Query found!")


            count += 1
        print(bool_list)



    if __name__ == '__main__':
     unittest.main()