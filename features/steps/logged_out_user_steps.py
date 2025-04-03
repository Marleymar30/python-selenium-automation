from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


@given('Open target.com')
def open_target_main(context):
    context.driver.get('https://www.target.com/')
    sleep(5)


@when('Click Sign In')
def click_on_login_button(context):
    context.driver.find_element(By.ID, 'header-login-link').click()
    sleep(5)


@then('Verify Sign In form opened')
def verify_login_form(context):
    actual_text = context.driver.find_element(By.XPATH, "//h1[@class='login__title']").text
    expected_text = 'Sign In'
    assert expected_text in actual_text, f'Expected. Text {expected_text} not in {actual_text}'
sleep(5)

