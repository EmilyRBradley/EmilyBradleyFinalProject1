from tkinter import *


class GUI:
    MAX_VOLUME = 3
    MIN_VOLUME = 0
    MAX_CHANNEL = 3
    MIN_CHANNEL = 0

    def __init__(self, window):
        self.window = window
        self.current_volume = 0
        self.current_channel = 0
        buttonBlackUp = PhotoImage("UpTriangleBlack.png")
        buttonBlackDown = PhotoImage("DownTriangleBlack.png")
        buttonRedUp = PhotoImage("UpTriangleRed.png")
        buttonRedDown = PhotoImage("DownTriangleRed.png")

        self.frame_volume = Frame(self.window)
        # self.button_volume_up = Label(self.frame_volume, image=buttonBlackUp)
        self.button_volume_up = Button(self.frame_volume, text='^', command=self.volume_up)
        self.label_volume = Label(self.frame_volume, text='VOL')
        # self.button_volume_down = Label(self.frame_volume, image=buttonBlackDown)
        self.button_volume_down = Button(self.frame_volume, text='v', command=self.volume_down)
        self.button_volume_up.pack(padx=5, side='left')
        self.label_volume.pack(padx=5, side='left')
        self.button_volume_down.pack(padx=5, side='left')
        self.frame_volume.pack(anchor='e', pady=10)

        self.frame_channel = Frame(self.window)
        # self.button_channel_up = Label(self.frame_channel, image=buttonBlackUp, command=self.button_up)
        self.button_channel_up = Button(self.frame_channel, text='^', command=self.channel_up)
        self.label_channel = Label(self.frame_channel, text='CHNL')
        # self.button_channel_down = Label(self.frame_channel, image=buttonBlackDown)
        self.button_channel_down = Button(self.frame_channel, text='v', command=self.channel_down)
        self.button_channel_up.pack(padx=5, side='left')
        self.label_channel.pack(padx=5, side='left')
        self.button_channel_down.pack(padx=5, side='left')
        self.frame_channel.pack(anchor='w', pady=10)

        self.frame_screen = Frame(self.window)
        self.canvas_screen = Canvas(self.frame_screen, width=300, height=300, bg='black')
        self.canvas_screen.create_image((100, 100), image=buttonBlackUp)
        self.canvas_screen.pack(padx=5, side='left')
        self.frame_channel.pack(anchor='w', pady=10)

    def volume_up(self, max=MAX_VOLUME):
        current_volume = self.current_volume.get()
        if current_volume < max:
            return current_volume + 1

    def volume_down(self, min=MIN_VOLUME):
        current_volume = self.current_volume.get()
        if current_volume > min:
            return current_volume - 1

    def channel_up(self, max=MAX_CHANNEL):
        current_channel = self.current_channel.get()
        if current_channel < max:
            return current_channel + 1

    def channel_down(self, min=MIN_CHANNEL):
        current_channel = self.current_channel.get()
        if current_channel > min:
            return current_channel - 1






