sys.stderr.write('0%')
sys.stderr.write('5%')
sys.stderr.write('10%')
sys.stderr.write('15%')

import sys
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import Firefox 
from selenium.webdriver.firefox.options import Options
import time

def wait_element_by_id(id_value):
    try:
        elem = d.find_element_by_id(id_value)
#        return elem
    except:
        time.sleep(2)
        sys.stderr.write('Waiting for id '+id_value)
        wait_element_by_id(id_value)


def wait_elements_by_class_name(id_value):
    try:
        elem = d.find_elements_by_class_name(id_value)
#        return elem
    except:
        time.sleep(2)
        sys.stderr.write('Waiting for id '+id_value)
        wait_element_by_id(id_value)


sys.stderr.write('20%')
url= sys.argv[1]
sys.stderr.write('25%')
opts = Options()
sys.stderr.write('30%')
opts.set_headless()
sys.stderr.write('35%')
assert opts.headless
sys.stderr.write('40%')
d = Firefox(options=opts)
sys.stderr.write('45%')
d.get(url)
sys.stderr.write('50%')
elem1 = wait_elements_by_class_name('button_button--lgX0P')
sys.stderr.write('55%')
elem1[2].click()
#try:
#    button[2].click()
#except:
#    sys.stderr.write('Error no.1')
#    pass
sys.stderr.write('60%')
linia = d.find_elements_by_class_name('line')
sys.stderr.write('65%')
linia[0].find_element_by_id('watchBtn').click()
sys.stderr.write('70%')
iframes = d.find_elements_by_tag_name("iframe")
sys.stderr.write('75%')
d.switch_to_frame(iframes[2])
sys.stderr.write('80%')
elem2 = wait_element_by_id('accept')
sys.stderr.write('85%')
elem2.click()
sys.stderr.write('90%')
embed = d.find_elements_by_tag_name("iframe")
sys.stderr.write('95%')
sys.stderr.write('100%')
print(embed[0].get_attribute('src'))



