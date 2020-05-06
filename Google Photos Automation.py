import time
from selenium import webdriver
import pyautogui
from selenium.webdriver.common.keys import Keys
import os

#
# driver = webdriver.Chrome()
# driver.get("https://photos.google.com/u/1/")
# time.sleep(10)
# gp_button = driver.find_element_by_xpath('//*[@id="js-hero-btn"]')
# gp_button.click()
# time.sleep(10)
# enter_username = driver.find_element_by_xpath('//*[@id="identifierId"]')
# enter_username.click()
# time.sleep(10)
# username = "stefhonjc@gmail.com"
# for i in username:
#     pyautogui.typewrite(i)
#     time.sleep(2)
# time.sleep(10)
# next_button = driver.find_element_by_xpath('//*[@id="identifierNext"]/span/span')
# next_button.click()
# first_pic = driver.find_element_by_xpath('//*[@id="ow129"]/div[1]/div[2]/div[1]/div[2]/a/div')
# first_pic.click()
# more_options_tab = driver.find_element_by_xpath("")
# more_options_tab.click()
# download_button = driver.find_element_by_xpath("")
# download_button.click()
#
#

x_times = int(input("How many times do you want to loop?:   "))

time.sleep(14)

pyautogui.FAILSAFE = False

# click the first image on the far left
pyautogui.moveTo(189, 441, duration=0.50)
pyautogui.click()
time.sleep(3)
# click the more options buttons
pyautogui.moveTo(1422, 165, duration=0.50)
pyautogui.click()
time.sleep(2)
# click the download button
pyautogui.moveTo(1328, 240, duration=0.50)
pyautogui.click()
time.sleep(3)
# opens the arrow button to show the show folder
pyautogui.moveTo(250,1050, duration=0.50)
pyautogui.click()
time.sleep(3)
# clicks show in folder
pyautogui.moveTo(250,950, duration=0.50)
pyautogui.click()
time.sleep(3)
# copies the image file
pyautogui.hotkey('ctrl', 'c')
time.sleep(3)
# close the file explore window
pyautogui.hotkey('ctrl', 'w')
time.sleep(2)
# opens the python program file
os.startfile("c:/Users/kiki/PycharmProjects/Procore Bot System")
time.sleep(3)
# pastes the file in the clipboard
pyautogui.hotkey('ctrl', 'v')
time.sleep(2)
# closes the pop up window
pyautogui.hotkey('ctrl', 'w')
time.sleep(2)
# click on the next photo button
pyautogui.moveTo(1400, 572, duration=0.50)
pyautogui.click()
time.sleep(2)

for number in range(x_times):
    # looping code next
    # downloads the next picture
    pyautogui.hotkey('shift', 'd')
    time.sleep(4)
    # opens the arrow button to show the show folder
    pyautogui.moveTo(250,1050, duration=0.50)
    pyautogui.click()
    time.sleep(3)
    # clicks show in folder
    pyautogui.moveTo(250,950, duration=0.50)
    pyautogui.click()
    time.sleep(3)
    # copies the image file
    pyautogui.hotkey('ctrl', 'c')
    time.sleep(3)
    # close the file explore window
    pyautogui.hotkey('ctrl', 'w')
    time.sleep(2)
    # opens the python program file
    os.startfile("c:/Users/kiki/PycharmProjects/Procore Bot System")
    time.sleep(3)
    # pastes the file in the clipboard
    pyautogui.hotkey('ctrl', 'v')
    time.sleep(2)
    # closes the pop up window
    pyautogui.hotkey('ctrl', 'w')
    time.sleep(2)
    # click on the next photo button
    pyautogui.moveTo(1400, 572, duration=0.50)
    pyautogui.click()
    time.sleep(2)







