from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

options = Options()
options.add_experimental_option("detach", True)
service = ChromeService(executable_path=ChromeDriverManager().install())
options.add_extension('D:\\extensions\\MPBJKEJCLGFGADIEMMEFGEBJFOOFLFHL_2_0_1_0.crx')

driver = webdriver.Chrome(service=service, options=options)


driver.implicitly_wait(3)

driver.get(url='https://jirory2.mallpie.kr/')


driver.find_element(By.XPATH, '//*[@id="__next"]/div/header/nav[2]/div[3]/span').click()
driver.find_element(By.XPATH, '//*[@id="__next"]/div/div/div/div[4]/ul/li[1]').click()

try:
    # 캡챠 미발생 시 
    kakao_id = 'kk22jj22@gmail.com'
    kakao_pw = 'rlawl128'

    driver.find_element(By.XPATH, '//*[@id="loginId--1"]').send_keys(kakao_id)
    driver.find_element(By.XPATH, '//*[@id="password--2"]').send_keys(kakao_pw)
    driver.find_element(By.XPATH, '//*[@id="mainContent"]/div/div/form/div[4]/button[1]').click()
 
    driver.find_element(By.XPATH, '//*[@id="__next"]/div/header/nav[2]/div[3]').click()
    print('마이페이지 진입..')
    
    user_namenickname = driver.find_element(By.XPATH, '//*[@id="__next"]/div/div/div[2]/ul[1]/li/div[1]/div[1]').text
    user_email = driver.find_element(By.XPATH, '//*[@id="__next"]/div/div/div[2]/ul[1]/li/div[1]/div[2]').text

    if(user_namenickname) == '김지원(김지원ㅋㅋ)' and user_email == kakao_id:
        print(user_namenickname+', '+user_email+' 로그인 완료')
        print('login2 pass')
    else:
        print('login2 fail')
        print('사유 : '+user_namenickname+', '+user_email)

except NoSuchElementException as e: 
    
    #캡챠 발생 시
    print('캡챠 발생')
    driver.switch_to.frame(driver.find_element(By.XPATH, '//*[@id="captchaContainer"]/div/div/div/div/div/div/iframe'))
    driver.find_element(By.XPATH, '//*[@id="recaptcha-anchor"]/div[1]').click()
    
    # 캡챠 발생 후 예외처리 작성 필요

    
    if(user_namenickname) == '김지원(김지원ㅋㅋ)' and user_email == kakao_id:
        print(user_namenickname+', '+user_email+' 카카오 로그인 완료')
        print('login2 pass')
    else:
        print('login2 fail')
        print('사유 : '+user_namenickname+', '+user_email)

    
    
