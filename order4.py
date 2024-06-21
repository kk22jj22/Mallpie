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

try :
    email = 'jwkim@genieworks.net'
    password = 'sellerd2$'

    driver.get(url='https://jirory4.mallpie.kr/')
    driver.maximize_window()

    driver.find_element(By.XPATH, '//*[@id="__next"]/div/div/div/div/div[1]/div[2]/div[3]/button').click()
    driver.find_element(By.XPATH, '//*[@id="__next"]/div/div/div/div[4]/form/div[1]/label/div/input').send_keys(email)
    driver.find_element(By.XPATH, '//*[@id="__next"]/div/div/div/div[4]/form/div[2]/label/div/input').send_keys(password)
    driver.find_element(By.XPATH, '//*[@id="__next"]/div/div/div/div[4]/form/button').click()

    user_name = driver.find_element(By.XPATH, '//*[@id="__next"]/div/header/nav[2]/div[3]').text
    print(user_name+'으로 로그인 완료')

    driver.implicitly_wait(10)
    
    driver.get(url='https://jirory4.mallpie.kr/product/10001661')
    ProductName = driver.find_element(By.XPATH, '//*[@id="__next"]/div/div/div/div/div[1]/div[2]/div[1]/div[1]/div[1]').text
    ProductPrice = driver.find_element(By.XPATH, '//*[@id="__next"]/div/div/div/div/div[1]/div[2]/div[3]/div[1]/div').text
    print('상품명 : '+ProductName+', 가격 : '+ProductPrice)


    print('주문서 진입')
    driver.find_element(By.XPATH, '//*[@id="__next"]/div/div/div/div/div[1]/div[2]/div[3]/button').click()
    bankpayment_btn = driver.find_element(By.XPATH, '//*[@id="__next"]/div/div/div[2]/div[6]/div[2]/div/fieldset/div[4]/label/input')

    action.move_to_element(bankpayment_btn).perform()
    bankpayment_btn.click()
    driver.implicitly_wait(30)

    pyautogui.press('end')
    driver.implicitly_wait(30)

    order_checkbox = driver.find_element(By.XPATH, '//*[@id="__next"]/div/div/div[2]/div[8]/div[3]/div/label/span[1]')
    order_btn = driver.find_element(By.XPATH, '//*[@id="__next"]/div/div/div[2]/div[9]/button')
    order_checkbox.click()
    order_btn.click()

    driver.implicitly_wait(30)

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
    print('주문 완료')
    
    isDisplayed = driver.find_element(By.XPATH, '//*[@id="__next"]/div/div/div/div[2]/button[2]').is_displayed()

    if isDisplayed == True :
        #마이페이지 > 주문내역 > 주문번호 확인 > 닫기
        driver.find_element(By.XPATH, '//*[@id="__next"]/div/header/nav[2]/div[3]').click()
        driver.find_element(By.XPATH, '//*[@id="__next"]/div/div/div[2]/ul[3]/li[1]/div[2]').click()
        Order_Num = driver.find_element(By.XPATH, '//*[@id="__next"]/div/div/div[2]/div/div/div[3]/div/div[1]/div[1]/div[1]/span').text
        print('주문번호 : '+Order_Num)
        
        driver.find_element(By.XPATH, '//*[@id="__next"]/div/div/div[2]/div/div/div[3]/div/div[1]/div[2]/div[3]/button[1]').click()
        driver.find_element(By.XPATH, '//*[@id="__next"]/div[2]/form/div/div/div[1]/div[2]/button[2]').click()        
        Cancel_Msg = driver.find_element(By.XPATH, '//*[@id="__next"]/div[2]/div/div/div[1]/div[1]/div[2]/div[1]/h6').text        
        driver.find_element(By.XPATH, '//*[@id="__next"]/div[2]/div/div/div[1]/div[2]/button').click()
        
        if(Cancel_Msg == '주문이 취소되었습니다.') :
            #취소/반품/교환 탭 진입
            driver.implicitly_wait(30)
            driver.find_element(By.XPATH, '//*[@id="__next"]/div/div/div[2]/ul/li[2]').click()
                               
            #주문번호 비교하고, 같다면 해당 주문번호 주문 상세 진입
            Cancel_Num = driver.find_element(By.XPATH, '//*[@id="__next"]/div/div/div[2]/div/div/div[2]/div/div[1]/div[1]/div[1]/span').text
            if(Order_Num == Cancel_Num) :
                driver.find_element(By.XPATH, '//*[@id="__next"]/div/div[1]/div[2]/div/div/div[2]/div/div[1]/div[1]/div[2]/p').click()
                
                #Cancel_Status == 취소완료, 취소 금액이 - + 'Product_Price라면' order3 Pass
                Cancel_Status = driver.find_element(By.XPATH, '//*[@id="__next"]/div/div/div[2]/ul/li/ul/li/div[1]/div').text
                Cancel_Price = driver.find_element(By.XPATH, '//*[@id="__next"]/div/div/div[2]/div[3]/div/div[3]/p[2]').text
                
                if(Cancel_Status == '취소완료') and (Cancel_Price == '-'+ProductPrice) :                  
                    print('주문번호 : '+Cancel_Num+', 상태 : '+Cancel_Status+', 취소 금액 : '+ProductPrice)
                    driver.implicitly_wait(30)
                    print('order4 pass. 주문 취소 완료')
                    driver.quit()
                    
                else :
                    print('order4 fail. 주문번호 불일치')
            else :
                print('order4 fail. 주문취소 되지 않음')
            
    else :
        print('order4 fail')
        driver.quit()


except NoSuchElementException as e :
    print('order4 fail. 로그인/상품 정보를 확인해주세요.')