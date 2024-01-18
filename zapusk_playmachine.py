import pyautogui
from time import sleep

son = 1
img_sl = {'спецпредложение':'img/spec_predlog.png', 'закрыть в спецпредложении':'img/s_p_zakr.png',
          'продолжить как Гаврил':'img/b_autoriz.png',
          'мои игры V1':'img/my_game1.png','мои игры V2':'img/my_game2.png',
          'иконка на рабочем столе':'img/icon_in_desktop.png'}

# если закрыта программа
def start_prog():
    pos_my_game = pyautogui.locateCenterOnScreen(img_sl.get('мои игры V1'), confidence=0.8)
    pos_my_game1 = pyautogui.locateCenterOnScreen(img_sl.get('мои игры V2'), confidence=0.8)
    if pos_my_game == pos_my_game1:
        pos_icon_my_game = pyautogui.locateCenterOnScreen(img_sl.get('иконка на рабочем столе'), confidence=0.8)

# клик по кнопке "мои игры"
def _my_game():
    pos_my_game = pyautogui.locateCenterOnScreen(img_sl.get('мои игры V1'), confidence=0.8)
    pos_my_game1 = pyautogui.locateCenterOnScreen(img_sl.get('мои игры V2'), confidence=0.8)
    while pos_my_game is None and pos_my_game1 is None:
        sleep(0.5)
        pos_my_game = pyautogui.locateCenterOnScreen(img_sl.get('мои игры V1'), confidence=0.8)
        print(pos_my_game)
        pos_my_game1 = pyautogui.locateCenterOnScreen(img_sl.get('мои игры V2'), confidence=0.8)
        print(pos_my_game1)

    if pos_my_game is not None:
        pyautogui.moveTo(pos_my_game, duration=1, tween=pyautogui.easeInOutQuad)
        pyautogui.click(pos_my_game)
        print('pos_my_game' + str(pos_my_game))
    elif pos_my_game1 is not None:
        pyautogui.moveTo(pos_my_game1, duration=1, tween=pyautogui.easeInOutQuad)
        pyautogui.click(pos_my_game1)
        print('pos_my_game1' + str(pos_my_game1))
    else:
        print('Не найдено кнопки "My game"')
        im1 = pyautogui.screenshot('img/screen1.png')
        im1.save('img/screen1.png')
        sleep(son * 2)

def spec_predlog():
    sz = 0
    spec = pyautogui.locateCenterOnScreen(img_sl.get('спецпредложение'), confidence=0.96)
    if spec is not None:
        s_p_zakr = pyautogui.locateCenterOnScreen(img_sl.get('закрыть в спецпредложении'), confidence=0.96)
        while s_p_zakr is not None and sz <= 5:
            sleep(son * 2)
            s_p_zakr = pyautogui.locateCenterOnScreen(img_sl.get('закрыть в спецпредложении'), confidence=0.96)
            sz += 1
        pyautogui.click(s_p_zakr)


def authorization():  # авторизация при необходимости
    sleep(son * 2)
    pos_autoriz = pyautogui.locateCenterOnScreen(img_sl.get('продолжить как Гаврил'), confidence=0.8)
    if pos_autoriz is not None:
        pyautogui.moveTo(pos_autoriz, duration=1, tween=pyautogui.easeInOutQuad)
        pyautogui.click(pos_autoriz)
        sleep(son * 2)


def geograf():
    # растягивание вверх
    pyautogui.moveTo(670, 86, duration=1, tween=pyautogui.easeInOutQuad)
    pyautogui.dragTo(670, 1, duration=1)
    sleep(1)
    # растягивание вниз
    pyautogui.moveTo(670, 763, duration=1, tween=pyautogui.easeInOutQuad)
    pyautogui.dragTo(670, 848, duration=1)
    # уменьшение масштаба
    pyautogui.hotkey('Ctrl', '-')
    pyautogui.hotkey('Ctrl', '-')

    # смещение окна в лево на 384
    pyautogui.moveTo(684, 11, duration=1, tween=pyautogui.easeInOutQuad)
    pyautogui.dragTo(300, 11, duration=1)

    # смещение позунка на 45
    polzun = pyautogui.locateCenterOnScreen('img/polzun_1.png', confidence=0.7)
    print(polzun, 'polsun')
    if polzun is not None:
        x, y = polzun
        pyautogui.moveTo(x, y, duration=1, tween=pyautogui.easeInOutQuad)
        pyautogui.dragTo(x, y + 45, duration=1)


# клик на запуск игры
def klik_icon_game():
    p_i = 0
    # sleep(son * 2)
    pos_icon_game = pyautogui.locateCenterOnScreen('img/icon_game.png', confidence=0.8)
    while pos_icon_game is None and p_i <= 100:
        p_i += 1
        print('p_i = ' + str(p_i))
        sleep(son)
        pos_icon_game = pyautogui.locateCenterOnScreen('img/icon_game.png', confidence=0.8)
    pyautogui.click(pos_icon_game)
    sleep(son)

def zapusk():
    authorization()
    _my_game()
    klik_icon_game()
    geograf()
    spec_predlog()