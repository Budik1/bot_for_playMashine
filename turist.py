import pyautogui
from time import sleep, time
from fun_na4 import enemy_battle, vybor_zadaniya_na_puli
import baza_dannyx as b_d
from fun import push_close, move_to_click

# son = 1
# station = 1
number_of_gifts = 0
number_of_kiki = 0
number_of_krysa = 0


def _gift():
    """Поиск подарков на станции. Возвращает его позицию"""
    sleep(1)
    pos_gift = pyautogui.locateCenterOnScreen('img/tonelli/gift.png', confidence=0.75)
    # print(pos_gift, "подарок")
    if pos_gift is not None:
        x, y = pos_gift
        # x += 15
        # y -= 15
        pyautogui.moveTo(x, y, duration=0.5, tween=pyautogui.easeInOutQuad)
        pyautogui.click(x, y)
        sleep(1 * 2)
        close = pyautogui.locateCenterOnScreen('img/close.png', confidence=0.9)
        # если тормозит отрисовка, ожидает появление кнопки "закрыть"
        it = 0
        while close is None:
            it += 1
            sleep(1)
            close = pyautogui.locateCenterOnScreen('img/close.png', confidence=0.9)
            print(it, 'поиск закрыть в подарках')
        # print(close)
        pyautogui.moveTo(close, duration=1, tween=pyautogui.easeInOutQuad)
        pyautogui.click(close)
        sleep(1)
    return pos_gift


#
def to_map():
    """Из окна станции открывает карту. На Тургеневской выход смещен"""
    # print('def to_map')
    sleep(1)
    id_st = pyautogui.locateCenterOnScreen(b_d.turgenev[2], confidence=0.85)
    if id_st is not None:
        pos_or1 = pyautogui.locateCenterOnScreen('img/klan_red.png', confidence=0.85)
        x1, y1 = pos_or1
        x1, y1 = x1 + 205, y1 + 205
        pos_or1 = x1, y1
        pyautogui.moveTo(pos_or1, duration=0.2)
    else:
        pos_or1 = pyautogui.locateCenterOnScreen('img/klan_red.png', confidence=0.85)
        x1, y1 = pos_or1
        x1, y1 = x1 + 270, y1 + 180
        #
        pos_or1 = x1, y1
        pyautogui.moveTo(pos_or1, duration=0.2)
    sleep(1)
    pyautogui.click(pos_or1)
    sleep(1)
    vss = pyautogui.locateCenterOnScreen('img/tonelli/station_exit.png', confidence=0.8)

    pyautogui.moveTo(vss, duration=0.2)


def tunnel_events(st0, st2):
    """
    События в туннеле
    :param st0: название станции из списка
    :param st2: имя файла ID станции
    """
    # st0 , st2
    global number_of_gifts, number_of_kiki, number_of_krysa
    sleep(1)
    id_st = pyautogui.locateCenterOnScreen(st2, confidence=0.85)
    while id_st is None:
        info = pyautogui.locateCenterOnScreen('img/info.png', confidence=0.8)
        x, y = info
        y += 400
        pyautogui.moveTo(x, y)
        post = pyautogui.locateCenterOnScreen('img/tonelli/post.png', confidence=0.8)
        krysa = pyautogui.locateCenterOnScreen('img/tonelli/krysa.png', confidence=0.85)
        kiki = pyautogui.locateCenterOnScreen('img/tonelli/kikimora.png', confidence=0.85)
        skip_battle = pyautogui.locateCenterOnScreen('img/skip_battle.png', confidence=0.79)
        if skip_battle is not None:
            if krysa is not None:
                number_of_krysa += 1
                print(f'{number_of_krysa} Detekt krysa')
            if kiki is not None:
                number_of_kiki += 1
                print(f'{number_of_kiki} Detekt Kikimora')
            enemy_battle(1)
        if post is not None:
            pyautogui.moveTo(post, duration=0.2)
            attack = pyautogui.locateCenterOnScreen('img/tonelli/attack.png', confidence=0.85)
            entry = pyautogui.locateCenterOnScreen('img/tonelli/entry_station.png', confidence=0.8)
            if entry is not None:
                move_to_click(entry, 0.3)
                sleep(1)
            elif attack is not None:
                move_to_click(attack, 0.3)
                sleep(1)
        sleep(0.1)
        id_st = pyautogui.locateCenterOnScreen(st2, confidence=0.85)
    # print(st0)  # название станции
    pyautogui.moveTo(id_st, duration=1, tween=pyautogui.easeInOutQuad)
    # вызов функции "_gift()" и подсчет количества найденных
    pos_gift = _gift()
    if pos_gift is not None:
        number_of_gifts += 1
    # print(st0, ' подарков ', number_of_gifts)


