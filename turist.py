import pyautogui
from time import sleep, time
from fun_na4 import boy_v_puti, moveTo_click, vybor_zadaniya_na_puli
import baza_dannyx as b_d
from fun import zakryt

# import datetime

son = 0.5
station = 1
number_of_gifts = 0
number_of_kiki = 0
number_of_krysa = 0


# def time_now():
#     now = datetime.datetime.now()
#     date_time = (now.strftime('%Y-%m-%d_%H:%M:%S'))
#     date = (now.date())
#     return date_time, date

# ищет подарок на станции
def _podarok():
    '''Сбор подарков на станциях'''
    sleep(son)
    pos_podarok = pyautogui.locateCenterOnScreen('img/tonelli/podarok.png', confidence=0.75)
    # print(pos_podarok, "podarok")
    if pos_podarok is not None:
        x, y = pos_podarok
        # x += 15
        # y -= 15
        pyautogui.moveTo(x, y, duration=0.5, tween=pyautogui.easeInOutQuad)
        pyautogui.click(x, y)
        sleep(son * 2)
        zakryt = pyautogui.locateCenterOnScreen('img/zakryt.png', confidence=0.9)
        # если тормозит отрисовка ожидает появление кнопки "закрыть"
        it = 0
        while zakryt is None:
            it += 1
            sleep(son)
            zakryt = pyautogui.locateCenterOnScreen('img/zakryt.png', confidence=0.9)
            print(it, 'поиск закрыть в подарках')
        # print(zakryt)
        pyautogui.moveTo(zakryt, duration=1, tween=pyautogui.easeInOutQuad)
        pyautogui.click(zakryt)
        sleep(son)
    return pos_podarok


# Из окна станции открывает карту. На Тургеневской выход смещен
def vyxod__na__kartu():
    # print('def vyxod__na__kartu')
    sleep(son)
    stanciya = pyautogui.locateCenterOnScreen(b_d.turgenev[2], confidence=0.85)
    if stanciya is not None:
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
    sleep(son)
    pyautogui.click(pos_or1)
    # можно попробовать фукцию poisk
    sleep(son)
    vss = pyautogui.locateCenterOnScreen('img/tonelli/vyxod_so_stanc.png', confidence=0.8)

    pyautogui.moveTo(vss, duration=0.2)


# 149
def tunnel_events(st0, st2):
    # st0 название станции из списка, st2 имя файла ID станции
    global number_of_gifts, number_of_kiki, number_of_krysa
    sleep(son)
    stanciya = pyautogui.locateCenterOnScreen(st2, confidence=0.85)
    while stanciya is None:
        info = pyautogui.locateCenterOnScreen('img/info.png', confidence=0.8)
        x, y = info
        y += 400
        pyautogui.moveTo(x, y)
        post = pyautogui.locateCenterOnScreen('img/tonelli/post.png', confidence=0.8)
        krysa = pyautogui.locateCenterOnScreen('img/tonelli/krysa.png', confidence=0.85)
        kiki = pyautogui.locateCenterOnScreen('img/tonelli/kikimora.png', confidence=0.85)
        propusk_boy = pyautogui.locateCenterOnScreen('img/propustit_boy.png', confidence=0.79)
        if propusk_boy is not None:
            if krysa is not None:
                number_of_krysa += 1
                print(f'{number_of_krysa} Detekt krysa')
            if kiki is not None:
                number_of_kiki += 1
                print(f'{number_of_kiki} Detekt Kikimora')
            boy_v_puti(1)
        if post is not None:
            pyautogui.moveTo(post, duration=0.2)
            ataka = pyautogui.locateCenterOnScreen('img/tonelli/ataka.png', confidence=0.85)
            voyti = pyautogui.locateCenterOnScreen('img/tonelli/voyti_na_stanciyu.png', confidence=0.8)
            if voyti is not None:
                moveTo_click(voyti, 0.3)
                sleep(son)
            elif ataka is not None:
                moveTo_click(ataka, 0.3)
                sleep(son)
        sleep(0.1)
        stanciya = pyautogui.locateCenterOnScreen(st2, confidence=0.85)
    # print(st0)  # название станции
    pyautogui.moveTo(stanciya, duration=1, tween=pyautogui.easeInOutQuad)
    # вызов функции "_podarok()" и подсчет количества найденных
    pos_podarka = _podarok()
    if pos_podarka is not None:
        number_of_gifts += 1
    # print(st0, ' подарков ', number_of_gifts)


# принимает имя файла поиска, выдаёт Point(x, y), параметр confidence
def poisk(chto_ishchem, param_confidence=0.99):
    sleep(son)
    pos_poiska = pyautogui.locateCenterOnScreen(chto_ishchem, confidence=param_confidence)
    while pos_poiska is None:
        param_confidence -= 0.01
        # print('в поиске станции confidence=', param_confidence)
        pos_poiska = pyautogui.locateCenterOnScreen(chto_ishchem, confidence=param_confidence)
        # print(pos_poiska)
    return pos_poiska, param_confidence


# получает в переменной станцию из списка, при необходимости смещает карту. Передав в poisk название следующей станциии,
# получает из него
# Point(x, y) поиска и параметр confidence,
def traffic_on_the_map(stan):
    vyxod__na__kartu()
    sleep(son * 2)
    pos_stanc1 = stan[3]
    pos_stanc2 = pyautogui.locateCenterOnScreen(stan[1], confidence=0.84)
    if pos_stanc1 == 'стрелка север' and pos_stanc2 is None:
        pos_lok = pyautogui.locateCenterOnScreen('img/tonelli/strelka_sever.png', confidence=0.85)
        moveTo_click(pos_lok, 0.3)
        sleep(son)
    elif pos_stanc1 == 'стрелка юг' and pos_stanc2 is None:
        pos_lok = pyautogui.locateCenterOnScreen('img/tonelli/strelka_yug.png', confidence=0.85)
        moveTo_click(pos_lok, 0.3)
        sleep(son)
    point_poisk, confidence_poisk = poisk(stan[1])
    moveTo_click(point_poisk, 0.3)
    tunnel_events(stan[0], stan[2])


