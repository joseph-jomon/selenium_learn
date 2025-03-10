Explanation of the Combined Script:

Imports:
Same as before: selenium.webdriver, selenium.webdriver.common.by, selenium.webdriver.support.ui, selenium.webdriver.support.expected_conditions, selenium.common.exceptions, time.
Configuration:
CHROME_DRIVER_PATH: You must replace /path/to/your/chromedriver with the actual path to your ChromeDriver executable.
INITIAL_URL: You must replace https://example.com with the actual URL of the initial page you want to start from.
EMAIL_ADDRESS: You must replace test@example.com with the actual email address you want to use.
click_button_by_css_selector(driver, selector, timeout=10):
This function remains the same. It clicks a button identified by a CSS selector, waiting for it to be clickable.
fill_email_and_click_next(driver, email, timeout=10):
This function also remains the same. It fills the email input field (id="username") and clicks the "Next" button.
main():
driver = webdriver.Chrome(executable_path=CHROME_DRIVER_PATH): Creates a new Chrome browser instance.
driver.get(INITIAL_URL): Navigates to the initial URL.
initial_button_selector = "button.btn.btn-primary.btn-next.mt-0": This is the CSS selector for the button that takes you to the email page. Make sure this is the correct selector for the button on the initial page.
click_button_by_css_selector(driver, initial_button_selector): Clicks the button to navigate to the email page.
fill_email_and_click_next(driver, EMAIL_ADDRESS): Calls the function to fill the email field and click "Next".
time.sleep(5): An optional delay.
The try...except...finally block handles errors and closes the browser.
if __name__ == "__main__"::
Ensures main() is called when the script is run directly.
Key Changes to Combine Functionality:

main() Function Flow: The main() function now has a clear sequence:
Go to the initial URL.
Click the button to reach the email page.
Fill the email and click "Next".
INITIAL_URL: A new configuration variable to specify the starting URL.
EMAIL_ADDRESS: A new configuration variable to specify the email to use.
initial_button_selector: A variable to hold the CSS selector for the button on the initial page.