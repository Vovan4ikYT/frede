from tkinter import *
from cam03c import Camera03c
from PIL import Image, ImageTk
from random import choice
from pygame import mixer

chica_near_the_office = False
bonnie_near_the_office = False
freddy_near_the_office = False

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
chica_action = choice(chica_states)
print(chica_action)
if chica_action == 'attack':
    mixer.init()
    mixer.music.load('sounds/encounter.wav')
    mixer.music.play()
    chica_near_the_office = True
    office.create_image(1385, 246, image=chic_img, anchor='nw')

bonn_img = ImageTk.PhotoImage(Image.open('animatronics/bonnie/bonnie_near_the_office.png'))
bonnie_states = ['idle', 'attack']
bonnie_action = choice(bonnie_states)
print(bonnie_action)
if bonnie_action == 'attack':
    mixer.init()
    mixer.music.load('sounds/encounter.wav')
    mixer.music.play()
    bonnie_near_the_office = True
    office.create_image(185, 116, image=bonn_img, anchor='nw')

fred_left = ImageTk.PhotoImage(Image.open('animatronics/freddy/freddy_left_hall.png'))
fred_right = ImageTk.PhotoImage(Image.open('animatronics/freddy/freddy_right_hall.png'))
freddy_states = ['idle', 'attack_left', 'attack_right']
freddy_action = choice(freddy_states)
print(freddy_action)
if freddy_action == 'attack_left':
    mixer.init()
    mixer.music.load('sounds/freddy_laugh1.wav')
    mixer.music.play()
    freddy_near_the_office = True
    office.create_image(519, 531, image=fred_left, anchor='nw')
elif freddy_action == 'attack_right':
    mixer.init()
    mixer.music.load('sounds/freddy_laugh2.wav')
    mixer.music.play()
    freddy_near_the_office = True
    office.create_image(1702, 430, image=fred_right, anchor='nw')


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

    if chica_near_the_office is False and bonnie_near_the_office is False:
        cam01_img = ImageTk.PhotoImage(Image.open('cams/images/cam01/cam01_all_set.jpg'))
        cam01 = Label(camera01, image=cam01_img)
        cam01.photo = cam01_img
        cam01.pack()
    elif chica_near_the_office is True and bonnie_near_the_office is False:
        cam01_img = ImageTk.PhotoImage(Image.open('cams/images/cam01/cam01_without_chica.jpg'))
        cam01 = Label(camera01, image=cam01_img)
        cam01.photo = cam01_img
        cam01.pack()
    elif chica_near_the_office is False and bonnie_near_the_office is True:
        cam01_img = ImageTk.PhotoImage(Image.open('cams/images/cam01/cam01_without_bonnie.jpg'))
        cam01 = Label(camera01, image=cam01_img)
        cam01.photo = cam01_img
        cam01.pack()
    else:
        cam01_img = ImageTk.PhotoImage(Image.open('cams/images/cam01/cam01_only_freddy.jpg'))
        cam01 = Label(camera01, image=cam01_img)
        cam01.photo = cam01_img
        cam01.pack()


def open_cam_03B():
    camera03b = Toplevel()
    camera03b.title('Режим камеры')
    camera03b.geometry('1920x1080')

    cam03b_img = ImageTk.PhotoImage(Image.open('cams/images/cam03b.jpg'))
    cam03b = Label(camera03b, image=cam03b_img)
    cam03b.photo = cam03b_img
    cam03b.pack()


open_button_03C = Button(office, command=open_cam_03C, text='Камера 03C')
open_button_03C.place(x=621, y=710)

open_button_03B = Button(office, command=open_cam_03B, text='Камера 03B')
open_button_03B.place(x=1235, y=717)

open_button_02 = Button(office, command=open_cam_02, text='Камера 02')
open_button_02.place(x=1112, y=723)

open_button_01 = Button(office, command=open_cam_01, text='Камера 01')
open_button_01.place(x=846, y=619)


def check_event(event):
    print(event)


main_mshkfrede.bind('<Button-1>', check_event)

main_mshkfrede.mainloop()