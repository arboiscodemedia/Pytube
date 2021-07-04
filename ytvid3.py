from pytube import YouTube
link = [
        "https://www.youtube.com/watch?v=GcHRna76O7s",
        "https://www.youtube.com/watch?v=5RFu9dGtVCw"
       ]

SAVE_PATH="./Youtube"

for vid in link: 
    yt = YouTube(vid) 
    stream = yt.streams.first()
    stream.download(SAVE_PATH) 