import unittest
from certifications.BaseChallenge import BaseChallenge
from certifications.WebHelpers import WebHelpers
import requests
from bs4 import BeautifulSoup

class Challenge11(BaseChallenge):

    def test_challenge11(self):
        web_helpers = WebHelpers(self.driver)
        link_to_click = ''
        link_list = []
        page_count = 0
        count = 0
        copart_url = "https://www.copart.com"
        self.driver.get(copart_url)
        cookie = {x["name"]: x["value"] for x in self.driver.get_cookies()}
        source = requests.get(copart_url,cookies=cookie)
        source_text = source.text
        simplified = BeautifulSoup(source_text,features="lxml")
        for link in simplified.findAll('a',):
            # link_to_click = copart_url + link.get("href")
            #print(link.get('href'))
            if link.get('href') == None:
                link_to_click = ""
                #print("It is None")
            elif link.get('href').startswith("en/"):
                link_to_click = copart_url + "/" + link.get('href')
                link_list.append(link_to_click)
                #print(link_to_click)
            elif link.get('href') == "./":
                link_to_click = ""
                #print("Only ./")
            elif link.get('href').startswith("./"):
                slink = link.get('href')
                link_to_click = copart_url + slink[1:]
                link_list.append(link_to_click)
                #print(link_to_click)
            elif link.get('href').startswith("/"):
                link_to_click = copart_url + link.get('href')
                link_list.append(link_to_click)
                #print(link_to_click)
            count += 1

        final_links = web_helpers.remove_duplicates_from_list(link_list)
        for link in final_links:
            print("Going to " + link)
            self.driver.get(link)
            page_count += 1

        print("Went to " + str(page_count) + " pages!")
        #print(final_links)
        #print(count)