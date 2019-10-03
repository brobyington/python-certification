import unittest
from selenium import webdriver
from certifications.Helpers import Helpers

class BaseChallenge(unittest.TestCase):

    def setUp(self):
        #code to startup webdriver
        self.driver = webdriver.Chrome("../chromedriver.exe")

    def tearDown(self):
        #code to close webdriver
        self.driver.close()