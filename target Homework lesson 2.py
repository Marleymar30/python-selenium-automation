from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

# Set up Chrome options for incognito mode
chrome_options = Options()
chrome_options.add_argument("--incognito")

# set up the chrome driver
service = Service('path/to/chromedriver')
driver = webdriver.Chrome(service=service, options=chrome_options)


# Step 1: Open the url
driver.get('https://www.target.com/')
sleep(2)

# Step 2: Click SignIn button
sign_in_button = driver.find_element(By.XPATH, "//a[contains(text(), 'Sign in')]")
sign_in_button.click()
sleep(2)

# Step 3: Click SignIn from side navigation
side_nav_sign_in = driver.find_element(By.XPATH, "//a[contains(text(), 'Sign in')]")
side_nav_sign_in.click()
sleep(2)

# Step 4: Verify SignIN page opened
# Check for the presence of the "Sign in to your Target account" text
sign_in_text = driver.find_element(By.XPATH, "//h1[contains(text(), 'Sign into your Target account')]")
sign_in_button_present = driver.find_element(By.XPATH, "//button[contains(text(), 'Sign in')]")

# Print results
print("Sign in text is present:", sign_in_text.is_displayed())
print("Sign in button is present:", sign_in_button_present.is_displayed())

driver.quit()