from tkinter import *
from PIL import Image, ImageTk
from pygame import mixer

main_guide = Tk()
main_guide.title('ИНСТРУКЦИЯ')
main_guide.geometry('1920x1080')
main_guide.resizable(False, False)

count_sc = 0
count_fred = 0
count_bonn = 0
count_chic = 0
count_fox = 0

main_image = ImageTk.PhotoImage(Image.open('cams/images/cam03b/cam03b.jpg'))
gameplay_image = ImageTk.PhotoImage(Image.open('cams/images/cam04/cam04.jpg'))
anim_image = ImageTk.PhotoImage(Image.open('cams/images/cam02/cam02.jpg'))

anims = [ImageTk.PhotoImage(Image.open('animatronics/freddy/freddy_icon.ico')),
         ImageTk.PhotoImage(Image.open('animatronics/bonnie/bonnie_icon.ico')),
         ImageTk.PhotoImage(Image.open('animatronics/chica/chica_icon.ico')),
         ImageTk.PhotoImage(Image.open('animatronics/foxy_icon.ico'))]

canvas = Canvas(bg='black', width=1920, height=1080)
canvas.pack()
canvas.create_image(0, 0, image=main_image, anchor='nw')
canvas.create_text(960, 35, text='ВНИМАНИЕ!\nДанную инструкцию '
                                 'настоятельно рекомендуется прочитать '
                                 'тем, \nкто впервые в Fazbear Entertainment.', fill='#FF00FF', font='Times 15')


def open_gameplay():
    gameplay = Toplevel()
    gameplay.title('ОБЩЕЕ')
    gameplay.geometry('1920x1080')
    gameplay.resizable(False, False)

    canvas1 = Canvas(gameplay, bg='black', width=1920, height=1080)
    canvas1.pack()
    canvas1.create_image(0, 0, image=gameplay_image, anchor='nw')

    canvas1.create_text(960, 155, text='Теперь прочитайте это сообщение '
                                      'очень внимательно - от него зависит ваша жизнь. \n'
                                      'Ваше время в офисе идёт ТОЛЬКО тогда, когда Вы отражаете атаку '
                                      'аниматроников Фредди, Бонни или Чики. \nЭто означает, '
                                      'что просто просидеть всё время на камерах НЕ ВЫЙДЕТ - Вы просто '
                                      'не выберетесь отсюда.\nЕщё не стоит забывать, \n'
                                      'что большинство аниматроников (Фокси - исключение) '
                                      'движутся только при открытии камеры 01. \n'
                                      'При открытии какой-либо другой камеры они будут стоять на месте, '
                                      'но их будет видно.\nНу и наконец, всё здание питается от электричества.\n'
                                       'Открытие камеры тратит 1 процент заряда, '
                                       'закрытие двери - 2 процента.\nЕсли энергия '
                                       'кончится, то это конец!', fill='#FF00FF', font='Times 25')


    def sister_cam():
        global count_sc, sis_cam
        count_sc += 1
        if count_sc % 2 != 0:
            sis_cam = canvas1.create_text(960, 500, text='Почти у каждого аниматроника '
                                               'есть своя так называемая '
                                               '"родственная камера":\nесли аниматроник стоит у офиса, '
                                               'а игрок в это время открыл эту камеру, '
                                               'то аниматроник нападёт.\nПри открытии в этот момент '
                                               'других камер атаки не произойдёт, но не забывайте: '
                                               'время идёт только при отражении атаки.\nУ Бонни '
                                               'всего одна родственная камера - 03B, \n'
                                               'У Чики - две: 03A и 04. \nКогда у офиса стоит Фокси, все камеры, кроме 02, '
                                               'становятся для него родственными.\nТо же самое и с Фредди',
                                          fill='#FF00FF', font='Times 25')
        else:
            canvas1.delete(sis_cam)


    sc = Button(canvas1, text='Родственные камеры', bg='#842593', fg='white', command=sister_cam)
    sc.place(x=960, y=700)


