import unittest
from termcolor import colored
from selenium.webdriver.common.by import By
from certifications.BaseChallenge import BaseChallenge
from certifications.WebHelpers import WebHelpers

class hw3(BaseChallenge):

    def test_hw3(self):
        web_helpers = WebHelpers(self.driver)
        self.driver.get("https://www.doterra.com/US/en/product-education-blends")

        web_helpers.get_doterra_products()