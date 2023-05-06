from tkinter import *
from cam03c import Camera03c
from PIL import Image, ImageTk
from random import choice
from pygame import mixer
from attack import Jumpscare
from win import EndTheNight

chica_near_the_office = False
bonnie_near_the_office = False
freddy_near_the_office = False

am = 0
power = 100

bonnie_counter = 0
chica_counter = 0
freddy_counter = 0

main_mshkfrede = Tk()
main_mshkfrede.title('Возвращение Фредди')
main_mshkfrede.geometry('1920x1080')
main_mshkfrede.iconbitmap('frede.ico')
main_mshkfrede.resizable(False, False)

of_img = ImageTk.PhotoImage(Image.open('office/office.jpg'))
office = Canvas(bg='black', width=1920, height=1080)
office.pack()
office.create_image(0, 0, image=of_img, anchor='nw')

left_dr_img = ImageTk.PhotoImage(Image.open('office/left_door.png'))
right_dr_img = ImageTk.PhotoImage(Image.open('office/right_door.png'))

left_count = 0
right_count = 0

chic_img = ImageTk.PhotoImage(Image.open('animatronics/chica/chica_near_the_office.png'))

bonn_img = ImageTk.PhotoImage(Image.open('animatronics/bonnie/bonnie_near_the_office.png'))

chic_ind = 0
bonn_ind = 0


def open_and_close_left_door():
    global am
    global left_count
    global power
    left_count += 1

    mixer.init()
    mixer.music.load('sounds/door.wav')
    mixer.music.play()

    if left_count % 2 != 0:
        office.create_image(168, 60, image=left_dr_img, anchor='nw', tag='left_door')
        global bonnie_near_the_office
        if bonnie_near_the_office is True:
            bonnie_near_the_office = False
            office.delete('bonnie_here')
            am += 1
            if am == 6:
                passed = Toplevel()
                passed.title('6 УТРА!!!')
                passed.geometry('1920x1080')

                six_am = EndTheNight(passed)
                six_am.pack()
                six_am.load('6am.gif')

                mixer.init()
                mixer.music.load('sounds/6am.wav')
                mixer.music.play()

                def no_salvation():
                    pass

                passed.protocol('WM_DELETE_WINDOW', no_salvation)

                passed.after(16000, main_mshkfrede.destroy)
        power -= 1
        print(power)
        if power == 0:
            jump = Toplevel()
            jump.title('СМЕРТЬ')
            jump.geometry('1920x1080')

            freddy = Jumpscare(jump)
            freddy.pack()
            freddy.load('jumpscares/freddy_jumpscare.gif')

            mixer.init()
            mixer.music.load('sounds/jumpscares/jumpscare_default.wav')
            mixer.music.play()

            def no_salvation():
                pass

            jump.protocol('WM_DELETE_WINDOW', no_salvation)

            jump.after(5000, main_mshkfrede.destroy)
    else:
        office.delete('left_door')


def open_and_close_right_door():
    global am
    global power
    global right_count
    right_count += 1

    mixer.init()
    mixer.music.load('sounds/door.wav')
    mixer.music.play()

    if right_count % 2 != 0:
        office.create_image(1535, 60, image=right_dr_img, anchor='nw', tag='right_door')
        global chica_near_the_office
        if chica_near_the_office is True:
            chica_near_the_office = False
            office.delete('chica_came_to_eat')
            am += 1
            if am == 6:
                passed = Toplevel()
                passed.title('6 УТРА!!!')
                passed.geometry('1920x1080')

                six_am = EndTheNight(passed)
                six_am.pack()
                six_am.load('6am.gif')

                mixer.init()
                mixer.music.load('sounds/6am.wav')
                mixer.music.play()

                def no_salvation():
                    pass

                passed.protocol('WM_DELETE_WINDOW', no_salvation)

                passed.after(16000, main_mshkfrede.destroy)
        power -= 1
        print(power)
        if power == 0:
            jump = Toplevel()
            jump.title('СМЕРТЬ')
            jump.geometry('1920x1080')

            freddy = Jumpscare(jump)
            freddy.pack()
            freddy.load('jumpscares/freddy_jumpscare.gif')

            mixer.init()
            mixer.music.load('sounds/jumpscares/jumpscare_default.wav')
            mixer.music.play()

            def no_salvation():
                pass

            jump.protocol('WM_DELETE_WINDOW', no_salvation)

            jump.after(5000, main_mshkfrede.destroy)
    else:
        office.delete('right_door')


