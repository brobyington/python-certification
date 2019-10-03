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

class Challenge5(BaseChallenge):

    def test_challenge5(self):
        web_helpers = WebHelpers(self.driver)
        hundred = 100
        self.driver.get("https://www.copart.com")
        self.assertIn("Auto Auction", self.driver.title)

        search_button = "//*[@id='input-search']"
        self.driver.find_element(By.XPATH,search_button).click()
        self.driver.find_element(By.XPATH,search_button).send_keys("porsche" + Keys.ENTER)

        first_row = '//table[@id="serverSideDataTable"]//tbody/tr[1]'
        web_helpers.wait_for_object_to_load(first_row)

        hundred_option = "//div[@class='top']//option[text()='100']"
        self.driver.find_element(By.XPATH, hundred_option).click()

        load = "//div[@class='top']/following-sibling::div[@style='display: none;']"
        web_helpers.wait_for_object_to_load(load)

        number_of_entries = self.driver.find_element_by_xpath("//div[@class='top']//div[contains(text(),'Showing')]").text
        self.assertIn("100",number_of_entries,"Number of entries didn't change!")

        clist = web_helpers.get_models()
        small_list = web_helpers.remove_duplicates_from_list(clist)
        model_total =  web_helpers.count_each_member_in_list(clist,small_list)

        self.assertEqual(model_total, hundred, "Didn't count all models!")

        damage_total = web_helpers.count_damage_types()

        self.assertEqual(damage_total,hundred,"Didn't count all damages!")


    if __name__ == '__main__':
     unittest.main()