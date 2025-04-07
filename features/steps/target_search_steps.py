from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

SEARCH_FIELD= (By.ID,'search_field')
SEARCH_BTN = (By.XPATH,"//button[@data-test=@web/Search/search-button]")
CART_ICON = (By.CSS_SELECTOR,"[data-test='@web/CartLink']")
SEARCH_RESULTS_TEXT = (By.XPATH,"//div[@data-test='lp-resultsCount']")
BENEFITS_CELLS = (By.XPATH,"//div[@data-test='lp-benefit-cell']")
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


@given('Open the Target Circle page')
def open_target_circle_page(context):
    context.driver.get('https://www.target.com/s/search?q=circle')
    sleep(5)


@when('Count the benefit cells')
def count_benefit_cells(context):
    cells = context.driver.find_elements(*BENEFITS_CELLS)
    context.benefit_cells_count = len(cells)
    sleep(5)


@then('There should be {cells_count} benefit cells')
def verify_benefit_cells(context, cells_count):
    cells_count = int(cells_count)
    assert context.benefit_cells_count == cells_count, f'Expected {cells_count} cells, got {context.benefit_cells_count}'


@given('Open the Target website')
def open_target_website(context):
    context.driver.get('https://www.target.com/')
    sleep(3)


@when('Search for {search_word}')
def search_product(context, search_word):
    context.driver.find_element(*SEARCH_FIELD).send_keys('Headphones')
    context.driver.find_element(*SEARCH_BTN).click()
    sleep(2)


@when('Add the product to the cart')
def add_product_to_cart(context):
    context.driver.find_element(*CART_ICON).click()
    sleep(2)


@then('The cart should contain the {product_name}')
def verify_product_in_cart(context, product_name):
    actual_text = context.driver.find_element(By.XPATH, "//div[@data-test='lp-resultsCount']").text
    expected_text = 'product_name'
    assert expected_text in actual_text, f'Expected. Text {expected_text} not in {actual_text}'