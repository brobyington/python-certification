import unittest
from selenium import webdriver
from certifications.BaseChallenge import BaseChallenge


class Challenge3(BaseChallenge):

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