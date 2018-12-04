import time
import random
import pyautogui
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


options = Options()
options.add_argument("start-maximized")
options.add_argument("disable-infobars")

options.add_argument("--disable-notifications")
browser = webdriver.Chrome(chrome_options=options, executable_path=r'chromedriver.exe')


browser.get('https://www.instagram.com/accounts/login/?hl=en')
time.sleep(3)
pyautogui.click(625,194)#login field
time.sleep(1)
pyautogui.typewrite('your instagram username here')
pyautogui.click(593,242)#password field
time.sleep(1)
pyautogui.typewrite('your password')
time.sleep(1)

pyautogui.click(654,291)#login button

time.sleep(7)
pyautogui.click(659,542)#turn off notifications
time.sleep(1)
pyautogui.click(943,222)#your profile click
time.sleep(7)
pyautogui.click(809,276)#check all the people you are following
time.sleep(8)
d=1

while d<200:
    y=str(d)
    try:
        #/html/body/div[3]/div/div/div[2]/ul/div/li[1]/div/div[2]/button
        unfollow = browser.find_element_by_xpath('/html/body/div[3]/div/div/div[2]/ul/div/li['+y+']/div/div[2]/button')  # unfollow button
        unfollow.click()
        time.sleep(10)
        confirm=browser.find_element_by_xpath('/html/body/div[4]/div/div/div/div[3]/button[1]')
        confirm.click()

        time.sleep(random.randint(30,60))
        d+=1

    except Exception:
        pyautogui.click(864,580)
        continue
print("200 mofos succesully unfollowed")
