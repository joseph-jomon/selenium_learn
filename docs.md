## Explanation

### Import Necessary Modules:
- **webdriver**: For controlling the browser.
- **By**: For specifying how to locate elements (e.g., by CSS selector).
- **WebDriverWait**: For waiting for elements to be in a specific state.
- **expected_conditions**: For defining conditions to wait for (e.g., element to be clickable).
- **TimeoutException, NoSuchElementException**: For handling potential errors.
- **time**: To add a delay.

### Configuration:
- **CHROME_DRIVER_PATH**: Replace this with the actual path to your ChromeDriver executable.
- **TARGET_URL**: Replace this with the URL of the web page containing the button.

### `click_button_by_css_selector(driver, selector, timeout=10)` Function:
- Takes the driver, the selector, and an optional timeout as input.
- Uses `WebDriverWait` to wait for the element to be clickable. This is crucial because elements might not be immediately available when the page loads.
- `EC.element_to_be_clickable((By.CSS_SELECTOR, selector))`: This is the condition we're waiting for. It checks if an element matching the CSS selector is clickable.
- `button.click()`: Clicks the button.

### Error Handling:
- **TimeoutException**: Handles the case where the button doesn't become clickable within the specified timeout.
- **NoSuchElementException**: Handles the case where the element is not found.
- **Exception**: Handles other potential errors.

### `main()` Function:
- Sets up the Chrome WebDriver using `webdriver.Chrome(executable_path=CHROME_DRIVER_PATH)`.
- Navigates to the `TARGET_URL` using `driver.get(TARGET_URL)`.
- Defines the `button_selector` as `"a.cta.cta--homepage"`.
- Calls `click_button_by_css_selector()` to click the button.
- Includes an optional `time.sleep(5)` to pause for 5 seconds so you can observe the result. You can adjust or remove this as needed.

### Error Handling:
- **Exception**: Handles other potential errors.

### Cleanup:
- `driver.quit()`: Closes the browser window and ends the WebDriver session. This is important to release resources.

### `if __name__ == "__main__":`
- Ensures that the `main()` function is called only when the script is executed directly (not when imported as a module).

## How to Run:

### Install Selenium: