from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from CONSTANTS import PAGENUMBER,SITEHTML,SECRET,VOUCHERPROGRAM
from time import sleep
from helpers.logins import getPass
from helpers.logs import lprint




class fetchData:
    def __init__(self):
        self.driver= webdriver.Firefox()
        self.driver.get("https://voucher.gov.gr/kekadmin/user/login")
        self._loadWait()
        self._login()
        self._loadWait()
        self._GetHtml() ##uncomment

    def _loadWait(self):
        try:
            WebDriverWait(self.driver, 15).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "#poweredby > img:nth-child(1)"))
            )
            return True
        except TimeoutError:
            lprint(f"{self.driver.current_url} didnt load properly" )
            return False
             

    def _login(self):
        usrename=getPass(SECRET)
        password=getPass(usrename)
        nameBox = self.driver.find_element(By.XPATH, '//*[@id="username"]')
        passBox= self.driver.find_element(By.XPATH, '//*[@id="password"]')
        nameBox.send_keys(usrename)
        passBox.send_keys(password)
        enterSite= self.driver.find_element(By.XPATH, '//*[@id="dologin"]')
        enterSite.click()
        print(self.driver.title)

    def _GetHtml(self):
        for i in range(1,PAGENUMBER+1):
            self.driver.get(f'{VOUCHERPROGRAM}{i}') #fstrings are cool.
            print(self.driver.title)
            self._loadWait()
            with open(f"{SITEHTML}{i}", "w" , encoding="utf-8") as file:
                file.write(self.driver.page_source)
    
    def getPageSource(self, page: int):
        print(f"file://{SITEHTML}{page}")
        self.driver.get(f"file://{SITEHTML}{page}") #change windows
        return self.driver.page_source


