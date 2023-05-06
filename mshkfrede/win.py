from tkinter import *
from PIL import Image, ImageTk


class EndTheNight(Label):
    def load(self, im):
        im = Image.open(im)
        self.cadr = 0
        self.frames = []

        for i in range(20):
            self.frames.append(ImageTk.PhotoImage(im.copy()))
            im.seek(i)

        self.delay = 1000

        self.next_frame()

    def unload(self):
        self.config(image='')
        self.frames = []

    def next_frame(self):
        if self.frames:
            self.cadr += 1
            self.cadr %= len(self.frames)
            self.config(image=self.frames[self.cadr])
            self.after(self.delay, self.next_frame)
        if self.cadr == 19:
            self.unload()