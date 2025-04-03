The behavior you're experiencing can be due to several factors, including the specificity of the CSS selector, the timing of element availability, or even the structure of the HTML. Here are some insights and best practices for handling such scenarios:

### Why `By.NAME` Worked but `By.CSS_SELECTOR` Didn't
1. **Element Type Mismatch**: The CSS selector you used (`button[name='_submit'][value='Sign in']`) specifies a `<button>` element. However, the actual element might be an `<input>` element with `type="submit"`. This mismatch can cause the selector to fail.
2. **Specificity and Timing**: Sometimes, the element might not be immediately available or fully rendered when the CSS selector is applied. Using `By.NAME` might work because it directly targets the `name` attribute, which is less likely to be affected by rendering issues.

### Best Practices for Element Selection
1. **Understand the HTML Structure**: Ensure you fully understand the HTML structure of the page. Use browser developer tools to inspect the element and confirm its type and attributes.
2. **Use Unique Identifiers**: Prefer using unique identifiers like `id` or `name` attributes when available, as they are less likely to be duplicated and are more reliable.
3. **Fallback Strategies**: If one method fails, try alternative methods. For example, if `By.CSS_SELECTOR` fails, try `By.NAME`, `By.ID`, or `By.XPATH`.
4. **Wait for Elements**: Use explicit waits to ensure the element is available before interacting with it. This can help with timing issues.

### Example with Explicit Wait
Here's an example using explicit waits to ensure the element is available before interacting with it:

```python
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

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

# Wait for the "Sign in" button to be clickable and click it
sign_in_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.NAME, "_submit"))
)
sign_in_button.click()
```

### Summary
- **Use Unique Identifiers**: Prefer `id` or `name` attributes when available.
- **Fallback Strategies**: Try different methods if one fails.
- **Explicit Waits**: Use explicit waits to handle timing issues.
- **Understand HTML Structure**: Ensure you understand the element's type and attributes.

By following these best practices, you can handle element selection more effectively and professionally.