left_dr_btn = ImageTk.PhotoImage(Image.open('office/left_door_button.png'))
left_door_button = Button(office, image=left_dr_btn, bg='#1A162A', command=open_and_close_left_door)
left_door_button.place(x=105, y=423)

right_dr_btn = ImageTk.PhotoImage(Image.open('office/right_door_button.png'))
right_door_button = Button(office, image=left_dr_btn, bg='#1A162A', command=open_and_close_right_door)
right_door_button.place(x=1771, y=423)

fred_left = ImageTk.PhotoImage(Image.open('animatronics/freddy/freddy_left_hall.png'))
fred_right = ImageTk.PhotoImage(Image.open('animatronics/freddy/freddy_right_hall.png'))
freddy_states = ['idle', 'attack_left', 'attack_right']
freddy_action = choice(freddy_states)
print(freddy_action)
if freddy_action == 'attack_left':
    mixer.init()
    mixer.music.load('sounds/freddy_laugh/freddy_laugh1.wav')
    mixer.music.play()
    freddy_near_the_office = True
    office.create_image(519, 554, image=fred_left, anchor='nw')
elif freddy_action == 'attack_right':
    mixer.init()
    mixer.music.load('sounds/freddy_laugh/freddy_laugh2.wav')
    mixer.music.play()
    freddy_near_the_office = True
    office.create_image(1705, 430, image=fred_right, anchor='nw')


def open_cam_03C():
    if freddy_near_the_office is False:
        camera03c = Toplevel()
        camera03c.title('Режим камеры')
        camera03c.geometry('1920x1080')

        video03c = Camera03c(camera03c)
        video03c.pack()
        video03c.load('cams/images/static.gif')
    else:
        jump = Toplevel()
        jump.title('СМЕРТЬ')
        jump.geometry('1920x1080')

        freddy = Jumpscare(jump)
        freddy.pack()
        freddy.load('jumpscares/freddy_jumpscare.gif')

        mixer.init()
        mixer.music.load('sounds/jumpscares/jumpscare_default.wav')
        mixer.music.play()


        def no_salvation():
            pass


        jump.protocol('WM_DELETE_WINDOW', no_salvation)

        jump.after(5000, main_mshkfrede.destroy)


def open_cam_02():
    camera02 = Toplevel()
    camera02.title('Режим камеры')
    camera02.geometry('1920x1080')

    cam02_img = ImageTk.PhotoImage(Image.open('cams/images/cam02.jpg'))
    cam02 = Label(camera02, image=cam02_img)
    cam02.photo = cam02_img
    cam02.pack()

def open_cam_01():
    global bonnie_near_the_office
    global chica_near_the_office
    global bonn_ind
    global chic_ind
    global bonnie_action
    global chica_action
    camera01 = Toplevel()
    camera01.title('Режим камеры')
    camera01.geometry('1920x1080')

    bonnie_states = ['idle', 'cam03b', 'attack']
    chica_states = ['idle', 'cam03a', 'cam04', 'attack']
    bonnie_action = bonnie_states[bonn_ind]
    chica_action = chica_states[chic_ind]
    bonn_ind += 1
    if bonn_ind == 3:
        bonn_ind = 0
    chic_ind += 1
    if chic_ind == 4:
        chic_ind = 0
    print(bonnie_action)
    print(chica_action)
    if bonnie_action == 'idle' and chica_action == 'idle':
        eyes = [1, 2]
        eye = choice(eyes)
        if eye == 1:
            cam01_img = ImageTk.PhotoImage(Image.open('cams/images/cam01/cam01_all_set.jpg'))
            cam01 = Label(camera01, image=cam01_img)
            cam01.photo = cam01_img
            cam01.pack()
        else:
            mixer.init()
            mixer.music.load('sounds/rare.wav')
            mixer.music.play()

            cam01_img = ImageTk.PhotoImage(Image.open('cams/images/cam01/cam_01_rare.jpg'))
            cam01 = Label(camera01, image=cam01_img)
            cam01.photo = cam01_img
            cam01.pack()
    elif bonnie_action != 'idle' and chica_action != 'idle':
        cam01_img = ImageTk.PhotoImage(Image.open('cams/images/cam01/cam01_only_freddy.jpg'))
        cam01 = Label(camera01, image=cam01_img)
        cam01.photo = cam01_img
        cam01.pack()
    elif bonnie_action != 'idle':
        cam01_img = ImageTk.PhotoImage(Image.open('cams/images/cam01/cam01_without_bonnie.jpg'))
        cam01 = Label(camera01, image=cam01_img)
        cam01.photo = cam01_img
        cam01.pack()
    elif chica_action != 'idle':
        cam01_img = ImageTk.PhotoImage(Image.open('cams/images/cam01/cam01_without_chica.jpg'))
        cam01 = Label(camera01, image=cam01_img)
        cam01.photo = cam01_img
        cam01.pack()

    if bonnie_action == 'attack':
        mixer.init()
        mixer.music.load('sounds/encounter.wav')
        mixer.music.play()
        bonnie_near_the_office = True
        office.create_image(185, 125, image=bonn_img, anchor='nw', tag='bonnie_here')

    if chica_action == 'attack':
        mixer.init()
        mixer.music.load('sounds/encounter.wav')
        mixer.music.play()
        chica_near_the_office = True
        office.create_image(1378, 306, image=chic_img, anchor='nw', tag='chica_came_to_eat')


