import unittest
from selenium import webdriver
from certifications.BaseChallenge import BaseChallenge

class Challenge1(BaseChallenge):

    def test_challenge1(self):
        self.driver.get("https://www.google.com")
        self.assertIn("Google", self.driver.title)

    if __name__ == '__main__':
     unittest.main()