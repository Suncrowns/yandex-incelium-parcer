import time 
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import os 
import shutil

def dir_create(adr, dr):
    global esh
    pr1 = adr[21::]
    pr1 = pr1.split('/')
    esh = dr  
    for i in range(1, len(pr1)):
        os.mkdir(f'{esh}/{pr1[i]}')
        esh += f'/{pr1[i]}'
    os.mkdir(f'{esh}/lessons')


def login(drver, log, pasw):
    try:
        btn = driver.find_element('id', 'js-button')
        btn.click()
        time.sleep(5)
        email = driver.find_element('id', 'passp-field-login')
        email.send_keys(log)
        time.sleep(2)
    except:
        email = driver.find_element('id', 'passp-field-login')
        email.send_keys(log)
        time.sleep(2)

    btn = driver.find_element('id', 'passp:sign-in')
    btn.click()
    time.sleep(5)
    pas = driver.find_element('id', "passp-field-passwd")
    pas.send_keys(pasw)
    time.sleep(5)
    btn = driver.find_element('id', 'passp:sign-in')
    btn.click()
    time.sleep(5)


def main(driver, esh):
    file = open('1.html', 'w+', encoding='utf-8')
    tecst = str(driver.page_source)
    tecst1 = BeautifulSoup(tecst, features='lxml')
    refs = tecst1.find_all('a', {'class': 'link-list__link'})
    for i in refs:
        tecst = tecst.replace(str(i)[0:71], str(i)[0:71] + '/1.html')
    file.write(tecst)
    file.close()
    try:
        shutil.move(str(os.getcwd()) + '/1.html', esh)
    except:
        pass
    for i in range(30, 47):
        flag = False
        themes = driver.find_elements(By.CLASS_NAME, 'link-list__link')
        time.sleep(5)
        
        print(i)
        if i != 2 and i != 11 and i != 17 and i != 27 and i != 30 and i != 31:
             flag = True 
        theme = themes[i]
        theme.click() 
        time.sleep(5)

        tecst = str(driver.page_source)
        tecst1 = BeautifulSoup(tecst, features='lxml')
        
        ref = tecst1.find('a', {'class': 'nav-tab nav-tab_back nav-tab_view_button'})
        ref1 = tecst1.find('a', {'class': 'material-list__material-link'})
        refs2 = tecst1.find_all('a', {'class': 'student-task-list__task'})
        for i in refs2:
            tecst = tecst.replace(str(i)[:91], str(i)[:91] + '/1.html')
        
        tecst = tecst.replace(str(ref1)[59:100], str(ref1)[59:100] + '/1.html')
        tecst = tecst.replace(str(ref)[0:83], 'testdir/' + str(ref)[0:83] + '/1.html')

        os.mkdir(esh + '/lessons/' + str(driver.current_url).split('/')[-1])
        rl1 = esh + '/lessons/' + str(driver.current_url).split('/')[-1]
        os.chdir('D:/' + str(driver.current_url)[22:len(str(driver.current_url))])
        dr1488 = 'D:/' + str(driver.current_url)[22:len(str(driver.current_url))]
        
        file = open('1.html', 'w+', encoding='utf-8')
        file.write(tecst)
        file.close()
        
        if flag == True:

            time.sleep(2)
            btn_prekol = driver.find_element(By.CLASS_NAME, 'material-list__material-link')
            btn_prekol.click() 
            time.sleep(5)

            rl = (str(driver.current_url)).split('/')[-1]
            rf = '' 
            
            for _ in range(len(((str(ref1)[59:100]).split('/'))) - 3, len(((str(ref1)[59:100]).split('/'))) - 1):
                rf += ((str(ref1)[59:100]).split('/'))[_] + '/'
            os.mkdir(dr1488 + '/' + ((str(ref1)[59:100]).split('/'))[-2])
            os.mkdir(dr1488 + '/' + ((str(ref1)[59:100]).split('/'))[-2] + '/' + ((str(ref1)[59:100]).split('/'))[-1])
            os.chdir(dr1488 + '/' + ((str(ref1)[59:100]).split('/'))[-2] + '/' + ((str(ref1)[59:100]).split('/'))[-1])
            tecst = str(driver.page_source)
            tecst1 = BeautifulSoup(tecst, features='lxml')
            ref = tecst1.find('a', {'class': 'nav-tab nav-tab_back nav-tab_view_button'})
            ref1488 = ref 
            tecst = tecst.replace(str(ref)[59:96], str(ref)[59:96] + '/1.html')
            
            file = open('1.html', 'w+', encoding='utf-8')
            file.write(tecst)
            file.close()
            
            driver.find_element(By.XPATH, '/html[1]/body[1]/div[2]/div[1]/div[2]/div[2]/div[1]/div[1]/main[1]/div[1]/a[1]').click()
        else:
            pass
            
        time.sleep(5)
        
        for i in range(len(driver.find_elements(By.CLASS_NAME, 'student-task-list__task'))):
            print(i, len(driver.find_elements(By.CLASS_NAME, 'student-task-list__task')))
            btns_prekol = driver.find_elements(By.CLASS_NAME, 'student-task-list__task')
            btns_prekol[i].click()
            time.sleep(5)
            
            url = str(driver.current_url).split('/')[3:]
            rf = 'D:/'
            for i in url:
                rf += i + '/'
                try:
                    os.mkdir(rf)
                except:
                    os.chdir(rf)
            os.chdir(rf)
            
            tecst = driver.page_source
            tecst1 = BeautifulSoup(tecst, features='lxml')
            ref = tecst1.find('a', {'class': 'nav-tab nav-tab_back nav-tab_view_button'})
            tecst = tecst.replace(str(ref)[:96], str(ref)[:96] + '/1.html')
            ref = tecst1.find('a', {'class': 'nav-tab nav-tab_view_button'})
            tecst = tecst.replace(str(ref)[:95], str(ref)[:95] + '/1.html')
            ref1488 = ref 

            file = open('1.html', 'w+', encoding='utf-8')
            file.write(tecst)
            file.close()

            ref = str(ref).split('/')[1:-3]
            try:
                ref.append(str(ref1488).split('/')[-3].split('"')[0])
                os.chdir('D:/')
                rf = 'D:/'
                for i in range(len(ref)):
                    rf += ref[i] + '/'
                    print(1161)
                    try:
                        os.mkdir(rf)
                    except:
                        os.chdir(rf)
                os.chdir(rf)
                
                driver.find_element(By.XPATH, '/html[1]/body[1]/div[2]/div[1]/div[2]/div[2]/div[1]/main[1]/div[1]/a[1]').click()
                time.sleep(3)

                tecst = driver.page_source
                tecst1 = BeautifulSoup(driver.page_source, features='lxml')
                ref = tecst1.find('a', {'class': 'nav-tab nav-tab_back nav-tab_view_button'})
                tecst = tecst.replace(str(ref)[:96], str(ref)[:96] + '/1.html')

                file = open('1.html', 'w+', encoding='utf-8')
                file.write(tecst)
                file.close()

                
            except:
                print(1488)
                pass 
            
            exit_btn = driver.find_element(By.XPATH, '/html[1]/body[1]/div[2]/div[1]/div[2]/div[2]/div[1]/main[1]/a[1]')
            exit_btn.click()
            time.sleep(2)

        driver.find_element(By.XPATH, '/html[1]/body[1]/div[2]/div[1]/div[2]/article[1]/div[1]/div[1]/div[1]/header[1]/a[1]').click()
        
        time.sleep(5)


dr = "D:" + '/' 
esh = ''
adr = input('Введите адрес вашего обзора курса в яндекс лицее: ')
dir_create(adr, dr)

driver = webdriver.Chrome()

driver.get('https://lms.yandex.ru/courses/1053/groups/8737')
time.sleep(2)
log, pas = str(input('Введите ваш логин (почту вроде) и пароль через пробел: '))
login(driver, log, pas)
time.sleep(10)


main(driver, esh)
