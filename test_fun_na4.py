import pyautogui
from time import sleep
from fun import zakryt

conf = 0.99
son = 0.9
zadergka = 2
par_conf = 0.8
xp_imag = ['img/23xp.png', 'img/45xp.png', 'img/68xp.png', 'img/90xp.png', 'img/113xp.png']
nali4ie_energii = 1
koli4estvo_zadaniy = 1
shirina, vysota = 70, 70
variable = ' pust '
region1, region2, region3 = 0, 0, 0

def proverka_None(peremennaya):
    # print('proverka_None')
    az, za = peremennaya
def moveTo_click(xxxxx):
    # print('moveTo_click', xxxxx)
    sleep(0.3)
    pyautogui.moveTo(xxxxx)  # , duration=1, tween=pyautogui.easeInOutQuad)
    sleep(0.225)
    pyautogui.click(xxxxx)
    sleep(0.18)

def v_puti(zadanie):
    # print('v_puti', zadanie)
    boy_end = pyautogui.locateCenterOnScreen('img/b_boy_end.png', confidence=par_conf)
    propusk_boy = pyautogui.locateCenterOnScreen('img/propustit_boy.png', confidence=par_conf)
    sobaka = pyautogui.locateCenterOnScreen('img/sobaka.png', confidence=par_conf)
    while boy_end is None:
        # print(boy_end, 'boy_end')
        # print(zakryt, 'zakryt')
        # print('пропуск боя', propusk_boy)

        if propusk_boy is not None:  # нажать " пропустить бой"
            if sobaka is not None:  # нажать " пропустить бой"
                # print(sobaka, 'sobaka')
                moveTo_click(sobaka)
            # print(propusk_boy, 'propusk_boy')
            moveTo_click(propusk_boy)
        sleep(son * zadergka)
        boy_end = pyautogui.locateCenterOnScreen('img/b_boy_end.png', confidence=par_conf)
        zakryt = pyautogui.locateCenterOnScreen('img/zakryt.png', confidence=par_conf)
        sobaka = pyautogui.locateCenterOnScreen('img/sobaka.png', confidence=par_conf)
        propusk_boy = pyautogui.locateCenterOnScreen('img/propustit_boy.png', confidence=par_conf)
        # if zakryt is not None:
        #     sleep(1)
        if boy_end is not None and zakryt is not None:  # нажать закрыть в конце боя
            # print(boy_end, 'boy 1')
            # print(zakryt, 'zakryt 1')
            # print('конец v_puti ')
            moveTo_click(zakryt)

def na4Stanc():
    # print('na4Stanc')
    proverka = pyautogui.locateCenterOnScreen('img/na4_stanc.png', confidence=0.9)
    if proverka is not None:
        na4 = pyautogui.locateCenterOnScreen('img/na4_stanc.png', confidence=par_conf)
        proverka_None(na4)
        pyautogui.moveTo(na4, duration=1, tween=pyautogui.easeInOutQuad)
        # print(" уже у начальника ")
        sleep(son)
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
        moveTo_click(pos_or1)
        # print('зашел к начальнику')
        sleep(son)
        na4 = pyautogui.locateCenterOnScreen('img/na4_stanc.png', confidence=par_conf)
        proverka_None(na4)
        pyautogui.moveTo(na4, duration=1, tween=pyautogui.easeInOutQuad)


def orientir():

    son = 1
    # закрыть если открыто
    zakr = pyautogui.locateCenterOnScreen('img/zakryt.png', confidence=0.9)
    if zakr is not None:
        moveTo_click(zakr)
    # получение координат привязки
    pos_orV = pyautogui.locateCenterOnScreen('img/klan_red.png', confidence=0.9)
    pyautogui.moveTo(pos_orV)
    sleep(0.5)
    # print(pos_orV, 'ориентир верх')
    xorV, yorV = pos_orV
    pos_orN = pyautogui.locateCenterOnScreen('img/shesternya.png', confidence=0.9)
    # print(pos_orN, 'ориентир низ')
    xorN, yorN = pos_orN

    na4Stanc()

    # регион поиска 1 (позиция анализа)
    x_pOan1 = (xorN - xorV) / 2 + xorV + 210
    y_pOan1 = (yorN - yorV) / 2 + yorV - 60
    x_pOan1, y_pOan1 = int(x_pOan1), int(y_pOan1)
    region1 = [x_pOan1, y_pOan1, shirina, vysota]

    # регион поиска 2 (позиция анализа)
    x_pOan2 = (xorN - xorV) / 2 + xorV + 210
    y_pOan2 = (yorN - yorV) / 2 + yorV + 43
    x_pOan2, y_pOan2 = int(x_pOan2), int(y_pOan2)
    region2 = [x_pOan2, y_pOan2, shirina, vysota]

    # регион поиска 3 (позиция анализа)
    x_pOan3 = (xorN - xorV) / 2 + xorV + 210
    y_pOan3 = (yorN - yorV) / 2 + yorV + 146
    x_pOan3, y_pOan3 = int(x_pOan3), int(y_pOan3)
    region3 = [x_pOan3, y_pOan3, shirina, vysota]


    return region1, region2, region3


