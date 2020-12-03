
import pytube,  celery


#thise script download audio from youtube.com and processing on  https://vocalremover.org

yt = pytube.YouTube('https://www.youtube.com/watch?v=dQw4w9WgXcQ')
streams = yt.streams

audio_best = streams.filter(only_audio=True).desc().first()












