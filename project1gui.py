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
        self.is_power = False
        self.is_muted = False
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
        self.button_channel_up.pack(padx=5, side='right')
        self.label_channel.pack(padx=5, side='right')
        self.button_channel_down.pack(padx=5, side='right')
        self.frame_channel.pack(anchor='e', pady=10)

        """

        self.frame_screen = Frame(self.window)
        self.canvas_screen = Canvas(self.frame_screen, width=300, height=300, bg='black')
        self.canvas_screen.create_image((100, 100), image=buttonBlackUp)
        self.canvas_screen.pack(padx=5, side='left')
        self.frame_channel.pack(anchor='w', pady=10)
        
        """

        self.frame_power_mute = Frame(self.window)
        self.button_mute = Button(self.frame_power_mute, text='MUTE', command=self.set_mute)
        self.button_power = Button(self.frame_power_mute, text='PWR', command=self.set_power)
        self.button_mute.pack(padx=5, side='left')
        self.button_power.pack(padx=5, side='left')
        self.frame_channel.pack(anchor='s', pady=10)

    def volume_up(self, max=MAX_VOLUME):
        """
        Function to increase the volume of the television.
        :param max: Maximum volume allowed for the television
        :return: Returns the current volume increased by one, provided the television is powered on
        """
        if self.is_power:
            current_volume = self.current_volume.get()
            if current_volume < max:
                return current_volume + 1

    def volume_down(self, min=MIN_VOLUME):
        """
        Function to decrease the volume of the television.
        :param min: Minimum volume allowed for the television
        :return: Returns the current volume decreased by one, provided the television is powered on
        """
        if self.is_power:
            current_volume = self.current_volume.get()
            if current_volume > min:
                return current_volume - 1

    def channel_up(self, max=MAX_CHANNEL):
        """
        Function to increase the channel of the television.
        :param max: The maximum numbered channel for the television
        :return: Returns the current channel value increased by one, provided the television is powered on. If the
         current channel value is equal to the maximum channel, the channel is reset to 0.
        """
        if self.is_power:
            current_channel = self.current_channel.get()
            if current_channel < max:
                current_channel = current_channel + 1
                return current_channel
            elif current_channel == max:
                current_channel = 0
                return current_channel

    def channel_down(self, min=MIN_CHANNEL, max=MAX_CHANNEL):
        """
        Function to decrease the channel of the television.
        :param min: The minimum numbered channel for the television
        :param max: The maximum numbered channel for the television
        :return: Returns the current channel value decreased by one, provided the television is powered on. If the
         current channel value is 0, the channel is reset to the maximum channel.
        """
        if self.is_power:
            current_channel = self.current_channel.get()
            if current_channel > min:
                current_channel = current_channel - 1
                return current_channel
            elif current_channel == min:
                current_channel = max
                return current_channel

    def set_mute(self):
        """
        Changes whether the television is muted
        :return: Returns True if the television was unmuted, or False if the television was muted
        """
        if self.is_power:
            if self.is_muted:
                self.is_muted = False
                return self.is_muted
            else:
                self.is_muted = True
                return self.is_muted

    def set_power(self):
        """
        Changes whether the television is powered on
        :return: Returns True if the television was powered off, or False if the television was powered on
        """
        if self.is_power:
            self.is_power = False
            return self.is_power
        else:
            self.is_power = True
            return self.is_power
