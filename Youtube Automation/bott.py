from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time
import keyboard
import random

option = webdriver.ChromeOptions() 
option.add_argument('--disable-extensions')
option.add_argument("--mute-audio")
option.add_argument("window-size=900,650")
page = webdriver.Chrome(executable_path=r'C:/Users/Boran/Desktop/chromedriver_win32/chromedriver.exe',chrome_options=option)
actions = ActionChains(page)

video_tek_demo = ["https://www.youtube.com/watch?v=HwEydYq_kUQ"]

videolar =["https://www.youtube.com/watch?v=VuPoeyu7Ioo",
           "https://www.youtube.com/watch?v=U304ZOKHGz4",
           "https://www.youtube.com/watch?v=AjS_awV6tKI",
           "https://www.youtube.com/watch?v=H20rOhX141U",
           "https://www.youtube.com/watch?v=HwEydYq_kUQ"]

random_liste = [25,50,75]

"""def süre_hesaplama():
    video_süre = page.find_element_by_class_name("ytp-time-duration").text
    video_süre2 = video_süre.split(":")
    video_süre_dak = int(video_süre2[0])
    video_süre_san = int(video_süre2[1])
    video_toplam_san = (video_süre_dak*60)+video_süre_san
    return video_toplam_san"""



for y in range(len(videolar)):
 
 page.get(videolar[y])

 time.sleep(2)

 reklam_kontrol = 1 #Standart olarak başlangıçta reklam var olarak alır !!! 
 tıklama = page.find_element_by_xpath("/html/body/ytd-app/div/ytd-page-manager/ytd-watch-flexy/div[5]/div[1]/div/div[1]/div/div/div/ytd-player/div/div")
 kendiliginden_toplam_san = 0
 a = 0
 while True:
    try:
        # Buraya giriyorsak kesin bir reklam var demek 
        is_ad = page.find_element_by_class_name("ytp-ad-player-overlay")
        reklam_tıklama_sayfası = page.find_element_by_class_name("ytp-ad-visit-advertiser-button")
        print("Bu video da reklam var !!!!")
        
        tıklama.click()
        time.sleep(0.5)
        tıklama.click()

        # Aşağıdaki try exceptler reklamın türü neyse onu bulacak olanlar
        try:
            # burası skip edilen reklamlar
            skip_ad_text = page.find_element_by_class_name("ytp-ad-skip-button-text").text
            print("Atlanabilen reklam var !")
            if skip_ad_text == "":
                print("Atlanabilen reklam yok !")
            else:
                print("Atlama butonu var")
                skip_ad_button = page.find_element_by_class_name("ytp-ad-skip-button-text").text
                atlanabilen_süre = page.find_element_by_class_name("ytp-time-duration").text
                atlanabilen_süre2 = atlanabilen_süre.split(":")
                atlanabilen_dak = int(atlanabilen_süre2[0])
                atlanabilen_san = int(atlanabilen_süre2[1])
                atlanabilen_toplam_san = (atlanabilen_dak*60)+atlanabilen_san
                print("Bu reklamı geçiyorum")
                skip_ad_button = page.find_element_by_class_name("ytp-ad-skip-button-text")
                reklam_tıklama_sayfası.click()
                keyboard.press_and_release("ctrl + 1")
                tıklama.click()
                tıklama.click()
                oran = random.choice(random_liste)
                time.sleep((atlanabilen_toplam_san*oran)/100)
                skip_ad_button.click()
                print("Reklamı geçtim")
                #tıklama.click()
                
        except:
            # burası kendiliğinden geçen reklamların yeri
            #! kendiliğinden geçen reklamlarda soldaki reklam linki bazen çıkmıyor ondan dolayı o reklamı saymaya çalııyor

            kendiliginden = page.find_element_by_class_name("ytp-ad-preview-text").text
            kendiliginden_süre = page.find_element_by_class_name("ytp-time-duration").text

            if a == 0:
                reklam_tıklama_sayfası.click()
                keyboard.press_and_release("ctrl + 1")
                tıklama.click()
                tıklama.click()
                a = 1
            
            kendiliginden_süre2 = kendiliginden_süre.split(":")
            kendiliginden_dak = int(kendiliginden_süre2[0])
            kendiliginden_san = int(kendiliginden_süre2[1])
            kendiliginden_toplam_san = (kendiliginden_dak*60)+kendiliginden_san
            print("Reklam suresi toplam "+str(kendiliginden_toplam_san)+" saniye.")
    
    #reklam bulamaz ise buraya girer
    except:
        reklam_kontrol = 0
        time.sleep(0.5)
        try:
            denemeyi_atla = page.find_element_by_id("dismiss-button")
            denemeyi_atla.click()
        except:
            print("Preminum deneme butonu bulunamadı !")
            
        print("Reklam bulamadım ya da bitti !!!.")
        if y == 0:
            print("Bu "+str(y+1)+". video !!!")
            tıklama.click()
        if y != 0:
            print("Bu "+str(y+1)+". video !!!")
            tıklama.click()
            time.sleep(0.5)
            tıklama.click()

        break

    time.sleep(1)

    
 #Videonun süresini çekme ve saniye cinsinden hesaplatma
 video_süre = page.find_element_by_class_name("ytp-time-duration").text
 video_süre2 = video_süre.split(":")
 video_süre_dak = int(video_süre2[0])
 video_süre_san = int(video_süre2[1])
 video_toplam_san = (video_süre_dak*60)+video_süre_san



 #Videonun ve reklamların zamanı için oluşturulan sayaç !!!
 for i in range(video_toplam_san):
      if reklam_kontrol == 1:
          sayac = (video_toplam_san-i)
      if reklam_kontrol == 0:
          sayac = (video_toplam_san-i)
      print(sayac)
      
      try:
          alt_orta_reklam_banner = page.find_element_by_class_name("ytp-ad-overlay-image")
          alt_orta_reklam_banner.click()
          keyboard.press_and_release("ctrl + 1")
          tıklama.click()
          alt_orta_reklam_banner_kapatma = page.find_element_by_xpath("/html/body/ytd-app/div/ytd-page-manager/ytd-watch-flexy/div[5]/div[1]/div/div[1]/div/div/div/ytd-player/div/div/div[4]/div[2]/div/div[3]/div[2]/button")
          alt_orta_reklam_banner_kapatma.click()
        
      except:
          pass

      try:
          tekrar_oynat = page.find_element_by_class_name("ytp-play-button").get_attribute("title")
          if tekrar_oynat == "Tekrar Oynat":
              break
      except:
          pass
   
      time.sleep(1)
      if sayac == 0:
         break

 print(str(y+1)+". Video bitti sıradakine geçiliyor.")


 #! ytp-ad-overlay-title    ytp-ad-overlay-close-container



 
   

