import unittest
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from certifications.BaseChallenge import BaseChallenge
import pandas as pd
import math as math

class WebHelpers:

    def __init__(self, driver):
        self.driver = driver

    def wait_for_object_to_load(self,xpath):
        load = xpath
        wait = 5
        try:
            myElem = WebDriverWait(self.driver, wait).until(EC.presence_of_element_located((By.XPATH, load)))

        except TimeoutException:
            print ("Loading took too much time!")

    def get_models(self):
        model_list = []
        count = 1
        for car in self.driver.find_elements_by_xpath("//tbody/tr/td[6]"):
            car_model = car.find_element_by_xpath("//tbody/tr[" + str(count) + "]//span[@data-uname='lotsearchLotmodel']").text
            count += 1
            model_list.append(car_model)

        #print(model_list)
        return model_list

    def remove_duplicates_from_list(self,clist):
        list_with_no_dups = list(set(clist))
        #print(list_with_no_dups)
        return list_with_no_dups

    def count_each_member_in_list(self,clist,slist):
        model_count = 0
        total = 0
        for car in slist:
            model_count = clist.count(car)
            total = model_count + total
            print(car + " appears " + str(model_count) + " times!")
        return total


    def count_damage_types(self):
        count = 1
        damage_list = {
            "REAR END": 0,
            "FRONT END": 0,
            "MINOR DENT/SCRATCHES": 0,
            "UNDERCARRIAGE": 0,
            "MISC": 0
        }

        for type in self.driver.find_elements_by_xpath("//tbody/tr/td[12]"):
            damage_type = type.find_element_by_xpath("//tbody/tr[" + str(count) + "]//span[@data-uname='lotsearchLotdamagedescription']").text
            count += 1
            if damage_type not in damage_list:
                damage_list["MISC"] += 1
            else:
                damage_list[damage_type] = damage_list.get(damage_type) + 1
        print(damage_list)

        total = sum(damage_list.values())
        return total

    def makes_and_models(self):
        web_helpers = WebHelpers(self.driver)
        count = 1
        model_list = []
        url_list = []

        for item in self.driver.find_elements_by_xpath('//li[@ng-repeat]'):
            car_model = item.find_element_by_xpath(
                "//*[@id='tabTrending']/descendant-or-self::a[@href][" + str(count) + "]").text
            model_list.append(car_model)
            car_url = item.find_element_by_xpath(
                "//*[@id='tabTrending']/descendant-or-self::a[@href][" + str(count) + "]").get_attribute("href")
            url_list.append(car_url)

            #print(str(count) + " " + car_modal + " - " + str(car_url))
            count += 1

        model_and_url =  web_helpers.merge_list(model_list,url_list)
        return model_and_url

    def merge_list(self,l1,l2):
        merged_list = [(l1[i],l2[i])for i in range(0,len(l1))]
        return merged_list

    def verify_link_is_correct(self,mlist):
        for page in mlist:
            self.driver.find_element(By.XPATH, page[0]).click()

    def top_ten_items(self):
        web_helpers = WebHelpers(self.driver)
        count = 1
        product_list = []
        name_list = []

        for item in self.driver.find_elements_by_xpath('//ol[1]/li'):
            product = item.find_element_by_xpath(
                "//ol[1]/li[" + str(count) + "]").text
            product_list.append(product)
            product_name = product.split(" ")
            name_list.append(product_name[0])

            #print(str(count) + " " + car_modal + " - " + str(car_url))
            count += 1

        product_and_name =  web_helpers.merge_list(product_list,name_list)
        return product_and_name

    def validate_ok_status(self,rcode):
        ok = '2'
        str_rcode = str(rcode)
        if ok == str_rcode[0]:
            return True
        else:
            return False

    def get_query_data(self,count,qdata):
        web_helpers = WebHelpers(self.driver)
        row =  count
        df = pd.DataFrame(qdata,index=[row])
        make = df.loc[row,'make']
        model = df.loc[row,'model']
        year = df.loc[row,'year']
        vtype = df.loc[row,'Vehicle type']

        query = {
            'make': make,
            'model': model,
            'year': year,
            'vtype': vtype
        }
        final_query = web_helpers.verify_if_item_is_nan(query)
        return final_query

    def verify_if_item_is_nan(self,nlist):
        for k,v in nlist.items():
            if type(v) == str:
                nlist[k] = v
            elif math.isnan(v):
                nlist[k] = ''
            else:
                nlist[k] = int(v)

        return nlist

    def search_for_items_in_api_results(self,qdict,res):
        count = 0
        real_final = []
        num_of_dicts = len(list(res))
        # print(num_of_dicts)
        while count < num_of_dicts:
            rdict = list(res)[count]
            final_bool_list = []
            for v in qdict.values():
                bool_list = []
                if v == '':
                    bool_list.append('')
                    continue
                # print(v)
                for t in rdict.values():
                    if str(t).lower() in str(v):
                        bool_list.append(True)
                    else:
                        bool_list.append(False)

                if any(bool_list):
                    final_bool_list.append(True)
                    # print(bool_list)
                else:
                    final_bool_list.append(False)
                    # print(bool_list)
            if not any(final_bool_list):
                real_final.append(True)
                # print(final_bool_list)
            else:
                real_final.append(False)
                # print(final_bool_list)
            count += 1
        finL = []
        bool_count = 0

        for v in qdict.values():
            if v == '':
                continue
            if final_bool_list[bool_count] == True:
                val = "" + str(v) + " was found!"
                finL.append(val)
                bool_count += 1
            else:
                val = "" + str(v) + " wasn't found!"
                finL.append(val)
                bool_count += 1

        #print(finL)
        return finL

    def search_copart(self,search):
        search_button = "//*[@id='input-search']"
        self.driver.find_element(By.XPATH, search_button).click()
        self.driver.find_element(By.XPATH, search_button).send_keys(search + Keys.ENTER)

    def get_doterra_footer_links(self):
        web_helpers = WebHelpers(self.driver)
        count = 1
        page_list = []
        url_list = []

        for item in self.driver.find_elements_by_xpath("//a[contains(@class,'footer__links__list__link')]"):
            link_page = item.find_element_by_xpath("(//div[@class='footer__links__groups']"
                                                   "//a[contains(@class,'footer__links__list__link')])"
                                                   "["+str(count)+"]").text
            page_list.append(link_page)
            page_url = item.find_element_by_xpath("(//div[@class='footer__links__groups']"
                                                   "//a[contains(@class,'footer__links__list__link')])"
                                                   "["+str(count)+"]").get_attribute("href")
            url_list.append(page_url)

            # print(str(count) + " " + car_modal + " - " + str(car_url))
            count += 1

        page_and_url = web_helpers.merge_list(page_list, url_list)
        return page_and_url

    def get_doterra_products(self):
        product_list = {
            'doTERRA' : 0,
            'DigestZen' : 0,
            'Misc' : 0
        }

        count = 1
        for item in self.driver.find_elements_by_xpath("//div[@class='grid-image']"):
            name = item.find_element_by_xpath("(//div[@class='results row']//span[@class='title'])[" + str(count) + "]").text
            count += 1

            if "doTERRA" in name:
                product_list["doTERRA"] = product_list.get("doTERRA") + 1
            elif "DigestZen" in name:
                product_list["DigestZen"] = product_list.get("DigestZen") + 1
            else:
                product_list["Misc"] += 1


        print(product_list)