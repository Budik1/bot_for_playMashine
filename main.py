from tkinter import *
from tkinter import ttk
from PIL import ImageTk
import fun
import fun_na4
import turist
import person
import obysk

im_en1 = [1, 'img/en1v2.png', 'img/23xp.png']
# im_en2 = [2, 'img/en2v2.png', 'img/45xp.png']
# im_en3 = [3, 'img/en3v2.png', 'img/68xp.png']
status_bonus = "0"
# status_vip = 10
sum_krys = 0


def bonus():
    fun.bonus()


def en_1():
    fun_na4.en_nomer_zadaniya(1)


def en_2():
    fun_na4.en_nomer_zadaniya(2)


def en_3():
    fun_na4.en_nomer_zadaniya(3)


def dvizh_test():
    sum_krys = turist.test()
    status_krysa.set(sum_krys)


def obysk_vip():
    fun.shmon()
    status_vip.set(fun.sum_vip)


# def test_obysk_vip():
#     status_vip = obysk.tent_raid()
#     while status_vip < 10:


root = Tk()

root.title(' помощник ')
root.geometry("327x380+1240+50")  # Ширина x Высота + координатаX + координатаY
root.resizable(False, False)

status_kiki = IntVar(value=0)
status_krysa = StringVar(value='0')
status_vip = StringVar(value='0')

ttk.Button(text=" Start ", width=13, command=fun.zapusk).place(x=0, y=0)
ttk.Button(text=" сбор бонуса ", width=13, command=fun.bonus, state="disabled").place(x=0, y=32)
ttk.Label(text=status_bonus).place(x=130, y=32)
ttk.Button(text="  сбор подарков  ", width=13, command=fun.podapok, state="disabled").place(x=0, y=64)
ttk.Button(text=" обход VIP ", width=13, command=obysk_vip).place(x=0, y=96)
ttk.Label(textvariable=status_vip).place(x=130, y=96)
# шаг 31
ttk.Button(text=" на Киевскую ", width=11, command=turist.frunze_kiev).place(x=120, y=169)
ttk.Button(text=" домой ", width=11, command=turist.kiev_frunze).place(x=120, y=200)
ttk.Button(text="кикиморы", width=11, command=turist.za_kikimorami).place(x=153, y=31)
ttk.Label(textvariable=status_kiki, background="#FFCDD2", foreground="#B71C1C", padding=4).place(x=263, y=31)
ttk.Button(text="Паук + Ящер", width=11, command=turist.pauk_yascher).place(x=153, y=0)

ttk.Button(text="test гардероб", width=11, command=person.pereodevanie).place(x=109, y=245)

ttk.Button(text="most_frunze", width=11, command=turist.most_frunze).place(x=218, y=277)
ttk.Button(text="frunze_most", width=11, command=turist.frunze_most).place(x=218, y=308)

ttk.Button(text="most_riga", width=11, command=turist.most_riga).place(x=109, y=277) # x=133
ttk.Button(text="riga_most", width=11, command=turist.riga_most).place(x=109, y=308)

ttk.Button(text="frunze_riga", width=11, command=turist.frunze_riga).place(x=0, y=277)
ttk.Button(text="riga_frunze", width=11, command=turist.riga_frunze).place(x=0, y=308)

ttk.Button(text="задания на Киевской", width=17, command=turist.zadaniya_na_Kievskoy).place(x=120, y=138)
# тест пробежка
ttk.Button(text="тест пробежка", width=13, command=dvizh_test).place(x=153, y=64)
ttk.Label(textvariable=status_krysa, background="#FFCDD2", foreground="#0000FF", padding=4).place(x=285, y=64)
ttk.Button(text="обход всех станций", width=16, command=turist.sbor_podarkov).place(x=153, y=96)

imagePul = ImageTk.PhotoImage(file="img/pulya.png")
ttk.Button(root, image=imagePul, command=fun_na4.vybor_zadaniya_na_puli).place(x=60, y=145)

imag_e1 = ImageTk.PhotoImage(file="img/en1v3.png")
ttk.Button(root, image=imag_e1, command=en_1).place(x=0, y=128)
#
imag_e2 = ImageTk.PhotoImage(file="img/en2v3.png")
ttk.Button(root, image=imag_e2, command=en_2).place(x=0, y=168)
#
imag_e3 = ImageTk.PhotoImage(file="img/en3v3.png")
ttk.Button(root, image=imag_e3, command=en_3).place(x=0, y=208)

root.mainloop()
