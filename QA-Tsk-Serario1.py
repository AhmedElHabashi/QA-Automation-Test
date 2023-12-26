from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.webdriver.common.action_chains import ActionChains
import time

# Configure the WebDriver on chrom
driver = webdriver.Chrome()

def BrowserConfigz():
    # Maximize the browser window
    driver.maximize_window()

# Test Scenario 1
def tst_search_4_product_usng_selection():
    try:
#########################################################################################################################################
        # 1. Open the Vodafone eShop website.
        driver.get("https://eshop.vodafone.com.eg/en")
        print("Step 1: Opened the Vodafone eShop website - Completed")
        time.sleep(7)  # w8 for 7 sec
#########################################################################################################################################
        # 2. Write in the search bar “samsung” and select from the search list “Samsung in Smart Phones”.
        search_input = driver.find_element(By.ID, "searchInput")
        # Search for the product
        search_input.send_keys("samsung")
        print("Step 2: Typed 'samsung' in the search bar - Completed")

        # w8 time to 20 sec
        wait = WebDriverWait(driver, 20)
#########################################################################################################################################
        # 3. Select "Samsung in Smart Phones Deals".
        wait.until(EC.presence_of_element_located((By.XPATH, "//div[p[text()='Samsung'] and p[text()=' In Smart Phones ']]"))).click()
        print("Step 3: Selected 'Samsung in Smart Phones Deals' - Completed")
        time.sleep(3)  # Wait for 7 seconds

#########################################################################################################################################
        # 4. Select "Oppo Tab".
        wait.until(EC.presence_of_element_located((By.XPATH, "//div[text()=' Oppo ']"))).click()
        print("Step 4: Selected 'Oppo Tab' - Completed")
        time.sleep(3)  # Wait for 7 seconds

#########################################################################################################################################

        # 5. Select the product “OPPO Smart Phone A98 (5G)”.
        partial_text = "OPPO Smart Phone A98 (5G)"
        element = wait.until(EC.presence_of_element_located((By.XPATH, f"//p[contains(text(), '{partial_text}')]")))
        # Scroll into view using JavaScript
        driver.execute_script("arguments[0].scrollIntoView();", element)

        try:
            # Click the element using regular click
            element.click()
            print("Step 5: Selected 'OPPO Smart Phone A98 (5G)' - Completed")
        except ElementClickInterceptedException:
            # If element click is intercepted, try using JavaScript click
            driver.execute_script("arguments[0].click();", element)
            print("Step 5: Selected 'OPPO Smart Phone A98 (5G)' using JavaScript click - Completed")

        # Wait for 3 seconds
        time.sleep(3)



        # 6. Click 'Add to Cart' (add the avilavble mobile to cart.
        add_to_cart_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Add To Cart')]")))
        add_to_cart_button.click()
        print("Step 9: Clicked 'Add to Cart' - Completed")
        time.sleep(5)  # Wait for 5 seconds

        print("First Senario Has been compleated successfully")


    except Exception as e:
        print(e)

# Close the browser after all tests
def CloseTheBrowser():
    driver.quit()

if __name__ == "__main__":
    BrowserConfigz()
    tst_search_4_product_usng_selection()
    CloseTheBrowser()
