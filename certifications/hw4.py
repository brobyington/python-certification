import time
import unittest
from termcolor import colored
from selenium.webdriver.common.by import By
from certifications.BaseChallenge import BaseChallenge
from certifications.WebHelpers import WebHelpers

class hw4(BaseChallenge):

    def test_hw4(self):
        web_helpers = WebHelpers(self.driver)
        cart = {}
        self.driver.get("https://www.youniqueproducts.com/products/view/US-51081-01")

        add_to_cart = "//button[text()='Add to cart']"
        self.driver.find_element_by_xpath(add_to_cart).click()
        time.sleep(1)
        checkout = "//span[@id='cartItems']"
        self.driver.find_element_by_xpath(checkout).click()
        time.sleep(4)
        cart_items = "//tr[@class='totals groupRow']"
        i = 1

        for c in self.driver.find_elements_by_xpath(cart_items):
            key = self.driver.find_element_by_xpath("(//td[contains(@class,'totalLbls')])[" + str(i) +"]").text
            value = self.driver.find_element_by_xpath("(//td[contains(@class,'totalDisplay')])[" + str(i) + "]").text
            if len(key) > 1:
                cart[key] = value
            i += 1


        print(cart)