# def analiz_zadaniy(img1, img2, region):
#     #print(img1, img2, region)
#     # print('analiz_zadaniy')
#     global variable
#     # print('вызов na4Stanc в анализе')
#     na4Stanc()
#
#     print('в analiz_zadaniy conf =', conf)
#     variant1 = pyautogui.locateCenterOnScreen(img1, confidence=conf, region=region)
#     variant2 = pyautogui.locateCenterOnScreen(img2, confidence=conf, region=region)
#     if variant1 is not None:
#         variable = variant1
#     else:
#         variable = variant2
#         return (variable)

def analiz_zadaniy(img, region):
    # print( region)
    # print('analiz_zadaniy')
    global variable
    # print('вызов na4Stanc в анализе')
    na4Stanc()
    print('в analiz_zadaniy conf =', conf)
    variant1 = pyautogui.locateCenterOnScreen(img[0], confidence=conf, region=region)
    # print(variant1, 'variant1')
    variant2 = pyautogui.locateCenterOnScreen(img[1], confidence=conf, region=region)
    # print(variant2, 'variant2')
    variant3 = pyautogui.locateCenterOnScreen(img[2], confidence=conf, region=region)
    # print(variant3, 'variant3')
    variant4 = pyautogui.locateCenterOnScreen(img[3], confidence=conf, region=region)
    # print(variant4, 'variant4')
    variant5 = pyautogui.locateCenterOnScreen(img[4], confidence=conf, region=region)
    # print(variant5, 'variant5')
    # variant6 = pyautogui.locateCenterOnScreen(img[5], confidence=conf, region=region)
    if variant1 is not None:
        variable = variant1
    elif variant2 is not None:
        variable = variant2
    elif variant3 is not None:
        variable = variant3
    elif variant4 is not None:
        variable = variant4
    elif variant5 is not None:
        variable = variant5
    else:
        variable = variant1
    return (variable)


def press_en(nom, pos):
    # print('press_en')
    global nali4ie_energii, zadanie
    zadanie = nom
    pos_clik = pos[0], pos[1]
    # print(img_en, 'img_en', energ, 'energ')

    moveTo_click(pos_clik)
    sleep(0.5)
    nal_energii = pyautogui.locateCenterOnScreen('img/malo_energii.png', confidence=0.8)
    # print(" не хватает энергии", nal_energii)
    if nal_energii is None:
        print('Выполняю ', nom, ' задание')
        v_puti(nom)
    else:
        nali4ie_energii = 0
        print(' Энергия закончилась!!')
        sleep(son)
        zakr = pyautogui.locateCenterOnScreen('img/zakryt.png')
        moveTo_click(zakr)

def move(pos):
    if pos is not None:
        pyautogui.moveTo(pos, duration=1)
        sleep(3)


def test__vybor_zadaniya_na_puli():
    region1, region2, region3 = orientir()
    global nali4ie_energii, koli4estvo_zadaniy, conf
    while nali4ie_energii == 1 and koli4estvo_zadaniy > 0:

        # print('вызов analiz_zadaniy из vybor_zadaniya_na_puli')
        analiz_zadaniy(xp_imag, region1)
        # analiz_zadaniy(xp_imag[0], xp_imag[1], region1)
        pul1 = variable
        move(pul1)
        print('pul1 = ', pul1)
        sleep(0.5)

        # print('вызов analiz_zadaniy из vybor_zadaniya_na_puli')
        analiz_zadaniy(xp_imag, region2)
        # analiz_zadaniy(xp_imag[1], xp_imag[2], region2)
        pul2 = variable
        move(pul2)
        print('pul2 = ', pul2)
        sleep(0.5)

        # print('вызов analiz_zadaniy из vybor_zadaniya_na_puli')
        analiz_zadaniy(xp_imag, region3)
        #analiz_zadaniy(xp_imag[2], xp_imag[3], region3)
        pul3 = variable
        move(pul3)
        print('pul3 = ', pul3)
        sleep(0.5)

        if pul1 is not None:
            press_en(1, region1)
        if pul2 is not None:
            press_en(2, region2)
        if pul3 is not None:
            press_en(3,region3)

        if pul1 == pul2 == pul3:
            print('confidence=', conf)
            conf -=0.01


    print(' Задания выполнены!!!!')
    koli4estvo_zadaniy = 1
    nali4ie_energii = 1
    zakr = pyautogui.locateCenterOnScreen('img/zakryt.png', confidence=0.9)
    while zakr is not None:
        moveTo_click(zakr)
        zakr = pyautogui.locateCenterOnScreen('img/zakryt.png', confidence=0.9)

# test__vybor_zadaniya_na_puli()
