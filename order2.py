from selenium import webdriver
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains
import pyautogui

options = Options()
options.add_experimental_option("detach", True)
service = ChromeService(executable_path=ChromeDriverManager().install())

driver = webdriver.Chrome(service=service, options=options)
action = ActionChains(driver)

driver.implicitly_wait(3)

driver.get(url='https://jirory2.mallpie.kr/product/10000042')

email = 'jwkim@genieworks.net'
password = 'sellerd2$'

driver.find_element(By.XPATH, '//*[@id="__next"]/div/div/div/div/div[1]/div[2]/div[3]/button').click()
driver.find_element(By.XPATH, '//*[@id="__next"]/div/div/div/div[4]/form/div[1]/label/div/input').send_keys(email)
driver.find_element(By.XPATH, '//*[@id="__next"]/div/div/div/div[4]/form/div[2]/label/div/input').send_keys(password)
driver.find_element(By.XPATH, '//*[@id="__next"]/div/div/div/div[4]/form/button').click()

user_name = driver.find_element(By.XPATH, '//*[@id="__next"]/div/header/nav[2]/div[3]').text
print(user_name+'으로 로그인 완료')

driver.implicitly_wait(10)
driver.find_element(By.XPATH, '//*[@id="__next"]/div/div/div/div/div[1]/div[2]/div[3]/button').click()
print('주문서 진입')

cardpayment_btn = driver.find_element(By.XPATH, '//*[@id="__next"]/div/div/div[2]/div[6]/div[2]/div[1]/fieldset/div[1]/label/input')

action.move_to_element(cardpayment_btn).perform()
cardpayment_btn.click()
print('결제수단 : 카드')

driver.implicitly_wait(30)

pyautogui.press('end')
order_checkbox = driver.find_element(By.XPATH, '//*[@id="__next"]/div/div/div[2]/div[8]/div[3]/div/label/span[1]')
order_btn = driver.find_element(By.XPATH, '//*[@id="__next"]/div/div/div[2]/div[9]/button')
order_checkbox.click()
order_btn.click()

driver.implicitly_wait(10)

print('신한카드 pg 진입')
order_iframe = driver.find_element(By.ID, 'imp-iframe')
driver.switch_to.frame(order_iframe)

shinhan_iframe = driver.find_element(By.NAME, '토스페이먼츠 전자결제')
driver.switch_to.frame(shinhan_iframe)

driver.find_element(By.XPATH, '//*[@id="fanView"]/div[3]/div/div/a').click()
driver.find_element(By.XPATH, '//*[@id="app_pwd"]').click()

driver.find_element(By.XPATH, '//*[@id="nppfs-keypad-app_pwd"]/div/div[2]/img[4]').click()
driver.find_element(By.XPATH, '//*[@id="nppfs-keypad-app_pwd"]/div/div[2]/img[6]').click()
driver.find_element(By.XPATH, '//*[@id="nppfs-keypad-app_pwd"]/div/div[2]/img[4]').click()
driver.find_element(By.XPATH, '//*[@id="nppfs-keypad-app_pwd"]/div/div[2]/img[6]').click()
driver.find_element(By.XPATH, '//*[@id="nppfs-keypad-app_pwd"]/div/div[2]/img[9]').click()
driver.find_element(By.XPATH, '//*[@id="nppfs-keypad-app_pwd"]/div/div[2]/img[9]').click()
driver.find_element(By.XPATH, '//*[@id="nppfs-keypad-app_pwd"]/div/div[2]/img[15]').click()

driver.find_element(By.XPATH, '/html/body/div[2]/form/div[3]/div[3]/div/button').click()