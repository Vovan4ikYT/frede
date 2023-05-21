from tkinter import *
from PIL import Image, ImageTk
from pygame import mixer

credits = Tk()
credits.title('СОЗДАТЕЛИ')
credits.geometry('1920x1080')
credits.resizable(False, False)

anims = [ImageTk.PhotoImage(Image.open('animatronics/freddy/freddy_icon.ico')),
         ImageTk.PhotoImage(Image.open('animatronics/bonnie/bonnie_icon.ico')),
         ImageTk.PhotoImage(Image.open('animatronics/chica/chica_icon.ico')),
         ImageTk.PhotoImage(Image.open('animatronics/foxy_icon.ico')),
         ImageTk.PhotoImage(Image.open('animatronics/strange_bunny1.png'))]

cred_img = ImageTk.PhotoImage(Image.open('cams/images/cam01/cam01_empty.jpg'))

canvas = Canvas(bg='black', width=1920, height=1080)
canvas.pack()
canvas.create_image(0, 0, image=cred_img, anchor='nw')

canvas.create_text(960, 125, text='Возвращение Фредди\nСОЗДАТЕЛИ\nКод, алгоритмы:\nВладимир Кузнецов\nПрообраз:\n'
                                  'Серия игр Five Nights at Freddy (создатель: Скотт Коутон)\nЗвуки:\nЭмбиенс, '
                                  'звуки аниматроников, звуки офиса и камер, '
                                  'звуки скримеров взяты из игр FNaF 1, FNaF 3 и '
                                  'FNaF Security Breach (создатели: Скотт Коутон, Steel Wool Studios)\nЗвук '
                                  'пасхалки на камерах взят из игры Minecraft (создатели: Mojang)\nМузыка:\nFNaF 3 - '
                                  'Dont Go (Good Ending Theme) (композитор: Tim Juliano)\nSuper '
                                  'FNaF - Title (переделано LSDevelompent, оригинал - '
                                  'Five Nights at Freddys (The Living Tombstone))\nSuper FNaF - Credits '
                                  '(переделано LSDevelopment, оригинал - Die in a Fire (The Living Tombstone))\n'
                                  'И ты, мой дорогой игрок. Спасибо тебе за игру.', fill='lime', font='Times 15')

canvas.create_image(0, 800, image=anims[0], anchor='nw')
canvas.create_image(256, 800, image=anims[1], anchor='nw')
canvas.create_image(512, 800, image=anims[2], anchor='nw')
canvas.create_image(1664, 800, image=anims[3], anchor='nw')
canvas.create_image(1096, 890, image=anims[-1], anchor='nw')

mixer.init()
mixer.music.load('sounds/credits_theme.wav')
mixer.music.play(loops=-1)

credits.mainloop()
