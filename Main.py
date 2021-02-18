from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.action_chains import ActionChains 


from shutil import which
from PIL import Image 
import time

chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_path = which("./chromedriver")
driver = webdriver.Chrome(executable_path=chrome_path,options=chrome_options)

user_name = "ID_@gmail.com"
password = "password"
url = 'https://www.linkedin.com/'
file_name = 'Screen.png'
parameters_to_search = 'Muhammad Aadil'
Delay = 10

driver.get(url)

try: 
    Email = driver.find_element_by_xpath('(//input[@class="input__input"])[1]')
    Email.send_keys(user_name)
    time.sleep(2)

    Passw = driver.find_element_by_xpath('(//input[@class="input__input"])[2]')
    Passw.send_keys(password)
    time.sleep(2)

    Login_Button = driver.find_element_by_xpath('//button[@class="sign-in-form__submit-button"]')
    Login_Button.click()
    time.sleep(2)

    SearchInput = driver.find_element_by_xpath('//input[@class="search-global-typeahead__input always-show-placeholder"]')
    SearchInput.send_keys(parameters_to_search)
    time.sleep(5)

    driver.save_screenshot(file_name)
    image = Image.open(file_name)
    image.show()

except TimeoutException:
    print('Page is not loading')
finally:
    driver.quit()


