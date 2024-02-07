import baza_dannyx as b_d
import pyautogui
from time import sleep
from fun import move_to_click

conf = 0.97
# son = 0.9

par_conf = 0.8
# xp_imag = ['img/23xp.png', 'img/45xp.png', 'img/68xp.png', 'img/90xp.png', 'img/113xp.png']
energy_availability = 1
koli4estvo_zadaniy = 1
width, height = 87, 39
variable = None
region1, region2, region3 = 0, 0, 0


def station_master():
    """заходит в палатку к нач станции"""
    # print('station_master')
    check = pyautogui.locateCenterOnScreen('img/station_master.png', confidence=0.9)
    # if check is not None:
    if check:
        na4 = pyautogui.locateCenterOnScreen('img/station_master.png', confidence=par_conf)
        pyautogui.moveTo(na4, duration=1, tween=pyautogui.easeInOutQuad)
        # print(" уже у начальника ")
        sleep(1 / 3)
    else:
        pos_klan = pyautogui.locateCenterOnScreen('img/klan_red.png', confidence=0.85)
        # while pos_klan is None:
        while not pos_klan:
            sleep(0.1)
            pos_klan = pyautogui.locateCenterOnScreen('img/klan_red.png', confidence=0.85)
            # print('в поиске клана', pos_klan)
        # print('клан = ', pos_klan)
        x1, y1 = pos_klan
        x1, y1 = x1 - 60, y1 + 200
        pos_klan = x1, y1
        move_to_click(pos_klan, 0.2)
        # print('зашел к начальнику')
        sleep(1)
        na4 = pyautogui.locateCenterOnScreen('img/station_master.png', confidence=par_conf)
        pyautogui.moveTo(na4, duration=1, tween=pyautogui.easeInOutQuad)


def orientir():
    """ Получение значений "region=" для поиска заданий """
    #
    # закрыть если открыто
    close = pyautogui.locateCenterOnScreen('img/close.png', confidence=0.9)
    if close:
        move_to_click(close, 0.2)
    # получение координат привязки
    pos_or_v = pyautogui.locateCenterOnScreen('img/klan_red.png', confidence=0.9)
    pyautogui.moveTo(pos_or_v)
    sleep(0.5)
    # print(pos_or_v, 'ориентир верх')
    xor_v, yor_v = pos_or_v
    pos_or_n = pyautogui.locateCenterOnScreen('img/shesternya.png', confidence=0.9)
    # print(pos_or_n, 'ориентир низ')
    xor_n, yor_n = pos_or_n

    station_master()

    # регион поиска 1 (позиция анализа)
    x_p_oan1 = (xor_n - xor_v) / 2 + xor_v + 193
    y_p_oan1 = (yor_n - yor_v) / 2 + yor_v - 39
    x_p_oan1, y_p_oan1 = int(x_p_oan1), int(y_p_oan1)
    region_1 = [x_p_oan1, y_p_oan1, width, height]

    # регион поиска 2 (позиция анализа)
    x_p_oan2 = (xor_n - xor_v) / 2 + xor_v + 193
    y_p_oan2 = (yor_n - yor_v) / 2 + yor_v + 64
    x_p_oan2, y_p_oan2 = int(x_p_oan2), int(y_p_oan2)
    region_2 = [x_p_oan2, y_p_oan2, width, height]

    # регион поиска 3 (позиция анализа)
    x_p_oan3 = (xor_n - xor_v) / 2 + xor_v + 193
    y_p_oan3 = (yor_n - yor_v) / 2 + yor_v + 167
    x_p_oan3, y_p_oan3 = int(x_p_oan3), int(y_p_oan3)
    region_3 = [x_p_oan3, y_p_oan3, width, height]

    return region_1, region_2, region_3


def enemy_attack(delay=2):
    '''
    Событие атаки противника
    :param delay:
    '''
    # дождаться "пропустить бой", нажать собаку если активна, закрыть бой
    # print('v_puti')
    boy_end = pyautogui.locateCenterOnScreen('img/b_boy_end.png', confidence=par_conf)
    skip_fight = pyautogui.locateCenterOnScreen('img/skip_fight.png', confidence=par_conf)
    dog = pyautogui.locateCenterOnScreen('img/dog.png', confidence=par_conf)
    it = 0
    while boy_end is None:
        # print(boy_end, 'boy_end')
        # print('пропуск боя', skip_fight)
        if dog is not None:  # нажать "на собаку"
            # print(dog, 'dog')
            move_to_click(dog, 0.1)
        # print(it)
        if skip_fight is not None and it >= 2:  # нажать "пропустить бой"
            move_to_click(skip_fight, 0.5)
            # print(skip_fight, 'skip_fight')
        it += 1
        sleep(1 * delay)
        boy_end = pyautogui.locateCenterOnScreen('img/b_boy_end.png', confidence=par_conf)
        close = pyautogui.locateCenterOnScreen('img/close.png', confidence=par_conf)
        dog = pyautogui.locateCenterOnScreen('img/dog.png', confidence=par_conf)
        skip_fight = pyautogui.locateCenterOnScreen('img/skip_fight.png', confidence=par_conf)
        if boy_end is not None and close is not None:  # нажать закрыть в конце боя
            move_to_click(close, 0.2)
            sleep(0.5)


