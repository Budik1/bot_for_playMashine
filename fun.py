import pyautogui
from time import sleep, time
import datetime

# son = 1
# zadergka = 10
sum_vip = 0
status_bonus = "0"
par_conf = 0.79
energy_availability = 1
number_tasks = 3
oblast = (51, 707, 92, 111)
img_sl = {'спецпредложение': 'img/spec_proposal.png', 'закрыть спецпредложение': 'img/s_p_close.png',
          'продолжить как Гаврил': 'img/authorization_button.png',
          'мои игры V1': 'img/my_game1.png', 'мои игры V2': 'img/my_game2.png',
          'иконка на рабочем столе': 'img/icon_in_desktop.png'}
iter_detect_search_region = 0


def print_to_file(text: str) -> None:
    date_time, date = time_now()
    file_name = date_time + ".txt"
    file = open(file_name, 'a+', encoding='utf-8')
    print(date_time, text, file=file)
    file.close()  # закрыть файл после работы с ним.


def time_now():
    """Получение текущего времени и даты. Отдаёт формирование имени файла"""
    now = datetime.datetime.now()
    date_time_now = (now.strftime('%Y-%m-%d %H°%M\'\'%S\''))  # '%Y-%m-%d %H:%M:%S'
    date = (now.date())
    return date_time_now, date


def daily_gifts():
    """Обмен ежедневными подарками"""
    pass
    gifts = pyautogui.locateCenterOnScreen('img/b_gifts.png', confidence=0.91)
    pyautogui.moveTo(gifts, duration=1, tween=pyautogui.easeInOutQuad)
    pyautogui.click(gifts)

    open_ = pyautogui.locateCenterOnScreen('img/b_gift_open.png', confidence=0.9)
    while open_:
        pyautogui.moveTo(open_, duration=1, tween=pyautogui.easeInOutQuad)
        pyautogui.click(open_)
        sleep(1)
        thanks = pyautogui.locateCenterOnScreen('img/b_thanks.png', confidence=0.9)
        pyautogui.moveTo(thanks, duration=1, tween=pyautogui.easeInOutQuad)
        pyautogui.click(thanks)
        sleep(1)
        give = pyautogui.locateCenterOnScreen('img/b_give.png', confidence=0.85)
        print(give)
        pyautogui.moveTo(give, duration=1, tween=pyautogui.easeInOutQuad)
        pyautogui.click(give)

        open_ = pyautogui.locateCenterOnScreen('img/b_gift_open.png', confidence=0.9)


def push_close_all():
    pos_close = pyautogui.locateCenterOnScreen('img/close.png', confidence=0.9)
    # print(pos_close)
    while pos_close:
        # print(push_close_all)
        pyautogui.moveTo(pos_close, duration=1, tween=pyautogui.easeInOutQuad)
        pyautogui.click(pos_close)
        sleep(1)
        pos_close = pyautogui.locateCenterOnScreen('img/close.png', confidence=0.9)


def bonus():
    # кнопка добавить
    add_bonus = pyautogui.locateCenterOnScreen('img/add.png', confidence=0.8)
    pyautogui.moveTo(add_bonus, duration=1, tween=pyautogui.easeInOutQuad)
    sleep(1)
    pyautogui.click(add_bonus)
    sleep(2)
    # кнопка забрать
    take_bonus = pyautogui.locateCenterOnScreen('img/take.png', confidence=0.9)
    if take_bonus:  # != None:
        pyautogui.moveTo(take_bonus, duration=1, tween=pyautogui.easeInOutQuad)
        pyautogui.click()
        print('Бонус найден')
    else:
        print('Бонус не найден')
    # кнопка закрыть
    push_close_all()


