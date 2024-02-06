import pyautogui
from fun import move_to_click
from time import sleep

# duration=d_drag и duration=d с предметом и в свободном состоянии
d = 0.4
d_drag = 1.4
item = {'куртка рейдовоя': 'img/person/kurtka_r.png', 'куртка броня': 'img/person/kurtka_b.png',
        'брюки Бурбон': 'img/person/bruki_z.png', 'брюки броня': 'img/person/bruki_b.png',
        'перчатки': 'img/person/gloves.png', 'место перчаток': 'img/person/gloves_point.png',
        'орден': 'img/person/orden.png', 'инвентарь': 'img/person/inventar.png',
        'пустой слот': 'img/person/slot.png', 'маленький слот': 'img/person/p_slot.png',
        'фото Гаврила': 'img/person/gavril.png', 'выход': 'img/b_exit.png'}


def smena_kurtok():
    kurtka_r = pyautogui.locateCenterOnScreen(item.get("куртка рейдовоя"), confidence=0.9)
    kurtka_b = pyautogui.locateCenterOnScreen(item.get('куртка броня'), confidence=0.9)
    pyautogui.moveTo(kurtka_r, duration=d)
    pyautogui.dragTo(kurtka_b, duration=d_drag)
    # отводим указатель
    p_slot = pyautogui.locateCenterOnScreen(item.get('маленький слот'), confidence=0.9)
    pyautogui.moveTo(p_slot, duration=d)
    sleep(0.5)


def smena_bruk():
    bruki_z = pyautogui.locateCenterOnScreen(item.get('брюки Бурбон'), confidence=0.9)
    bruki_b = pyautogui.locateCenterOnScreen(item.get('брюки броня'), confidence=0.9)
    pyautogui.moveTo(bruki_z, duration=d)
    pyautogui.dragTo(bruki_b, duration=d_drag)
    # отводим указатель
    p_slot = pyautogui.locateCenterOnScreen(item.get('маленький слот'), confidence=0.9)
    pyautogui.moveTo(p_slot, duration=d)
    sleep(0.5)


def smena_per4():
    gloves_point = pyautogui.locateCenterOnScreen(item.get('место перчаток'), confidence=0.9)
    # если перчатки не надеты одеваем
    if gloves_point is not None:
        gloves = pyautogui.locateCenterOnScreen(item.get('перчатки'), confidence=0.9)
        pyautogui.moveTo(gloves, duration=d)
        pyautogui.dragTo(gloves_point, duration=d_drag)
    # иначе снимаем
    else:
        gloves = pyautogui.locateCenterOnScreen(item.get('перчатки'), confidence=0.9)
        slot = pyautogui.locateCenterOnScreen(item.get('пустой слот'), confidence=0.9)
        pyautogui.moveTo(gloves, duration=d)
        pyautogui.dragTo(slot, duration=d_drag)
    # отводим указатель
    p_slot = pyautogui.locateCenterOnScreen(item.get('маленький слот'), confidence=0.9)
    pyautogui.moveTo(p_slot, duration=d)
    sleep(0.5)


def smena_garderoba():
    inventar = pyautogui.locateCenterOnScreen(item.get('инвентарь'), confidence=0.9)
    # цикл в ожидании появления инвентаря
    move_to_click(inventar, 0.3)
    print('готов к переодеванию')
    smena_kurtok()
    smena_bruk()
    smena_per4()
    print('переодет')


def pereodevanie():
    gavril = pyautogui.locateCenterOnScreen(item.get('фото Гаврила'), confidence=0.9)
    if gavril is not None:
        move_to_click(gavril,0.3)
        sleep(0.5)
        smena_garderoba()
    else:
        smena_garderoba()
    vyxod = pyautogui.locateCenterOnScreen(item.get('выход'), confidence=0.9)
    move_to_click(vyxod, 0.3)

