
from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager



firefox_service = webdriver.firefox.service.Service(GeckoDriverManager().install())
go_driver = webdriver.Firefox(service=firefox_service)
go_driver.get('https://www.goibibo.com/')
go_driver.implicitly_wait(2)
go_driver.find_element(webdriver.common.by.By.XPATH, '/html/body/div[1]/div[1]/header/div[2]/div/div/p').click()
go_driver.implicitly_wait(2)
go_driver.find_element(webdriver.common.by.By.CSS_SELECTOR, 'html body.desktop.gr-bodyFixed div#root div.cm__modalWraper.centerMode div.cm__modal div.cm__modalContent div.lgContainer div.lgRightSection div.loginCont div form div.loginCont__inputwrap input.loginCont__input').send_keys('123456789')
go_driver.implicitly_wait(2)
go_driver.back()
go_driver.find_element(webdriver.common.by.By.CLASS_NAME, '')
go_driver.quit()

