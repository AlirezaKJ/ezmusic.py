from pytube import YouTube
import colorama
from colorama import Fore, Back, Style
from youtubesearchpython import VideosSearch
import os

def clear():
	try:
		subprocess.run("clear")
	except:
		os.system('cls')

colorama.init(autoreset=True)
clear()

def getaudio(link,name):
	audio = YouTube(link)
	streams = audio.streams.get_audio_only()
	# print(streams)
	streams.download("Music")
	os.rename(f"Music/{name}.mp4",f"Music/{name}.mp3")
	# video = VideoFileClip(os.path.join(f"Music/{name}.mp4"))
	# video.audio.write_audiofile(os.path.join("Music/{name}.mp3"))

	print("Download Completed File Saved In Music Folder Next To This File")


def search(term):
	query = VideosSearch(term, limit = 1)
	resultjson = query.result()
	resultjson = resultjson.get("result")[0]
	print(f'''   	{Style.BRIGHT + Fore.CYAN}Title {Fore.WHITE}: {Fore.RED + resultjson.get("title")}
	{Style.BRIGHT + Fore.CYAN}Description {Fore.WHITE}: {Fore.RED + resultjson.get("descriptionSnippet")[0].get("text")}
	{Style.BRIGHT + Fore.CYAN}Duration {Fore.WHITE}: {Fore.RED + resultjson.get("duration")}
	{Style.BRIGHT + Fore.CYAN}Plays {Fore.WHITE}: {Fore.RED + resultjson.get("viewCount").get("short")}''')
	termlink = resultjson.get("link")
	audioname = resultjson.get("title")
	correct = input("download audio? y/n :")
	if correct == "y":
		print("Starting Download")
		getaudio(termlink,audioname)


print("\n    EZMUSIC.PY\n")
while True:
	searchquery = input("enter your music search term: ")
	search(searchquery)
