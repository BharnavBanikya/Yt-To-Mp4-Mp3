import os
import threading
from pytube import YouTube

os.system("clear")

def mp3(Link):
   if Link:
       v = YouTube(Link).streams.get_audio_only().download()
       name = YouTube(Link).title + ".mp3"
       os.rename(v, name)
       print(f"Succesfully Installed >> {YouTube(Link).title}")
   else:
      print("No Link Provided")

def convert(Link):
    if Link:
       YouTube(Link).streams.get_highest_resolution().download()
       print(f"Succesfully Installed >> {YouTube(Link).title}")
    else:
      print("No Link Provided")

def main():
  type = input("""1.Mp4
2.Mp3
Choice >> """)
  if type == "1":
    Link = input("Link >> ")
    convert(Link)
  elif type == "2":
    Link = input("Link >> ")
    mp3(Link)
    
threading.Thread(target=main).start()