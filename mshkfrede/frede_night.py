from tkinter import *
from cam03c import Camera03c
from PIL import Image, ImageTk
from random import choice
from pygame import mixer
from attack import Jumpscare
from win import EndTheNight
from foxy_get_back import FoxyBack

beaten = False

chica_near_the_office = False
bonnie_near_the_office = False
freddy_near_the_office = False

am = 0
power = 100

bonnie_counter = 0
chica_counter = 0
foxy_state = 0

mixer.init(channels=2)

main_mshkfrede = Tk()
main_mshkfrede.title('Возвращение Фредди')
main_mshkfrede.geometry('1920x1080')
main_mshkfrede.iconbitmap('frede.ico')
main_mshkfrede.resizable(False, False)

of_img = ImageTk.PhotoImage(Image.open('office/office.jpg'))
office = Canvas(bg='black', width=1920, height=1080)
office.pack()
office.create_image(0, 0, image=of_img, anchor='nw')

start_text = office.create_text(927, 216, text='Добро пожаловать на работу ночным охранником в Fazbear Entertainment.\n'
                                               'Ваша задача - следить за аниматрониками ночью, и если они ведут себя '
                                  'агрессивно, защищаться от них.\nЗа ними нужно следить на камерах.\nЧтобы '
                                  'запустить систему камер, откройте камеру 01.\n'
                                  'ВНИМАНИЕ: Некоторые камеры работают отдельно от других.\n'
                                  'Работа кончится в 6 утра.\n'
                                  'Удачи!', fill='white')

left_dr_img = ImageTk.PhotoImage(Image.open('office/left_door.png'))
right_dr_img = ImageTk.PhotoImage(Image.open('office/right_door.png'))

left_count = 0
right_count = 0

chic_img = ImageTk.PhotoImage(Image.open('animatronics/chica/chica_near_the_office.png'))

bonn_img = ImageTk.PhotoImage(Image.open('animatronics/bonnie/bonnie_near_the_office.png'))

alert_img = ImageTk.PhotoImage(Image.open('foxy_alert.png'))

chic_ind = 0
bonn_ind = 0
fred_ind = 0


def open_and_close_left_door():
    global am, beaten
    global left_count
    global power
    left_count += 1

    door_sound = mixer.Sound('sounds/door.wav')
    mixer.Channel(1).play(door_sound)

    if left_count % 2 != 0:
        office.create_image(168, 60, image=left_dr_img, anchor='nw', tag='left_door')
        global bonnie_counter
        global freddy_counter
        global bonnie_near_the_office
        global freddy_near_the_office
        if bonnie_near_the_office is True:
            bonnie_near_the_office = False
            office.delete('bonnie_here')
            bonnie_counter += 1
            if bonnie_counter == 3:
                am += 1
                am_sound = mixer.Sound('sounds/am.wav')
                mixer.Channel(1).play(am_sound)
            if bonnie_counter == 5:
                am += 1
                am_sound = mixer.Sound('sounds/am.wav')
                mixer.Channel(1).play(am_sound)
            if am == 6:
                beaten = True
                passed = Toplevel()
                passed.title('6 УТРА!!!')
                passed.geometry('1920x1080')

                six_am = EndTheNight(passed)
                six_am.pack()
                six_am.load('6am.gif')

                six_am_sound = mixer.Sound('sounds/6am.wav')
                mixer.Channel(0).play(six_am_sound)

                def no_salvation():
                    pass

                passed.protocol('WM_DELETE_WINDOW', no_salvation)

                passed.after(16000, main_mshkfrede.destroy)
        power -= 1
        print(power)
        if power <= 0:
            jump = Toplevel()
            jump.title('СМЕРТЬ')
            jump.geometry('1920x1080')

            freddy = Jumpscare(jump)
            freddy.pack()
            freddy.load('jumpscares/freddy_jumpscare.gif')

            freddy_jump = mixer.Sound('sounds/jumpscares/jumpscare_default.wav')
            mixer.Channel(0).play(freddy_jump)

            def no_salvation():
                pass

            jump.protocol('WM_DELETE_WINDOW', no_salvation)

            jump.after(5000, main_mshkfrede.destroy)
        if freddy_near_the_office is True:
            freddy_near_the_office = False
            office.delete('freddy_left')
            am += 1
            am_sound = mixer.Sound('sounds/am.wav')
            mixer.Channel(1).play(am_sound)
            if am == 6:
                beaten = True
                passed = Toplevel()
                passed.title('6 УТРА!!!')
                passed.geometry('1920x1080')

                six_am = EndTheNight(passed)
                six_am.pack()
                six_am.load('6am.gif')

                six_am_sound = mixer.Sound('sounds/6am.wav')
                mixer.Channel(0).play(six_am_sound)

                def no_salvation():
                    pass

                passed.protocol('WM_DELETE_WINDOW', no_salvation)

                passed.after(16000, main_mshkfrede.destroy)
        power -= 1
        print(power)
        if power <= 0:
            jump = Toplevel()
            jump.title('СМЕРТЬ')
            jump.geometry('1920x1080')

            freddy = Jumpscare(jump)
            freddy.pack()
            freddy.load('jumpscares/freddy_jumpscare.gif')

            freddy_jump = mixer.Sound('sounds/jumpscares/jumpscare_default.wav')
            mixer.Channel(0).play(freddy_jump)

            def no_salvation():
                pass

            jump.protocol('WM_DELETE_WINDOW', no_salvation)

            jump.after(5000, main_mshkfrede.destroy)
    else:
        office.delete('left_door')


