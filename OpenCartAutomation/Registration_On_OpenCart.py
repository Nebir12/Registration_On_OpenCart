from selenium import webdriver
import time
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class Demo_cart_reg():
    def Registration(self):
        driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
        driver.maximize_window()
        driver.get("https://demo.opencart.com/")

        Myaccount_Btn = driver.find_element(By.CSS_SELECTOR, "#top > div.container > div.nav.float-end > ul > li:nth-child(2) > div > a > span")
        Myaccount_Btn.click()
        time.sleep(2)

        Register_Btn = driver.find_element(By.CSS_SELECTOR, "#top > div.container > div.nav.float-end > ul > li:nth-child(2) > div > ul > li:nth-child(1) > a")
        Register_Btn.click()
        time.sleep(2)

        Frist_Name_Btn = driver.find_element(By.NAME, "firstname")
        Frist_Name_Btn.send_keys("Omor")
        time.sleep(2)

        Last_Name_Btn = driver.find_element(By.NAME, "lastname")
        Last_Name_Btn.send_keys("Nebir")
        time.sleep(2)

        Email_Btn = driver.find_element(By.NAME, "email")
        Email_Btn.send_keys("ntahsan@gmail.com")
        time.sleep(2)

        Password_Btn = driver.find_element(By.NAME, "password")
        Password_Btn.send_keys("Araf1234")
        time.sleep(2)

        html = driver.find_element(By.XPATH, "/html")
        html.send_keys(Keys.END)
        time.sleep(2)

        Subscribe_Btn = driver.find_element(By.CSS_SELECTOR, "#input-newsletter-yes")
        Subscribe_Btn.click()
        time.sleep(2)

        html = driver.find_element(By.XPATH, "/html")
        html.send_keys(Keys.END)
        time.sleep(2)

        Privacy_Btn = driver.find_element(By.CSS_SELECTOR, "#form-register > div > div > div > input")
        Privacy_Btn.click()
        time.sleep(2)

        Continue_Btn = driver.find_element(By.CSS_SELECTOR, "#form-register > div > div > button")
        Continue_Btn.click()
        time.sleep(2)


test_obj = Demo_cart_reg()
test_obj.Registration()