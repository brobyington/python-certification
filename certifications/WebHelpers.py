import unittest
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from certifications.BaseChallenge import BaseChallenge


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
        damage_list = []
        count = 1
        total = 0
        rear_end = "REAR END"
        front_end = "FRONT END"
        minor_dent = "MINOR DENT/SCRATCHES"
        undercarriage = "UNDERCARRIAGE"
        misc = 0
        rear_count = 0
        front_count = 0
        minor_count = 0
        under_count = 0

        for type in self.driver.find_elements_by_xpath("//tbody/tr/td[12]"):
            damage_type = type.find_element_by_xpath("//tbody/tr[" + str(count) + "]//span[@data-uname='lotsearchLotdamagedescription']").text
            count += 1
            damage_list.append(damage_type)

        #print(damage_list)
        for damage in damage_list:
            if damage == rear_end:
                rear_count += 1
                total += 1
            elif damage == front_end:
                front_count += 1
                total += 1
            elif damage == minor_dent:
                minor_count += 1
                total += 1
            elif damage == undercarriage:
                under_count += 1
                total += 1
            else:
                misc += 1
                total += 1

        print("\n" + rear_end + ": " + str(rear_count) + "\n" + front_end + ": " + str(front_count) + "\n" +
              minor_dent + ": " + str(minor_count) + "\n" + undercarriage + ": " + str(rear_count) + "\n" +
                "MISC : " + str(misc))

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
