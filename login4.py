from selenium import webdriver
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

options = Options()
options.add_experimental_option("detach", True)

service = ChromeService(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)

driver.implicitly_wait(3)

driver.get(url='https://jirory2.mallpie.kr/')

email = 'jwkim@genieworks.net'
password = 'sellerd2$'

driver.find_element(By.XPATH, '//*[@id="__next"]/div/header/nav[2]/div[3]/span').click()
driver.find_element(By.XPATH, '//*[@id="__next"]/div/div/div/div[4]/form/div[1]/label/div/input').send_keys(email)
driver.find_element(By.XPATH, '//*[@id="__next"]/div/div/div/div[4]/form/div[2]/label/div/input').send_keys(password)
driver.find_element(By.XPATH, '//*[@id="__next"]/div/div/div/div[4]/form/button').click()

user_name = driver.find_element(By.XPATH, '//*[@id="__next"]/div/header/nav[2]/div[3]').text
print(user_name+'으로 로그인 완료')

print('마이페이지 진입..')
driver.find_element(By.XPATH, '//*[@id="__next"]/div/header/nav[2]/div[3]').click()

print('로그아웃')
driver.find_element(By.XPATH, '//*[@id="__next"]/div/div[1]/div[2]/div/div[1]/div[2]').click()

print('로그인 페이지 진입')
driver.find_element(By.XPATH, '//*[@id="__next"]/div/header/nav[2]/div[3]/span').click()

login_page_message = driver.find_element(By.XPATH, '//*[@id="__next"]/div/div/div/div[3]').text

print(login_page_message)

if '몰파이의 마이몰 서비스로 만들어진 쇼핑몰 입니다.' in login_page_message :
    print('login4 pass')
else :
    print('login4 fail')