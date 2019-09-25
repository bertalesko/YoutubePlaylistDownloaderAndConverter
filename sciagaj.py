from imutils import paths
import os
from pytube import Playlist
import subprocess

path = os.getcwd()
elo = paths.list_files(path)


files = []
# r=root, d=directories, f = files

def downloadPlaylist(address):
    pl = Playlist(address)
    pl.download_all()


def convert(f):
    tempFileName = f
    tempFileName.strip()
    tempFileName2 = tempFileName.replace('.mp4', '.mp3')
    ffmpeg = ('ffmpeg -i %s ' % tempFileName + tempFileName2)
    subprocess.call(ffmpeg, shell=True)



#downloadPlaylist(addressGoesHere)


for r, d, f in os.walk(path):
    for file in f:
        if '.mp4' in file:
            files.append(os.path.join(r, file))

for f in files:
    print(f)
    convert(f)



