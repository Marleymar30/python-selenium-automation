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
driver.get('https://www.Amazon.com/')
sleep(5)

amazon_logo_locator = driver.find_element(By.XPATH, "//a[@aria-label='Amazon']")

email_field_locator = driver.find_element(By.ID, "ap_email")

continue_button_locator = driver.find_element(By.ID, "continue")

conditions_of_use_locator = driver.find_element(By.XPATH, "//a[contains(@href, 'conditions')]")

privacy_notice_locator = driver.find_element(By.XPATH, "//a[contains(@href, 'privacy')]")

need_help_locator = driver.find_element(By.XPATH, "//a[contains(text(), 'Need help?')]")

forgot_password_locator = driver.find_element(By.ID, "auth-ffp-link-bottom")

other_issues_locator = driver.find_element(By.XPATH, "//a[contains(text(), 'Other issues with Sign-In')]")

create_account_locator = driver.find_element(By.ID, "createAccountSubmit")

