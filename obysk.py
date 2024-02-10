import pyautogui
from time import sleep
from fun import move_left_friends_list


# определить регион поиска
def detect_region_search():
    pos_klan = pyautogui.locateCenterOnScreen('img/klan_red.png', confidence=0.9)
    pos_settings = pyautogui.locateCenterOnScreen('img/setting.png', confidence=0.9)
    if pos_klan:
        x_region, y_region = pos_klan
        x_region -= 125
        y_region += 503
        region_search = (x_region, y_region, 59, 132)
    else:
        x_region, y_region = pos_settings
        x_region -= 776
        y_region -= 10
        region_search = (x_region, y_region, 59, 132)

    return region_search


def vip_click(region_search):
    sleep(1)
    pos_vip = pyautogui.locateCenterOnScreen('img/b_vip.png', region=region_search, confidence=0.8)
    pyautogui.moveTo(pos_vip, duration=1, tween=pyautogui.easeInOutQuad)
    pyautogui.click(pos_vip)
    # print('клик по VIP ' + str(pos_vip))
    sleep(1)


def tent_detected(region_search):
    sleep(1)
    dom = pyautogui.locateCenterOnScreen('img/b_tent.png', region=region_search, confidence=0.9)
    pyautogui.moveTo(dom, duration=1, tween=pyautogui.easeInOutQuad)
    pyautogui.click(dom)
    # print('клик по дом ' + str(dom))
    sleep(1)


def visit_to_tent():
    """Возвращает 1 если есть и 0 если пусто """
    visit = pyautogui.locateCenterOnScreen('img/visit_to_tent.png', confidence=0.8)
    if visit:
        pyautogui.moveTo(visit, duration=1, tween=pyautogui.easeInOutQuad)
        pyautogui.click(visit)
        # print("клик обыск" + str(visit))
        vip = 1
    else:
        # print(' уже обыскан ')
        vip = 0
    return vip


def end_raid():
    pyautogui.moveTo(200, 670)
    sleep(1)
    exit_ = pyautogui.locateCenterOnScreen('img/b_exit.png', confidence=0.9)
    pyautogui.moveTo(exit_, duration=1, tween=pyautogui.easeInOutQuad)
    pyautogui.click(exit_)
    print('обход палаток окончен')
    pyautogui.moveTo(200, 670, duration=2, tween=pyautogui.easeInOutQuad)


def tent_raid():
    region = detect_region_search()
    pos_vip = pyautogui.locateCenterOnScreen('img/b_vip.png', region=region, confidence=0.8)
    while not pos_vip:
        move_left_friends_list()
        region = detect_region_search()
        pos_vip = pyautogui.locateCenterOnScreen('img/b_vip.png', region=region, confidence=0.8)
    vip_click(region)
    tent = pyautogui.locateCenterOnScreen('img/b_tent.png', confidence=0.9)
    while not tent:
        sleep(0.2)
        vip_click(region)
        tent = pyautogui.locateCenterOnScreen('img/b_tent.png', confidence=0.9)
    print(' дом найден')
    tent_detected(region)
    vip_result = visit_to_tent()
    return vip_result