def open_cam_03B():
    if bonnie_near_the_office is False:
        camera03b = Toplevel()
        camera03b.title('Режим камеры')
        camera03b.geometry('1920x1080')

        if bonnie_action != 'cam03b':
            cam03b_img = ImageTk.PhotoImage(Image.open('cams/images/cam03b/cam03b.jpg'))
            cam03b = Label(camera03b, image=cam03b_img)
            cam03b.photo = cam03b_img
            cam03b.pack()
        else:
            cam03b_img = ImageTk.PhotoImage(Image.open('cams/images/cam03b/cam03b_with_bonnie.jpg'))
            cam03b = Label(camera03b, image=cam03b_img)
            cam03b.photo = cam03b_img
            cam03b.pack()
    else:
        jump = Toplevel()
        jump.title('СМЕРТЬ')
        jump.geometry('1920x1080')

        bonnie = Jumpscare(jump)
        bonnie.pack()
        bonnie.load('jumpscares/bonnie_jumpscare.gif')

        mixer.init()
        mixer.music.load('sounds/jumpscares/jumpscare_default.wav')
        mixer.music.play()


        def no_salvation():
            pass


        jump.protocol('WM_DELETE_WINDOW', no_salvation)

        jump.after(5000, main_mshkfrede.destroy)


def open_cam_03A():
    camera03a = Toplevel()
    camera03a.title('Режим камеры')
    camera03a.geometry('1920x1080')

    if chica_action != 'cam03a':
        cam03a_img = ImageTk.PhotoImage(Image.open('cams/images/cam03a/cam03a.jpg'))
        cam03a = Label(camera03a, image=cam03a_img)
        cam03a.photo = cam03a_img
        cam03a.pack()
    else:
        cam03a_img = ImageTk.PhotoImage(Image.open('cams/images/cam03a/cam03a_with_chica.jpg'))
        cam03a = Label(camera03a, image=cam03a_img)
        cam03a.photo = cam03a_img
        cam03a.pack()


def open_cam_04():
    camera04 = Toplevel()
    camera04.title('Режим камеры')
    camera04.geometry('1920x1080')

    if chica_action != 'cam04':
        cam04_img = ImageTk.PhotoImage(Image.open('cams/images/cam04/cam04.jpg'))
        cam04 = Label(camera04, image=cam04_img)
        cam04.photo = cam04_img
        cam04.pack()
    else:
        cam04_img = ImageTk.PhotoImage(Image.open('cams/images/cam04/cam04_with_chica.jpg'))
        cam04 = Label(camera04, image=cam04_img)
        cam04.photo = cam04_img
        cam04.pack()


open_button_04 = Button(office, command=open_cam_04, text='Камера 04')
open_button_04.place(x=1224, y=570)

open_button_03C = Button(office, command=open_cam_03C, text='Камера 03C')
open_button_03C.place(x=621, y=710)

open_button_03B = Button(office, command=open_cam_03B, text='Камера 03B')
open_button_03B.place(x=1235, y=717)

open_button_03A = Button(office, command=open_cam_03A, text='Камера 03A')
open_button_03A.place(x=1122, y=585)

open_button_02 = Button(office, command=open_cam_02, text='Камера 02')
open_button_02.place(x=1112, y=723)

open_button_01 = Button(office, command=open_cam_01, text='Камера 01')
open_button_01.place(x=846, y=619)


def check_event(event):
    print(event)
    x, y = event.x, event.y
    if x in range(800, 810) and y in range(380, 390):
        mixer.init()
        mixer.music.load('sounds/nos_frede.wav')
        mixer.music.play()


main_mshkfrede.bind('<Button-1>', check_event)

main_mshkfrede.mainloop()