import pyautogui
from time import sleep

# определить регион поиска
def detect_region_poiska():
    pos_klan = pyautogui.locateCenterOnScreen('img/klan_red.png', confidence=0.9)
    pos_settings = pyautogui.locateCenterOnScreen('img/shesternya.png', confidence=0.9)
    if pos_klan is not None:
        x_region, y_region = pos_klan
        x_region -= 125
        y_region += 503
        region_poiska = (x_region, y_region, 59, 132)
    else:
        x_region, y_region = pos_settings
        x_region -= 776
        y_region -= 10
        region_poiska = (x_region, y_region, 59, 132)

    return region_poiska


def vna4flo():
    begin = pyautogui.locateCenterOnScreen('img/b_begin.png', confidence=0.96)
    if begin is not None:  # если увидел
        pyautogui.moveTo(begin, duration=1, tween=pyautogui.easeInOutQuad)
        print(' перемотка в начало ')
        sleep(1)
        pyautogui.click(begin)
        print('клик в начало ' + str(begin))
    pyautogui.moveTo(50, 600, duration=1, tween=pyautogui.easeInOutQuad)
    sleep(1)


def vip_detected(region_poiska):
    sleep(1)
    pos_vip = pyautogui.locateCenterOnScreen('img/b_vip.png', region=region_poiska, confidence=0.8)
    pyautogui.moveTo(pos_vip, duration=1, tween=pyautogui.easeInOutQuad)
    pyautogui.click(pos_vip)
    print('клик по VIP ' + str(pos_vip))
    sleep(1)


def dom_detected(region_poiska):
    sleep(1)
    dom = pyautogui.locateCenterOnScreen('img/b_dom.png', region=region_poiska, confidence=0.9)
    pyautogui.moveTo(dom, duration=1, tween=pyautogui.easeInOutQuad)
    pyautogui.click(dom)
    print('клик по дом ' + str(dom))
    sleep(1)


def obysk():
    obysk = pyautogui.locateCenterOnScreen('img/b_obysk.png', confidence=0.8)
    if obysk is not None:
        pyautogui.moveTo(obysk, duration=1, tween=pyautogui.easeInOutQuad)
        pyautogui.click(obysk)
        print("клик обыск" + str(obysk))
        vip = 1
    else:
        print(' уже обыскан ')
        vip = 1
    return vip


def new_analysis():
    sleep(1)
    ar_right = pyautogui.locateCenterOnScreen('img/b_arrow_right.png', confidence=0.8)
    pyautogui.moveTo(ar_right, duration=1, tween=pyautogui.easeInOutQuad)
    pyautogui.click(ar_right)
    sleep(1)

def end_obysk():
    pyautogui.moveTo(200, 670)
    sleep(1)
    vyxod = pyautogui.locateCenterOnScreen('img/b_vyxod.png', confidence=0.9)
    pyautogui.moveTo(vyxod, duration=1, tween=pyautogui.easeInOutQuad)
    pyautogui.click(vyxod)
    print('клик на выход')
    pyautogui.moveTo(200, 670, duration=2, tween=pyautogui.easeInOutQuad)

def foto(put_imya, _region):
    im1 = pyautogui.screenshot(region=_region)
    im1.save(put_imya)


def tent_raid():

    region = detect_region_poiska()
    pos_vip = pyautogui.locateCenterOnScreen('img/b_vip.png', region=region, confidence=0.8)
    while pos_vip is None:
        new_analysis()
        region = detect_region_poiska()
        pos_vip = pyautogui.locateCenterOnScreen('img/b_vip.png', region=region, confidence=0.8)

    vip_detected()
    dom = pyautogui.locateCenterOnScreen('img/b_dom.png', confidence=0.9)
    while dom is None:
        vip_detected(region)
        dom = pyautogui.locateCenterOnScreen('img/b_dom.png', confidence=0.9)
    print(' дом найден')
    dom_detected(region)
    vip_result = obysk()

    return vip_result
#
# snimok_region = 'img/test/region_poiska_vip.png'
# foto(snimok_region, region)
