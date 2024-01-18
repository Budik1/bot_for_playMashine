from tkinter import *
from tkinter import ttk
from PIL import ImageTk
import fun
import fun_na4
import turist
import person


im_en1 = [1, 'img/en1v2.png', 'img/23xp.png']
# im_en2 = [2, 'img/en2v2.png', 'img/45xp.png']
# im_en3 = [3, 'img/en3v2.png', 'img/68xp.png']
status_bonus = "0"
status_vip = "0"

# status_kiki = int(turist.number_of_kiki)
# status_krysa = int(turist.number_of_krysa)


def bonus():
    fun.bonus()


def en_1():
    fun_na4.press_en(im_en1[0], im_en1[1])

def dvizh():
    sum_krys = turist.test()
    status_krysa.set(sum_krys)

def obysk_vip():
    fun.shmon()
    status_vip.set(fun.sum_vip)


root = Tk()

root.title(' помощник ')
root.geometry("310x390+1200+50")  # Ширина x Высота + координатаX + координатаY
root.resizable(False, False)

status_kiki= IntVar(value=0)
status_krysa = StringVar(value='0')
status_vip = StringVar(value='0')

ttk.Button(text=" Start ", width=13, command=fun.zapusk).place(x=0, y=0)
ttk.Button(text=" сбор бонуса ", width=13, command=fun.bonus).place(x=0, y=32)
ttk.Label(text=status_bonus).place(x=135, y=32)
ttk.Button(text="  сбор подарков  ", width=13, command=fun.podapok).place(x=0, y=64)
ttk.Button(text=" обход VIP ", width=13, command=obysk_vip).place(x=0, y=96)
ttk.Label(textvariable=status_vip).place(x=130, y=96)

ttk.Button(text=" на Киевскую ", width=13, command=turist.most_kiev).place(x=0, y=230)
ttk.Button(text=" домой ", width=13, command=turist.kiev_most).place(x=0, y=261)
ttk.Button(text="кикиморы", width=13, command=turist.za_kikimorami).place(x=0, y=292)
ttk.Label(textvariable=status_kiki, background="#FFCDD2", foreground="#B71C1C", padding=4).place(x=130, y=292)

ttk.Button(text="test гардероб", width=16, command=person.pereodevanie).place(x=155, y=230)
ttk.Button(text="most_riga", width=13, command=turist.most_riga).place(x=155, y=262)
ttk.Button(text="riga_most", width=13, command=turist.riga_most).place(x=155, y=293)

ttk.Button(text="задания на Киевской", width=17, command=turist.zadaniya_na_Kievskoy).place(x=120, y=147)

ttk.Button(text="тест передвижения ", width=16, command=dvizh).place(x=0, y=323)
ttk.Label(textvariable=status_krysa, background="#FFCDD2", foreground="#0000FF", padding=4).place(x=180, y=323)
ttk.Button(text="обход всех станций", width=16, command=turist.sbor_podarkov).place(x=0, y=354)

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

root.mainloop()
