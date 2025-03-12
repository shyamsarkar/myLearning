# selenium 4
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

# selector 
from selenium.webdriver.common.by import By

# waiting to load complete full webpage
from selenium.webdriver.support.wait import WebDriverWait


# for waiting to close
import time

# for stopping auto closing
from selenium.webdriver.chrome.options import Options
options = Options()


driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get("http://localhost:8080/login")
print(driver.title)
# driver.implicitly_wait(5)


options.add_experimental_option("detach", False)
# options.add_argument("--start-maximized")
driver.maximize_window()

username = "super_admin1@francium.com"
password = "Password"


inputbox_username = WebDriverWait(driver, timeout=3).until(lambda d: driver.find_element(by=By.ID, value="standard-name"))
inputbox_username.send_keys(username)

inputbox_password = driver.find_element(by=By.ID, value="standard-password")
inputbox_password.send_keys(password)

submit_button = driver.find_element(By.TAG_NAME,"button")
submit_button.click()


inventory_link = WebDriverWait(driver, timeout=3).until(lambda d: driver.find_element(by=By.XPATH, value="/html/body/div/div/div[2]/div[1]/div/div/div/div/div[2]"))
inventory_link.click()


driver.get("http://localhost:8080/add-inventory")



# wait 100 seconds
time.sleep(100)