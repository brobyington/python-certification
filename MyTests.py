import unittest
from certifications.BaseChallenge import BaseChallenge
from certifications.WebHelpers import WebHelpers
import requests
import json
import pandas as pd


class myTests(unittest.TestCase):

    def test_my_tests(self):
        count = 0
        info = {"lotNumberStr":"18881174","ln":18881174,"mkn":"TOYOTA","lm":"SCION XB","lcy":2006,
                "fv":"JTLKT324464093337","la":7901.0,"rc":11479.0,"obc":"E","orr":0.0,"ord":"EXEMPT","egn":"1.5L  4",
                "cy":"4","ld":"2006 TOYOTA SCION XB","yn":"SC - COLUMBIA","cuc":"USD","tz":"EDT","ad":1571407200000,
                "at":"10:00:00","aan":0,"hb":0.0,"ss":5,"bndc":"","bnp":0.0,"ts":"SC","stt":"ST",
                "td":"CERT OF TITLE-SALVAGE","tgc":"TITLEGROUP_S","dd":"FRONT END",
                "tims":"https://cs.copart.com/v1/AUTH_svc.pdoc00001/NAP140417/6e2bd65c-afe3-4139-a28e-46bfe43adde0.JPG",
                "lic":["IV","CERT-E"],"gr":" J010","dtc":"FR","adt":"E","ynumb":56,"phynumb":56,"ymin":175,
                "htsmn":"Y","myb":0.0,"lmc":"TOYT","lcc":"CERT-E","sdd":"SIDE","bstl":"4DR SPOR",
                "lcd":"ENHANCED VEHICLES","ft":"GAS","hk":"YES","drv":"Front-wheel Drive",
                "ess":"Pure Sale","brand":"COPART"}
        testIn =[{'lotNumberStr': '18881174', 'ln': 18881174, 'mkn': 'TOYOTA', 'lm': 'SCION', 'lcy': 2006,
                  'fv': 'JTLKT324464093337', 'la': 7901.0, 'rc': 11479.0, 'obc': 'E', 'orr': 0.0, 'ord': 'EXEMPT',
                  'egn': '1.5L  4', 'cy': '4', 'ld': '2006 TOYOTA SCION XB', 'yn': 'SC - COLUMBIA', 'cuc': 'USD',
                  'tz': 'EDT', 'ad': 1571407200000, 'at': '10:00:00', 'aan': 0, 'hb': 0.0, 'ss': 5, 'bndc': '',
                  'bnp': 0.0, 'sbf': False, 'ts': 'SC', 'stt': 'ST', 'td': 'CERT OF TITLE-SALVAGE',
                  'tgc': 'TITLEGROUP_S', 'dd': 'FRONT END',
                  'tims': 'https://cs.copart.com/v1/AUTH_svc.pdoc00001/NAP140417/6e2bd65c-afe3-4139-a28e-46bfe43adde0.JPG',
                  'lic': ['IV', 'CERT-E'], 'gr': ' J010', 'dtc': 'FR', 'adt': 'E', 'ynumb': 56, 'phynumb': 56,
                  'bf': False, 'ymin': 175, 'htsmn': 'Y', 'myb': 0.0, 'lmc': 'TOYT', 'lcc': 'CERT-E', 'sdd': 'SIDE',
                  'bstl': '4DR SPOR', 'lcd': 'ENHANCED VEHICLES', 'ft': 'GAS', 'hk': 'YES', 'drv': 'Front-wheel Drive',
                  'ess': 'Pure Sale', 'showSeller': False, 'sstpflg': False, 'syn': 'SC - COLUMBIA', 'ifs': True,
                  'pbf': False, 'crg': 0.0, 'brand': 'COPART'},{'lotNumberStr': '18881174', 'ln': 18881174, 'mkn': 'TOYOTA', 'lm': 'CAMRY', 'lcy': 2006,
                  'fv': 'JTLKT324464093337', 'la': 7901.0, 'rc': 11479.0, 'obc': 'E', 'orr': 0.0, 'ord': 'EXEMPT',
                  'egn': '1.5L  4', 'cy': '4', 'ld': '2006 TOYOTA SCION XB', 'yn': 'SC - COLUMBIA', 'cuc': 'USD',
                  'tz': 'EDT', 'ad': 1571407200000, 'at': '10:00:00', 'aan': 0, 'hb': 0.0, 'ss': 5, 'bndc': '',
                  'bnp': 0.0, 'sbf': False, 'ts': 'SC', 'stt': 'ST', 'td': 'CERT OF TITLE-SALVAGE',
                  'tgc': 'TITLEGROUP_S', 'dd': 'FRONT END',
                  'tims': 'https://cs.copart.com/v1/AUTH_svc.pdoc00001/NAP140417/6e2bd65c-afe3-4139-a28e-46bfe43adde0.JPG',
                  'lic': ['IV', 'CERT-E'], 'gr': ' J010', 'dtc': 'FR', 'adt': 'E', 'ynumb': 56, 'phynumb': 56,
                  'bf': False, 'ymin': 175, 'htsmn': 'Y', 'myb': 0.0, 'lmc': 'TOYT', 'lcc': 'CERT-E', 'sdd': 'SIDE',
                  'bstl': '4DR SPOR', 'lcd': 'ENHANCED VEHICLES', 'ft': 'GAS', 'hk': 'YES', 'drv': 'Front-wheel Drive',
                  'ess': 'Pure Sale', 'showSeller': False, 'sstpflg': False, 'syn': 'SC - COLUMBIA', 'ifs': True,
                  'pbf': False, 'crg': 0.0, 'brand': 'COPART'},{'lotNumberStr': '18881174', 'ln': 18881174, 'mkn': 'TOYOTA', 'lm': 'CAMRY', 'lcy': 2006,
                  'fv': 'JTLKT324464093337', 'la': 7901.0, 'rc': 11479.0, 'obc': 'E', 'orr': 0.0, 'ord': 'EXEMPT',
                  'egn': '1.5L  4', 'cy': '4', 'ld': '2006 TOYOTA SCION XB', 'yn': 'SC - COLUMBIA', 'cuc': 'USD',
                  'tz': 'EDT', 'ad': 1571407200000, 'at': '10:00:00', 'aan': 0, 'hb': 0.0, 'ss': 5, 'bndc': '',
                  'bnp': 0.0, 'sbf': False, 'ts': 'SC', 'stt': 'ST', 'td': 'CERT OF TITLE-SALVAGE',
                  'tgc': 'TITLEGROUP_S', 'dd': 'FRONT END',
                  'tims': 'https://cs.copart.com/v1/AUTH_svc.pdoc00001/NAP140417/6e2bd65c-afe3-4139-a28e-46bfe43adde0.JPG',
                  'lic': ['IV', 'CERT-E'], 'gr': ' J010', 'dtc': 'FR', 'adt': 'E', 'ynumb': 56, 'phynumb': 56,
                  'bf': False, 'ymin': 175, 'htsmn': 'Y', 'myb': 0.0, 'lmc': 'TOYT', 'lcc': 'CERT-E', 'sdd': 'SIDE',
                  'bstl': '4DR SPOR', 'lcd': 'ENHANCED VEHICLES', 'ft': 'GAS', 'hk': 'YES', 'drv': 'Front-wheel Drive',
                  'ess': 'Pure Sale', 'showSeller': False, 'sstpflg': False, 'syn': 'SC - COLUMBIA', 'ifs': True,
                  'pbf': False, 'crg': 0.0, 'brand': 'car'}]
        query = {
            'make': 'toyota',
            'model': 'camry',
            'year': 1999,
            'vtype': "car"
        }


        real_final = []
        num_of_dicts = len(list(testIn))
        #print(num_of_dicts)
        while count < num_of_dicts:
            rdict = list(testIn)[count]
            final_bool_list = []
            for v in query.values():
                bool_list = []
                #print(v)
                for t in rdict.values():
                    if str(t).lower() == str(v):
                        bool_list.append(True)
                    else:
                        bool_list.append(False)

                if any(bool_list):
                    final_bool_list.append(True)
                    #print(bool_list)
                else:
                    final_bool_list.append(False)
                    #print(bool_list)
            if not any(final_bool_list):
                real_final.append(True)
                #print(final_bool_list)
            else:
                real_final.append(False)
                #print(final_bool_list)
            count += 1
        finL = []
        bool_count = 0

        for v in query.values():
            if final_bool_list[bool_count] == True:
                val = ""+ str(v) + " was found!"
                finL.append(val)
                bool_count += 1
            else:
                val = ""+ str(v) + " wasn't found!"
                finL.append(val)
                bool_count += 1

        print(finL)