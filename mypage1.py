from selenium import webdriver
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains

#mypage1 : 상품 찜하기 > 상품 찜 삭제 확인 시나리오

options = Options()
options.add_experimental_option("detach", True)
service = ChromeService(executable_path=ChromeDriverManager().install())

driver = webdriver.Chrome(service=service, options=options)
action = ActionChains(driver)

email = 'jwkim@genieworks.net'
password = 'sellerd2$'

driver.implicitly_wait(3)

driver.get(url='https://jirory4.mallpie.kr/')
driver.maximize_window()

try:
    driver.find_element(By.XPATH, '//*[@id="__next"]/div/header/nav[2]/div[3]/span').click()
    driver.find_element(By.XPATH, '//*[@id="__next"]/div/div/div/div[4]/form/div[1]/label/div/input').send_keys(email)
    driver.find_element(By.XPATH, '//*[@id="__next"]/div/div/div/div[4]/form/div[2]/label/div/input').send_keys(password)
    driver.find_element(By.XPATH, '//*[@id="__next"]/div/div/div/div[4]/form/button').click()

    user_name = driver.find_element(By.XPATH, '//*[@id="__next"]/div/header/nav[2]/div[3]').text
    print(user_name+'으로 로그인 완료')

    driver.implicitly_wait(10)

    driver.get(url='https://jirory4.mallpie.kr/product/10001661')

    ProductName = driver.find_element(By.XPATH, '//*[@id="__next"]/div/div/div/div/div[1]/div[2]/div[1]/div[1]/div[1]/h3').text
    ProductPrice = driver.find_element(By.XPATH, '//*[@id="__next"]/div/div/div/div/div[1]/div[2]/div[1]/div[1]/div[3]/div[1]/div[2]').text
    driver.find_element(By.XPATH, '//*[@id="__next"]/div/div/div/div/div[1]/div[2]/div[1]/div[1]/div[3]/div[2]/button[1]').click()
    print(ProductName+', '+ProductPrice+' 상품 찜하기 완료')

    print('마이페이지 > 찜한 상품 진입..')
    driver.find_element(By.XPATH, '//*[@id="__next"]/div/header/nav[2]/div[3]').click()
    driver.find_element(By.XPATH, '//*[@id="__next"]/div/div/div[2]/ul[2]/li[3]/div[2]').click()

    ZzimProductInfo = driver.find_element(By.XPATH, '//*[@id="__next"]/div/div/div[2]/div[2]/div/div/div/div/div[2]').text
    
    if (ProductName in ZzimProductInfo) and (ProductPrice in ZzimProductInfo) :        
        print('상품 찜하기 완료. 찜한 상품 삭제 처리..')
        driver.find_element(By.XPATH, '//*[@id="__next"]/div/div/div[2]/div[2]/div/div/div/button/span').click()
        driver.find_element(By.XPATH, '//*[@id="__next"]/div[2]/div/div[1]/div[3]/button[2]').click()
        
        delete_message = driver.find_element(By.XPATH, '//*[@id="__next"]/div[2]/div/div[1]/div[2]').text
        
        if ('삭제되었습니다' in delete_message) :
            print(delete_message)
            driver.find_element(By.XPATH, '//*[@id="__next"]/div[2]/div/div[1]/div[3]/button').click()            
            print('찜 삭제 완료')
            print('mypage1 pass')
            
        else :
            print('mypage1 fail. 찜 삭제 안됨')
            
    else :
        print('mypage1 fail. 상품 정보 미포함')

except :
    print('mypage1 fail. 로그인/상품 정보를 확인해주세요')