import os
from pytube import YouTube
class Video_downloader():
    def __init__(self , link):
        self.link = link
        self.yt = YouTube('{}'.format(self.link))
    def downloader(self):
        video = self.yt.streams.filter(only_audio=True).first()
        video.download()
        os.rename(self.yt.streams.first().default_filename , self.yt.streams.first().default_filename[0:-4] + ".mp3")
    def thumb(self):
        return self.yt.thumbnail_url , self.yt.streams.first().default_filename
