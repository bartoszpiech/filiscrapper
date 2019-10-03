from selenium.webdriver import Firefox 
from selenium.webdriver.firefox.options import Options
import time
import sys
url= sys.argv[1]
opts = Options()
opts.set_headless()
assert opts.headless
d = Firefox(options=opts)
d.get(url)
button = d.find_elements_by_class_name('button_button--lgX0P')
button[2].click()
linia = d.find_elements_by_class_name('line')
linia[0].find_element_by_id('watchBtn').click()
iframes = d.find_elements_by_tag_name("iframe")
d.switch_to_frame(iframes[2])
time.sleep(3)
button = d.find_element_by_id('accept')
button.click()
url = d.find_elements_by_tag_name("iframe")
print(url[0].get_attribute('src'))



