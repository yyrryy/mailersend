from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

path='C:/Users/anthony1/Desktop/pythony/selenium/chromedriver.exe'
driver=webdriver.Chrome(path)

def find(sel, n):
    dribver.find_element(By.sel, f'{n}')

def fill():
    print('filling data')
    find('NAME', 'ip').send_keys('test')
    # driver.find_element(By.NAME, 'ip').send_keys('')
    # driver.find_element(By.NAME, 'user').send_keys('')
    # driver.find_element(By.NAME, 'pass').send_keys('')
    # driver.find_element(By.CSS_SELECTOR , "input[type='radio'][value='NON']").click()
    # driver.find_element(By.ID, 'add').click
    # driver.find_element(By.NMAE, 'pause').send_keys(5)
    # driver.find_element(By.NMAE, 'pemails').send_keys(18)
    # driver.find_element(By.NMAE, 'reconnect').send_keys(18)
    # select = Select(driver.find_element(By.NAME, 'encodety'))
    # select.select_by_index(2)
    find('NAME', 'from')
    sleep(3)

mailer='https://www.samspedispa.com/admin/controller/extension/extension/bcc.php'
def init():
    driver.get(mailer)
    fill()

# pause
# pemails
# reconnect










#methode 1: open the tabs first
# for i in range(3):
#     print('start')
#     cmd=f'window.open("{mailer}","_blank")'
#     driver.execute_script(cmd)
#     fill()