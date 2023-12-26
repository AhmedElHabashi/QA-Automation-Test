from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.webdriver.common.action_chains import ActionChains
import time
from selenium.webdriver.common.keys import Keys #to add somekeys
from selenium.webdriver.support.ui import Select #4 selections in comboboxx

# Configure the WebDriver on chrom
driver = webdriver.Chrome()

def BrowserConfigz():
    # Maximize the browser window
    driver.maximize_window()

# Test Scenario 2
def tst_validate_chkout_parameters():
    try:
#########################################################################################################################################
        # 1. Open the Vodafone eShop website.
        driver.get("https://eshop.vodafone.com.eg/en/prod/oppo-smart-phone-a-98-5-g?variantID=01HD3DKDDFJWWP04QFCA740MCG&Storage=256&Color=BLACK")
        print("Step 1: Open Vodafone Website with a random product")
        time.sleep(5)  # w8 for 7 sec untill i add the credintioals 
#########################################################################################################################################
        wait = WebDriverWait(driver, 5)
#########################################################################################################################################
        # 2. Click 'Add to Cart' (add the avilavble mobile to cart).
        add_to_cart_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Add To Cart')]")))
        add_to_cart_button.click()
        print("Step 2: Add the product to 'Add to Cart' - Completed")
        time.sleep(5)  # Wait for 5 seconds to have chance to 
#########################################################################################################################################
        # 3. Write username to login
        search_input = driver.find_element(By.ID, "username")
        # Search for the product
        search_input.send_keys("01011429000")
        print("Step 3: Typng the username (mobile num) - Completed")
        time.sleep(2)  # Wait for 2 seconds 
#########################################################################################################################################
        # 4 and 5. Write username to login
        search_input = driver.find_element(By.ID, "password")
        # Search for the product
        search_input.send_keys("W3d@AVVf22437",Keys.RETURN) #Writing the password and Press Enter
        print("Step 4, and 5 : typing the password '********' in the password txtbox then Press Enter- Completed")
        time.sleep(4)  # Wait for 2 seconds 
#########################################################################################################################################
        # # 6. Click el Trolly  (add the avilavble mobile to cart).
        cck_order_summery_image = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "img[src='assets/icon-center/shopping-trolley.svg']")))
        # Click the image
        cck_order_summery_image.click()
        time.sleep(4)  # Wait for 2 seconds 
        print("Step 6 : Now We are in the Cart Arrvied to thee cart for checking the Order Summery- Completed")

#########################################################################################################################################


        # # 7. Click el Trolly  (add the avilavble mobile to cart).
        Chk_Out_whatsin_cart = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "img[src='assets/images/wallet.svg']")))
        # Click the image
        Chk_Out_whatsin_cart.click()
        time.sleep(4)  # Wait for 2 seconds 
        print("Step 7 : Now we've passed to checking whats in the Cart- Completed")

#########################################################################################################################################
        # # 8. Here is the Option to Create a New Address for shipping the ordr.
        cart_image = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "img[src='../../../../assets/icon-center/add.svg']")))
        # Click the image
        cart_image.click()
        time.sleep(4)  # Wait for 2 seconds 
        print("Step 8 : Clicking the New Address - Completed")

#########################################################################################################################################
        
        # 9 Chhosing the Country from the countrt Comboooboxx
        select_city_element = driver.find_element(By.CSS_SELECTOR, "select[formcontrolname='city']")
        # Using Selenium's Select class for dropdown
        select_city = Select(select_city_element)
        # Choose the option "Alexandria" by value (assuming the value is "3")
        select_city.select_by_value("3")
        print("Step 9 : Selecting the Citiy - Assuming it will be shipped to Alex - Completed")
        time.sleep(1)  # Wait for 2 seconds 

#########################################################################################################################################
        # 10 Chhosing the District Place from the district Comboooboxx

        select_district_element = driver.find_element(By.CSS_SELECTOR, "select[formcontrolname='district']")
        # Using Selenium's Select class for dropdown
        select_district = Select(select_district_element)
        # Choose the option "Moharam Bek" by value (assuming the value is "61")
        # search_input.send_keys("mmm")
        select_district.select_by_value("61")
        time.sleep(4)  # Wait for 2 seconds 
        print("Step 10 : Selecting the District - Assuming it will be shipped to Moharm Bek - Completed")
        time.sleep(1)  # Wait for 2 seconds 

