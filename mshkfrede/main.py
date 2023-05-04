from tkinter import *
from cam03c import Camera03c
from PIL import Image, ImageTk
from random import choice
from pygame import mixer

main_mshkfrede = Tk()
main_mshkfrede.title('Возвращение Фредди')
main_mshkfrede.geometry('1920x1080')
main_mshkfrede.iconbitmap('frede.ico')
main_mshkfrede.resizable(False, False)

of_img = ImageTk.PhotoImage(Image.open('office.jpg'))
office = Canvas(bg='black', width=1920, height=1080)
office.pack()
office.create_image(0, 0, image=of_img, anchor='nw')

chic_img = ImageTk.PhotoImage(Image.open('animatronics/chica/chica_near_the_office.png'))
chica_states = ['idle', 'attack']
action = choice(chica_states)
if action == 'attack':
    mixer.init()
    mixer.music.load('encounter.wav')
    mixer.music.play()
    office.create_image(1385, 246, image=chic_img, anchor='nw')


def open_cam_03C():
    camera03c = Toplevel()
    camera03c.title('Режим камеры')
    camera03c.geometry('1920x1080')

    video03c = Camera03c(camera03c)
    video03c.pack()
    video03c.load('cams/images/static.gif')


def open_cam_02():
    camera02 = Toplevel()
    camera02.title('Режим камеры')
    camera02.geometry('1920x1080')

    cam02_img = ImageTk.PhotoImage(Image.open('cams/images/cam02.jpg'))
    cam02 = Label(camera02, image=cam02_img)
    cam02.photo = cam02_img
    cam02.pack()

def open_cam_01():
    camera01 = Toplevel()
    camera01.title('Режим камеры')
    camera01.geometry('1920x1080')

    cam01_img = ImageTk.PhotoImage(Image.open('cams/images/cam01_all_set.jpg'))
    cam01 = Label(camera01, image=cam01_img)
    cam01.photo = cam01_img
    cam01.pack()

open_button_03C = Button(office, command=open_cam_03C, text='Камера 03C')
open_button_03C.place(x=621, y=710)

open_button_02 = Button(office, command=open_cam_02, text='Камера 02')
open_button_02.place(x=1112, y=723)

open_button_01 = Button(office, command=open_cam_01, text='Камера 01')
open_button_01.place(x=846, y=619)

def check_event(event):
    print(event)


main_mshkfrede.bind('<Button-1>', check_event)

main_mshkfrede.mainloop()