import unittest
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from certifications.BaseChallenge import BaseChallenge

class Challenge2(BaseChallenge):

    def test_challenge2(self):
        self.driver.get("https://www.copart.com")
        self.assertIn("Auto Auction", self.driver.title)

        search_button = "//*[@id='input-search']"
        self.driver.find_element(By.XPATH,search_button).click()
        self.driver.find_element(By.XPATH,search_button).send_keys("Exotic" + Keys.ENTER)

        first_row = '//table[@id="serverSideDataTable"]//tbody/tr[1]'
        wait = 5
        try:
            myElem = WebDriverWait(self.driver, wait).until(EC.presence_of_element_located((By.XPATH, first_row)))

        except TimeoutException:
            print ("Loading took too much time!")

        car = "PORSCHE"
        self.assertTrue(car in self.driver.page_source,"The car wasn't found on the page")

    if __name__ == '__main__':
     unittest.main()