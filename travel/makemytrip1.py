
from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from time import sleep


ff_service = webdriver.firefox.service.Service(GeckoDriverManager().install())
mmt_driver = webdriver.Firefox(service=ff_service)
mmt_driver.get('https://www.makemytrip.com/hotels/')
mmt_driver.implicitly_wait(2)
if mmt_driver.find_element(webdriver.common.by.By.CSS_SELECTOR, '#SW > div.landingContainer > div.makeFlex.hrtlCenter.prependTop5.appendBottom40 > ul > li.makeFlex.hrtlCenter.font10.makeRelative.lhUser.userLoggedOut > div.autopop__wrap.makeFlex.column.defaultCursor').is_displayed():
    print('Login selected')
    #mmt_driver.find_element(webdriver.common.by.By.XPATH, '//*[@id="SW"]/div[1]/div[1]/ul/li[3]/div[3]/div/div[2]').click()
    mmt_driver.implicitly_wait(2)
#mmt_driver.find_element(webdriver.common.by.By.XPATH, '/html/body/div[1]/div/div[2]/div[1]/div[2]/div/div/nav/ul/li[2]/a/span[1]').click()
sleep(20)
mmt_driver.quit()