def open_and_close_right_door():
    global am, beaten
    global power
    global right_count
    right_count += 1

    door_sound = mixer.Sound('sounds/door.wav')
    mixer.Channel(1).play(door_sound)

    if right_count % 2 != 0:
        office.create_image(1535, 60, image=right_dr_img, anchor='nw', tag='right_door')
        global chica_counter
        global freddy_counter
        global chica_near_the_office
        global freddy_near_the_office
        if chica_near_the_office is True:
            chica_near_the_office = False
            office.delete('chica_came_to_eat')
            chica_counter += 1
            if chica_counter == 4:
                am += 1
                am_sound = mixer.Sound('sounds/am.wav')
                mixer.Channel(1).play(am_sound)
            if am == 6:
                beaten = True
                passed = Toplevel()
                passed.title('6 УТРА!!!')
                passed.geometry('1920x1080')

                six_am = EndTheNight(passed)
                six_am.pack()
                six_am.load('6am.gif')

                six_am_sound = mixer.Sound('sounds/6am.wav')
                mixer.Channel(0).play(six_am_sound)

                def no_salvation():
                    pass

                passed.protocol('WM_DELETE_WINDOW', no_salvation)

                passed.after(16000, main_mshkfrede.destroy)
        power -= 1
        print(power)
        if power <= 0:
            jump = Toplevel()
            jump.title('СМЕРТЬ')
            jump.geometry('1920x1080')

            freddy = Jumpscare(jump)
            freddy.pack()
            freddy.load('jumpscares/freddy_jumpscare.gif')

            freddy_jump = mixer.Sound('sounds/jumpscares/jumpscare_default.wav')
            mixer.Channel(0).play(freddy_jump)

            def no_salvation():
                pass

            jump.protocol('WM_DELETE_WINDOW', no_salvation)

            jump.after(5000, main_mshkfrede.destroy)
        if freddy_near_the_office is True:
            freddy_near_the_office = False
            office.delete('freddy_right')
            am += 1
            am_sound = mixer.Sound('sounds/am.wav')
            mixer.Channel(1).play(am_sound)
            if am == 6:
                beaten = True
                passed = Toplevel()
                passed.title('6 УТРА!!!')
                passed.geometry('1920x1080')

                six_am = EndTheNight(passed)
                six_am.pack()
                six_am.load('6am.gif')

                six_am_sound = mixer.Sound('sounds/6am.wav')
                mixer.Channel(0).play(six_am_sound)

                def no_salvation():
                    pass

                passed.protocol('WM_DELETE_WINDOW', no_salvation)

                passed.after(16000, main_mshkfrede.destroy)
        power -= 1
        print(power)
        if power <= 0:
            jump = Toplevel()
            jump.title('СМЕРТЬ')
            jump.geometry('1920x1080')

            freddy = Jumpscare(jump)
            freddy.pack()
            freddy.load('jumpscares/freddy_jumpscare.gif')

            freddy_jump = mixer.Sound('sounds/jumpscares/jumpscare_default.wav')
            mixer.Channel(0).play(freddy_jump)

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


