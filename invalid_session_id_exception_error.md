The `InvalidSessionIdException` error occurs because the browser session has been closed or disconnected. This can happen if the browser was manually closed or if the session timed out.

To avoid this issue, ensure that the browser session is active before running your code. If you need to re-run the code after some time, you should re-initialize the WebDriver.

Here's how you can modify your code to handle this:

```python
from selenium import webdriver

# Initialize the Chrome driver
driver = webdriver.Chrome()

# Open the webpage
driver.get("https://circabc.europa.eu/ui/welcome")

# Loading can take time
driver.implicitly_wait(5)  # Time to wait for the page to load; don't have to wait for the complete duration if the page loads faster

# Locate the "Accept all cookies" button by class name and click it
accept_cookies_button = driver.find_element_by_class_name("wt-ecl-button--primary")
accept_cookies_button.click()
```

If you need to re-run the code after some time, make sure to re-initialize the `driver`:

```python
# Re-initialize the Chrome driver if needed
driver = webdriver.Chrome()

# Open the webpage again
driver.get("https://circabc.europa.eu/ui/welcome")

# Loading can take time
driver.implicitly_wait(5)

# Locate the "Accept all cookies" button by class name and click it
accept_cookies_button = driver.find_element_by_class_name("wt-ecl-button--primary")
accept_cookies_button.click()
```

This ensures that a new browser session is created each time you run the code.