#########################################################################################################################################

        # 11 Adding the Streeeeet Nam
        street_name_element = driver.find_element(By.CSS_SELECTOR, "input[formcontrolname='streetName']")
        # Input the address into the text box
        street_name_element.send_keys("zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz")
        print("Step 11 : Setting the Address - Completed")
        time.sleep(1)  # Wait for 2 seconds 


#########################################################################################################################################

        # 12 Adding bulding Num to the textbo
        building_Num_element = driver.find_element(By.CSS_SELECTOR, "input[formcontrolname='buildingNo']")
        # Input the address into the text box
        building_Num_element.send_keys("zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz")
        print("Step 12 : Adding Building Num - Completed")
        time.sleep(1)  # Wait for 2 seconds 


#########################################################################################################################################

        # 13 adding Floot number to the textbox
        floor_num_element = driver.find_element(By.CSS_SELECTOR, "input[formcontrolname='floorNo']")
        # Input the address into the text box
        floor_num_element.send_keys("zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz")
        print("Step 13 : Adding Floor Number to the textbox - Completed")
        time.sleep(1)  # Wait for 2 seconds 




#########################################################################################################################################

        # 14 Chhosing the Country from the countrt Comboooboxx
        Apprat_num_element = driver.find_element(By.CSS_SELECTOR, "input[formcontrolname='appartmentNo']")
        # Input the address into the text box
        Apprat_num_element.send_keys("zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz")
        print("Step 14 : adding appratment number to the txt boxz - Completed")
        time.sleep(1)  # Wait for 2 seconds 



#########################################################################################################################################

        # 15 adding the landmark to the addr
        street_name_element = driver.find_element(By.CSS_SELECTOR, "input[formcontrolname='landmark']")
        # Input the address into the text box
        street_name_element.send_keys("zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz")
        print("Step 15 : Adding LandMark for the address - Completed")
        time.sleep(10)  # Wait for 2 seconds 

#########################################################################################################################################
        # # 16. Click 'Add to Cart' (add the avilavble mobile to cart).
        # save_address_button = driver.find_element(By.CSS_SELECTOR, "button.btn-primary.delievry--btn--checkout")
        # # Click the element using JavaScript
        # driver.execute_script("arguments[0].click();", save_address_button)
        # print("Step 16: Add the product to 'Add to Cart' - Completed")
        # time.sleep(5)  # Wait for 5 seconds to have chance see the changes

#########################################################################################################################################

        # # 17. Click 'Add to Cart' (add the avilavble mobile to cart).
        # Bk2_address_button = driver.find_element(By.CSS_SELECTOR, "btn-primary btn-submit")
        # # Click the element using JavaScript
        # driver.execute_script("arguments[0].click();", Bk2_address_button)
        # print("Step 18: Click Back to Address button to set a Vaild Address' - Completed")
        # time.sleep(5)  # Wait for 5 seconds to have chance see the changes

        # save_address_button = driver.find_element(By.CSS_SELECTOR, "button.btn-primary.delievry--btn--checkout")
        # # Click the element using JavaScript
        # driver.execute_script("arguments[0].click();", save_address_button)


#########################################################################################################################################









# #########################################################################################################################################
#Below tested with Valid Address and save address option .
# #########################################################################################################################################
#         # # 8. Here is the Option to Create a New Address for shipping the ordr.
#         cart_image = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "img[src='../../../../assets/icon-center/add.svg']")))
#         # Click the image
#         cart_image.click()
#         time.sleep(4)  # Wait for 2 seconds 
#         print("Step 8 : Clicking the New Address - Completed")

# #########################################################################################################################################
        
#         # 9 Chhosing the Country from the countrt Comboooboxx
#         select_city_element = driver.find_element(By.CSS_SELECTOR, "select[formcontrolname='city']")
#         # Using Selenium's Select class for dropdown
#         select_city = Select(select_city_element)
#         # Choose the option "Alexandria" by value (assuming the value is "3")
#         select_city.select_by_value("3")
#         print("Step 9 : Selecting the Citiy - Assuming it will be shipped to Alex - Completed")
#         time.sleep(1)  # Wait for 2 seconds 

# #########################################################################################################################################
#         # 10 Chhosing the District Place from the district Comboooboxx

