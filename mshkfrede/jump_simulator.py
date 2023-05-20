from tkinter import *
from PIL import Image, ImageTk
from pygame import mixer
from attack import Jumpscare

main_jump = Tk()
main_jump.title('СИМУЛЯТОР СКРИМЕРОВ')
main_jump.geometry('1920x1080')
main_jump.resizable(False, False)

mixer.init(channels=2)

img = ImageTk.PhotoImage(Image.open('cams/images/cam03b/cam03b.jpg'))
img1 = ImageTk.PhotoImage(Image.open('animatronics/strange_bunny2.png'))

talking = 'Какой же ты всё-таки наивный.\nНу сломал ты аниматроников, и что теперь?\n' \
          'Ну документы нашёл, отдал их полиции.\nВот только она тебя не спасёт.\n' \
          'Она нас покрывает, понимаешь?\nПокрывает всю Fazbear Entertainment!\n' \
          'И пусть прошло много времени с тех пор, как я застрял в этом костюме зайца с пружинами, ничего ' \
          'не изменилось.\nВообще. И поэтому я хочу, чтобы знал, КТО Я ТАКОЙ.\n' \
          'Я Уильям Афтон, создатель аниматроников.\nЯ всегда возвращаюсь. Я ВСЕГДА ОСТАЮСЬ.\n'

canvas = Canvas(bg='black', width=1920, height=1080)
canvas.pack()
canvas.create_image(0, 0, image=img, anchor='nw')


def summon_freddy():
    jump = Toplevel()
    jump.title('СМЕРТЬ')
    jump.geometry('1920x1080')
    jump.resizable(False, False)

    anim = Jumpscare(jump)
    anim.pack()
    anim.load('jumpscares/freddy_jumpscare.gif')

    jump_sound = mixer.Sound('sounds/jumpscares/jumpscare_default.wav')
    mixer.Channel(1).play(jump_sound)

    def no_salvation():
        pass

    jump.protocol('WM_DELETE_WINDOW', no_salvation)

    jump.after(5000, jump.destroy)


def summon_bonnie():
    jump = Toplevel()
    jump.title('СМЕРТЬ')
    jump.geometry('1920x1080')
    jump.resizable(False, False)

    anim = Jumpscare(jump)
    anim.pack()
    anim.load('jumpscares/bonnie_jumpscare.gif')

    jump_sound = mixer.Sound('sounds/jumpscares/jumpscare_default.wav')
    mixer.Channel(1).play(jump_sound)

    def no_salvation():
        pass

    jump.protocol('WM_DELETE_WINDOW', no_salvation)

    jump.after(5000, jump.destroy)


def summon_chica():
    jump = Toplevel()
    jump.title('СМЕРТЬ')
    jump.geometry('1920x1080')
    jump.resizable(False, False)

    anim = Jumpscare(jump)
    anim.pack()
    anim.load('jumpscares/chica_jumpscare.gif')

    jump_sound = mixer.Sound('sounds/jumpscares/jumpscare_default.wav')
    mixer.Channel(1).play(jump_sound)

    def no_salvation():
        pass

    jump.protocol('WM_DELETE_WINDOW', no_salvation)

    jump.after(5000, jump.destroy)


def summon_foxy():
    jump = Toplevel()
    jump.title('СМЕРТЬ')
    jump.geometry('1920x1080')
    jump.resizable(False, False)

    anim = Jumpscare(jump)
    anim.pack()
    anim.load('jumpscares/foxy_jumpscare.gif')

    jump_sound = mixer.Sound('sounds/jumpscares/jumpscare_default.wav')
    mixer.Channel(1).play(jump_sound)

    def no_salvation():
        pass

    jump.protocol('WM_DELETE_WINDOW', no_salvation)

    jump.after(5000, jump.destroy)


def what():
    spring_jump = Toplevel()
    spring_jump.title('???')
    spring_jump.geometry('1920x1080')
    spring_jump.resizable(False, False)

    canv = Canvas(spring_jump, bg='black', width=1920, height=1080)
    canv.pack()


    def talk():
        canv.create_text(960, 95, text=talking, fill='#842593')


    spring_sound = mixer.Sound('sounds/jumpscares/jumpscare_spring.wav')
    mixer.Channel(0).play(spring_sound)

    canv.create_image(0, 0, image=img1, anchor='nw')
    spring_jump.after(2000, talk)


    def no_salvation():
        pass


    spring_jump.protocol('WM_DELETE_WINDOW', no_salvation)

    spring_jump.after(15000, main_jump.destroy)


fred_button = Button(canvas, text='Фредди', bg='#593720', fg='white', command=summon_freddy)
fred_button.place(x=1440, y=75)

bonn_button = Button(canvas, text='Бонни', bg='#423e54', fg='white', command=summon_bonnie)
bonn_button.place(x=480, y=75)

chic_button = Button(canvas, text='Чика', bg='#b3923c', fg='white', command=summon_chica)
chic_button.place(x=960, y=75)

fox_button = Button(canvas, text='Фокси', bg='#a4352e', fg='white', command=summon_foxy)
fox_button.place(x=955, y=125)

what_button = Button(canvas, text='???', bg='#393611', fg='white', command=what)
what_button.place(x=955, y=300)

ambience = mixer.Sound('sounds/ambience2.wav')
mixer.Channel(0).play(ambience, loops=-1)

main_jump.mainloop()