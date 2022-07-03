from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import os
from time import sleep
import sys

def set_chrome_driver():
    appdata = os.getenv('APPDATA')
    appdata.replace("Roaming", "")
    appdata += r"Local\Google\Chrome\User Data\Default"    
    print(appdata)
    appdata = r"C:\Users\muhjh\AppData\Local\Google\Chrome\User Data\Default"
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument(r"user-data-dir="+appdata) #Path to your chrome profile
    chrome_options.add_argument("--window-size=10,10")
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
    driver.implicitly_wait(10)
    return driver

def login(id, pw):
    url = "https://nxlogin.nexon.com/common/login.aspx"
    driver.get(url)
    driver.find_element(By.ID, "txtNexonID").send_keys(id)
    driver.find_element(By.ID, "txtPWD").send_keys(pw)
    driver.find_element(By.ID, "txtPWD").send_keys(Keys.ENTER)
    while driver.current_url != url:
        sleep(0.1)
        

def SelectGame(title):
    if title in "메이플스토리":
        driver.get("https://maplestory.nexon.com/Home/Main")
        driver.find_element(By.CSS_SELECTOR, "#section02 > div > span > div > a").click()
    elif title in "서든어택":
        driver.get("https://sa.nexon.com/main/index.aspx")
        driver.find_element(By.CSS_SELECTOR, "#gamestart > a").click()

if len(sys.argv) != 4:
    print('아이디 비밀번호 게임명을 인자로 전달해주세요')
    exit()

driver = set_chrome_driver()
login(sys.argv[1], sys.argv[2])
sleep(1)
SelectGame(sys.argv[3])
sleep(10)
driver.close()