def press_en(task_number, pos):
    global energy_availability
    x = pos[0]
    y = pos[1] - 20
    pos_clik = x, y
    # pyautogui.moveTo(pos_clik) # для отладки
    # print('тут должен быть клик') # для отладки
    move_to_click(pos_clik, 1.5)
    sleep(0.5)
    nal_energy = pyautogui.locateCenterOnScreen('img/low_energy.png', confidence=0.8)
    # print(" не хватает энергии", nal_energy)
    if not nal_energy:
        print('Выполняю ', task_number, ' задание')
        enemy_attack()
    else:
        energy_availability = 0
        print(' Энергия закончилась!!')
        sleep(1)
        close = pyautogui.locateCenterOnScreen('img/close.png')
        move_to_click(close, 0.5)


def task_analysis(img1, img2, region):
    """
    При анализе через картинки получает их и region= поиска
    :param img1: *.png
    :param img2: *.png
    :param region:
    :return: Point | None
    """

    # print('task_analysis')
    # print( region) # полученный region
    global variable
    # print('вызов na4Stanc в анализе')
    station_master()
    # print('в task_analysis conf =', conf)
    variant1 = pyautogui.locateCenterOnScreen(img1, confidence=conf, region=region)
    # print(variant1, 'variant1')
    variant2 = pyautogui.locateCenterOnScreen(img2, confidence=conf, region=region)
    # print(variant2, 'variant2')
    if variant1:
        variable = variant1
    else:
        variable = variant2
    return (variable)


def move(pos):
    if pos is not None:
        pyautogui.moveTo(pos, duration=1)
        sleep(3)


def data_station():
    # получение списка заданий
    it = 0
    n_in_list = 0
    while it < len(b_d.list_of_stations):
        img_station = b_d.list_of_stations[it][2]
        # print(img_station)
        # print(it, n_in_list)
        pos = pyautogui.locateCenterOnScreen(img_station, confidence=0.9)
        if pos is not None:
            it = len(b_d.list_of_stations)
        else:
            n_in_list += 1
            it += 1
    zadaniya = (b_d.list_of_stations[n_in_list][4])
    # print(img_station)
    # print(zadaniya)
    return zadaniya


def vybor_zadaniya_na_puli():
    xp_imag = data_station()
    region1, region2, region3 = orientir()
    global energy_availability, koli4estvo_zadaniy, conf
    while energy_availability == 1 and koli4estvo_zadaniy > 0:
        # print('вызов task_analysis из vybor_zadaniya_na_puli')
        task_analysis(xp_imag[0], xp_imag[1], region1)
        variant1 = variable
        # print('variant1 = ', variant1)
        move(variant1)
        sleep(0.1)

        # print('вызов task_analysis из vybor_zadaniya_na_puli')
        task_analysis(xp_imag[2], xp_imag[3], region2)
        variant2 = variable
        # print('variant2 = ', variant2)
        move(variant2)
        sleep(0.1)

        # print('вызов task_analysis из vybor_zadaniya_na_puli')
        task_analysis(xp_imag[4], xp_imag[5], region3)
        variant3 = variable
        # print('variant3 = ', variant3)
        move(variant3)
        sleep(0.1)

        if variant1 is not None:
            press_en(1, region1)
        if variant2 is not None:
            press_en(2, region2)
        if variant3 is not None:
            press_en(3, region3)

        if variant1 == variant2 == variant3:
            print('confidence=', conf)
            conf -= 0.01

    print(' Задания выполнены!!!!')
    koli4estvo_zadaniy = 1
    energy_availability = 1
    zakr = pyautogui.locateCenterOnScreen('img/close.png', confidence=0.9)
    while zakr is not None:
        move_to_click(zakr, 0.3)
        zakr = pyautogui.locateCenterOnScreen('img/close.png', confidence=0.9)


def en_nomer_zadaniya(nomer_zadaniya):
    global energy_availability, koli4estvo_zadaniy, conf
    region1, region2, region3 = orientir()
    if nomer_zadaniya == 1:
        region = region1
    elif nomer_zadaniya == 2:
        region = region2
    else:
        region = region3

    while energy_availability == 1 and koli4estvo_zadaniy > 0:
        station_master()
        press_en(nomer_zadaniya, region)
    print(' Задания выполнены!!!!')
    koli4estvo_zadaniy = 1
    energy_availability = 1
    zakr = pyautogui.locateCenterOnScreen('img/close.png', confidence=0.9)
    while zakr is not None:
        move_to_click(zakr, 0.3)
        zakr = pyautogui.locateCenterOnScreen('img/close.png', confidence=0.9)
