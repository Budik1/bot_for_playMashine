import pyautogui
from time import sleep
from fun import moveTo_click




son = 0.9
par_conf = 0.8


def foto(put_imya, _region):
    im1 = pyautogui.screenshot(region=_region)
    im1.save(put_imya)


def poisk(chto_ishchem):
    param_confidence = 0.99
    sleep(son)
    pos_poiska = pyautogui.locateCenterOnScreen(chto_ishchem, confidence=param_confidence)
    while pos_poiska is None:
        param_confidence -= 0.01
        # print('в поиске станции confidence=', param_confidence)
        pos_poiska = pyautogui.locateCenterOnScreen(chto_ishchem, confidence=param_confidence)
        # print(pos_lok)
    return pos_poiska, param_confidence


def skriny_energii_u_na4stanc():
    xp_imag = ['img/23xp.png', 'img/45xp.png', 'img/68xp.png', 'img/90xp.png', 'img/113xp.png']
    shirina, vysota = 87, 39
    region1, region2, region3 = 0, 0, 0
    # смещение скрина внутри региона
    popravka_x_s = 4
    popravka_y_s = 9
    popravka_s_s = 14
    popravka_v_s = 17


    def na4Stanc():
        # print('na4Stanc')
        proverka = pyautogui.locateCenterOnScreen('img/na4_stanc.png', confidence=0.9)
        print(proverka)
        if proverka is not None:
            na4 = pyautogui.locateCenterOnScreen('img/na4_stanc.png', confidence=par_conf)
            print(na4)
            # proverka_None(na4)
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
            moveTo_click(pos_or1, 0.3)
            # print('зашел к начальнику')
            sleep(son)
            na4 = pyautogui.locateCenterOnScreen('img/na4_stanc.png', confidence=par_conf)
            # proverka_None(na4)
            pyautogui.moveTo(na4, duration=1, tween=pyautogui.easeInOutQuad)

    def orientir():
        # закрыть если открыто
        zakr = pyautogui.locateCenterOnScreen('img/zakryt.png', confidence=0.9)
        if zakr is not None:
            moveTo_click(zakr, 0.3)
        # получение координат привязки
        pos_orV = pyautogui.locateCenterOnScreen('img/klan_red.png', confidence=0.9)
        pyautogui.moveTo(pos_orV)
        sleep(0.5)
        print(pos_orV, 'ориентир верх')
        xorV, yorV = pos_orV
        pos_orN = pyautogui.locateCenterOnScreen('img/shesternya.png', confidence=0.9)
        print(pos_orN, 'ориентир низ')
        xorN, yorN = pos_orN

        na4Stanc()

        # регион поиска 1 (позиция анализа)
        x_pOan1 = (xorN - xorV) / 2 + xorV + 193  # 210
        y_pOan1 = (yorN - yorV) / 2 + yorV - 39  # 60
        x_pOan1, y_pOan1 = int(x_pOan1), int(y_pOan1)
        region1 = [x_pOan1, y_pOan1, shirina, vysota]

        # регион поиска 2 (позиция анализа)
        x_pOan2 = (xorN - xorV) / 2 + xorV + 193  # 210
        y_pOan2 = (yorN - yorV) / 2 + yorV + 64  # 43
        x_pOan2, y_pOan2 = int(x_pOan2), int(y_pOan2)
        region2 = [x_pOan2, y_pOan2, shirina, vysota]

        # регион поиска 3 (позиция анализа)
        x_pOan3 = (xorN - xorV) / 2 + xorV + 193  # 210
        y_pOan3 = (yorN - yorV) / 2 + yorV + 167  # 146
        x_pOan3, y_pOan3 = int(x_pOan3), int(y_pOan3)
        region3 = [x_pOan3, y_pOan3, shirina, vysota]

        return region1, region2, region3

    def snimok():
        region1, region2, region3 = orientir()

        snimok1 = 'img/test/primer_1.png'
        foto(snimok1, region1)

        snimok2 = 'img/test/primer_2.png'
        foto(snimok2, region2)

        snimok3 = 'img/test/primer_3.png'
        foto(snimok3, region3)

    def pokaz_pos():
        region1, region2, region3 = orientir()
        # 1
        x_pOan1, y_pOan1, shirina, vysota = region1
        x_s = x_pOan1 + popravka_x_s
        y_s = y_pOan1 + popravka_y_s
        shirina_s = shirina - popravka_s_s
        vysota_s = vysota - popravka_v_s
        snimok_1 = 'img/test/1.png'
        foto(snimok_1, (x_s, y_s, shirina_s, vysota_s))

        pos = (x_pOan1, y_pOan1)
        pyautogui.moveTo(pos, duration=1)

        # 2
        x_pOan2, y_pOan2, shirina, vysota = region2
        x_s = x_pOan2 + popravka_x_s
        y_s = y_pOan2 + popravka_y_s
        shirina_s = shirina - popravka_s_s
        vysota_s = vysota - popravka_v_s
        snimok2 = 'img/test/2.png'
        foto(snimok2, (x_s, y_s, shirina_s, vysota_s))

        pos = (x_pOan2, y_pOan2)
        pyautogui.moveTo(pos, duration=1)

        # 3
        x_pOan3, y_pOan3, shirina, vysota = region3
        x_s = x_pOan3 + popravka_x_s
        y_s = y_pOan3 + popravka_y_s
        shirina_s = shirina - popravka_s_s
        vysota_s = vysota - popravka_v_s
        snimok3 = 'img/test/3.png'
        foto(snimok3, (x_s, y_s, shirina_s, vysota_s))

        pos = (x_pOan3, y_pOan3)
        pyautogui.moveTo(pos, duration=1)

    snimok()
    sleep(2)
    pokaz_pos()



skriny_energii_u_na4stanc()

# 23 45 68 90 113 135 203