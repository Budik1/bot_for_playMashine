import baza_dannyx as b_d
import pyautogui
from time import sleep
from fun import move_to_click

conf = 0.97
son = 0.9
zadergka = 2
par_conf = 0.8
# xp_imag = ['img/23xp.png', 'img/45xp.png', 'img/68xp.png', 'img/90xp.png', 'img/113xp.png']
energy_availability = 1
koli4estvo_zadaniy = 1
shirina, vysota = 87, 39
variable = ' pust '
region1, region2, region3 = 0, 0, 0


def na4stanc():
    # заходит в палатку к начстанции
    # print('na4_stanc')
    proverka = pyautogui.locateCenterOnScreen('img/station_master.png', confidence=0.9)
    if proverka is not None:
        na4 = pyautogui.locateCenterOnScreen('img/station_master.png', confidence=par_conf)
        # proverka_None(na4)
        pyautogui.moveTo(na4, duration=1, tween=pyautogui.easeInOutQuad)
        # print(" уже у начальника ")
        sleep(son / 3)
    else:
        pos_or1 = pyautogui.locateCenterOnScreen('img/klan_red.png', confidence=0.85)
        while pos_or1 is None:
            sleep(0.1)
            pos_or1 = pyautogui.locateCenterOnScreen('img/klan_red.png', confidence=0.85)
            # print('в поиске клана', pos_or1)
        # print('клан = ', pos_or1)
        x1, y1 = pos_or1
        x1, y1 = x1 - 60, y1 + 200
        pos_or1 = x1, y1
        move_to_click(pos_or1, 0.2)
        # print('зашел к начальнику')
        sleep(son)
        na4 = pyautogui.locateCenterOnScreen('img/station_master.png', confidence=par_conf)
        # proverka_None(na4)
        pyautogui.moveTo(na4, duration=1, tween=pyautogui.easeInOutQuad)


def orientir():
    # получение значиний "region=" поиска заданий
    # закрыть если открыто
    zakr = pyautogui.locateCenterOnScreen('img/close.png', confidence=0.9)
    if zakr is not None:
        move_to_click(zakr,0.2)
    # получение координат привязки
    pos_orV = pyautogui.locateCenterOnScreen('img/klan_red.png', confidence=0.9)
    pyautogui.moveTo(pos_orV)
    sleep(0.5)
    # print(pos_orV, 'ориентир верх')
    xorV, yorV = pos_orV
    pos_orN = pyautogui.locateCenterOnScreen('img/shesternya.png', confidence=0.9)
    # print(pos_orN, 'ориентир низ')
    xorN, yorN = pos_orN

    na4stanc()

    # регион поиска 1 (позиция анализа)
    x_pOan1 = (xorN - xorV) / 2 + xorV + 193
    y_pOan1 = (yorN - yorV) / 2 + yorV - 39
    x_pOan1, y_pOan1 = int(x_pOan1), int(y_pOan1)
    region1 = [x_pOan1, y_pOan1, shirina, vysota]

    # регион поиска 2 (позиция анализа)
    x_pOan2 = (xorN - xorV) / 2 + xorV + 193
    y_pOan2 = (yorN - yorV) / 2 + yorV + 64
    x_pOan2, y_pOan2 = int(x_pOan2), int(y_pOan2)
    region2 = [x_pOan2, y_pOan2, shirina, vysota]

    # регион поиска 3 (позиция анализа)
    x_pOan3 = (xorN - xorV) / 2 + xorV + 193
    y_pOan3 = (yorN - yorV) / 2 + yorV + 167
    x_pOan3, y_pOan3 = int(x_pOan3), int(y_pOan3)
    region3 = [x_pOan3, y_pOan3, shirina, vysota]

    return region1, region2, region3



