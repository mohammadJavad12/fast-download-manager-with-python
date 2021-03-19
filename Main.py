import requests
from tkinter import *
def download():
    DT = DE.get()
    FT = FE.get()
    with open( FT,"wb") as f:
        f.write(requests.get(DT).content)

win = Tk()
DL = Label(win, text="download link")
DL.pack()
DE = Entry(win)
DE.pack()
FS = Label(win, text="filename(with format)")
FS.pack()
FE = Entry(win)
FE.pack()
DB = Button(win, text="download" , command = download)
DB.pack()
win.mainloop()
