"""
Генератор паролей
"""
import random
from tkinter import *

root = Tk()
root.title("Генератор паролей")
root.geometry("300x150")
root.resizable(width=False, height=False)

alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J',
            'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
            'U', 'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd',
            'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n',
            'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x',
            'y', 'z', '1', '2', '3', '4', '5', '6', '7', '8',
            '9', '0', '!', '@', '#', '№', '$', '%', '^', '&',
            '?', '*', ')', ')', '-', '_', '=', '+', '/', '<',
            '>', ':', ';', '*']


def get_pass():
    len_pass = int(length.get())
    for i in range(len_pass):
        psw.insert(0, random.choice(alphabet))


l1 = Label(text="Длинна пароля:")
l2 = Label(text="Ваш пароль:")
length = Entry(root, width=5)
psw = Entry(root)
btn = Button(root, text="Сгенерировать", command=get_pass)

l1.place(relx=0.1, y=11)
l2.place(relx=0.1, y=40)
psw.place(relx=0.4, y=42)
btn.place(relx=0.25, y=100, anchor=CENTER)

length.place(relx=0.5, y=20, anchor=CENTER)


root.mainloop()
