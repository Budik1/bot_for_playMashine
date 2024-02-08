import pyautogui
from time import sleep

img_sl = {'спецпредложение': 'img/spec_proposal.png', 'закрыть в спецпредложении': 'img/s_p_close.png',
          'продолжить как Гаврил': 'img/authorization_button.png', 'свернуть всё': 'collapse()',
          'мои игры V1': 'img/my_game1.png', 'мои игры V2': 'img/my_game2.png',
          'иконка на рабочем столе': 'img/icon_in_desktop.png'}

pos_my_game = pyautogui.locateCenterOnScreen(img_sl.get('мои игры V1'), confidence=0.8)
pos_my_game1 = pyautogui.locateCenterOnScreen(img_sl.get('мои игры V2'), confidence=0.8)
print(pos_my_game1, pos_my_game1)

if pos_my_game == pos_my_game1:
    def collapse():
        # свернуть всё
        collapse_all = pyautogui.size()
        print(collapse_all)
        x, y = collapse_all
        x -= 2
        y -= 20
        collapse_all = x, y
        print(collapse_all)
        pyautogui.moveTo(collapse_all, duration=2)
        pyautogui.click(collapse_all)


    collapse()
    pos_icon_my_game = pyautogui.locateCenterOnScreen(img_sl.get('иконка на рабочем столе'), confidence=0.9)
    while pos_icon_my_game is None:
        sleep(0.1)
        pos_icon_my_game = pyautogui.locateCenterOnScreen(img_sl.get('иконка на рабочем столе'), confidence=0.9)
    pos_icon_my_game = pyautogui.locateCenterOnScreen(img_sl.get('иконка на рабочем столе'), confidence=0.9)
    print(f'иконка {pos_icon_my_game}')
    pyautogui.moveTo(pos_icon_my_game, duration=1)
    pyautogui.click(pos_icon_my_game)

    pos_my_game = pyautogui.locateCenterOnScreen(img_sl.get('мои игры V1'), confidence=0.8)
    pos_my_game1 = pyautogui.locateCenterOnScreen(img_sl.get('мои игры V2'), confidence=0.8)

    while pos_my_game is None and pos_my_game1 is None:
        sleep(0.03)
        print('!')
        pos_my_game = pyautogui.locateCenterOnScreen(img_sl.get('мои игры V1'), confidence=0.8)
        pos_my_game1 = pyautogui.locateCenterOnScreen(img_sl.get('мои игры V2'), confidence=0.8)

    if pos_my_game is not None:
        pyautogui.moveTo(pos_my_game)
        print(1)
    else:
        print(2)
        pyautogui.moveTo(pos_my_game1)
    print(pos_my_game, pos_my_game1)