def open_cam_03C():
    global foxy_state, power
    power -= 1
    if power <= 0:
        jump = Toplevel()
        jump.title('СМЕРТЬ')
        jump.geometry('1920x1080')

        freddy = Jumpscare(jump)
        freddy.pack()
        freddy.load('jumpscares/freddy_jumpscare.gif')

        freddy_jump = mixer.Sound('sounds/jumpscares/jumpscare_default.wav')
        mixer.Channel(0).play(freddy_jump)

        def no_salvation():
            pass

        jump.protocol('WM_DELETE_WINDOW', no_salvation)

        jump.after(5000, main_mshkfrede.destroy)
    else:
        if freddy_near_the_office is False:
            camera03c = Toplevel()
            camera03c.title('Режим камеры')
            camera03c.geometry('1920x1080')

            video03c = Camera03c(camera03c)
            video03c.pack()
            video03c.load('cams/images/static.gif')

            foxy_state += 1
            if foxy_state == 3:
                foxy_poet = mixer.Sound('sounds/foxy_poet.wav')
                mixer.Channel(1).play(foxy_poet)
                office.create_image(2, 1, image=alert_img, anchor='nw', tag='foxy_here')

            if foxy_state == 4:
                camera03c.destroy()

                jump = Toplevel()
                jump.title('СМЕРТЬ')
                jump.geometry('1920x1080')

                foxy = Jumpscare(jump)
                foxy.pack()
                foxy.load('jumpscares/foxy_jumpscare.gif')

                foxy_jump = mixer.Sound('sounds/jumpscares/jumpscare_default.wav')
                mixer.Channel(0).play(foxy_jump)
                mixer.Channel(1).pause()

                def no_salvation():
                    pass

                jump.protocol('WM_DELETE_WINDOW', no_salvation)

                camera03c.after(5000, main_mshkfrede.destroy)
        else:
            jump = Toplevel()
            jump.title('СМЕРТЬ')
            jump.geometry('1920x1080')

            freddy = Jumpscare(jump)
            freddy.pack()
            freddy.load('jumpscares/freddy_jumpscare.gif')

            freddy_jump = mixer.Sound('sounds/jumpscares/jumpscare_default.wav')
            mixer.Channel(0).play(freddy_jump)


            def no_salvation():
                pass


            jump.protocol('WM_DELETE_WINDOW', no_salvation)

            jump.after(5000, main_mshkfrede.destroy)