def start_p_m():
    def spec_proposal():
        sz = 0
        proposal = pyautogui.locateCenterOnScreen('img/spec_proposal.png', confidence=0.96)
        if proposal is not None:
            s_p_close = pyautogui.locateCenterOnScreen('img/s_p_close.png', confidence=0.96)
            while s_p_close is not None and sz <= 5:
                sleep(2)
                s_p_close = pyautogui.locateCenterOnScreen('img/s_p_close.png', confidence=0.96)
                sz += 1
            pyautogui.click(s_p_close)

    def authorization():  # авторизация при необходимости
        sleep(2)
        pos_authorization = pyautogui.locateCenterOnScreen('img/authorization_button.png', confidence=0.8)
        if pos_authorization is not None:
            pyautogui.moveTo(pos_authorization, duration=1, tween=pyautogui.easeInOutQuad)
            pyautogui.click(pos_authorization)
            sleep(2)

    def click_my_game():
        pos_my_game = pyautogui.locateCenterOnScreen('img/my_game1.png', confidence=0.8)
        pos_my_game1 = pyautogui.locateCenterOnScreen('img/my_game2.png', confidence=0.8)
        while pos_my_game is None and pos_my_game1 is None:
            sleep(0.5)
            pos_my_game = pyautogui.locateCenterOnScreen('img/my_game1.png', confidence=0.8)
            pos_my_game1 = pyautogui.locateCenterOnScreen('img/my_game2.png', confidence=0.8)
            print(pos_my_game, pos_my_game1, ' в ожидании появления кнопки "my_game"')
        if pos_my_game is not None:
            pyautogui.moveTo(pos_my_game, duration=1, tween=pyautogui.easeInOutQuad)
            pyautogui.click(pos_my_game)
            print('pos_my_game ' + str(pos_my_game))
        elif pos_my_game1 is not None:
            pyautogui.moveTo(pos_my_game1, duration=1, tween=pyautogui.easeInOutQuad)
            pyautogui.click(pos_my_game1)
            print('pos_my_game1' + str(pos_my_game1))
        else:
            print('Не найдено кнопки "My game"')
            im1 = pyautogui.screenshot('img/screen1.png')
            im1.save('img/screen1.png')
            sleep(2)
        pos_autor = pyautogui.locateCenterOnScreen('img/authorization_button.png', confidence=0.8)
        if pos_autor is not None:
            authorization()

    def click_icon_game():
        p_i = 0
        # sleep(2)
        pos_icon_game = pyautogui.locateCenterOnScreen('img/icon_game.png', confidence=0.8)
        while pos_icon_game is None and p_i <= 100:
            p_i += 1
            sleep(1)
            pos_icon_game = pyautogui.locateCenterOnScreen('img/icon_game.png', confidence=0.8)
        pyautogui.click(pos_icon_game)
        sleep(1)

    def geography():
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
        # смещение окна в лево на 382
        pyautogui.moveTo(682, 11, duration=1, tween=pyautogui.easeInOutQuad)
        pyautogui.dragTo(300, 11, duration=1)
        # смещение ползунка на 45
        slider = pyautogui.locateCenterOnScreen('img/slider_v.png', confidence=0.7)
        print(slider, 'ползунок')
        if slider is not None:
            x, y = slider
            pyautogui.moveTo(x, y, duration=1, tween=pyautogui.easeInOutQuad)
            pyautogui.dragTo(x, y + 45, duration=1)

    authorization()
    click_my_game()
    click_icon_game()
    geography()
    spec_proposal()


def move_left_friends_list():
    """
    Смещает список друзей в лево на одну позицию
    :return: 1
    """
    sleep(1)
    ar_right = pyautogui.locateCenterOnScreen('img/b_arrow_right.png', confidence=0.8)
    pyautogui.moveTo(ar_right, duration=1, tween=pyautogui.easeInOutQuad)
    pyautogui.click(ar_right)
    sleep(1)
    return 1


def move_right_friends_list():
    """
    Смещает список друзей в право на одну позицию
    :return: 1
    """
    sleep(1)
    ar_right = pyautogui.locateCenterOnScreen('img/b_arrow_left.png', confidence=0.8)
    pyautogui.moveTo(ar_right, duration=1, tween=pyautogui.easeInOutQuad)
    pyautogui.click(ar_right)
    sleep(1)
    return 1


def move_friends_list_to_top():
    """Смещает список друзей в лево в начало"""
    begin = pyautogui.locateCenterOnScreen('img/b_begin.png', confidence=0.96)
    if begin:  # если увидел
        pyautogui.moveTo(begin, duration=1, tween=pyautogui.easeInOutQuad)
        print(' перемотка в начало ')
        sleep(1)
        pyautogui.click(begin)
        print('клик в начало ' + str(begin))
    # pyautogui.moveTo(50, 600, duration=1, tween=pyautogui.easeInOutQuad)
    sleep(1)


