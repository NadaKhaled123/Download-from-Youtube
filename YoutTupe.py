from tkinter import *
from tkinter import filedialog
from pytube import YouTube

root = Tk()
root.title("Youtube Downloader")
root.geometry("600x32")

def browse():
    directory = filedialog.askdirectory(title="Save video")
    folderLink.delete(0,"end")
    folderLink.insert(0, directory )
def don_yut():
    link= ytlink.get()
    folder = folderLink.get()
    YouTube(link).streams.filter(progressive=True , file_extension="mp4").order_by("resolution").desc().first().download(folder)
ytlabel = Label(root, text="Youtube Link")
ytlabel.place(x=25, y=150)

ytlink = Entry(root, width=60)
ytlink.place(x=140, y=150)

# Download folder

folderLabel = Label(root, text="Download folder")
folderLabel.place(x=25, y=183)

folderLink= Entry(root, width=50)
folderLink.place(x=140, y=183)

 #Browse Button 

browse = Button(root, text="Browse" , command=browse)
browse.place(x=140, y=183)

#Download Button 

download = Button(root, text="Download" , command=don_yut)
download.place(x=280, y=220)


root.mainloop()







# def Download(link):
#     youtubeObject = YouTube(link)
#     youtubeObject = youtubeObject.streams.get_highest_resolution()
#     try:
#         youtubeObject.download()
#     except:
#         print("An error has occurred")
#     print("Download is completed successfully")


# link = input("Enter the YouTube video URL: ")
# Download(link)
# from pytube import Playlist
# from pytube import YouTube as YT
# import threading as th
# import time

# plist=input('Enter the playlist: ')

# videos=list(Playlist(plist))
# i=videos[0]
# video=YT(i, use_oauth=True, allow_oauth_cache=True)
# strm=video.streams.filter(res="720p")
# print(strm)