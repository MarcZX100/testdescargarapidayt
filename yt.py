# pip install pytube
import pytube

link = input('Pon el enlace de descarga: ')
yt = pytube.YouTube(link)
yt.streams.first().download()
print('Descarga completada', link)