def open_anim():
    anim = Toplevel()
    anim.title('АНИМАТРОНИКИ')
    anim.geometry('1920x1080')
    anim.resizable(False, False)

    canvas2 = Canvas(anim, bg='black', width=1920, height=1080)
    canvas2.pack()
    canvas2.create_image(0, 0, image=anim_image, anchor='nw')

    canvas2.create_text(960, 50, text='Добро пожаловать на работу '
                                      'в Fazbear Entertainment. \nПишет Уильям Афтон - '
                                      'создатель всех аниматроников. \nЗдесь я подробно расскажу, '
                                      'как найти подход к каждому из них.', fill='#FF00FF', font='Times 20')


    def freddy():
        global count_fred, fred
        count_fred += 1
        if count_fred % 2 != 0:
            canvas2.create_image(960, 470, image=anims[0], anchor='nw', tag='freddy')
            fred = canvas2.create_text(960, 400, text='Как же я обожаю '
                                                       'этого аниматроника.\nФредди Фазбер, Фредди, Фреде, '
                                                       'Мишка Фредди, Мшк Фреде...\nУ него много имён, '
                                                       'и это далеко не все.\nЕго словно '
                                                       'специально для убийств делали: '
                                                       'он быстро передвигается, невидим для камер '
                                                       'и может подойти с любой стороны. \n'
                                                       'Единственный его минус - его легче всего опознать: '
                                                       'когда он подходит к двери, он смеётся, а не '
                                                       'издаёт страшные звуки. \nЗакрой дверь - он и уйдёт.\nФредди '
                                                       'активируется в 3 ночи.\nПосле его '
                                                       'активации Фокси продолжит пытаться пройти в офис, '
                                                       'но вот Бонни и Чика станут пассивными.\nОни твёрдо знают - '
                                                       'лучше уступить дорогу Фредди Фазберу...',
                                       fill='#964B00', font='Times 15')
        else:
            canvas2.delete(fred)
            canvas2.delete('freddy')


    def bonnie():
        global count_bonn, bonn
        count_bonn += 1
        if count_bonn % 2 != 0:
            canvas2.create_image(960, 470, image=anims[1], anchor='nw', tag='bonnie')
            bonn = canvas2.create_text(960, 400, text='Кролик Бонни - '
                                                       'местный гитарист, '
                                                       'который иногда ну слишком уж переигрывает.\n'
                                                       'Он идёт к офису и встаёт около левой двери, '
                                                       'издавая страшный звук.\nЧтобы он ушёл, '
                                                       'закрой дверь.\nЕсли посмотреть на камеру 03B, '
                                                       'когда он там, можно испугаться '
                                                       'до жути...\nОшибка программы.',
                                       fill='#42aaff', font='Times 15')
        else:
            canvas2.delete(bonn)
            canvas2.delete('bonnie')


    def chica():
        global count_chic, chic
        count_chic += 1
        if count_chic % 2 != 0:
            canvas2.create_image(960, 470, image=anims[2], anchor='nw', tag='chica')
            chic = canvas2.create_text(960, 400, text='Цыплёнок Чика любит есть - такова её программа.\n'
                                                      'Но программа программой, '
                                                      'а обжорство никогда не поощрялось!\nИменно '
                                                      'поэтому она идёт к офису дольше, чем Бонни - '
                                                      'потому что она ест.\nДаже на камерах видно, '
                                                      'как она ходит по столовой.\nНо наевшись, '
                                                      'она подходит к офису с правой стороны, '
                                                      'издавая тот же звук, что и Бонни.\nЧтобы она ушла, '
                                                      'закрой дверь.\nДа, кстати, '
                                                      'Кекс - тоже аниматроник.',
                                       fill='#FFFF00', font='Times 15')
        else:
            canvas2.delete(chic)
            canvas2.delete('chica')


    def foxy():
        global count_fox, fox
        count_fox += 1
        if count_fox % 2 != 0:
            canvas2.create_image(960, 470, image=anims[-1], anchor='nw', tag='foxy')
            fox = canvas2.create_text(960, 400, text='Этот товарищ всегда был немного дёрганым.\n'
                                                     'Поэтому его поместили отдельно '
                                                     'от других аниматроников.\nИ всё же все его любят.\n'
                                                     'Фокси - единственный, '
                                                     'кто движется не только от включения камеры 01\n'
                                                     'и от которого не спасут двери.\n'
                                                     'Постепенно подходя к офису, '
                                                     'он будет петь пиратскую песню, \n'
                                                     'и в этот момент зайди на камеру 02 - '
                                                     'он убежит обратно.\nЕсли же открыть '
                                                     'другую камеру, когда он у офиса - всё, нет тебя.\n'
                                                     'Ещё можно смотреть на камеру 02, '
                                                     'и он не будет двигаться.',
                                      fill='#FF0000', font='Times 15')
        else:
            canvas2.delete(fox)
            canvas2.delete('foxy')


    fred_button = Button(canvas2, text='Фредди', bg='#593720', fg='white', command=freddy)
    fred_button.place(x=1440, y=90)

    bonn_button = Button(canvas2, text='Бонни', bg='#423e54', fg='white', command=bonnie)
    bonn_button.place(x=480, y=90)

    chic_button = Button(canvas2, text='Чика', bg='#b3923c', fg='white', command=chica)
    chic_button.place(x=960, y=90)

    fox_button = Button(canvas2, text='Фокси', bg='#a4352e', fg='white', command=foxy)
    fox_button.place(x=955, y=140)

button1 = Button(text='Общее', bg='#842593', fg='white', command=open_gameplay)
button1.place(x=480, y=700)

button2 = Button(text='Аниматроники', bg='#842593', fg='white', command=open_anim)
button2.place(x=1350, y=700)

mixer.init()
mixer.music.load('sounds/guide_theme.wav')
mixer.music.play(loops=-1)

main_guide.mainloop()
mixer.music.pause()
import main_launch
