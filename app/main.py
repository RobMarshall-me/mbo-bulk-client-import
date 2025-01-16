from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import pandas as pd
import time
from dotenv import load_dotenv
import os

load_dotenv()

df = pd.read_csv("contacts.csv")

chromedriver_path = os.getenv("chromedriver_path")
service = Service(executable_path=chromedriver_path)
driver = webdriver.Chrome(service=service)
driver.maximize_window()

# MindBodyOnline login details
login_url = os.getenv("login_url")
business_name = os.getenv("business")
username = os.getenv("username")
password = os.getenv("password")

driver.get(login_url)

# Click staff sign in
sign_in_link = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CLASS_NAME, "staffSignIn"))
)
sign_in_link.click()

username_input = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, "username"))
)
username_input.send_keys(username)
password_input = driver.find_element(By.ID, "password")
password_input.send_keys(password)
sign_in_button = WebDriverWait(driver, 5).until(
    EC.element_to_be_clickable((By.CLASS_NAME, "Button_button_3z5lHiQjwG"))
)
sign_in_button.click()

# Make sure there is enough time for the driver to load the client add page
time.sleep(5)

for index, row in df.iterrows():
    print(f"Importing {row['First Name']} {row['Last Name']}")
    try:
        # Jump to add clients url
        driver.get(
            "https://clients.mindbodyonline.com/app/business/asp/adm/adm_clt_qadd.asp"
        )

        # Switch to the iframe
        WebDriverWait(driver, 10).until(
            EC.frame_to_be_available_and_switch_to_it((By.ID, "portal"))
        )

        # Add client details
        first_name_input = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.ID, "requiredtxtFirst_Name"))
        )
        first_name_input.send_keys(row["First Name"])

        last_name_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "requiredtxtLast_Name"))
        )
        last_name_input.send_keys(row["Last Name"])

        email = row["E-mail"]
        if type(email) is str:
            email_input = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.ID, "txtEmail"))
            )
            email_input.send_keys(email)
        else:
            no_email = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.ID, "optRefusedEmail"))
            )
            no_email.click()

        phone_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, "requiredtxtPhoneNumber"))
        )
        phone_input.send_keys(row["Phone"])

        # Submit the form
        add_client_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "addNewClientButton"))
        )
        add_client_button.click()

        driver.switch_to.default_content()  # Switch back to the main content after interacting

    except Exception as e:
        print(f"Error adding client {row['First Name']} {row['Last Name']}: {e}")

print("Bulk import completed.")
