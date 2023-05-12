from tkinter import *
from PIL import ImageTk, Image


class GUI:
    def __init__(self, window):
        self.window = window
        buttonBlackUp = Image.PhotoImage(ImageTk.open("UpTriangleBlack.png"))
        buttonBlackDown = Image.PhotoImage(ImageTk.open("DownTriangleBlack.png"))
        buttonRedUp = Image.PhotoImage(ImageTk.open("UpTriangleRed.png"))
        buttonRedDown = Image.PhotoImage(ImageTk.open("DownTriangleRed.png"))

        self.frame_volume = Frame(self.window)
        self.button_volume_up = Label(self.frame_volume, image=buttonBlackUp)
        self.label_volume = Label(self.frame_volume, text='VOL')
        self.button_volume_down = Label(self.frame_volume, image=buttonBlackDown)
        self.button_volume_up.pack(padx=5, side='left')
        self.label_volume.pack(padx=5, side='left')
        self.button_volume_down.pack(padx=5, side='left')
        self.frame_volume.pack(anchor='e', pady=10)

        self.frame_channel = Frame(self.window)
        self.button_channel_up = Label(self.frame_channel, image=buttonBlackUp)
        self.label_channel = Label(self.frame_channel, text='CHNL')
        self.button_channel_down = Label(self.frame_channel, image=buttonBlackDown)
        self.button_channel_up.pack(padx=5, side='left')
        self.label_channel.pack(padx=5, side='left')
        self.button_channel_down.pack(padx=5, side='left')
        self.frame_channel.pack(anchor='e', pady=10)

        self.frame_screen = Frame(self.window)