def open_cam_02():
    global foxy_state
    global power
    power -= 1
    if power <= 0:
        jump = Toplevel()
        jump.title('СМЕРТЬ')
        jump.geometry('1920x1080')

        freddy = Jumpscare(jump)
        freddy.pack()
        freddy.load('jumpscares/freddy_jumpscare.gif')

        freddy_jump = mixer.Sound('sounds/jumpscares/jumpscare_default.wav')
        mixer.Channel(0).play(freddy_jump)

        def no_salvation():
            pass

        jump.protocol('WM_DELETE_WINDOW', no_salvation)

        jump.after(5000, main_mshkfrede.destroy)
    else:
        camera02 = Toplevel()
        camera02.title('Режим камеры')
        camera02.geometry('1920x1080')

        if foxy_state == 0:
            cam02_img = ImageTk.PhotoImage(Image.open('cams/images/cam02/cam02.jpg'))
            cam02 = Label(camera02, image=cam02_img)
            cam02.photo = cam02_img
            cam02.pack()
        elif foxy_state == 1:
            cam02_img = ImageTk.PhotoImage(Image.open('cams/images/cam02/cam02_foxy1.jpg'))
            cam02 = Label(camera02, image=cam02_img)
            cam02.photo = cam02_img
            cam02.pack()
        elif foxy_state == 2:
            cam02_img = ImageTk.PhotoImage(Image.open('cams/images/cam02/cam02_foxy2.jpg'))
            cam02 = Label(camera02, image=cam02_img)
            cam02.photo = cam02_img
            cam02.pack()
        elif foxy_state == 3:
            foxy = FoxyBack(camera02)
            foxy.pack()
            foxy.load('cams/images/cam02/foxy_coming_back.gif')
            foxy_state = 0
            office.delete('foxy_here')


