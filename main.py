from pytube import YouTube
import os
import time


def fix_filename(filename):
    illegal_chars = r'<>:"/\|?*'
    for char in illegal_chars:
        filename = filename.replace(char, '_')
    return filename

link = input("Enter the YouTube link: ")
yt = YouTube(link)
title = yt.title

print("Title: ", yt.title)
print("Views: ", yt.views)

ghr = yt.streams.get_highest_resolution()

download_path = "C:/Users/crjan/OneDrive/Desktop/YouTube Downloads"
ghr.download(download_path)

sanitized_title = fix_filename(title)
filename = sanitized_title + ".mp4"
desktop_path = os.path.expanduser(download_path)
file_path = os.path.join(desktop_path, filename)

while not os.path.exists(file_path):
    print("Downloading...")
    time.sleep(5)

print(f"'{filename}' has finished downloading!")
