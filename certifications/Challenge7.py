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

class Challenge7(BaseChallenge):

    def test_challenge7(self):
        web_helpers = WebHelpers(self.driver)
        model_and_url = []
        self.driver.get("https://www.copart.com")
        self.assertIn("Auto Auction", self.driver.title)

        model_and_url =  web_helpers.makes_and_models()
        #print(model_and_url)

        for page in model_and_url:
            click_car = "//a[text()='" + page[0] + "']"
            self.driver.find_element(By.XPATH, click_car).click()
            self.driver.back()
            self.assertEqual(page[1],self.driver.current_url,"Didn't navigate to correct page!")
            self.driver.back()



    if __name__ == '__main__':
     unittest.main()