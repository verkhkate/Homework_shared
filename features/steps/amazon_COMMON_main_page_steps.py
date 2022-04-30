# COMMON STEPS FOR AMAZON MAIN PAGE

from selenium import webdriver
from selenium.webdriver.common.by import By
from behave import given, when, then
import time

# Amazon main page loading
@given('Open Amazon page')
def open_amazon_page(context):
    context.driver.get('https://www.amazon.com/')
    time.sleep(2)

@when('Verify Amazon page is opened')
def verify_amazon_page_opened(context):
    actual_result = context.driver.title
    expected_result = 'Amazon.com. Spend less. Smile more.'
    assert expected_result == actual_result, f'Test case failed! Actual text {actual_result} does not match expected {expected_result}'
    print('Test case passed')

# BOTTOM MENU - Let Us Help You - Help
@when('Open Amazon Help page')
def open_amazon_help_page(context):
    context.driver.get('https://www.amazon.com/gp/help/customer/display.html')
    time.sleep(2)

@when('Verify Amazon Help page is opened')
def verify_amazon_help_page_opened(context):
    actual_result = context.driver.title
    expected_result = 'Help & Customer Service - Amazon Customer Service'
    assert expected_result == actual_result, f'Test case failed! Actual text {actual_result} does not match expected {expected_result}'
    print('Test case passed')