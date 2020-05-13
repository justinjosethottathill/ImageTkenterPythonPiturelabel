import tkinter as tk


mainWindowSize="1350x690+0+0"
win=tk.Tk()
win.title("Picture")
win.geometry(mainWindowSize)
win.resizable(0,0) 
win.configure(background='white')

#image label settings
Height=100
Width=100
Left=0
Top=0
size = (Width+3, Height+3)
Path='j.jpg'

#view image
from PIL import ImageTk, Image, ImageOps
img = ImageTk.PhotoImage(ImageOps.fit(Image.open(Path), size, Image.ANTIALIAS))
name = tk.Label(win, image = img, width=Width, height=Height)
name.place(x = Left,y = Top )



win.mainloop()
