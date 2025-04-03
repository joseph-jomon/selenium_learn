Yes, you can access elements using various attributes such as `name`, `class`, `id`, `css selector`, etc. Each of these attributes corresponds to a method in the `By` class that allows you to locate elements based on that attribute.

### Methods in `By` Class
Here are some common methods provided by the `By` class:

- `By.ID`: Locate an element by its `id` attribute.
- `By.NAME`: Locate an element by its `name` attribute.
- `By.CLASS_NAME`: Locate an element by its class name.
- `By.CSS_SELECTOR`: Locate an element using a CSS selector.
- `By.XPATH`: Locate an element using an XPath expression.
- `By.TAG_NAME`: Locate an element by its tag name.
- `By.LINK_TEXT`: Locate a link element by its visible text.
- `By.PARTIAL_LINK_TEXT`: Locate a link element by a part of its visible text.

### Example Code
You can use any of these methods to locate the "Next" button. Here are examples using different attributes:

#### Using `By.NAME`
```python
submit_button = driver.find_element(By.NAME, "whoamiSubmit")
submit_button.click()
```

#### Using `By.CLASS_NAME`
```python
submit_button = driver.find_element(By.CLASS_NAME, "btn-next")
submit_button.click()
```

#### Using `By.CSS_SELECTOR`
```python
submit_button = driver.find_element(By.CSS_SELECTOR, "button.btn.btn-primary.btn-next.mt-0")
submit_button.click()
```

#### Using `By.XPATH`
```python
submit_button = driver.find_element(By.XPATH, "//button[@name='whoamiSubmit']")
submit_button.click()
```

### Updated Code Example
Here's your updated code with different methods to locate the "Next" button:

```python
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

# Locate the "Next" button by name and click it
submit_button = driver.find_element(By.NAME, "whoamiSubmit")
submit_button.click()
```

### Summary
- **`By.NAME`**: Use when you want to locate an element by its `name` attribute.
- **`By.CLASS_NAME`**: Use when you want to locate an element by a single class name.
- **`By.CSS_SELECTOR`**: Use when you need more flexibility, such as selecting elements by multiple class names, element types, or other attributes.
- **`By.XPATH`**: Use when you want to locate an element using an XPath expression.

You can choose the method that best fits your needs based on the attributes available for the element you want to interact with.