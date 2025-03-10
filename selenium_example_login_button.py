from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
import time

# --- Configuration ---
# Replace with the actual path to your ChromeDriver executable
CHROME_DRIVER_PATH = '/path/to/your/chromedriver'  
# Replace with the URL of the page you want to test
TARGET_URL = 'https://example.com'  # Replace with the actual URL
# --- End Configuration ---

def click_button_by_css_selector(driver, selector, timeout=10):
    """
    Clicks a button identified by a CSS selector.

    Args:
        driver: The Selenium WebDriver instance.
        selector: The CSS selector to locate the button.
        timeout: The maximum time to wait for the button to be clickable (in seconds).
    """
    try:
        # Wait for the button to be clickable
        button = WebDriverWait(driver, timeout).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, selector))
        )
        # Click the button
        button.click()
        print(f"Successfully clicked the button with selector: {selector}")
    except TimeoutException:
        print(f"Timeout: Button with selector '{selector}' was not clickable within {timeout} seconds.")
    except NoSuchElementException:
        print(f"Element not found: Button with selector '{selector}' was not found.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

def main():
    """
    Main function to set up the WebDriver, navigate to the page, and click the button.
    """
    try:
        # Set up the Chrome WebDriver
        driver = webdriver.Chrome(executable_path=CHROME_DRIVER_PATH)

        # Navigate to the target URL
        driver.get(TARGET_URL)

        # --- Locate and click the button ---
        # Using the CSS selector for the button
        button_selector = "a.cta.cta--homepage"
        click_button_by_css_selector(driver, button_selector)

        # --- Optional: Add a delay to observe the result ---
        time.sleep(5)  # Wait for 5 seconds (adjust as needed)

    except Exception as e:
        print(f"An error occurred during the test: {e}")
    finally:
        # Close the browser
        if 'driver' in locals() and driver:
            driver.quit()

if __name__ == "__main__":
    main()