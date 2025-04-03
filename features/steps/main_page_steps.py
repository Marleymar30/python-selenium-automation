from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


SEARCH_FIELD= (By.ID,'search_field')
SEARCH_BTN = (By.XPATH,"//button[@data-test=@web/Search/search-button]")
CART_ICON = (By.CSS_SELECTOR,"[data-test='@web/CartLink']")
HEADER_LINKS = (By.CSS_SELECTOR, "[id*='utilityNav']")


@given('Open target main page')
def open_target_main(context):
    context.driver.get('https://www.target.com/')
    sleep(5)


@when('Search for tea')
def search_tea(context):
    context.driver.find_element(*SEARCH_FIELD).send_keys('tea')
    context.driver.find_element(*SEARCH_BTN).click()


@when('Click on target cart icon')
def click_cart(context):
    context.driver.find_element(*CART_ICON).click()
    sleep(5)


@then('Verify at least 1 link shown')
def verify_1_header_link_shown(context):
    link = context.driver.find_element(*HEADER_LINKS)
    print(link)


@then('Verify {link_amount} links shown')
def verify_all_header_links_shown(context, link_amount):
    link_amount = int(link_amount)
    links = context.driver.find_elements(*HEADER_LINKS)
    assert len(links) == 6, f'Expected 6 links, got {len(links)}'
    print(links)