from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# User can search for solutions of Canceling an order on Amazon

#1. Open Amazon Help page https://www.amazon.com/gp/help/customer/display.html
driver = webdriver.Chrome()
driver.maximize_window()
driver.get('https://www.amazon.com/gp/help/customer/display.html')

# 2. Use “Search Help Library” field and search for Cancel order
search_cancel_order = driver.find_element(By.ID, 'helpsearch')
search_cancel_order.clear()
search_cancel_order.send_keys('Cancel order')

# 3. Emulate hitting keyboard ENTER btn with send_keys command
search_cancel_order.send_keys(Keys.RETURN)

# 4. Verify that ‘Cancel Items or Orders’ text is present
expected_result = 'Cancel Items or Orders'
actual_result = driver.find_element(By.XPATH, "//h1").text
assert expected_result == actual_result, f'Error! Actual text {actual_result} does not match expected {expected_result}'
print('Test case passed')
driver.quit()