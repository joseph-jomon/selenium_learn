from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
import time

# --- Configuration ---
# Replace with the actual path to your ChromeDriver executable
CHROME_DRIVER_PATH = '/path/to/your/chromedriver'  
# Replace with the URL of the initial page you want to test
INITIAL_URL = 'https://example.com'  # Replace with the actual URL
# Replace with the email you want to use
EMAIL_ADDRESS = 'test@example.com' # Replace with the actual email
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

def fill_email_and_click_next(driver, email, timeout=10):
    """
    Fills the email input field and clicks the "Next" button.

    Args:
        driver: The Selenium WebDriver instance.
        email: The email address to enter.
        timeout: The maximum time to wait for elements to be present (in seconds).
    """
    try:
        # Wait for the email input field to be present and visible
        email_input = WebDriverWait(driver, timeout).until(
            EC.presence_of_element_located((By.ID, "username"))
        )
        email_input = WebDriverWait(driver, timeout).until(
            EC.visibility_of(email_input)
        )

        # Clear any existing text in the input field (optional)
        email_input.clear()

        # Send the email address to the input field
        email_input.send_keys(email)

        # Find the "Next" button container
        next_button_container = WebDriverWait(driver, timeout).until(
            EC.presence_of_element_located((By.XPATH, "//div[@class='row']"))
        )

        # Find the "Next" button inside the container
        next_button = WebDriverWait(next_button_container, timeout).until(
            EC.presence_of_element_located((By.XPATH, ".//button[contains(text(), 'Next')]"))
        )

        # Click the "Next" button
        next_button.click()

        print("Email entered and 'Next' button clicked successfully.")

    except TimeoutException:
        print("Timeout: Element not found or not visible within the specified time.")
    except Exception as e:
        print(f"An error occurred: {e}")

def main():
    """
    Main function to set up the WebDriver, navigate to the initial page,
    click the button to reach the email page, fill the email, and click next.
    """
    try:
        # Set up the Chrome WebDriver
        driver = webdriver.Chrome(executable_path=CHROME_DRIVER_PATH)

        # Navigate to the initial URL
        driver.get(INITIAL_URL)

        # --- Locate and click the button to reach the email page ---
        # Using the CSS selector for the button
        initial_button_selector = "button.btn.btn-primary.btn-next.mt-0" # Replace with the actual selector if needed
        click_button_by_css_selector(driver, initial_button_selector)

        # --- Fill the email and click next ---
        fill_email_and_click_next(driver, EMAIL_ADDRESS)

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