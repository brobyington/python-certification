import time
import unittest
from termcolor import colored
from selenium.webdriver.common.by import By
from certifications.BaseChallenge import BaseChallenge
from certifications.WebHelpers import WebHelpers

class hw2(BaseChallenge):

    def test_hw2(self):
        web_helpers = WebHelpers(self.driver)
        self.driver.get("https://www.doterra.com/US/en/")
        self.assertIn("Essential", self.driver.title)

        footer = web_helpers.get_doterra_footer_links()
        #print(footer)

        for page in footer:
            click_link = "//div[@class='footer__links__group']//a[text()='"+ page[0] + "']"
            self.driver.find_element(By.XPATH, click_link).click()
            try:
                self.assertTrue("page-notFound" in self.driver.page_source)
                print(colored("The page " + page[0] + " didn't load correctly!","red"))
            except:
                print(colored(page[0] + " loaded correctly!","green"))
            self.driver.get("https://www.doterra.com/US/en/")

    if __name__ == '__main__':
     unittest.main()
