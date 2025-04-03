from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


@given('Open target main page')
def open_target_main(context):
    context.driver.get('https://www.target.com/')
    sleep(5)


@when('Click on target cart icon')
def click_cart(context):
    context.driver.find_element(By.CSS_SELECTOR, "[data-test='@web/CartLink/cart-link']")
    sleep(5)


@then('Verify cart is empty')
def verify_search_results(context):
    actual_text = context.driver.find_element(By.XPATH, "//div[@data-test='lp-resultsCount']").text
    expected_text = 'cart_icon'
    assert expected_text in actual_text, f'Expected. Text {expected_text} not in {actual_text}'
    sleep(5)