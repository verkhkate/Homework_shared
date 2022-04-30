# STEPS FOR AMAZON "RETURNS AND ORDERS"

from selenium import webdriver
from selenium.webdriver.common.by import By
from behave import given, when, then
import time

# Scenario: Logged out User sees Sign in page when clicking "Returns and Orders"
# Click on Returns and Orders
@when('Click on Returns and Orders')
def click_returns_and_orders(context):
    context.driver.find_element(By.XPATH, "//*[contains(@href, '/gp/css/order-history?ref_=nav_orders_first')]").click()
    time.sleep(1)

# Verify Sign in page is opened
@then('Verify Sign in page is opened')
def verify_signin_page_opened(context):
    expected_result = 'Sign-In'
    actual_result = context.driver.find_element(By.XPATH, "//h1").text
    assert expected_result == actual_result, f'Test case failed! Actual text {actual_result} does not match expected {expected_result}'
    print('Test case passed')