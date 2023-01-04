# from selenium import webdriver
# from selenium.webdriver.common.action_chains import ActionChains
# #ActionChains(browser).click(element).perform()
# driver = webdriver.Chrome(
#     executable_path=r'/home/sakthi/Desktop/Automation Projects/chromedriver_linux64')
# driver.get("https://www.w3schools.com/")
# driver.maximize_window()
# web_element=driver.find_element_by_link_text("LOGIN")
# web_element.click()
# search=driver.find_element_by_name("firstname")
# search.send_keys("arockia123@gmail.com")
# search=driver.find_element_by_name("lastname")
# search.send_keys("12345")

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://www.google.com/")
driver.maximize_window()
driver.sleep(10)
m = driver.find_element_by_name("q")
m.send_keys("Welcome")
