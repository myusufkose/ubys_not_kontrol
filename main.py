from selenium import webdriver
from selenium.webdriver.chrome.service import service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import chromedriver_autoinstaller
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.common.keys import Keys
from chump import Application
from dotenv import load_dotenv
import os



load_dotenv()
api_key = os.getenv("app_api_key")
user_secret = os.getenv("user_secret_api_key")
app = Application(api_key)
user = app.get_user(user_secret)
class ubys:
    def __init__(self):
        chrome_options = Options()
        chrome_options.add_argument("--use-fake-ui-for-media-stream")
        self.browser = webdriver.Chrome(options=chrome_options)
        self.browser.get("https://ubys.comu.edu.tr//Home/Index?ReturnUrl=https://ubys.comu.edu.tr//AIS/Student/Class/Index?sapid=8bY0b81coEBfsGIw5W2x6A!xGGx!!xGGx!#")
        self.browser.minimize_window()
        self.tc_no = os.getenv("ubys_tc_no")
        self.password = os.getenv("ubys_password")

    def giris(self):
            flag = True
            i = 0
            while flag:
                i+=1
                print(i)
                try:
                    self.browser.find_element(By.ID, "username").send_keys(self.tc_no)
                    self.browser.find_element(By.ID, "password").send_keys(self.password)
                    self.browser.find_element(By.ID, "password").send_keys(Keys.ENTER)
                    print(i)
                    flag = False
                except:
                    pass
            
    def gano_al(self,dk):
            self.browser.refresh()
            flag = True
            i = 0
            s = 0
            while flag:
                try:
                    text = self.browser.find_element(By.XPATH, "/html/body/div[2]/div[2]/div[2]/div/div[2]/div[4]/div[1]/div/div[1]/h4/b").text
                    
                    if text == "2024 - Güz - YANO: 3,18":
                        if dk:
                            for s in range(1):
                                message = user.send_message("30 dk oldu")
                                print(message.is_sent, message.id, str(message.sent_at))
                    else:
                        for s in range(10):
                            message = user.send_message("Not Girildi")
                            print(message.is_sent, message.id, str(message.sent_at))
                    print(text)
                    i+=1
                    flag = False
                except:
                    pass
            


sss = ubys()
sss.giris()
i = 0
while True:
    x = i% 6
    a = True
    
    if i % 6 == 0:
        print("i % 6 = ")
        print(x)
        a = True
    else:
         a = False
    print("a = ")
    print(a)
    sss.gano_al(a)
    time.sleep(300)   
    i+=1  