# принимает имя файла поиска, выдаёт Point(x, y), параметр confidence
def poisk(chto_ishchem, param_confidence=0.99):
    sleep(1)
    pos_search = pyautogui.locateCenterOnScreen(chto_ishchem, confidence=param_confidence)
    while pos_search is None:
        param_confidence -= 0.01
        # print('в поиске станции confidence=', param_confidence)
        pos_search = pyautogui.locateCenterOnScreen(chto_ishchem, confidence=param_confidence)
        # print(pos_search)
    return pos_search, param_confidence


# Получает в переменной станцию из списка, при необходимости смещает карту. Передав в poisk название следующей станции,
# получает из него Point(x, y) поиска и параметр confidence,
def traffic_on_the_map(stan):
    to_map()
    sleep(1 * 2)
    ev_map = stan[3]
    pos_stan = pyautogui.locateCenterOnScreen(stan[1], confidence=0.84)
    if ev_map == 'стрелка север' and pos_stan is None:
        pos_click = pyautogui.locateCenterOnScreen('img/tonelli/mark_sever.png', confidence=0.85)
        move_to_click(pos_click, 0.3)
        sleep(1)
    elif ev_map == 'стрелка юг' and pos_stan is None:
        pos_click = pyautogui.locateCenterOnScreen('img/tonelli/mark_yug.png', confidence=0.85)
        move_to_click(pos_click, 0.3)
        sleep(1)
    point_poisk, confidence_poisk = poisk(stan[1])
    move_to_click(point_poisk, 0.3)
    tunnel_events(stan[0], stan[2])


# получает список маршрута и осуществляет движение по нему
def travel(track: list):
    """
    Принимает список содержащий маршрут
    :param track: list
    """
    for it in range(len(track)):
        k = it % len(track)
        # print(k, track[k])
        traffic_on_the_map(track[k])


def test():
    """
    Тест передвижения между станциями
    :return: количество встреченных крыс
    """
    global number_of_krysa
    push_close()
    travel(b_d.test_running)
    print("тест успешно выполнен")
    return number_of_krysa


def tasks_na_kievskoy():
    """Движение от Кузнецкого моста на Киевскую - выполнение заданий нач. станции - движение до Кузнецкого моста -
    выполнение заданий нач. станции пока есть задания удовлетворяющие поиск"""
    push_close()
    most_kiev()
    vybor_zadaniya_na_puli()
    print('задания на Киевской выполнены')
    kiev_most()
    vybor_zadaniya_na_puli()
    print('энергия исчерпана')


