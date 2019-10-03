#!/bin/python
from selenium import webdriver
from selenium.webdriver import Firefox 
from selenium.webdriver.firefox.options import Options

import time
import sys
import subprocess

sys.stderr.write('0%')
sys.stderr.write('5%')
sys.stderr.write('10%')
sys.stderr.write('15%')
sys.stderr.write('20%')
sys.stderr.write('25%')
sys.stderr.write('30%')
sys.stderr.write('35%')
sys.stderr.write('40%')
sys.stderr.write('45%')
url= sys.argv[1]
opts = Options()
opts.set_headless()
assert opts.headless
d = Firefox(options=opts)
d.implicitly_wait(10)
d.get(url)
sys.stderr.write('50%')
button = d.find_elements_by_class_name('button_button--lgX0P')
sys.stderr.write('55%')
try:
    button[2].click()
except:
    sys.stderr.write('Error no.1')
    pass
sys.stderr.write('60%')
linia = d.find_elements_by_class_name('line')
sys.stderr.write('65%')
linia[1].find_element_by_id('watchBtn').click()
sys.stderr.write('70%')
iframes = d.find_elements_by_tag_name("iframe")
sys.stderr.write('75%')
d.switch_to_frame(iframes[2])
sys.stderr.write('80%')
sys.stderr.write('85%')
d.find_element_by_id('accept').click()
sys.stderr.write('90%')
embed = d.find_elements_by_tag_name("iframe")
sys.stderr.write('95%')
sys.stderr.write('100%')
result = embed[0].get_attribute('src')
d.close()
finalString = ''.join(sys.argv)
if ('-d' in finalString):
    subprocess.call(["youtube-dl", result])
else:
    print("\n" + result)