def open_cam_01():
    global am, bonnie_near_the_office, chica_near_the_office, \
        freddy_near_the_office, foxy_state, bonn_ind, chic_ind, fred_ind, \
        bonnie_action, chica_action, freddy_action, power
    power -= 1
    office.delete(start_text)
    if power <= 0:
        jump = Toplevel()
        jump.title('СМЕРТЬ')
        jump.geometry('1920x1080')

        freddy = Jumpscare(jump)
        freddy.pack()
        freddy.load('jumpscares/freddy_jumpscare.gif')

        freddy_jump = mixer.Sound('sounds/jumpscares/jumpscare_default.wav')
        mixer.Channel(0).play(freddy_jump)

        def no_salvation():
            pass

        jump.protocol('WM_DELETE_WINDOW', no_salvation)

        jump.after(5000, main_mshkfrede.destroy)
    else:
        if bonnie_near_the_office is True or chica_near_the_office is True:
            error = mixer.Sound('sounds/error.wav')
            mixer.Channel(1).play(error)
            pass
        elif freddy_near_the_office is True:
            jump = Toplevel()
            jump.title('СМЕРТЬ')
            jump.geometry('1920x1080')

            freddy = Jumpscare(jump)
            freddy.pack()
            freddy.load('jumpscares/freddy_jumpscare.gif')

            freddy_jump = mixer.Sound('sounds/jumpscares/jumpscare_default.wav')
            mixer.Channel(0).play(freddy_jump)

            def no_salvation():
                pass

            jump.protocol('WM_DELETE_WINDOW', no_salvation)

            jump.after(5000, main_mshkfrede.destroy)
        else:
            camera01 = Toplevel()
            camera01.title('Режим камеры')
            camera01.geometry('1920x1080')

            bonnie_states = ['idle', 'out', 'cam03b', 'attack']
            chica_states = ['idle', 'out', 'cam03a', 'cam04', 'attack']
            bonnie_action = bonnie_states[bonn_ind]
            chica_action = chica_states[chic_ind]
            bonn_ind += 1
            if bonn_ind == 4:
                bonn_ind = 0
            chic_ind += 1
            if chic_ind == 5:
                chic_ind = 0
            print(bonnie_action)
            print(chica_action)
            freddy_states = ['idle', 'out', choice(['attack_left', 'attack_right'])]
            freddy_action = freddy_states[fred_ind]
            fred_ind += 1
            if fred_ind == 3:
                fred_ind = 0
            print(freddy_action)
            if bonnie_action == 'idle' and chica_action == 'idle':
                if am >= 3:
                    if freddy_action == 'idle':
                        cam01_img = ImageTk.PhotoImage(Image.open('cams/images/cam01/cam01_only_freddy.jpg'))
                        cam01 = Label(camera01, image=cam01_img)
                        cam01.photo = cam01_img
                        cam01.pack()
                    else:
                        cam01_img = ImageTk.PhotoImage(Image.open('cams/images/cam01/cam01_empty.jpg'))
                        cam01 = Label(camera01, image=cam01_img)
                        cam01.photo = cam01_img
                        cam01.pack()
                else:
                    eyes = [1, 2]
                    eye = choice(eyes)
                    if eye == 1:
                        cam01_img = ImageTk.PhotoImage(Image.open('cams/images/cam01/cam01_all_set.jpg'))
                        cam01 = Label(camera01, image=cam01_img)
                        cam01.photo = cam01_img
                        cam01.pack()
                    else:
                        rare = mixer.Sound('sounds/rare.wav')
                        mixer.Channel(1).play(rare)

                        cam01_img = ImageTk.PhotoImage(Image.open('cams/images/cam01/cam01_rare.jpg'))
                        cam01 = Label(camera01, image=cam01_img)
                        cam01.photo = cam01_img
                        cam01.pack()
            elif bonnie_action != 'idle' and chica_action != 'idle':
                if am >= 3:
                    if freddy_action == 'idle':
                        cam01_img = ImageTk.PhotoImage(Image.open('cams/images/cam01/cam01_only_freddy.jpg'))
                        cam01 = Label(camera01, image=cam01_img)
                        cam01.photo = cam01_img
                        cam01.pack()
                    else:
                        cam01_img = ImageTk.PhotoImage(Image.open('cams/images/cam01/cam01_empty.jpg'))
                        cam01 = Label(camera01, image=cam01_img)
                        cam01.photo = cam01_img
                        cam01.pack()
                else:
                    cam01_img = ImageTk.PhotoImage(Image.open('cams/images/cam01/cam01_only_freddy.jpg'))
                    cam01 = Label(camera01, image=cam01_img)
                    cam01.photo = cam01_img
                    cam01.pack()
            elif bonnie_action != 'idle':
                if am >= 3:
                    if freddy_action == 'idle':
                        cam01_img = ImageTk.PhotoImage(Image.open('cams/images/cam01/cam01_only_freddy.jpg'))
                        cam01 = Label(camera01, image=cam01_img)
                        cam01.photo = cam01_img
                        cam01.pack()
                    else:
                        cam01_img = ImageTk.PhotoImage(Image.open('cams/images/cam01/cam01_empty.jpg'))
                        cam01 = Label(camera01, image=cam01_img)
                        cam01.photo = cam01_img
                        cam01.pack()
                else:
                    cam01_img = ImageTk.PhotoImage(Image.open('cams/images/cam01/cam01_without_bonnie.jpg'))
                    cam01 = Label(camera01, image=cam01_img)
                    cam01.photo = cam01_img
                    cam01.pack()
            elif chica_action != 'idle':
                if am >= 3:
                    if freddy_action == 'idle':
                        cam01_img = ImageTk.PhotoImage(Image.open('cams/images/cam01/cam01_only_freddy.jpg'))
                        cam01 = Label(camera01, image=cam01_img)
                        cam01.photo = cam01_img
                        cam01.pack()
                    else:
                        cam01_img = ImageTk.PhotoImage(Image.open('cams/images/cam01/cam01_empty.jpg'))
                        cam01 = Label(camera01, image=cam01_img)
                        cam01.photo = cam01_img
                        cam01.pack()
                else:
                    cam01_img = ImageTk.PhotoImage(Image.open('cams/images/cam01/cam01_without_chica.jpg'))
                    cam01 = Label(camera01, image=cam01_img)
                    cam01.photo = cam01_img
                    cam01.pack()

            foxy_state += 1
            if foxy_state == 3:
                foxy_poet = mixer.Sound('sounds/foxy_poet.wav')
                mixer.Channel(1).play(foxy_poet)
                office.create_image(2, 1, image=alert_img, anchor='nw', tag='foxy_here')

            if foxy_state == 4:
                camera01.destroy()

                jump = Toplevel()
                jump.title('СМЕРТЬ')
                jump.geometry('1920x1080')

                foxy = Jumpscare(jump)
                foxy.pack()
                foxy.load('jumpscares/foxy_jumpscare.gif')

                foxy_jump = mixer.Sound('sounds/jumpscares/jumpscare_default.wav')
                mixer.Channel(0).play(foxy_jump)
                mixer.Channel(1).pause()


                def no_salvation():
                    pass


                jump.protocol('WM_DELETE_WINDOW', no_salvation)

                camera01.after(5000, main_mshkfrede.destroy)

            if bonnie_action == 'attack':
                if am >= 3:
                    pass
                else:
                    encounter = mixer.Sound('sounds/encounter.wav')
                    mixer.Channel(1).play(encounter)
                    bonnie_near_the_office = True
                    office.create_image(185, 125, image=bonn_img, anchor='nw', tag='bonnie_here')

            if chica_action == 'attack':
                if am >= 3:
                    pass
                else:
                    encounter = mixer.Sound('sounds/encounter.wav')
                    mixer.Channel(1).play(encounter)
                    chica_near_the_office = True
                    office.create_image(1378, 306, image=chic_img, anchor='nw', tag='chica_came_to_eat')

            if freddy_action == 'attack_left':
                if am < 3:
                    pass
                else:
                    fred_laugh1 = mixer.Sound('sounds/freddy_laugh/freddy_laugh1.wav')
                    mixer.Channel(1).play(fred_laugh1)
                    freddy_near_the_office = True
                    office.create_image(185, 125, image=fred_left, anchor='nw', tag='freddy_left')

            if freddy_action == 'attack_right':
                if am < 3:
                    pass
                else:
                    fred_laugh2 = mixer.Sound('sounds/freddy_laugh/freddy_laugh2.wav')
                    mixer.Channel(1).play(fred_laugh2)
                    freddy_near_the_office = True
                    office.create_image(1538, 187, image=fred_right, anchor='nw', tag='freddy_right')


