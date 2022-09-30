from selenium import webdriver
import time
import pyautogui
import random

URL = "https://elgoog.im/t-rex/?bot"
num = random.randint(1, 2)
if num == 1:
    driver_path = "/Users/CKONG/Desktop/Python/msedgedriver.exe"
    driver = webdriver.Edge(executable_path=driver_path)
else:
    driver_path = "/Users/CKONG/Desktop/Python/chromedriver.exe"
    driver = webdriver.Chrome(executable_path=driver_path)

driver.get(URL)
time.sleep(2)
# Click UP button to start the game.
pyautogui.press('up')
width, height = pyautogui.size()
x = 420
# Need tolerance for pixel detection.
x1 = x
x2 = x-3
x3 = x+3
y = 572
is_continue = True
while is_continue:
    if pyautogui.pixelMatchesColor(x1, y, (50, 50, 50), tolerance=50) or pyautogui.pixelMatchesColor(x2, y, (50, 50, 50), tolerance=50) or pyautogui.pixelMatchesColor(x3, y, (50, 50, 50), tolerance=50):
        pyautogui.press('up')


    