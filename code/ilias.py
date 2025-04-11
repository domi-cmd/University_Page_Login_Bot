import time
import os
from selenium import webdriver
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# Get the credentials
credentials = {}

with open('credentials.txt', 'r') as file:
    for line in file:
        if '=' in line:
            key, value = line.strip().split('=', 1)
            credentials[key] = value

username = credentials.get('username')
password = credentials.get('password')


def element_locator(locating_type, adress_type, path):
    element = WebDriverWait(driver, 10).until(
        locating_type((adress_type, path))
    )
    return element


# Set Chrome options if needed
options = Options()
options.add_argument("--start-maximized")

# Automatically downloads and uses the correct ChromeDriver version
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

# Go to the login page
driver.get('https://ilias.unibe.ch/login.php?target=&client_id=ilias3_unibe')

# Wait for the login identity provider selector and click
choose_uni = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, 'user_idp_iddtext'))
)
choose_uni.click()

# Choose Universität Bern by its title
'''
unibern = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//*[@title='Meist benutzte Organisationen: Universität Bern']"))
    )
'''
unibern = element_locator(locating_type = EC.element_to_be_clickable, adress_type = By.XPATH, 
                        path="//*[@title='Meist benutzte Organisationen: Universität Bern']")
unibern.click()


# Continue to the login screen
element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, 'wayf_submit_button'))
    )
element.click()

# Enter username
username_entryfield = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "username"))
    )
username_entryfield.send_keys(username)

# Click login
login_button = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "button-submit"))
    )
login_button.click()

# Enter password
password_entryfield = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "password"))
    )
password_entryfield.send_keys(password)

# Click login
login_button = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "button-proceed"))
    )
login_button.click()

# Locate the element using its class name
#element = driver.find_element(By.CLASS_NAME, 'glyphicon-remove')

# Click the element
#element.click()


# Find the "Arbeitsraum" button by its label
#button = WebDriverWait(driver, 10).until(
#    EC.element_to_be_clickable((By.XPATH, '//span[contains(text(), "Arbeitsraum")]'))
#    )
# Click the button to change its state
button = element_locator(locating_type = EC.presence_of_element_located, adress_type = By.XPATH, 
                       path = '//span[contains(text(), "Arbeitsraum")]')
button.click()


link_element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//span[@class="bulky-label" and text()="Aktuelles Semester"]/ancestor::a[@class="il-link link-bulky"]'))
    )
# Click the link
link_element.click()


# Wait for the close button to be clickable
close_taskbar_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.CLASS_NAME, "il-mainbar-close-slates"))
)
close_taskbar_button.click()


# Loop that runs until the chromedriver is closed
try:
    # Enter an infinite loop to keep the script running
    while True:
        pass  # Do nothing, just keep looping indefinitely
        if not driver.current_url:
            print("ChromeDriver window closed. Exiting loop.")
            break

except WebDriverException:
    # This exception will be raised when the window is closed
    print("ChromeDriver window closed. Exiting loop.")

# Close the driver when the loop terminates
driver.quit()

# The script will keep running until terminated externally