def open_cam_03B():
    global foxy_state, power
    power -= 1
    if power <= 0:
        jump = Toplevel()
        jump.title('СМЕРТЬ')
        jump.geometry('1920x1080')

        freddy = Jumpscare(jump)
        freddy.pack()
        freddy.load('jumpscares/freddy_jumpscare.gif')

        freddy_jump = mixer.Sound('sounds/jumpscares/jumpscare_default.wav')
        mixer.Channel(0).play(freddy_jump)

        def no_salvation():
            pass

        jump.protocol('WM_DELETE_WINDOW', no_salvation)

        jump.after(5000, main_mshkfrede.destroy)
    else:
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
                eyes = [1, 2]
                eye = choice(eyes)
                if eye == 1:
                    cam03b_img = ImageTk.PhotoImage(Image.open('cams/images/cam03b/cam03b_with_bonnie.jpg'))
                    cam03b = Label(camera03b, image=cam03b_img)
                    cam03b.photo = cam03b_img
                    cam03b.pack()
                else:
                    rare = mixer.Sound('sounds/rare.wav')
                    mixer.Channel(1).play(rare)

                    cam03b_img = ImageTk.PhotoImage(Image.open('cams/images/cam03b/cam03b_rare.jpg'))
                    cam03b = Label(camera03b, image=cam03b_img)
                    cam03b.photo = cam03b_img
                    cam03b.pack()

            foxy_state += 1
            if foxy_state == 3:
                foxy_poet = mixer.Sound('sounds/foxy_poet.wav')
                mixer.Channel(1).play(foxy_poet)
                office.create_image(2, 1, image=alert_img, anchor='nw', tag='foxy_here')

            if foxy_state == 4:
                camera03b.destroy()

                jump = Toplevel()
                jump.title('СМЕРТЬ')
                jump.geometry('1920x1080')

                foxy_jump = mixer.Sound('sounds/jumpscares/jumpscare_default.wav')
                mixer.Channel(1).play(foxy_jump)
                mixer.Channel(1).pause()


                def no_salvation():
                    pass

                jump.protocol('WM_DELETE_WINDOW', no_salvation)

                jump.after(5000, main_mshkfrede.destroy)
        elif bonnie_near_the_office is True and freddy_near_the_office is False:
            jump = Toplevel()
            jump.title('СМЕРТЬ')
            jump.geometry('1920x1080')

            bonnie = Jumpscare(jump)
            bonnie.pack()
            bonnie.load('jumpscares/bonnie_jumpscare.gif')

            bonnie_jump = mixer.Sound('sounds/jumpscares/jumpscare_default.wav')
            mixer.Channel(0).play(bonnie_jump)


            def no_salvation():
                pass


            jump.protocol('WM_DELETE_WINDOW', no_salvation)

            jump.after(5000, main_mshkfrede.destroy)
        elif bonnie_near_the_office is False and freddy_near_the_office is True:
            jump = Toplevel()
            jump.title('СМЕРТЬ')
            jump.geometry('1920x1080')

            freddy = Jumpscare(jump)
            freddy.pack()
            freddy.load('jumpscares/freddy_jumpscare.gif')

            freddy_jump = mixer.Sound('sounds/jumpscares/jumpscare_default.wav')
            mixer.Channel(0).play(freddy_jump)

            def no_salvation():
                pass

            jump.protocol('WM_DELETE_WINDOW', no_salvation)

            jump.after(5000, main_mshkfrede.destroy)


