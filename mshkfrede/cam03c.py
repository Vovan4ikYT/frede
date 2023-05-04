from tkinter import *
from PIL import Image, ImageTk

class Camera03c(Label):
    def load(self, im):
        im = Image.open(im)
        self.loc = 0
        self.frames = []

        for i in range(15):
            self.frames.append(ImageTk.PhotoImage(im.copy()))
            im.seek(i)

        self.delay = 100

        self.next_frame()

    def unload(self):
        self.config(image="")
        self.frames = []

    def next_frame(self):
        if self.frames:
            self.loc += 1
            self.loc %= len(self.frames)
            self.config(image=self.frames[self.loc])
            self.after(self.delay, self.next_frame)