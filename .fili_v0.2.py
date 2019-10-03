import sys
sys.stderr.write('0%')
sys.stderr.write('5%')
from selenium.webdriver import Firefox 
sys.stderr.write('10%')
from selenium.webdriver.firefox.options import Options
sys.stderr.write('15%')
import time
sys.stderr.write('20%')
url= sys.argv[1]
sys.stderr.write('25%')
opts = Options()
sys.stderr.write('30%')
#opts.set_headless()
sys.stderr.write('35%')
#assert opts.headless
sys.stderr.write('40%')
d = Firefox(options=opts)
sys.stderr.write('45%')
d.get(url)
sys.stderr.write('50%')
button = d.find_elements_by_class_name('button_button--lgX0P')
sys.stderr.write('55%')
try:
    button[2].click()
except:
    sys.stderr.write('Error no.1')
sys.stderr.write('60%')
linia = d.find_elements_by_class_name('line')
sys.stderr.write('65%')
linia[0].find_element_by_id('watchBtn').click()
sys.stderr.write('70%')
iframes = d.find_elements_by_tag_name("iframe")
sys.stderr.write('75%')
d.switch_to_frame(iframes[2])
sys.stderr.write('80%')
time.sleep(1)
sys.stderr.write('85%')
d.find_element_by_id('accept').click()
sys.stderr.write('90%')
embed = d.find_elements_by_tag_name("iframe")
sys.stderr.write('95%')
sys.stderr.write('100%')
print(embed[0].get_attribute('src'))



