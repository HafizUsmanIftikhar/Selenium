from webbrowser import Chrome
import undetected_chromedriver as uc
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.service import Service
from selenium.common.exceptions import NoSuchElementException,TimeoutException
from selenium.webdriver.common.proxy import Proxy, ProxyType
import webdriver_manager
from fp.fp import FreeProxy

# proxy = FreeProxy(country_id=['US', 'BR'], timeout=0.3, rand=True).get()


# proxy_ip_port = "106.122.8.54:3128"
# proxy = Proxy()
# proxy.proxy_type=ProxyType.MANUAL
# proxy.http_proxy=proxy_ip_port
# proxy.ssl_proxy=proxy_ip_port


# capabilities = webdriver.DesiredCapabilities.CHROME
# proxy.add_to_capabilities(capabilities)

# Initialize the Firefox driver with the Service object
options= webdriver.ChromeOptions()
options.add_argument('proxy_server=106.122.8.54.3128')
options.add_argument('--user-data-dir=/home/usman/.config/google-chrome/default')

#provide the profile name with which we want to open browser
options.add_argument(r'--profile-directory=Profile 1')
driver = uc.Chrome(options=options)


# your data
your_first_name = "usman"
your_last_name = "Ch"
your_username = "usman111username"
your_birthday = "02 1 1998"
your_gender = "1" # 1:F 2:M 3:Not say 4:Custom
your_password = "x,nscldsj123...FDKZ"

try:
    driver.get("https://accounts.google.com/signup")

    first_name = driver.find_element(By.NAME, "firstName")
    last_name = driver.find_element(By.NAME, "lastName")

    first_name.clear()
    first_name.send_keys(your_first_name)

    last_name.clear()
    last_name.send_keys(your_last_name)

    next_button = driver.find_element(By.CLASS_NAME, "VfPpkd-LgbsSe")
    next_button.click()

    wait = WebDriverWait(driver, 20)
    day = wait.until(EC.visibility_of_element_located((By.NAME, "day")))

    birthday_elements = your_birthday.split()

    month_dropdown = Select(driver.find_element(By.ID, "month"))
    month_dropdown.select_by_value(birthday_elements[1])

    day_field = driver.find_element(By.ID, "day")
    day_field.clear()
    day_field.send_keys(birthday_elements[0])

    year_field = driver.find_element(By.ID, "year")
    year_field.clear()
    year_field.send_keys(birthday_elements[2])

    gender_dropdown = Select(driver.find_element(By.ID, "gender"))
    gender_dropdown.select_by_value(your_gender)

    next_button = driver.find_element(By.CLASS_NAME, "VfPpkd-LgbsSe")
    time.sleep(1)
    next_button.click()

    try:
        create_own_option = wait.until(EC.element_to_be_clickable((By.ID, "selectionc2")))
        create_own_option.click()
    except (TimeoutException, NoSuchElementException):
        print('NO Skip add phone number page found')
    time.sleep(1)
    
    
    create_own_email = wait.until(EC.element_to_be_clickable((By.NAME, "Username")))
    username_field = driver.find_element(By.NAME, "Username")
    username_field.clear()
    username_field.send_keys(your_username)

    next_button = driver.find_element(By.CLASS_NAME, "VfPpkd-LgbsSe")
    next_button.click()

    password_field = wait.until(EC.visibility_of_element_located((By.NAME, "Passwd")))
    password_field.clear()
    password_field.send_keys(your_password)

    driver.implicitly_wait(60)

    password_confirmation_field = driver.find_element(By.NAME, "PasswdAgain")
    password_confirmation_field.clear()
    password_confirmation_field.send_keys(your_password)


    next_button = driver.find_element(By.CLASS_NAME, "VfPpkd-LgbsSe")
    next_button.click()



    print('Done')

    time.sleep(20)

    # Skip add phone number
    try:
        skip_button_is_visible = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "button span.VfPpkd-vQzf8d")))
        skip_button = driver.find_element(By.CSS_SELECTOR, "button span.VfPpkd-vQzf8d")
        skip_button.click()
    except NoSuchElementException:
        print('NO Skip add phone number page found')
        

    # Skip add recovery email
    try:
        skip_button_is_visible = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "button span.VfPpkd-vQzf8d")))
        skip_button = driver.find_element(By.CSS_SELECTOR, "button span.VfPpkd-vQzf8d")
        skip_button.click()
    except NoSuchElementException:
        print('NO Add recovery email')

    

    next_button = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "VfPpkd-LgbsSe")))
    next_button.click()

    # Agree on Google's privacies
    agree_button = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "button span.VfPpkd-vQzf8d")))
    agree_button.click()

    # Close the browser window at the end of your automation
    driver.quit()

    print("Your Gmail successfully created:\n{\ngmail: " + your_username + "@gmail.com\npassword: " + your_password + "\n}")


except Exception as e:
    # Close the browser window in case of failure
    driver.quit()
    print("Failed to create your Gmail, Sorry")
    print(e)