# def shmon():
#     global sum_vip
#     start_time = time()
#     vi = 10  # задаёт количество обнаружений
#     analiz = 0
#     vizit = 0
#
#     # ============================
#     def detect_search_region():
#         global iter_detect_search_region
#         iter_detect_search_region += 1
#         pos_klan = pyautogui.locateCenterOnScreen('img/klan_red.png', confidence=0.9)
#         pos_settings = pyautogui.locateCenterOnScreen('img/setting.png', confidence=0.9)
#         if pos_klan is not None:
#             x_region, y_region = pos_klan
#             x_region -= 125
#             y_region += 503
#             search_region = (x_region, y_region, 59, 132)
#         else:
#             x_region, y_region = pos_settings
#             x_region -= 776
#             y_region -= 10
#             search_region = (x_region, y_region, 59, 132)
#         return search_region
#
#     def visit_tent():
#         """
#         Обыск палатки
#         :return: int (счетчик положительных обысков)
#         """
#         ransack = pyautogui.locateCenterOnScreen('img/visit_to_tent.png', confidence=0.8)
#         if ransack is not None:
#             pyautogui.moveTo(ransack, duration=1, tween=pyautogui.easeInOutQuad)
#             pyautogui.click(ransack)
#             # print("клик обыск" + str(visit_to_tent))
#             vip = 1
#         else:
#             # print(' уже обыскан ')
#             vip = 0
#         return vip
#
#     def tent_detected():
#         sleep(1)
#         tent_d = pyautogui.locateCenterOnScreen('img/b_tent.png', confidence=0.9)
#         pyautogui.moveTo(tent_d, duration=1, tween=pyautogui.easeInOutQuad)
#         pyautogui.click(tent_d)
#         # print('клик по дом ' + str(tent_d))
#         sleep(1)
#
#     def vip_detected():
#         region_poiska = detect_search_region()
#         sleep(1)
#         pos_vip = pyautogui.locateCenterOnScreen('img/b_vip.png', region=region_poiska, confidence=0.8)
#         pyautogui.moveTo(pos_vip, duration=1, tween=pyautogui.easeInOutQuad)
#         pyautogui.click(pos_vip)
#         # print('клик по VIP ' + str(pos_vip))
#         sleep(1)
#
#     def end_search():
#         pyautogui.moveTo(200, 670)
#         sleep(1)
#         to_exit = pyautogui.locateCenterOnScreen('img/b_exit.png', confidence=0.9)
#         pyautogui.moveTo(to_exit, duration=1, tween=pyautogui.easeInOutQuad)
#         pyautogui.click(to_exit)
#         print('клик на выход')
#         pyautogui.moveTo(200, 670, duration=2, tween=pyautogui.easeInOutQuad)
#
#     # ================================================================================================
#     move_friends_list_to_top()
#     while vizit < vi:
#         pos_vip = pyautogui.locateCenterOnScreen('img/b_vip.png', region=oblast, confidence=0.8)
#         analiz += 1
#         pd = 0
#         er = 0
#         if pos_vip is not None:
#             vizit += 1
#             vip_detected()
#             # print('VIP № ' + str(vizit) + ' найден')
#             print(f'VIP № {vizit} найден')
#             tent = pyautogui.locateCenterOnScreen('img/b_tent.png', confidence=0.9)
#             while tent is None and pd <= 25:
#                 pd += 1
#                 er += 1
#                 vip_detected()
#                 tent = pyautogui.locateCenterOnScreen('img/b_tent.png', confidence=0.9)
#             tent_detected()
#             visit_tent()
#         if vizit < vi:
#             move_left_friends_list()
#     end_search()
#     print(f'Проанализировано {analiz}  изображений. Найдено {vizit} VIP ')
#     sum_vip = vizit
#     finish_time = float(time() - start_time)  # общее количество секунд
#     minutes = int(finish_time // 60)  # количество минут
#     seconds = round((finish_time % minutes), 2)
#     # print('Потрачено время', minutes, 'минут', seconds, 'сек.')
#     print(f'Потрачено время {minutes} минут {seconds} сек.')

def move_to_click(pos_click: tuple, z_p_k: float):
    """
    Поместить указатель мыши по координатам и кликнуть, учитывая задержку.
    :param pos_click: Point
    :param z_p_k: задержка перед кликом(float)
    :return: None
    """
    # print('move_to_click', pos_click)
    sleep(0.3)
    pyautogui.moveTo(pos_click, duration=0.1, tween=pyautogui.easeInOutQuad)
    # print('должен быть клик')
    sleep(z_p_k)
    pyautogui.click(pos_click)
    sleep(0.18)


def find_link():  # width=77, height=42
    """
    Закрыть если открыто, т.к. за чем-то может быть не видна позиция привязки
    :return: Point 'Зал славы'
    """
    push_close_all()
    # получение координат привязки
    pos_or_v = pyautogui.locateCenterOnScreen('img/hall_of_glory.png', confidence=0.9)
    sleep(0.5)
    return pos_or_v