#         select_district_element = driver.find_element(By.CSS_SELECTOR, "select[formcontrolname='district']")
#         # Using Selenium's Select class for dropdown
#         select_district = Select(select_district_element)
#         # Choose the option "Moharam Bek" by value (assuming the value is "61")
#         # search_input.send_keys("mmm")
#         select_district.select_by_value("61")
#         time.sleep(4)  # Wait for 2 seconds 
#         print("Step 10 : Selecting the District - Assuming it will be shipped to Moharm Bek - Completed")
#         time.sleep(1)  # Wait for 2 seconds 

# #########################################################################################################################################

#         # 11 Adding the Streeeeet Nam
#         street_name_element = driver.find_element(By.CSS_SELECTOR, "input[formcontrolname='streetName']")
#         # Input the address into the text box
#         street_name_element.send_keys("AliBek Streeeet")
#         print("Step 11 : Setting the Address - Completed")
#         time.sleep(1)  # Wait for 2 seconds 


# #########################################################################################################################################

#         # 12 Adding bulding Num to the textbo
#         building_Num_element = driver.find_element(By.CSS_SELECTOR, "input[formcontrolname='buildingNo']")
#         # Input the address into the text box
#         building_Num_element.send_keys("32")
#         print("Step 12 : Adding Building Num - Completed")
#         time.sleep(1)  # Wait for 2 seconds 


# #########################################################################################################################################

#         # 13 adding Floot number to the textbox
#         floor_num_element = driver.find_element(By.CSS_SELECTOR, "input[formcontrolname='floorNo']")
#         # Input the address into the text box
#         floor_num_element.send_keys("5")
#         print("Step 13 : Adding Floor Number to the textbox - Completed")
#         time.sleep(1)  # Wait for 2 seconds 




# #########################################################################################################################################

#         # 14 Chhosing the Country from the countrt Comboooboxx
#         Apprat_num_element = driver.find_element(By.CSS_SELECTOR, "input[formcontrolname='appartmentNo']")
#         # Input the address into the text box
#         Apprat_num_element.send_keys("503")
#         print("Step 14 : adding appratment number to the txt boxz - Completed")
#         time.sleep(1)  # Wait for 2 seconds 



# #########################################################################################################################################

#         # 15 adding the landmark to the addr
#         street_name_element = driver.find_element(By.CSS_SELECTOR, "input[formcontrolname='landmark']")
#         # Input the address into the text box
#         street_name_element.send_keys("AlEsraa Tower")
#         print("Step 15 : Adding LandMark for the address - Completed")
#         time.sleep(1)  # Wait for 2 seconds 

# #########################################################################################################################################
#         # 16. Click 'Add to Cart' (add the avilavble mobile to cart).
#         # save_address_button = driver.find_element(By.CSS_SELECTOR, "button.btn-primary.delievry--btn--checkout")
#         # # Scroll into view using JavaScript
#         # driver.execute_script("arguments[0].scrollIntoView();", save_address_button)
#         # # Click the "Save Address" button
#         # save_address_button.click()
#         # print("Step 2: Add the product to 'Add to Cart' - Completed")
#         # time.sleep(5)  # Wait for 5 seconds to have chance to 


#         # 16. Click 'Add to Cart' (add the avilavble mobile to cart).
#         save_address_button = driver.find_element(By.CSS_SELECTOR, "button.btn-primary.delievry--btn--checkout")
#         # Click the element using JavaScript
#         driver.execute_script("arguments[0].click();", save_address_button)
#         print("Step 16: Add the product to 'Add to Cart' - Completed")
#         time.sleep(5)  # Wait for 5 seconds to have chance see the changes

# #########################################################################################################################################

#         # 17. Click 'Add to Cart' (add the avilavble mobile to cart).
#         Bk2_address_button = driver.find_element(By.CSS_SELECTOR, "btn-primary btn-submit")
#         # Click the element using JavaScript
#         driver.execute_script("arguments[0].click();", Bk2_address_button)
#         print("Step 17: Click Back to Address button to set a Vaild Address' - Completed")
#         time.sleep(5)  # Wait for 5 seconds to have chance see the changes

# #########################################################################################################################################












    except Exception as e:
        print(e)

# Close the browser after all tests
def CloseTheBrowser():
    driver.quit()

if __name__ == "__main__":
    BrowserConfigz()
    tst_validate_chkout_parameters()
    CloseTheBrowser()
