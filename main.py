# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

import time

from selenium import webdriver



def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    driver = webdriver.Chrome('/Users/password1234/chromedriver')  # Optional argument, if not specified will search path.

    driver.get('http://www.ebay-kleinanzeigen.de/');

    time.sleep(1)  # Let the user actually see something!

    # knopf = driver.find_element_by_xpath("/html/body/div[2]/div[2]/div[3]/span/div/div/div/div[3]/div[1]/button[1]/div")
    knopf = driver.find_element(By.XPATH, '//*[@id="gdpr-banner-accept"]')
    knopf.click()
    #
    time.sleep(1)  # Let the user actually see something!
    # //*[@id="site-signin"]/nav/ul/li[3]/a

    login_box = driver.find_element(By.XPATH, '//*[@id="site-signin"]/nav/ul/li[3]/a')
    login_box.click()

    time.sleep(5)

    username_box = driver.find_element(By.XPATH, '//*[@id="login-email"]')
    username_box.send_keys('lucidlifeug2@gmail.com')
    username_box.submit()
    time.sleep(1)
    password_box = driver.find_element(By.XPATH, '//*[@id="login-password"]')
    password_box.send_keys('nyqpob-xohgaD-nyhka7')
    password_box.submit()
    time.sleep(1)



    # search_box = driver.find_element(By.XPATH, '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input')
    #
    # search_box.send_keys('stuhl')
    #
    # search_box.submit()
    #
    # time.sleep(5)  # Let the user actually see something!

    #driver.quit()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/




driver = webdriver.Chrome('/path/to/chromedriver')  # Optional argument, if not specified will search path.

driver.get('http://www.google.com/');

time.sleep(5) # Let the user actually see something!

search_box = driver.find_element_by_name('q')

search_box.send_keys('ChromeDriver')

search_box.submit()

time.sleep(5) # Let the user actually see something!

driver.quit()