# получает список маршрута и осуществляет движение по нему
def peredvizgenie(kuda_idti):
    for it in range(len(kuda_idti)):
        k = it % len(kuda_idti)
        # print(k, kuda_idti[k])
        traffic_on_the_map(kuda_idti[k])


def test():
    global number_of_krysa
    zakryt()
    peredvizgenie(b_d.test_probezgka)
    print("тест успешно выполнен")
    return number_of_krysa


# движение от Кузнецкого моста на Киевскую, выполнение заданий начстанции, движение до Кузнецкого моста,
# выполнение заданий начстанции пока есть задания удовлетворяющие поиск
def zadaniya_na_Kievskoy():
    zakryt()
    most_kiev()
    vybor_zadaniya_na_puli()
    print('задания на Киевской выполнены')
    kiev_most()
    vybor_zadaniya_na_puli()
    print('энергия исчерпана')


# движение от park_kr до Кузнецкого моста
def riga_most():
    start_time = time()
    zakryt()
    peredvizgenie(b_d.riga_most)
    print("вернулся домой")
    finish_time = float(time() - start_time)  # общее количество секунд
    minuty = int(finish_time // 60)  # количество минут
    sekundy = round((finish_time % minuty), 2)
    print('Потрачено время', minuty, 'минут', sekundy, 'сек.')


def frunze_most():
    start_time = time()
    zakryt()
    peredvizgenie(b_d.frunze_most)
    finish_time = float(time() - start_time)  # общее количество секунд
    minuty = int(finish_time // 60)  # количество минут
    sekundy = round((finish_time % minuty), 2)
    print('Потрачено время', minuty, 'минут', sekundy, 'сек.')


def most_frunze():
    start_time = time()
    zakryt()
    peredvizgenie(b_d.most_frunze)
    finish_time = float(time() - start_time)  # общее количество секунд
    minuty = int(finish_time // 60)  # количество минут
    sekundy = round((finish_time % minuty), 2)
    print('Потрачено время', minuty, 'минут', sekundy, 'сек.')


# движение от Кузнецкого моста на Киевскую
def most_riga():
    start_time = time()
    zakryt()
    peredvizgenie(b_d.most_riga)
    print("пришел на Рижскую")
    finish_time = float(time() - start_time)  # общее количество секунд
    minuty = int(finish_time // 60)  # количество минут
    sekundy = round((finish_time % minuty), 2)
    print('Потрачено время', minuty, ' минут', sekundy, ' сек.')


# движение от Киевской до Кузнецкого моста
def kiev_most():
    start_time = time()
    zakryt()
    peredvizgenie(b_d.kiev_most)
    print("вернулся домой")
    finish_time = float(time() - start_time)  # общее количество секунд
    minuty = int(finish_time // 60)  # количество минут
    sekundy = round((finish_time % minuty), 2)
    print('Потрачено время', minuty, ' минут', sekundy, ' сек.')


def kiev_frunze():
    start_time = time()
    zakryt()
    peredvizgenie(b_d.kiev_frunze)
    print("вернулся домой")
    finish_time = float(time() - start_time)  # общее количество секунд
    minuty = int(finish_time // 60)  # количество минут
    sekundy = round((finish_time % minuty), 2)
    print('Потрачено время', minuty, ' минут', sekundy, ' сек.')


# движение от Кузнецкого моста на Киевскую
def most_kiev():
    start_time = time()
    zakryt()
    peredvizgenie(b_d.most_kiev)
    print("пришел на Киевскую")
    finish_time = float(time() - start_time)  # общее количество секунд
    minuty = int(finish_time // 60)  # количество минут
    sekundy = round((finish_time % minuty), 2)
    print('Потрачено время', minuty, ' минут', sekundy, ' сек.')


def frunze_kiev():
    start_time = time()
    zakryt()
    peredvizgenie(b_d.frunze_kiev)
    print("пришел на Киевскую")
    finish_time = float(time() - start_time)  # общее количество секунд
    minuty = int(finish_time // 60)  # количество минут
    sekundy = round((finish_time % minuty), 2)
    print('Потрачено время', minuty, 'минут', sekundy, 'сек.')


def za_kikimorami():
    start_time = time()
    zakryt()
    peredvizgenie(b_d.frunze_kikimory)
    print('на сегодня кикиморы выбиты')
    finish_time = float(time() - start_time)  # общее количество секунд
    minuty = int(finish_time // 60)  # количество минут
    sekundy = round((finish_time % minuty), 2)
    print('Потрачено время', minuty, 'минут', sekundy, 'сек.')


def pauk_yascher():
    start_time = time()
    zakryt()
    peredvizgenie(b_d.pauk_yascher)
    print('на сегодня все пауки с ящерами зачищены')
    finish_time = float(time() - start_time)  # общее количество секунд
    minuty = int(finish_time // 60)  # количество минут
    sekundy = round((finish_time % minuty), 2)
    print('Потрачено время', minuty, 'минут', sekundy, 'сек.')


def sbor_podarkov():
    zakryt()
    # peredvizgenie(b_d.beg_po_krugu)
    for it in range(len(b_d.beg_po_krugu)):
        k = it % len(b_d.beg_po_krugu)
        # print(k, b_d.beg_po_krugu[k])
        traffic_on_the_map(b_d.beg_po_krugu[k])
    print("все подарки под ёлками собраны")
