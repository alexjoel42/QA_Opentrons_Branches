from selenium import webdriver

from selenium.webdriver.common.by import By
from time import sleep

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# Todo Works until NEST 96 Deep Well Plate 2mL and the tube racks have different Xpaths for the button.
## Alex thoughts: Would be useful to see if we can search by the class name
## Agilent: driver.find_element(By.CLASS_NAME, '_clickable_icon_ccmtq_5 _info_button_ccmtq_44').click()
## For nest 96 deep_well driver.find_element(By.CLASS_NAME, "_clickable_icon_ccmtq_5 _info_button_ccmtq_44 _active_ccmtq_49").click()
## 41 is a separate one entirely "clickable_icon_ccmtq_5 _info_button_ccmtq_44" Opentrons 96 Deep Well Temperature Module Adapter
def get_dimensions_case_1(i):
    sleep(0.1)
    # Select Dropdown images
    dropdown_footprint = driver.find_element("xpath",
                                             "/html/body/div/div/div[2]/div/div/section/div[3]/section/div/div/div[3]/div[1]/button").click()
    sleep(0.1)
    # Does the footprint pop out at good size/exist?
    foot_print = driver.find_element("xpath",
                                     "/html/body/div/div/div[2]/div/div/section/div[3]/section/div/div/div[3]/div[2]/img[1]")
    if foot_print.size['height'] and foot_print.size['width'] > 100:
        pass
    else:
        return print("This picture isn't showing", foot_print.location, foot_print.size)
    sleep(0.1)

def get_dimensions_case_2(i):
    sleep(0.1)
    # Select Dropdown images
    dropdown_footprint = driver.find_element("xpath",
                                             "/html/body/div/div/div[2]/div/div/section/div[3]/section/div/div/div[3]/div[1]/button").click()
    sleep(0.1)
    # Does the image pop out at good size?

    foot_print = driver.find_element("xpath",
                                     "/html/body/div/div/div[2]/div/div/section/div[3]/section/div/div/div[3]/div[2]/img[1]")
    if foot_print.size['height'] and foot_print.size['width'] > 100:
        pass
    else:
        return print("This picture isn't showing", foot_print.location, foot_print.size)
    sleep(0.1)



## Actual code
with  webdriver.Chrome() as driver:
    # Options for URL
    driver.get("http://sandbox.labware.opentrons.com/labware-library@3.2.0-alpha.0/#/")
    # todo Maybe this is a better alternative to "sleep"
    ## wait = WebDriverWait(driver, 15)

    # Store the ID of the original window
    original_window = driver.current_window_handle

    # Check we don't have other windows open already
    assert len(driver.window_handles) == 1

    for i in range(1, 72):
        i = str(i)
        # Selects labware
        sleep(0.1)

        labware = driver.find_element("xpath", f'/html/body/div/div/div[2]/div/div/section/ul/li[{i}]/a/h2').click()
        sleep(1)

        print(i)

        # Back to Labware Library
        # <a class="_breadcrumbs_link_8pt8u_58" href="#/">Back to Labware Library</a>

        x = driver.find_element(By.LINK_TEXT, "Back to Labware Library").click()

        # #back_track_official_x_path = driver.find_element("xpath", "").click()
        sleep(0.1)
        ''' 
         if (int(i) > 60 or int(i) <= 18):
             get_dimensions_case_1(i)
         elif int(i) == 60:
             print("This is a sandbox error because there is no variable here")

         else:
             get_dimensions_case_2(i)

         sleep(1)
        '''
