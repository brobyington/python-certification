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

class Challenge6(BaseChallenge):

    def test_challenge6(self):
        web_helpers = WebHelpers(self.driver)
        hundred = 100
        search = 'nissan'
        self.driver.get("https://www.copart.com")
        self.assertIn("Auto Auction", self.driver.title)

        web_helpers.search_copart(search)

        first_row = '//table[@id="serverSideDataTable"]//tbody/tr[1]'
        web_helpers.wait_for_object_to_load(first_row)

        model_button = "//a[text()='Model']"
        self.driver.find_element_by_xpath(model_button).click()
        model_search = "//a[text()='Model']/parent::h4/parent::li//input[@type='text']"
        self.driver.find_element(By.XPATH, model_search).click()
        self.driver.find_element(By.XPATH, model_search).send_keys("skyline" + Keys.ENTER)

        try:
            skyline_model = "(//a[text()='Model']/parent::h4/parent::li//div[@class='checkbox']//input[@type='checkbox'])[1]"
            self.driver.find_element_by_xpath(skyline_model)
        except:
            not_found = False
            self.driver.save_screenshot("no_skyline.png")
            self.assertTrue(not_found,"Skyline wasn't found!")



    if __name__ == '__main__':
     unittest.main()