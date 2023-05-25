import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime, timedelta

# Specify the base URL and folder path
# Replace with the website URL
base_url = 'https://www.wunderground.com/history/daily/DNAA/date/'
# Replace with the desired folder path
folder_path = 'C:\\Users\\Baka sheddy.DESKTOP-H27QSPR\\Desktop\\weather/'

# Create the folder if it doesn't exist
os.makedirs(folder_path, exist_ok=True)

# Specify the start and end dates
start_date = datetime(2015, 1, 1)
end_date = datetime(2023, 1, 1)

# Define the time delta for incrementing the date
delta = timedelta(days=1)

# Set up the Selenium WebDriver (specify the appropriate driver for your browser)
# Replace with the path to your chromedriver
driver = webdriver.Chrome('C:\\Program Files\\chrome_driver\\chromedriver')

# Iterate over the range of dates
current_date = start_date
while current_date < end_date:
    # Format the current date as required (e.g., year-month-day)
    formatted_date = current_date.strftime('%Y-%m-%d')

    # Construct the URL for the specific date
    # Modify this according to the website's URL structure
    url = base_url + formatted_date

    # Open the URL in the browser
    driver.get(url)

    # Wait for the "View" button to be clickable
    wait = WebDriverWait(driver, 7)  # Adjust the timeout value as needed
    view_button = wait.until(EC.element_to_be_clickable((By.ID, 'dateSubmit')))

    # Click the "View" button
    view_button.click()

    # Wait for the tables to load (adjust the waiting time as needed)
    driver.implicitly_wait(7)  # Wait for 5 seconds (modify as required)

    # Get the page source with the loaded tables
    page_source = driver.page_source

    # Save the HTML content to a file
    file_path = os.path.join(folder_path, f'{formatted_date}.html')
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(page_source)

    print(f'Saved {formatted_date}.html')

    # Increment the current date by one day
    current_date += delta

print('Download completed.')

# Quit the WebDriver
driver.quit()
