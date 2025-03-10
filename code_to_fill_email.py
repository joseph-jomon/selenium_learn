from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

def fill_form_and_click_next(driver, email):
    """
    Fills the email input field and clicks the "Next" button.

    Args:
        driver: The Selenium WebDriver instance.
        email: The email address to enter.
    """
    try:
        # Wait for the email input field to be present and visible
        email_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "username"))
        )
        email_input = WebDriverWait(driver, 10).until(
            EC.visibility_of(email_input)
        )

        # Clear any existing text in the input field (optional)
        email_input.clear()

        # Send the email address to the input field
        email_input.send_keys(email)

        # Find the "Next" button container
        next_button_container = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//div[@class='row']"))
        )

        # Find the "Next" button inside the container
        next_button = WebDriverWait(next_button_container, 10).until(
            EC.presence_of_element_located((By.XPATH, ".//button[contains(text(), 'Next')]"))
        )

        # Click the "Next" button
        next_button.click()

        print("Email entered and 'Next' button clicked successfully.")

    except TimeoutException:
        print("Timeout: Element not found or not visible within the specified time.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage:
# driver = webdriver.Chrome()  # Or any other browser driver
# driver.get("your_page_url")
# fill_form_and_click_next(driver, "test@example.com")
# driver.quit()