from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


@then('Verify correct search results show')
def verify_search_results(context):
   actual_text = context.driver.find_element(By.XPATH, "//div[@data-test='lp-resultsCount']").text
   expected_text = 'tea'
   assert expected_text in actual_text, f'Expected. Text {expected_text} not in {actual_text}'
   sleep(5)