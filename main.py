# Python YouTube Downloader
# Author Abir Sarkar

# Importing the module
from pytube import YouTube
# Importing Playlist from the module
from pytube import Playlist

print("Welcome to YouTbe Video downloader By Abir")
print("Enter 0 for single video And Enter 1 for playlist Download")
a = int( input("Enter the choice : "))


if a == 0:
    # Enter the link which video you want to download
    link = input("Enter the Link Of the video :")

    # Creating a function To passing the values of that particular YouTube Video
    youtube_1 = YouTube(link)

    # Getting the video Title
    # print(youtube_1.title)
    # Getting the video thumbnail url
    # print(youtube_1.thumbnail_url)

    # Select Highest quality By using its inbuilt function
    videos = youtube_1.streams.get_highest_resolution()

    # Downloading the Video
    videos.download()

    print("Your video Has been downloaded")

if a == 1:
    # Taking input by the user for the link of the playlist
    link = Playlist(input("Enter the link of the playlist : "))

    # Running a for loop to download the videos in the playlist one by one
    for video in link.videos:
        video.streams.get_highest_resolution().download()  # Download videos automatically by the highest quality available

print("Your Playlist has been downloaded")