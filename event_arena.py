import pyautogui
from time import sleep
from fun_na4 import boy_v_puti
from fun import move_to_click


def foto(path_name, _region):
    """
    Создает снимок нужного участка экрана
    :param path_name: имя файла
    :param _region: регион (X, Y, ширина, высота)
    """
    im1 = pyautogui.screenshot(region=_region)
    im1.save(path_name)


def foto_pos(name_img: str, region: tuple, tune_x=0, tune_y=0, tune_s=0, tune_v=0):
    """Получает регион и корректирует регион снимка"""
    x_p_oan, y_p_oan, width, height = region
    x_s = x_p_oan + tune_x
    y_s = y_p_oan + tune_y
    width_s = width - tune_s
    height_s = height - tune_v
    foto(name_img, (x_s, y_s, width_s, height_s))


def pig():  # width=77, height=42
    """Закрыть если открыто, т.к. за чем-то может быть не видна позиция привязки"""
    #
    close = pyautogui.locateCenterOnScreen('img/close.png', confidence=0.9)
    if close is not None:
        move_to_click(close, 0.3)
    # получение координат привязки
    pos_or_v = pyautogui.locateCenterOnScreen('img/hall_of_glory.png', confidence=0.9)
    pyautogui.moveTo(pos_or_v)
    sleep(0.5)
    # print(pos_or_v, 'ориентир клан')
    return pos_or_v


def create_img_arena_object():
    pos_or_v = pig()  # ориентир на зал славы
    pyautogui.moveTo(pos_or_v)
    print(pos_or_v)
    move_to_click(pos_or_v, 0.3)  # открыть зал славы
    pyautogui.moveTo(pos_or_v[0] - 678, pos_or_v[1] + 144)
    sleep(1)
    step = 68
    region = (pos_or_v[0] - 678, pos_or_v[1] + 74 + (step * 1), 368, 80)
    tune_x = 73  #
    tune_y = 7  #
    tune_s = 243  # 21 с увеличением регион уменьшается
    tune_v = 20  #
    foto_pos('img/test/arena_object.png', region, tune_x, tune_y, tune_s, tune_v)


def kill():
    boy_in_arena = 0
    while True:
        pos_or_v = pig()
        # print(pos_or_v)
        move_to_click(pos_or_v, 0.3)
        x, y = pos_or_v
        x -= 665
        y += 144
        region = (x, y, 560, 80)
        region_ret = region
        pyautogui.moveTo(174, 260)
        sleep(1)
        arena_object = pyautogui.locateCenterOnScreen("img/test/arena_object.png", region=region,
                                                      confidence=0.9)
        pyautogui.moveTo(arena_object)
        scroll_up = pyautogui.locateCenterOnScreen('img/scroll_up.png', confidence=0.9)
        if arena_object is None:
            _it = 0
            x, y, sh, v = region
            while arena_object is None and _it <= 5:
                _it += 1
                y += 68
                # print(_it, y)
                region = (x, y, sh, v)
                arena_object = pyautogui.locateCenterOnScreen("img/test/arena_object.png", region=region,
                                                              confidence=0.9)

        while arena_object is None:
            region = region_ret
            while scroll_up is not None and arena_object is None:
                move_to_click(scroll_up, 0.5)
                pyautogui.moveTo(174, 260)
                scroll_up = pyautogui.locateCenterOnScreen('img/scroll_up.png', confidence=0.9)
                arena_object = pyautogui.locateCenterOnScreen("img/test/arena_object.png", region=region,
                                                              confidence=0.85)
            if arena_object is None:
                scroll_down = pyautogui.locateCenterOnScreen('img/scroll_down.png', confidence=0.9)
                move_to_click(scroll_down, 0.3)
                arena_object = pyautogui.locateCenterOnScreen("img/test/arena_object.png", region=region,
                                                              confidence=0.85)
        boy_in_arena += 1
        name_file = str("img/test/arena_obl_поиска" + str(boy_in_arena) + ".png")
        # print(boy_in_arena)
        print(name_file)
        foto(name_file, region)
        attack_arena_object = pyautogui.locateCenterOnScreen('img/attack.png', confidence=0.9, region=region)
        pyautogui.moveTo(attack_arena_object)
        # sleep()
        move_to_click(attack_arena_object, 0.5)
        hero_vs_arena_object = pyautogui.locateCenterOnScreen('img/hero_vs_arena_object.png', confidence=0.9)
        while hero_vs_arena_object is None:
            sleep(0.1)
            hero_vs_arena_object = pyautogui.locateCenterOnScreen('img/hero_vs_arena_object.png', confidence=0.9)
        move_to_click(hero_vs_arena_object, 0.3)
        sleep(2)
        boy_v_puti(0.1)


# create_img_arena_object()  # создание метки объекта атаки
kill()  # цикл атаки объекта
#
