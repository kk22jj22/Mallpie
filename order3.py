from selenium import webdriver
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException
import pyautogui

options = Options()
options.add_experimental_option("detach", True)
service = ChromeService(executable_path=ChromeDriverManager().install())

driver = webdriver.Chrome(service=service, options=options)
action = ActionChains(driver)

driver.implicitly_wait(3)

try:
    driver.get(url='https://jirory4.mallpie.kr/')
    driver.maximize_window()

    email = 'jwkim@genieworks.net'
    password = 'sellerd2$'

    driver.find_element(By.XPATH, '//*[@id="__next"]/div/header/nav[2]/div[3]/span').click()
    driver.find_element(By.XPATH, '//*[@id="__next"]/div/div/div/div[4]/form/div[1]/label/div/input').send_keys(email)
    driver.find_element(By.XPATH, '//*[@id="__next"]/div/div/div/div[4]/form/div[2]/label/div/input').send_keys(password)
    driver.find_element(By.XPATH, '//*[@id="__next"]/div/div/div/div[4]/form/button').click()

    user_name = driver.find_element(By.XPATH, '//*[@id="__next"]/div/header/nav[2]/div[3]').text
    print(user_name+'으로 로그인 완료')

    # 옵션상품 - 2단
    # 상품 판매안함/삭제 시 예외처리
    # 옵션1번 클릭 > 품절이면 > 옵션2번 클릭 > 구매하기    
    driver.get(url='https://jirory4.mallpie.kr/product/10001651')
    driver.find_element(By.XPATH, '//*[@id="__next"]/div/div/div/div/div[1]/div[2]/div[2]/div/div/div').click()

    is_soldout = True
    is_soldout2 = True
    i = 1
    j = 1

    while is_soldout == True :     
        prd_option = driver.find_element(By.XPATH, '//*[@id="__next"]/div/div/div/div/div[1]/div[2]/div[2]/div/div/ul/li['+str(i)+']').text
        is_True = ('품절' in prd_option) or (prd_option == '')
        
        if is_True == True and is_soldout == True:
            is_soldout = True  

            i = i+1
            prd_option = driver.find_element(By.XPATH, '//*[@id="__next"]/div/div/div/div/div[1]/div[2]/div[2]/div/div/ul/li['+str(i)+']').click()
            
        else : 
            is_soldout = False
           
            prd_option = driver.find_element(By.XPATH, '//*[@id="__next"]/div/div/div/div/div[1]/div[2]/div[2]/div/div/ul/li[1]').click()
            driver.find_element(By.XPATH, '//*[@id="__next"]/div/div/div/div/div[1]/div[2]/div[2]/div[2]/div/div').click()
            
            while is_soldout2 == True :     
                prd_option2 = driver.find_element(By.XPATH, '//*[@id="__next"]/div/div/div/div/div[1]/div[2]/div[2]/div[2]/div/ul/li['+str(j)+']').text
                is_True2 = ('품절' in prd_option2) or (prd_option2 == '')
                
                if is_True2 == True and is_soldout2 == True:
                    is_soldout2 = True 

                    j = j+1
                    prd_option2 = driver.find_element(By.XPATH, '//*[@id="__next"]/div/div/div/div/div[1]/div[2]/div[2]/div[2]/div/ul/li['+str(j)+']').click()
                    
                else : 
                    is_soldout = False
                    
                    driver.find_element(By.XPATH, '//*[@id="__next"]/div/div/div/div/div[1]/div[2]/div[2]/div[2]/div/ul/li[1]').click()
                    pyautogui.press('pgdn')
                    driver.find_element(By.XPATH, '//*[@id="__next"]/div/div/div/div/div[1]/div[2]/div[3]/button').click()
                    
            break

    # 주문서 진입
    pyautogui.press('pgdn')
    
    bankpayment_btn = driver.find_element(By.XPATH, '//*[@id="__next"]/div/div/div[2]/div[6]/div[2]/div/fieldset/div[4]/label/input')
    action.move_to_element(bankpayment_btn).perform()
    bankpayment_btn.click()
    print('결제수단 - 무통장입금')
    driver.implicitly_wait(10)

    # 화면 최하단으로 이동
    pyautogui.press('end')
    driver.implicitly_wait(10)

    # 주문에 동의하는 체크박스 클릭
    order_checkbox = driver.find_element(By.XPATH, '//*[@id="__next"]/div/div/div[2]/div[8]/div[3]/div/label/span[1]')
    order_btn = driver.find_element(By.XPATH, '//*[@id="__next"]/div/div/div[2]/div[9]/button')
    driver.implicitly_wait(10)
    order_checkbox.click()
    order_btn.click()

    driver.implicitly_wait(10)

    print('tosspayments pg 진입')
    order_iframe = driver.find_element(By.ID, 'imp-iframe')
    driver.switch_to.frame(order_iframe)

    driver.find_element(By.XPATH, '//*[@id="__next"]/div[1]/main/section/section/ul/a[3]').click()
    driver.find_element(By.XPATH, '//*[@id="input-:r9:-:ra:"]/span').click()
    pyautogui.press('down')
    pyautogui.press('down')
    pyautogui.press('down')
    pyautogui.press('enter')

    driver.find_element(By.XPATH, '//*[@id="__next"]/div[1]/main/div/div[2]/form/div[2]/div/div[1]/div/label').click()
    driver.find_element(By.XPATH, '//*[@id="__next"]/div[1]/main/div/div[2]/form/div[2]/button').click()

    driver.implicitly_wait(20)
    driver.switch_to.default_content()

    isDisplayed = driver.find_element(By.XPATH, '//*[@id="__next"]/div/div/div/div[2]/button[2]').is_displayed()

    if isDisplayed == True :
        driver.find_element(By.XPATH, '//*[@id="__next"]/div/div/div/div[2]/button[2]').click()
        order_num = driver.find_element(By.XPATH, '//*[@id="__next"]/div/div/div[2]/div/div/div[3]/div/div[1]/div[1]/div[1]/span').text
        print('주문번호 : '+order_num)
        print('order3 pass')

    else :
        print('order3 fail. 주문완료 실패.')

except NoSuchElementException as e :
    print('order3 fail. 로그인/상품 상태를 확인해주세요')