# движение от park_kr до Кузнецкого моста
def riga_most():
    """Маршрут Рижская - Кузнецкий мост"""
    start_time = time()
    push_close()
    travel(b_d.riga_most)
    print("вернулся домой")
    finish_time = float(time() - start_time)  # общее количество секунд
    minutes = int(finish_time // 60)  # количество минут
    seconds = round((finish_time % minutes), 2)
    print('Потрачено время', minutes, 'минут', seconds, 'сек.')


def frunze_most():
    """Маршрут Фрунзенская - Кузнецкий мост"""
    start_time = time()
    push_close()
    travel(b_d.frunze_most)
    finish_time = float(time() - start_time)  # общее количество секунд
    minutes = int(finish_time // 60)  # количество минут
    seconds = round((finish_time % minutes), 2)
    print('Потрачено время', minutes, 'минут', seconds, 'сек.')


def most_frunze():
    """Маршрут Кузнецкий мост - Фрунзенская"""
    start_time = time()
    push_close()
    travel(b_d.most_frunze)
    finish_time = float(time() - start_time)  # общее количество секунд
    minutes = int(finish_time // 60)  # количество минут
    seconds = round((finish_time % minutes), 2)
    print('Потрачено время', minutes, 'минут', seconds, 'сек.')


# движение от
def most_riga():
    # движение от
    """Маршрут Кузнецкий мост - Киевская"""
    start_time = time()
    push_close()
    travel(b_d.most_riga)
    print("пришел на Рижскую")
    finish_time = float(time() - start_time)  # общее количество секунд
    minutes = int(finish_time // 60)  # количество минут
    seconds = round((finish_time % minutes), 2)
    print('Потрачено время', minutes, ' минут', seconds, ' сек.')


def kiev_most():
    """Маршрут Киевская - Кузнецккий мост """
    start_time = time()
    push_close()
    travel(b_d.kiev_most)
    print("вернулся домой")
    finish_time = float(time() - start_time)  # общее количество секунд
    minutes = int(finish_time // 60)  # количество минут
    seconds = round((finish_time % minutes), 2)
    print('Потрачено время', minutes, ' минут', seconds, ' сек.')


def kiev_frunze():
    """Маршрут Киевская - Фрунзенская"""
    start_time = time()
    push_close()
    travel(b_d.kiev_frunze)
    print("вернулся домой")
    finish_time = float(time() - start_time)  # общее количество секунд
    minutes = int(finish_time // 60)  # количество минут
    seconds = round((finish_time % minutes), 2)
    print('Потрачено время', minutes, ' минут', seconds, ' сек.')


# движение от Кузнецкого моста на Киевскую
def most_kiev():
    """Маршрут Кузнецкий мост - Киевская"""
    start_time = time()
    push_close()
    travel(b_d.most_kiev)
    print("пришел на Киевскую")
    finish_time = float(time() - start_time)  # общее количество секунд
    minutes = int(finish_time // 60)  # количество минут
    seconds = round((finish_time % minutes), 2)
    print('Потрачено время', minutes, ' минут', seconds, ' сек.')


def frunze_kiev():
    """Маршрут Фрунзенская - Киевская"""
    start_time = time()
    push_close()
    travel(b_d.frunze_kiev)
    print("пришел на Киевскую")
    finish_time = float(time() - start_time)  # общее количество секунд
    minutes = int(finish_time // 60)  # количество минут
    seconds = round((finish_time % minutes), 2)
    print('Потрачено время', minutes, 'минут', seconds, 'сек.')


def frunze_riga():
    """Маршрут Фрунзенская"""
    start_time = time()
    push_close()
    travel(b_d.frunze_riga)
    print("вернулся домой")
    finish_time = float(time() - start_time)  # общее количество секунд
    minutes = int(finish_time // 60)  # количество минут
    seconds = round((finish_time % minutes), 2)
    print('Потрачено время', minutes, ' минут', seconds, ' сек.')


def riga_frunze():
    """Маршрут  Фрунзенская"""
    start_time = time()
    push_close()
    travel(b_d.riga_frunze)
    print("вернулся домой")
    finish_time = float(time() - start_time)  # общее количество секунд
    minutes = int(finish_time // 60)  # количество минут
    seconds = round((finish_time % minutes), 2)
    print('Потрачено время', minutes, ' минут', seconds, ' сек.')


def za_kikimorami():
    """При смене станции прописки список содержащий маршрут надо переписывать вручную."""
    start_time = time()
    push_close()
    travel(b_d.frunze_kikimory)
    print('на сегодня кикиморы выбиты')
    finish_time = float(time() - start_time)  # общее количество секунд
    minutes = int(finish_time // 60)  # количество минут
    seconds = round((finish_time % minutes), 2)
    print('Потрачено время', minutes, 'минут', seconds, 'сек.')


def pauk_yascher():
    """При смене станции прописки список содержащий маршрут надо переписывать вручную."""
    start_time = time()
    push_close()
    travel(b_d.pauk_yascher)
    print('на сегодня все пауки с ящерами зачищены')
    finish_time = float(time() - start_time)  # общее количество секунд
    minutes = int(finish_time // 60)  # количество минут
    seconds = round((finish_time % minutes), 2)
    print('Потрачено время', minutes, 'минут', seconds, 'сек.')


def sbor_podarkov():
    """Обход всех станций. При смене станции прописки список содержащий маршрут надо переписывать вручную."""
    push_close()
    # travel(b_d.bypass)
    for it in range(len(b_d.bypass)):
        k = it % len(b_d.bypass)
        # print(k, b_d.bypass[k])
        traffic_on_the_map(b_d.bypass[k])
    print("все подарки под ёлками собраны")
