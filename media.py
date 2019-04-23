import os,re
from datetime import datetime,timedelta
from dateutil.parser import parse
from dotenv import load_dotenv
from selenium import webdriver
import chromedriver_binary

def loan():
    # ========== 環境変数 ========== #
    BASE_URL = 'http://kosmos.lib.keio.ac.jp/primo_library/libweb/action/'
    LOAN_URL = r'https:\/\/keio-opac\.lib\.keio\.ac\.jp:443.*func=bor-loan&adm_library=KEI50'
    load_dotenv()
    UID = os.getenv('UID')
    PASSWD = os.getenv('PASSWD')

    # ========== オプション ========== #
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--single-process')
    
    # ========== Headless Chrome実行 ========== #
    driver = webdriver.Chrome(options=options)
    driver.get(BASE_URL+'search.do')
    
    # ========== ログイン ========== #
    login_url = driver.find_element_by_id('exlidSignOut').find_element_by_tag_name('a').get_attribute('href')
    driver.get(login_url)
    driver.find_element_by_name('keiojpuser').send_keys(UID)
    driver.find_element_by_name('keiojppassword').send_keys(PASSWD)
    table = driver.find_elements_by_class_name('button')[0]
    input = table.find_elements_by_tag_name('input')[0]
    input.submit()
    
    # ========== 貸出一覧 ========== #
    driver.get(BASE_URL+'myAccountMenu.do')
    iframe = driver.find_element_by_tag_name('iframe').get_attribute('src')
    driver.get(iframe)
    td = driver.find_element_by_class_name('td1')
    href = td.find_element_by_tag_name('a').get_attribute('href')
    # print(href)
    checkout_url = re.search(LOAN_URL, href).group()
    driver.get(checkout_url)
    # driver.save_screenshot('hoge.png')
    
    # ========== 更新 ========== #
    for i,tr in enumerate(driver.find_elements_by_tag_name('tr')):
        if i>=2:
            book_status(tr)
    a = driver.find_elements_by_class_name('text1')[1]
    a.click()
    # driver.get(login_url)
    
    # ========== スクショ ========== #
    driver.save_screenshot('screenshot.png')
    driver.quit()

def book_status(tr):
    # ========== 返却期限チェック ========== #
    td = tr.find_elements_by_tag_name('td')
    due = datetime.strptime(td[5].text,'%Y%m%d')
    tomorrow = datetime.today() + timedelta(days=1)
    if tomorrow >= due:
        td[1].find_element_by_tag_name('input').click()
    else:
        print(due - tomorrow)

if __name__ == "__main__":
    loan()
