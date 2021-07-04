from pytube import YouTube

yt = YouTube("https://www.youtube.com/watch?v=GcHRna76O7s")

#Title
print(f"Title: {yt.title}") 
#Thumbnail
print(f"Thumbnail Link: {yt.thumbnail_url}")

#Description
print(f"Description: {yt.description}")
#Views
print(f"Views: {yt.views}")
#Video ID
print(f"Video ID: {yt.video_id}")

#HDStream Info
myHDStream = yt.streams.first()
print(myHDStream)

#AudioStream info
myAudioStream = yt.streams.last()
print(myAudioStream)
