from selenium import webdriver
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import re

#mypage2 : 닉네임 변경 동작 확인 시나리오

options = Options()
options.add_experimental_option("detach", True)
service = ChromeService(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)
action = ActionChains(driver)

driver.implicitly_wait(3)


email = 'jwkim@genieworks.net'
password = 'sellerd2$'

driver.get(url='https://jirory4.mallpie.kr/')
driver.maximize_window()

try:   
    driver.find_element(By.XPATH, '//*[@id="__next"]/div/header/nav[2]/div[3]/span').click()
    driver.find_element(By.XPATH, '//*[@id="__next"]/div/div/div/div[4]/form/div[1]/label/div/input').send_keys(email)
    driver.find_element(By.XPATH, '//*[@id="__next"]/div/div/div/div[4]/form/div[2]/label/div/input').send_keys(password)
    driver.find_element(By.XPATH, '//*[@id="__next"]/div/div/div/div[4]/form/button').click()

    user_name = driver.find_element(By.XPATH, '//*[@id="__next"]/div/header/nav[2]/div[3]').text
    print('로그인 완료')

    #Mypage 버튼 클릭 가능한 상태가 될 때까지 기다림
    wait = WebDriverWait(driver, 10)
    MypageBtn = driver.find_element(By.XPATH, '//*[@id="__next"]/div/header/nav[2]/div[3]')
    MypageBtnWait = wait.until(EC.element_to_be_clickable((MypageBtn))) 
    MypageBtn.click()
    print('마이페이지 진입..')

    info = driver.find_element(By.XPATH, '//*[@id="__next"]/div/div/div[2]/ul[1]/li/div[1]/div[1]').text    
    compile_info = re.compile('\\(([^)]+)')
    nickname = compile_info.findall(info)

    print('수정 전 닉네임 : '+''.join(nickname))
    newNickname = '지로리'

    #여기 클릭 안되는 이슈 수정 필요
    ProfileEditBtn = driver.find_element(By.XPATH, '//*[@id="__next"]/div/div/div[2]/ul/li[1]')
    ProfileEditBtnWait = wait.until(EC.element_to_be_clickable(ProfileEditBtn))
    ProfileEditBtn.click()
    print('마이페이지 > 프로필 변경 진입..')

    driver.find_element(By.XPATH, '//*[@id="__next"]/div/div/div[2]/form/div[2]/label/div').click()
    driver.find_element(By.XPATH, '//*[@id="__next"]/div/div/div[2]/form/div[2]/label/div').clear()
    driver.find_element(By.XPATH, '//*[@id="__next"]/div/div/div[2]/form/div[2]/label/div').send_keys(newNickname)
    
    ProfileChgBtn = driver.find_element(By.XPATH, '//*[@id="__next"]/div/div/div[2]/form/button')
    action.move_to_element(ProfileChgBtn).perform()   
    ProfileChgBtn.click()
    
    confirmMsg = driver.find_element(By.XPATH, '//*[@id="__next"]/div[2]/div/div[1]/div[2]').text
    if('프로필변경이 완료되었습니다' in confirmMsg) :
        driver.find_element(By.XPATH, '//*[@id="__next"]/div[2]/div/div[1]/div[3]/button').click()
        
        newInfo = driver.find_element(By.XPATH, '//*[@id="__next"]/div/div/div[2]/div[1]/div[1]').text
        
        if(newNickname in newInfo) :
            print('mypage2 pass. '+newNickname+'(으)로 닉네임 변경 완료')
            
            driver.find_element(By.XPATH, '//*[@id="__next"]/div/div/div[2]/ul/li[1]/div[1]').click()
            driver.find_element(By.XPATH, '//*[@id="__next"]/div/div/div[2]/form/div[2]/label/div/input').clear()
            driver.find_element(By.XPATH, '//*[@id="__next"]/div/div/div[2]/form/div[2]/label/div/input').send_keys('지로리야')
            driver.find_element(By.XPATH, '//*[@id="__next"]/div/div/div[2]/form/button').click()
            
            print('닉네임 원복 완료')            
    else :
        print('mypage2 fail. 닉네임 변경 실패')
        
except NoSuchElementException as e:
    
    # 3개월간 동일 비밀번호 사용 시 나오는 페이지 진입 시 예외처리
    ChgPassword = driver.find_element(By.XPATH, '//*[@id="__next"]/div/div/div/div[1]').is_displayed()
    
    if(ChgPassword == True) :
        laterBtn = driver.find_element(By.XPATH, '//*[@id="__next"]/div/div/div/form/div[4]/button[2]')
        action.move_to_element(laterBtn).perform()    
        laterBtn.click()
    else :
        print('NoSuchElementException')
except :
        print('mypage2 fail.')