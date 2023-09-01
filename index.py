from tkinter import *
from pytube import YouTube

root = Tk()
root.geometry('500x300')
root.resizable(0, 0)
root.title('Youtube Downloader')

link = StringVar()

Label(root, text='Youtube Video Downloader', font='arial 20 bold').pack()
Label(root, text='Paste Link Here:', font='arial 14').place(x=160, y=60)
link_enter = Entry(root, width=70, textvariable=link).place(x=32, y=90)

def Downloader():
    url = YouTube(str(link.get()))
    print(url)
    video = url.streams.get_highest_resolution()
    video.download()
    Label(root, text='Downloaded', font='arial 14').place(x=180, y=210)
    
Button(root, text='Download', font='arial 15 bold', bg='pale violet red', padx=2, command=Downloader).place(x=180, y=150)

root.mainloop()