def boy_v_puti(nom_zadanie):
    # дождаться "пропустить бой", нажать собаку если активна, закрыть бой
    # print('v_puti', nom_zadanie)
    boy_end = pyautogui.locateCenterOnScreen('img/b_boy_end.png', confidence=par_conf)
    propusk_boy = pyautogui.locateCenterOnScreen('img/skip_fight.png', confidence=par_conf)
    sobaka = pyautogui.locateCenterOnScreen('img/dog.png', confidence=par_conf)
    while boy_end is None:
        # print(boy_end, 'boy_end')
        # print('пропуск боя', propusk_boy)
        if propusk_boy is not None:  # нажать " пропустить бой"
            if sobaka is not None:  # нажать "на собаку"
                # print(sobaka, 'sobaka')
                move_to_click(sobaka, 0.2)
            # print(propusk_boy, 'propusk_boy')
            move_to_click(propusk_boy, 0.2)
        sleep(son * zadergka)
        boy_end = pyautogui.locateCenterOnScreen('img/b_boy_end.png', confidence=par_conf)
        zakryt = pyautogui.locateCenterOnScreen('img/close.png', confidence=par_conf)
        sobaka = pyautogui.locateCenterOnScreen('img/dog.png', confidence=par_conf)
        propusk_boy = pyautogui.locateCenterOnScreen('img/skip_fight.png', confidence=par_conf)
        if boy_end is not None and zakryt is not None:  # нажать закрыть в конце боя
            # print(boy_end, 'boy 1')
            # print(push_close, 'push_close 1')
            # print('конец v_puti ')
            move_to_click(zakryt, 0.2)
            sleep(0.5)


def press_en(nomer_zadaniya, pos):
    global energy_availability
    if nomer_zadaniya == 1:
        x = pos[0]
        y = pos[1]- 20
        pos_clik = x, y
        # pyautogui.moveTo(pos_clik) # для отладки
        # print('тут должен быть клик') # для отладки
    elif nomer_zadaniya ==2:
        x = pos[0]
        y = pos[1] - 20
        pos_clik = x, y
    else:
        x = pos[0]
        y = pos[1] - 20
        pos_clik = x, y

    # zadanie = nom_zadaniya
    # y = pos[1] - 20
    # x = pos[0]
    # pos_clik = x, y
    # pyautogui.moveTo(pos_clik) # для отладки
    # print('тут должен быть клик') # для отладки

    move_to_click(pos_clik, 1.5)
    sleep(0.5)
    nal_energii = pyautogui.locateCenterOnScreen('img/low_energy.png', confidence=0.8)
    # print(" не хватает энергии", nal_energii)
    if nal_energii is None:
        print('Выполняю ', nomer_zadaniya, ' задание')
        boy_v_puti(nomer_zadaniya)
    else:
        nali4ie_energii = 0
        print(' Энергия закончилась!!')
        sleep(son)
        zakr = pyautogui.locateCenterOnScreen('img/close.png')
        move_to_click(zakr, 0.5)


def analiz_zadaniy(img1, img2, region):
    # print('task_analysis')
    # print( region) # полученный region
    global variable
    # print('вызов na4Stanc в анализе')
    na4stanc()
    # print('в task_analysis conf =', conf)
    variant1 = pyautogui.locateCenterOnScreen(img1, confidence=conf, region=region)
    # print(variant1, 'variant1')
    variant2 = pyautogui.locateCenterOnScreen(img2, confidence=conf, region=region)
    # print(variant2, 'variant2')
    if variant1 is not None:
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
    while nali4ie_energii == 1 and koli4estvo_zadaniy > 0:
        # print('вызов task_analysis из vybor_zadaniya_na_puli')
        analiz_zadaniy(xp_imag[0], xp_imag[1], region1)
        variant1 = variable
        # print('variant1 = ', variant1)
        move(variant1)
        sleep(0.1)

        # print('вызов task_analysis из vybor_zadaniya_na_puli')
        analiz_zadaniy(xp_imag[2], xp_imag[3], region2)
        variant2 = variable
        # print('variant2 = ', variant2)
        move(variant2)
        sleep(0.1)

        # print('вызов task_analysis из vybor_zadaniya_na_puli')
        analiz_zadaniy(xp_imag[4], xp_imag[5], region3)
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
    nali4ie_energii = 1
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
    while nali4ie_energii == 1 and koli4estvo_zadaniy > 0:
        press_en(nomer_zadaniya, region)
    print(' Задания выполнены!!!!')
    koli4estvo_zadaniy = 1
    nali4ie_energii = 1
    zakr = pyautogui.locateCenterOnScreen('img/close.png', confidence=0.9)
    while zakr is not None:
        move_to_click(zakr, 0.3)
        zakr = pyautogui.locateCenterOnScreen('img/close.png', confidence=0.9)

