from tkinter import *

class GUI:
    def __init__(self, window):
        self.window = window

        self.frame_name = Frame(self.window)
        self.label_volume = Label(self.frame_name, text='VOL')
        self.label_volume.pack(padx=5, side='left')
        self.frame_name.pack(anchor='e', pady=10)
