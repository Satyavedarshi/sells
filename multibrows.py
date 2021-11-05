import manager as manager
from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from time import sleep

s = webdriver.firefox.service.Service(GeckoDriverManager().install())
driver1 = webdriver.Firefox(service=s)
driver1.get('https://www.amazon.in/')
print(driver1.title)
sleep(5)
driver1.close()

s = webdriver.chrome.service.Service(ChromeDriverManager().install())
driver2 = webdriver.Chrome(service=s)
driver2.get('https://www.youtube.com/watch?v=R8iaViNIy3U')
print(driver2.title)
sleep(20)
driver2.close()