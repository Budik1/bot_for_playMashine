from tkinter import *
from tkinter import ttk
from PIL import ImageTk
import fun
import fun_na4

im_en1 = [1, 'img/en1v2.png', 'img/23xp.png']
im_en2 = [2, 'img/en2v2.png', 'img/45xp.png']
im_en3 = [3, 'img/en3v2.png', 'img/68xp.png']
status_bonus = ['O', 'V']

def load_from_File():
    global status_bonus
    print(status_bonus, 'status_bonus load')

def save_to_File():
    global status_bonus
    print(status_bonus, 'status_bonus save')


def bonus():
    global status_bonus
    fun.bonus()

def en_1():
    fun_na4.press_en(im_en1[0], im_en1[1])

def en_2():
    fun_na4.press_en(im_en2[0], im_en1[1])

def en_3():
    fun_na4.press_en(im_en3[0], im_en1[1])

root = Tk()

root.title(' помощник ')
root.geometry("200x350+1280+50")  # ШиринаxВысота+координатаX+координатаY
root.resizable(False, False)

status_bonus = "0"
status_vip = "0"

ttk.Button(text=" Start ", width=13, command=fun.zapusk).place(x=0, y=0)
ttk.Button(text=" сбор бонуса ", width=13, command=fun.bonus).place(x=0, y=32)
ttk.Label(text=status_bonus).place(x=135, y=32)
ttk.Button(text="  сбор подарков  ", width=13, command=fun.podapok).place(x=0, y=64)
ttk.Button(text=" обход VIP ", width=13, command=fun.shmon).place(x=0, y=96)
ttk.Label(text=status_vip).place(x=130, y=96)

imagePul = ImageTk.PhotoImage(file="img/pulya.png")
ttk.Button(root, image=imagePul, command=fun_na4.vybor_zadaniya_na_puli).place(x=60, y=145)

image1 = ImageTk.PhotoImage(file="img/en1v3.png")
ttk.Button(root, image=image1, command=en_1).place(x=0, y=128)
#
# image2 = ImageTk.PhotoImage(file="img/en2v3.png")
# ttk.Button(root, image=image2, command=fun_na4.press_en(im_en2[0], im_en1[1])).place(x=0, y=168)
#
# image3 = ImageTk.PhotoImage(file="img/en3v3.png")
# ttk.Button(root, image=image3, command=fun_na4.press_en(im_en3[0], im_en1[1])).place(x=0, y=208)

image2 = ImageTk.PhotoImage(file="img/en2v3.png")
ttk.Button(root, image=image2, command=en_2).place(x=0, y=168)

image3 = ImageTk.PhotoImage(file="img/en3v3.png")
ttk.Button(root, image=image3, command=en_3).place(x=0, y=208)



root.mainloop()


