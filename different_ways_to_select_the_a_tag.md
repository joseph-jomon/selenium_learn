from selenium import webdriver
from selenium.webdriver.common.by import By

# Initialize the Chrome driver
driver = webdriver.Chrome()

# Open the webpage
driver.get("https://circabc.europa.eu/ui/welcome")

# Loading can take time
driver.implicitly_wait(5)  # Time to wait for the page to load; don't have to wait for the complete duration if the page loads faster

# Locate the "Accept all cookies" button by class name and click it
try:
    accept_cookies_button = driver.find_element(By.CLASS_NAME, "wt-ecl-button--primary")
    accept_cookies_button.click()
except:
    print("No cookies button found")

# Locate the "EU Login" button by class name and click it
accept_eulogin_button = driver.find_element(By.CLASS_NAME, "cta--homepage")
accept_eulogin_button.click()

# Enter email in the email field
email_field = driver.find_element(By.ID, "username")
email_field.send_keys("support@cust-ai.com")

# Locate the "Next" button by CSS selector and click it
submit_button = driver.find_element(By.CSS_SELECTOR, "button.btn.btn-primary.btn-next.mt-0")
submit_button.click()

# Enter password in the password field
password_field = driver.find_element(By.ID, "password")
password_field.send_keys("TheFutureofCustoms123!#")

# Click the "Sign in" button using a more specific CSS selector
sign_in_button = driver.find_element(By.NAME, "_submit")
sign_in_button.click()

# Click the continue without changing password button if present
try:
    continue_without_changing_password_button = driver.find_element(By.ID, "imminentForceLogin")
    continue_without_changing_password_button.click()
except:
    print("No continue without changing password button found")

# Incase check for trusted platform appears
try:
    trusted_platform_button = driver.find_element(By.ID, "verif-method-dd-id")
    trusted_platform_button.click()
    select_password_button = driver.find_element(By.ID, "verif-method-dd-PASSWORD")
    select_password_button.click()
    # Enter password in the password field
    password_field = driver.find_element(By.ID, "password") # Locate the password field
    passwordfrom selenium import webdriver
from selenium.webdriver.common.by import By

# Initialize the Chrome driver
driver = webdriver.Chrome()

# Open the webpage
driver.get("https://circabc.europa.eu/ui/welcome")

# Loading can take time
driver.implicitly_wait(5)  # Time to wait for the page to load; don't have to wait for the complete duration if the page loads faster

# Locate the "Accept all cookies" button by class name and click it
try:
    accept_cookies_button = driver.find_element(By.CLASS_NAME, "wt-ecl-button--primary")
    accept_cookies_button.click()
except:
    print("No cookies button found")

# Locate the "EU Login" button by class name and click it
accept_eulogin_button = driver.find_element(By.CLASS_NAME, "cta--homepage")
accept_eulogin_button.click()

# Enter email in the email field
email_field = driver.find_element(By.ID, "username")
email_field.send_keys("support@cust-ai.com")

# Locate the "Next" button by CSS selector and click it
submit_button = driver.find_element(By.CSS_SELECTOR, "button.btn.btn-primary.btn-next.mt-0")
submit_button.click()

# Enter password in the password field
password_field = driver.find_element(By.ID, "password")
password_field.send_keys("TheFutureofCustoms123!#")

# Click the "Sign in" button using a more specific CSS selector
sign_in_button = driver.find_element(By.NAME, "_submit")
sign_in_button.click()

# Click the continue without changing password button if present
try:
    continue_without_changing_password_button = driver.find_element(By.ID, "imminentForceLogin")
    continue_without_changing_password_button.click()
except:
    print("No continue without changing password button found")

# Incase check for trusted platform appears
try:
    trusted_platform_button = driver.find_element(By.ID, "verif-method-dd-id")
    trusted_platform_button.click()
    select_password_button = driver.find_element(By.ID, "verif-method-dd-PASSWORD")
    select_password_button.click()
    # Enter password in the password field
    password_field = driver.find_element(By.ID, "password") # Locate the password field
    password