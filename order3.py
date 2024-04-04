from selenium import webdriver
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains

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

driver.find_element(By.XPATH, '//*[@id="__next"]/div/header/nav[2]/div[3]').click()
driver.find_element(By.XPATH, '//*[@id="__next"]/div/div/div[2]/ul[3]/li[1]/div[2]').click()
driver.find_element(By.XPATH, '//*[@id="__next"]/div/div/div[2]/div/div/div[3]/div/div[1]/div[2]/div[3]/button[1]').click()
driver.find_element(By.XPATH, '//*[@id="__next"]/div[2]/form/div/div/div[1]/div[2]/button[2]').click()

cancel_msg = driver.find_element(By.XPATH, '//*[@id="__next"]/div[2]/div/div/div[1]/div[1]/div[2]/div[1]/h6').text
print(cancel_msg)
print('order3 pass')