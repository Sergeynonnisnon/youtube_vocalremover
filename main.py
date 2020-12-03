
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
    driver = webdriver.Chrome()
    driver.get("https://vocalremover.org/en/")

if __name__=='main':
    main()









