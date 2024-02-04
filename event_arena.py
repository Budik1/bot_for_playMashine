import pyautogui
from time import sleep
from fun_na4 import moveTo_click, boy_v_puti


def foto(put_imya, _region):
    im1 = pyautogui.screenshot(region=_region)
    im1.save(put_imya)


def foto_pos(name_img, region, tune_x=0, tune_y=0, tune_s=0, tune_v=0):
    # получает регион и коректировки снимка внутри него
    x_pOan, y_pOan, shirina, vysota = region
    # print(x_pOan, y_pOan)
    x_s = x_pOan + tune_x
    y_s = y_pOan + tune_y
    shirina_s = shirina - tune_s
    vysota_s = vysota - tune_v
    foto(name_img, (x_s, y_s, shirina_s, vysota_s))


def orientir(shirina=77, vysota=42):
    # закрыть если открыто, т.к. за чем-то может быть не видна позиция привязки
    zakr = pyautogui.locateCenterOnScreen('img/zakryt.png', confidence=0.9)
    if zakr is not None:
        moveTo_click(zakr, 0.3)
    # получение координат привязки
    pos_orV = pyautogui.locateCenterOnScreen('img/zal_slavy.png', confidence=0.9)  # , region=(800, 80, 90, 90)
    pyautogui.moveTo(pos_orV)
    sleep(0.5)
    # print(pos_orV, 'ориентир клан')
    x_or, y_or = pos_orV
    return pos_orV


def create_img_arena_object():
    pos_orV = orientir()  # ориентир на зал славы
    pyautogui.moveTo(pos_orV)
    print(pos_orV)
    moveTo_click(pos_orV, 0.3)  # открыть зал славы
    pyautogui.moveTo(pos_orV[0] - 678, pos_orV[1] + 144)
    sleep(1)
    step = 68
    # pos_orV[0] - 778, pos_orV[1] + 144
    region = (pos_orV[0] - 678, pos_orV[1] + 74 + (step * 1), 368, 80)
    tune_x = 73  #
    tune_y = 7  #
    tune_s = 243  # 21 с увеличением регион уменьшается
    tune_v = 20  #
    # 235, 267,  378,
    foto_pos('img/test/arena_object.png', region, tune_x, tune_y, tune_s, tune_v)

    # pos2 = pos_orV[0] - 678, pos_orV[1] + 74 + (step * 2)
    # pyautogui.moveTo(pos2)
    # region = (pos2[0], pos2[1], 368, 80)
    # foto_pos('img/test/arena_object2.png', region)
    #
    # pos3 = pos_orV[0] - 678, pos_orV[1] + 74 + (step * 3)
    # pyautogui.moveTo(pos3)
    # region = (pos3[0], pos3[1], 368, 80)
    # foto_pos('img/test/arena_object3.png', region)

    # pos4 = pos_orV[0] - 678, pos_orV[1] + 74 + (step * 4)
    # pyautogui.moveTo(pos4)
    # region = (pos4[0], pos4[1], 368, 80)
    # foto_pos('img/test/arena_object4.png', region)
    #
    # pos5 = pos_orV[0] - 678, pos_orV[1] + 74 + (step * 5)
    # pyautogui.moveTo(pos5)
    # region = (pos5[0], pos5[1], 368, 80)
    # foto_pos('img/test/arena_object5.png', region)
    #
    # pos6 = pos_orV[0] - 678, pos_orV[1] + 74 + (step * 6)
    # pyautogui.moveTo(pos6)
    # region = (pos6[0], pos6[1], 368, 80)
    # foto_pos('img/test/arena_object6.png', region)


def cill():
    boy_in_arena = 0
    while True:
        pos_orV = orientir()
        # print(pos_orV)
        moveTo_click(pos_orV, 0.3)
        x, y = pos_orV
        x -= 665
        y += 144
        region = (x, y, 560, 80)
        region_ret = region
        pyautogui.moveTo(174, 260)
        sleep(1)
        arena_object = pyautogui.locateCenterOnScreen("img/test/arena_object.png", region=region,
                                                      confidence=0.9)
        # foto_pos('img/test/arena_obl_poiska.png', region)
        pyautogui.moveTo(arena_object)
        skroll_up = pyautogui.locateCenterOnScreen('img/skroll_up.png', confidence=0.9)
        if arena_object is None:
            _it = 0
            x, y, sh, v = region
            while arena_object is None and _it <= 5 :
                _it += 1
                y += 68
                # print(_it, y)
                region = (x, y, sh, v)
                arena_object = pyautogui.locateCenterOnScreen("img/test/arena_object.png", region=region,
                                                              confidence=0.9)


        while arena_object is None:
            region = region_ret
            while skroll_up is not None and arena_object is None:
                moveTo_click(skroll_up, 0.5)
                pyautogui.moveTo(174, 260)
                skroll_up = pyautogui.locateCenterOnScreen('img/skroll_up.png', confidence=0.9)
                arena_object = pyautogui.locateCenterOnScreen("img/test/arena_object.png", region=region,
                                                              confidence=0.85)
            if arena_object is None:
                skroll_down = pyautogui.locateCenterOnScreen('img/skroll_down.png', confidence=0.9)
                moveTo_click(skroll_down, 0.3)
                arena_object = pyautogui.locateCenterOnScreen("img/test/arena_object.png", region=region,
                                                              confidence=0.85)
            # print(arena_object)
        boy_in_arena +=1
        name_file =  str("img/test/arena_obl_poiska" + str(boy_in_arena) + ".png")
        # print(boy_in_arena)
        print(name_file)
        # foto_pos('img/test/arena_obl_poiska.png', region)
        foto(name_file, region)
        ataka_arena_object = pyautogui.locateCenterOnScreen('img/ataka.png', confidence=0.9, region=region)
        pyautogui.moveTo(ataka_arena_object)
        # sleep()
        moveTo_click(ataka_arena_object, 0.5)
        hero_vs_arena_object = pyautogui.locateCenterOnScreen('img/hero_vs_arena_object.png', confidence=0.9)
        while hero_vs_arena_object is None:
            sleep(0.1)
            hero_vs_arena_object = pyautogui.locateCenterOnScreen('img/hero_vs_arena_object.png', confidence=0.9)
        moveTo_click(hero_vs_arena_object, 0.3)
        sleep(2)
        boy_v_puti(0.1)


# create_img_arena_object()  # создание метки объекта атаки
cill()  # цикл атаки объекта
#
