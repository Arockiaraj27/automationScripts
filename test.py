from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
#ActionChains(browser).click(element).perform()
driver = webdriver.Chrome(executable_path=r'C:\arockiaraj\chromedriver.exe')
driver.get("https://www.flipkart.com/")
driver.maximize_window()
browser=driver.find_element_by_xpath('/html/body/div[2]/div/div/button')
browser.click()

# web_element=driver.find_element_by_link_text("LOGIN")
# web_element.click()
# search=driver.find_element_by_name("firstname")
# search.send_keys("arockia123@gmail.com")
# search=driver.find_element_by_name("lastname")
# search.send_keys("12345")
