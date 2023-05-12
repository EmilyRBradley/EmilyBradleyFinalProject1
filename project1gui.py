from tkinter import *


class GUI:
    def __init__(self, window):
        self.window = window
        self.current_volume = 0
        self.current_channel = 0
        buttonBlackUp = PhotoImage("UpTriangleBlack.png")
        buttonBlackDown = PhotoImage("DownTriangleBlack.png")
        buttonRedUp = PhotoImage("UpTriangleRed.png")
        buttonRedDown = PhotoImage("DownTriangleRed.png")

        self.frame_volume = Frame(self.window)
        self.button_volume_up = Label(self.frame_volume, image=buttonBlackUp)
        self.label_volume = Label(self.frame_volume, text='VOL')
        self.button_volume_down = Label(self.frame_volume, image=buttonBlackDown)
        self.button_volume_up.pack(padx=5, side='left')
        self.label_volume.pack(padx=5, side='left')
        self.button_volume_down.pack(padx=5, side='left')
        self.frame_volume.pack(anchor='e', pady=10)

        self.frame_channel = Frame(self.window)
        self.button_channel_up = Label(self.frame_channel, image=buttonBlackUp, command=self.button_up)
        self.label_channel = Label(self.frame_channel, text='CHNL')
        self.button_channel_down = Label(self.frame_channel, image=buttonBlackDown)
        self.button_channel_up.pack(padx=5, side='left')
        self.label_channel.pack(padx=5, side='left')
        self.button_channel_down.pack(padx=5, side='left')
        self.frame_channel.pack(anchor='w', pady=10)

        self.frame_screen = Frame(self.window)
        self.canvas_screen = Canvas(self.frame_screen, width=300, height=300, bg='black')
        self.canvas_screen.create_image((100, 100), image=buttonBlackUp)
        self.canvas_screen.pack(padx=5, side='left')
        self.frame_channel.pack(anchor='w', pady=10)

    def button_up(self):
        pass






