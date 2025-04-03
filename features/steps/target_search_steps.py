from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

SEARCH_FIELD= (By.ID,'search_field')
SEARCH_BTN = (By.XPATH,"//button[@data-test=@web/Search/search-button]")
CART_ICON = (By.CSS_SELECTOR,"[data-test='@web/CartLink']")
SEARCH_RESULTS_TEXT = (By.XPATH,"//div[@data-test='lp-resultsCount']")

@given('Open target main page')
def open_target_main(context):
    context.driver.get('https://www.target.com/')


@when('Search for {search_word}')
def search_product(context, search_word):
    context.driver.find_element(*SEARCH_FIELD).send_keys('search_word')
    context.driver.find_element(*SEARCH_BTN).click()


@when('Click on target cart icon')
def click_cart(context):
    context.driver.find_element(*CART_ICON).click()
    sleep(5)


@then('Verify correct search results')
def verify_search_results(context):
   actual_text = context.driver.find_element(By.XPATH, "//div[@data-test='lp-resultsCount']").text
   expected_text = 'tea'
   assert expected_text in actual_text, f'Expected. Text {expected_text} not in {actual_text}'
   sleep(5)