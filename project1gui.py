from tkinter import *
from PIL import Image, ImageTk


class GUI:
    def __init__(self, window):
        self.window = window
        buttonBlackUp = ImageTk.PhotoImage(Image.open("UpTriangleBlack.png"))
        buttonBlackDown = ImageTk.PhotoImage(Image.open("DownTriangleBlack.png"))
        buttonRedUp = ImageTk.PhotoImage(Image.open("UpTriangleRed.png"))
        buttonRedDown = ImageTk.PhotoImage(Image.open("DownTriangleRed.png"))

        self.frame_name = Frame(self.window)
        self.button_volume_up = Label(window, image=buttonBlackUp)
        self.label_volume = Label(self.frame_name, text='VOL')
        self.button_volume_down = Label(window, image=buttonBlackDown)
        self.button_volume_up.pack(padx=5, side='left')
        self.label_volume.pack(padx=5, side='left')
        self.button_volume_down.pack(padx=5, side='left')
        self.frame_name.pack(anchor='e', pady=10)