def open_cam_03A():
    global foxy_state, power
    power -= 1
    if power <= 0:
        jump = Toplevel()
        jump.title('СМЕРТЬ')
        jump.geometry('1920x1080')

        freddy = Jumpscare(jump)
        freddy.pack()
        freddy.load('jumpscares/freddy_jumpscare.gif')

        freddy_jump = mixer.Sound('sounds/jumpscares/jumpscare_default.wav')
        mixer.Channel(0).play(freddy_jump)

        def no_salvation():
            pass

        jump.protocol('WM_DELETE_WINDOW', no_salvation)

        jump.after(5000, main_mshkfrede.destroy)
    else:
        if chica_near_the_office is False:
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

            foxy_state += 1
            if foxy_state == 3:
                foxy_poet = mixer.Sound('sounds/foxy_poet.wav')
                mixer.Channel(1).play(foxy_poet)
                office.create_image(2, 1, image=alert_img, anchor='nw', tag='foxy_here')

            if foxy_state == 4:
                camera03a.destroy()

                jump = Toplevel()
                jump.title('СМЕРТЬ')
                jump.geometry('1920x1080')

                foxy = Jumpscare(jump)
                foxy.pack()
                foxy.load('jumpscares/foxy_jumpscare.gif')

                foxy_jump = mixer.Sound('sounds/jumpscares/jumpscare_default.wav')
                mixer.Channel(0).play(foxy_jump)
                mixer.Channel(1).pause()


                def no_salvation():
                    pass

                jump.protocol('WM_DELETE_WINDOW', no_salvation)

                jump.after(5000, main_mshkfrede.destroy)
        elif chica_near_the_office is True and freddy_near_the_office is False:
            jump = Toplevel()
            jump.title('СМЕРТЬ')
            jump.geometry('1920x1080')

            chica = Jumpscare(jump)
            chica.pack()
            chica.load('jumpscares/chica_jumpscare.gif')

            chica_jump = mixer.Sound('sounds/jumpscares/jumpscare_default.wav')
            mixer.Channel(0).play(chica_jump)

            def no_salvation():
                pass

            jump.protocol('WM_DELETE_WINDOW', no_salvation)

            jump.after(5000, main_mshkfrede.destroy)
        elif chica_near_the_office is False and freddy_near_the_office is True:
            jump = Toplevel()
            jump.title('СМЕРТЬ')
            jump.geometry('1920x1080')

            freddy = Jumpscare(jump)
            freddy.pack()
            freddy.load('jumpscares/freddy_jumpscare.gif')

            freddy_jump = mixer.Sound('sounds/jumpscares/jumpscare_default.wav')
            mixer.Channel(0).play(freddy_jump)

            def no_salvation():
                pass

            jump.protocol('WM_DELETE_WINDOW', no_salvation)

            jump.after(5000, main_mshkfrede.destroy)


