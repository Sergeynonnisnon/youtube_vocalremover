
import pytube
from selenium import webdriver

URL='https://www.youtube.com/watch?v=dQw4w9WgXcQ'
filename ='nevergiveup'

#thise script download audio from youtube.com and processing on  https://vocalremover.org

def get_audio (URL,filename):
    yt = pytube.YouTube(URL)
    streams = yt.streams
    audio_best = streams.filter(only_audio=True).desc().first()
    print ('Готово')
    return audio_best.download(filename=filename)

def main():
    driver = webdriver.Firefox('/geckodriver.exe')
    print(driver.get("https://vocalremover.org/en/"))
    upl_btn = driver.find_element_by_class_name(name='upload')
    print (upl_btn)

if __name__=='main':
    main()









