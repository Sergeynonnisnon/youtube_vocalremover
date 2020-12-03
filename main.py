
import pytube
from selenium import webdriver
import os,time

URL='https://www.youtube.com/watch?v=dQw4w9WgXcQ'
filename ='nevergiveup'

#thise script download audio from youtube.com and processing on  https://vocalremover.org

driver = webdriver.Firefox()
driver.get('https://vocalremover.org')
upl_btn = driver.find_element_by_id(id_='input-audio-file').send_keys(os.getcwd() + "\\nevergiveup.webm")

def check_exists_by_xpath(xpath):
    try:
        driver.find_element_by_xpath(xpath)
    except :
        return False
    return True
for i in range(150):
    if check_exists_by_xpath('//*[@id="app"]/main/div[2]/button[2]') == True:
        driver.find_element_by_xpath('//*[@id="app"]/main/div[2]/button[2]').click()
        print('найдено')
        break
    else:
        print('не найдено')
        time.sleep(1)
      #player-codec second
#print(upl_btn)
def get_audio (URL,filename):
    yt = pytube.YouTube(URL)
    streams = yt.streams
    audio_best = streams.filter(only_audio=True).desc().first()
    print ('Готово')
    return audio_best.download(filename=filename)



#def main():


#if __name__=='main':
#    main()