def open_cam_04():
    global foxy_state, power
    power -= 1
    if power <= 0:
        jump = Toplevel()
        jump.title('СМЕРТЬ')
        jump.geometry('1920x1080')

        freddy = Jumpscare(jump)
        freddy.pack()
        freddy.load('jumpscares/freddy_jumpscare.gif')

        freddy_jump = mixer.Sound('sounds/jumpscares/jumpscare_default.wav')
        mixer.Channel(0).play(freddy_jump)

        def no_salvation():
            pass

        jump.protocol('WM_DELETE_WINDOW', no_salvation)

        jump.after(5000, main_mshkfrede.destroy)
    else:
        if chica_near_the_office is False:
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

            foxy_state += 1
            if foxy_state == 3:
                foxy_poet = mixer.Sound('sounds/foxy_poet.wav')
                mixer.Channel(1).play(foxy_poet)
                office.create_image(2, 1, image=alert_img, anchor='nw', tag='foxy_here')

            if foxy_state == 4:
                camera04.destroy()

                jump = Toplevel()
                jump.title('СМЕРТЬ')
                jump.geometry('1920x1080')

                foxy = Jumpscare(jump)
                foxy.pack()
                foxy.load('jumpscares/foxy_jumpscare.gif')

                foxy_jump = mixer.Sound('sounds/jumpscares/jumpscare_default.wav')
                mixer.Channel(0).play(foxy_jump)
                mixer.Channel(1).pause()


                def no_salvation():
                    pass

                jump.protocol('WM_DELETE_WINDOW', no_salvation)

                jump.after(5000, main_mshkfrede.destroy)
        elif chica_near_the_office is True and freddy_near_the_office is False:
            jump = Toplevel()
            jump.title('СМЕРТЬ')
            jump.geometry('1920x1080')

            chica = Jumpscare(jump)
            chica.pack()
            chica.load('jumpscares/chica_jumpscare.gif')

            chica_jump = mixer.Sound('sounds/jumpscares/jumpscare_default.wav')
            mixer.Channel(0).play(chica_jump)


            def no_salvation():
                pass


            jump.protocol('WM_DELETE_WINDOW', no_salvation)

            jump.after(5000, main_mshkfrede.destroy)
        elif chica_near_the_office is False and freddy_near_the_office is True:
            jump = Toplevel()
            jump.title('СМЕРТЬ')
            jump.geometry('1920x1080')

            freddy = Jumpscare(jump)
            freddy.pack()
            freddy.load('jumpscares/freddy_jumpscare.gif')

            freddy_jump = mixer.Sound('sounds/jumpscares/jumpscare_default.wav')
            mixer.Channel(0).play(freddy_jump)

            def no_salvation():
                pass

            jump.protocol('WM_DELETE_WINDOW', no_salvation)

            jump.after(5000, main_mshkfrede.destroy)


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
        nos_frede = mixer.Sound('sounds/nos_frede.wav')
        mixer.Channel(1).play(nos_frede)


main_mshkfrede.bind('<Button-1>', check_event)

night_theme = mixer.Sound('sounds/ambience.wav')
channel0 = mixer.Channel(0)
channel0.play(night_theme, loops=-1)
channel0.set_volume(0.5, 0.5)

main_mshkfrede.mainloop()