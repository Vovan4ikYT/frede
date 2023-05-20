from tkinter import *
from PIL import Image, ImageTk
from frede_night import beaten
from pygame import mixer

ending = Tk()
jeremy_talks = ['Я всегда знал, что что-то с этими Fazbear Entertainment нечисто.',
                'И был прав.', 'Эти аниматроники - натуральные убийцы!',
                'Причём я нашёл парочку документов, где расписаны их функции.',
                'Функции, несущие смерть.', 'Видимо, полиция не знает об этом.',
                'Ну ничего.', 'Я возьму бумаги с собой, чтобы все всё знали.',
                'Но сначала мне надо избавиться от машин.', 'Я их сломаю и буду прав.',
                'Меня зовут Джереми Шмидт.', 'Никто больше не будет страдать.']
y = 10
jeremy_ind = 0
ending.title('КОНЕЦ')
ending.geometry('1920x1080')
ending.resizable(False, False)
end_img = ImageTk.PhotoImage(Image.open('ending.png'))
end = Canvas(bg='black', width=1920, height=1080)
end.pack()
end.create_image(0, 0, image=end_img, anchor='nw')


def talking():
    global jeremy_ind, y
    end.create_text(960, y, text=jeremy_talks[jeremy_ind], fill='#b4b4ba')
    ending.after(6000, talking)
    jeremy_ind += 1
    y += 20
    if jeremy_ind >= 11:
        return


ending.after(0, talking)
if beaten is False:
    pass
else:
    mixer.init()
    mixer.music.load('sounds/ending.wav')
    mixer.music.play()
    ending.after(68000, ending.destroy)
    ending.mainloop()