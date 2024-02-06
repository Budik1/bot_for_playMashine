import pyautogui
from fun_na4 import enemy_attack
from time import sleep
from fun import move_to_click, press_left_button, find_link


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
    friend_atack = pyautogui.locateCenterOnScreen("img/hero_vs_frend.png", region=(600, 600, 160, 83), confidence=0.95)
    # print(friend_atack)
    return friend_atack


def friend_kill(required_quantity=5):
    quantity_atack = 0
    while quantity_atack <= required_quantity:
        friend_atack = search_friend()
        if friend_atack:
            print('Атакую')
            quantity_atack += 1
            move_to_click(friend_atack, 0.5)
            hero_vs_opponent = pyautogui.locateCenterOnScreen('img/hero_vs_opponent.png', confidence=0.9)
            while hero_vs_opponent is None:
                sleep(0.1)
                hero_vs_opponent = pyautogui.locateCenterOnScreen('img/hero_vs_opponent.png', confidence=0.9)
            move_to_click(hero_vs_opponent, 0.3)
            sleep(1)
            enemy_attack(0.1)
            # enemy_attack()
            print(quantity_atack, 'quantity_atack')

        else:
            print('Следующий')
            press_left_button()


friend_kill()
