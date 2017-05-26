from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pymongo

leng = 0

connection = pymongo.MongoClient("localhost", 27017)
db = connection.sunrin
collection  = db.phrasess
docs = collection.find({})

driver = webdriver.Chrome('./chromedriver.exe')
driver.implicitly_wait(3)

# url에 접근한다.
driver.get('https://accounts.kakao.com/login?continue=https://center-pf.kakao.com/signup')
driver.find_element_by_name('email').send_keys('iwin12372@gmail.com')
driver.find_element_by_name('password').send_keys('asdfasdfadsf!')
driver.find_element_by_xpath('//*[@id="btn_login"]').click()

driver.get('https://center-pf.kakao.com/_LZamd/chats')
driver.find_element_by_xpath('//*[@id="mArticle"]/div[2]/button').click()
driver.find_element_by_xpath('//*[@id="mArticle"]/div[2]/div[2]/div/div/li[1]/a').click()
driver.find_element_by_xpath('//*[@id="chatWrite"]')

try:
    element = WebDriverWait(driver, 10).until(
        EC.text_to_be_present_in_element_value((By.CSS_SELECTOR, "txt_cont"))
    )
finally:
    driver.quit()


#msg = driver.find_element_by_id('messageInput')
#msg.send_keys('asdef')
#msg.send_keys(Keys.ENTER)

#while:
html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')
notices = soup.select('#chatLogs')
leng = len(notices)
print(notices)
#print(''.join(notices[0].text.strip().split()))
