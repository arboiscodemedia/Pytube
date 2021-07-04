from pytube import YouTube

yt = YouTube("https://www.youtube.com/watch?v=GcHRna76O7s")

SAVE_PATH="./Youtube"
stream = yt.streams.first()
stream.download(SAVE_PATH)