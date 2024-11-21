from selenium import webdriver

from selenium.webdriver.common.by import By
from time import sleep

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import requests
from urllib.parse import urljoin

with  webdriver.Chrome() as driver:
    #sandbox url
    #driver.get("http://sandbox.labware.opentrons.com/lc_fix-link-button/")
    #Working sandbox url
    #driver.get("https://labware.opentrons.com/")
    driver.get("http://sandbox.labware.opentrons.com/labware-library@3.1.0-candidate-b/")
    # get all links
    WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, "a"))
    )
    all_links = driver.find_elements(By.CSS_SELECTOR, "a")
    for link in all_links:
        url = link.get_attribute('href')
        if url:  # Check if URL is not None or empty
            # Convert relative URL to absolute URL if needed
            absolute_url = urljoin(driver.current_url, url)

            try:
                result = requests.get(absolute_url, timeout=5, allow_redirects=True)  # Add a timeout
                print(f"URL: {absolute_url} - Status: {result.status_code}")
            except requests.Timeout:
                print(f"Timeout accessing {absolute_url}")
            except requests.RequestException as e:
                print(f"Error accessing {absolute_url}: {e}")

            sleep(1)  # Delay between requests to avoid overwhelming the server
    ''' 
    #check each link if it is broken or not
    for link in all_links:
        #extract url from href attribute
        url = link.get_attribute('href')

        #send request to the url and get the result
        result = requests.head(url)

        #if status code is not 200 then print the url (customize the if condition according to the need)
        if result.status_code != 200:
            print(url, result.status_code)
    '''