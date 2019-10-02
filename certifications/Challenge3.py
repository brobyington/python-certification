import unittest
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Challenge3(unittest.TestCase):

    def setUp(self):
        #code to startup webdriver
        self.driver = webdriver.Chrome("../chromedriver.exe")

    def tearDown(self):
        #code to close webdriver
        self.driver.close()

    def test_challenge3(self):
        # code for our test steps
        self.driver.get("https://www.copart.com")
        self.assertIn("Auto Auction", self.driver.title)
        count = 1

        for item in self.driver.find_elements_by_xpath('//li[@ng-repeat]'):
            car_modal = item.find_element_by_xpath(
                "//*[@id='tabTrending']/descendant-or-self::a[@href][" + str(count) + "]").text
            car_url = item.find_element_by_xpath(
                "//*[@id='tabTrending']/descendant-or-self::a[@href][" + str(count) + "]").get_attribute("href")

            print(str(count) + " " + car_modal + " - " + str(car_url))
            count += 1


    if __name__ == '__main__':
        unittest.main()