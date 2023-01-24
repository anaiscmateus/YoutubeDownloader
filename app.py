# Import Module
import tkinter as tk
from pytube import YouTube
import os

# Root Window
root = tk.Tk()
root.title("Youtube Video Downloader")
root.geometry('500x200')

if os.name == "nt":
    DOWNLOAD_FOLDER = f"{os.getenv('USERPROFILE')}\\Downloads"
else:  # PORT: For *Nix systems
    DOWNLOAD_FOLDER = f"{os.getenv('HOME')}/Downloads"

#Functions
def temp_text(e):
    txt.delete(0,"end")

def downloadvid():
    link = txt.get()
    try:
        yt = YouTube(link)
        yd = yt.streams.get_highest_resolution()
        yd.download(DOWNLOAD_FOLDER)
        success_lbl = tk.Label(root, text="Download Complete! Please check your downloads folder.")
        success_lbl.place(x=100, y=90)
        success_lbl.after(5000, success_lbl.destroy)
        
    except Exception as ex:
        error_lbl = tk.Label(root, text="Oops! Something went wrong.")
        error_lbl.place(x=100, y=90)
        error_lbl.after(5000, error_lbl.destroy)

# Link Field
txt = tk.Entry(root, width= 10)
txt.insert(0, "Paste your video link here")
txt.config(width= 50)
txt.place(x= 50, y= 50)

# Button
btn = tk.Button(root, text = "Download", command = downloadvid)
btn.place(x= 400, y= 50)

txt.bind("<FocusIn>", temp_text)

# Execute Tkinter
root.mainloop()
