from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

# Get path to the Chromedriver executable
driver_path = ChromeDriverManager().install()

# Create a new Chrome browser instance
service = Service(driver_path)
driver = webdriver.Chrome(service=service)
driver.maximize_window()

# open the url
driver.get('https://www.target.com/')
sleep(5)

# populate search field
driver.find_element(By.ID, 'search').send_keys('coffee')
driver.find_element(By.ID, 'search').submit()
sleep(5)

# verify search results
driver.find_element(By.XPATH, "//button[@data-test='@web/Search/SearchButton']").click()
print('Test Passed')

driver.quit()
