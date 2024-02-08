import pyautogui
from fun_na4 import enemy_battle
from time import sleep
from fun import move_to_click, move_right_friends_list, find_link


def search_friend():
    """
    Анализ друга. Возвращает позицию активной кнопки 'Атаковать'
    :return: Point | None
    """
    pos_or = find_link()  # ориентир на зал славы
    x, y = pos_or
    x -= 160
    y += 650
    pos_frend = x, y
    pyautogui.moveTo(pos_frend, duration=1)
    # Point(x=613, y=627), Point(x=748, y=660)
    move_to_click(pos_frend, 0.2)
    friend_battle = pyautogui.locateCenterOnScreen("img/hero_vs_frend.png", region=(600, 600, 160, 83), confidence=0.95)
    # print(friend_battle)
    return friend_battle


def friend_kill(required_quantity=5):  # требуемое количество=5
    quantity_battle = 0
    while quantity_battle <= required_quantity:
        friend_battle_ = search_friend()
        if friend_battle_:
            print('Атакую')
            quantity_battle += 1
            move_to_click(friend_battle_, 0.5)
            hero_vs_opponent = pyautogui.locateCenterOnScreen('img/hero_vs_opponent.png', confidence=0.9)
            while hero_vs_opponent is None:
                sleep(0.1)
                hero_vs_opponent = pyautogui.locateCenterOnScreen('img/hero_vs_opponent.png', confidence=0.9)
            move_to_click(hero_vs_opponent, 0.3)
            sleep(1)
            enemy_battle(0.1)
            # enemy_battle()
            print(quantity_battle, 'quantity_battle')

        else:
            print('Следующий')
            move_right_friends_list()


friend_kill()
