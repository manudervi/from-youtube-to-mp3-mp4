from pytube import YouTube
import pytube as pt
import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo
import os






def Downloadmp4():
    var = link.get()
    ytObj = YouTube(var)
    ytObj = ytObj.streams.get_highest_resolution()
    try:
        # Download the video
        downloaded_file_path = ytObj.download(output_path="downloading_yt/saves/mp4")

        # Rename the file
        new_file_name = file_name.get() + ".mp4"
        new_file_path = os.path.join(os.path.dirname(downloaded_file_path), new_file_name)
        os.rename(downloaded_file_path, new_file_path)

    except Exception as e:
        print("Error:", e)
        return

    print("File downloaded and renamed successfully")
    return True

def Downloadmp3():
    var = link.get()
    yt = pt.YouTube(var)
    t = yt.streams.filter(only_audio=True)
    try:
        # Download the audio
        downloaded_file_path = t[0].download(output_path="downloading_yt/saves/mp3")

        # Rename the file
        new_file_name = file_name.get() + ".mp3"
        new_file_path = os.path.join(os.path.dirname(downloaded_file_path), new_file_name)
        os.rename(downloaded_file_path, new_file_path)

    except Exception as e:
        print("Error:", e)
        return

    print("File downloaded and renamed successfully")
    return True

#size
width = 600
height = 600

#interface
#root
root = tk.Tk()
root.title("youtube to mp4")
root.geometry(str(width)+"x"+str(height))
root.resizable(False,False)
root.iconbitmap("downloading_yt\youtube_108041.ico")

#name_label
ttk.Label(root, text='rename your file').pack()
file_name = tk.StringVar()
name_box = ttk.Entry(root,textvariable=file_name)
name_box.pack(fill="x",expand=False)

#link_label

ttk.Label(root, text='Link of Youtube').pack()
link = tk.StringVar()
linkbox = ttk.Entry(root,textvariable=link)
linkbox.pack(fill="x",expand=False)
linkbox.focus()


#buttons submit

mp4 = tk.Button(root, text="toMP4",command=Downloadmp4).pack()
mp3 = tk.Button(root, text="toMP3",command=Downloadmp3).pack()

root.mainloop()

#link = input("put the Youtube link\n")
#Download(link)