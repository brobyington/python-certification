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

class hw1(BaseChallenge):

    def test_hw1(self):
        web_helpers = WebHelpers(self.driver)
        self.driver.get("https://www.doterra.com/US/en/using-essential-oils")
        self.assertIn("Essential", self.driver.title)

        product_and_name = web_helpers.top_ten_items()
        #print(product_and_name)
        name = "//h1"
        for page in product_and_name:
            click_product = "//ol[1]/li/a[contains(text(),'"+ page[0] + "')]"
            self.driver.find_element(By.XPATH, click_product).click()
            try:

                self.assertIn(page[1],self.driver.find_element_by_xpath(name).text,"Didn't navigate to"" page!")
            except:
                print("Didn't navigate to "+page[1]+" page!")
            self.driver.back()








    if __name__ == '__main__':
     unittest.main()
