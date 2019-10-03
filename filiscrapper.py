#!/bin/python

#Python fili.cc scrapping tool which takes fili.cc link and finds the source url
#of it. Tool uses selenium python webdriver and geckodriver (firefox)

from selenium import webdriver


from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver import Firefox 
from selenium.webdriver.firefox.options import Options

import time
import sys
import subprocess

url= sys.argv[1]
finalString = ''.join(sys.argv)
opts = Options()
opts.set_headless()
assert opts.headless
d = Firefox(options=opts)
d.implicitly_wait(10)

d.get(url)
time.sleep(1)
button = d.find_elements_by_class_name('button_button--lgX0P')
button[2].click()
linia = d.find_elements_by_class_name('line')
if ('-s' in finalString):
    print ('1.' + linia[0].text)
    print ('2.' + linia[1].text)
    print ('3.' + linia[2].text)
    print ('4.' + linia[3].text)
    print ('5.' + linia[4].text)
    number = input("Podaj numer: ")
    number = number - 1
    linia[number].find_element_by_id('watchBtn').click()
else:
    linia[0].find_element_by_id('watchBtn').click()
iframes = d.find_elements_by_tag_name("iframe")
d.switch_to_frame(iframes[2])
d.find_element_by_id('accept').click()
embed = d.find_elements_by_tag_name("iframe")
result = embed[0].get_attribute('src')
d.close()

if ('-d' in finalString):
    subprocess.call(["youtube-dl", result])
else:
    print("\n" + result)
