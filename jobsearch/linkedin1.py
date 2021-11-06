
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.support.ui import Select
from time import sleep


ff_s = webdriver.firefox.service.Service(GeckoDriverManager().install())
ln_driver = webdriver.Firefox(service=ff_s)

ln_driver.get('https://www.linkedin.com/')

#Login to linkedin
get_buttons = ln_driver.find_elements(By.CLASS_NAME, 'input__input')
print(len(get_buttons))
print([i for i in get_buttons], sep='\n')
sleep(5)
links = ln_driver.find_elements(By.TAG_NAME, 'a')
print([i.text for i in links], sep='\n')
ln_driver.find_element(By.LINK_TEXT, 'Post a job').click()
sleep(5)
ln_driver.back()
sleep(2)
ln_driver.find_element(By.PARTIAL_LINK_TEXT, 'Join').click()
sleep(5)
ln_driver.back()
ln_driver.execute_script('window.scrollBy(0,2000)', '')
sleep(5)
#scr_elem = ln_driver.find_element(By.XPATH, '/html/body/main/section[8]/div/a')
#ln_driver.execute_script('arguments[0].scrollIntoView();', scr_elem)
#sleep(5)
ln_driver.execute_script('window.scrollBy(0,document.body.scrollHeight)')
sleep(5)

print(ln_driver.get_cookies())
#Close the Browsers
ln_driver.quit()

