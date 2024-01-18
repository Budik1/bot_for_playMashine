import pyautogui
from time import sleep
import datetime

son = 1
zadergka = 10
sum_vip = 0
status_bonus = "0"
par_conf = 0.79
nali4ie_energii = 1
koli4estvo_zadaniy = 3
oblast = (51, 707, 92, 111)
img_sl = {'спецпредложение':'img/spec_predlog.png', 'закрыть в спецпредложении':'img/s_p_zakr.png',
          'продолжить как Гаврил':'img/b_autoriz.png',
          'мои игры V1':'img/my_game1.png','мои игры V2':'img/my_game2.png',
          'иконка на рабочем столе':'img/icon_in_desktop.png'}

def time_now():
    now = datetime.datetime.now()
    date_time = (now.strftime('%Y-%m-%d_%H:%M:%S'))
    date = (now.date())
    return date_time, date


def podapok():
    podarok = pyautogui.locateCenterOnScreen('img/b_pod.png', confidence=0.91)
    pyautogui.moveTo(podarok, duration=1, tween=pyautogui.easeInOutQuad)
    pyautogui.click(podarok)

    otkryt = pyautogui.locateCenterOnScreen('img/b_p_otkr.png', confidence=0.9)
    while otkryt is not None:
        pyautogui.moveTo(otkryt, duration=1, tween=pyautogui.easeInOutQuad)
        pyautogui.click(otkryt)
        sleep(son)
        spasib = pyautogui.locateCenterOnScreen('img/b_p_spasibo.png', confidence=0.9)
        pyautogui.moveTo(spasib, duration=1, tween=pyautogui.easeInOutQuad)
        pyautogui.click(spasib)
        sleep(son)
        podar = pyautogui.locateCenterOnScreen('img/b_p_podarit.png', confidence=0.85)
        print(podar)
        pyautogui.moveTo(podar, duration=1, tween=pyautogui.easeInOutQuad)
        pyautogui.click(podar)

        otkryt = pyautogui.locateCenterOnScreen('img/b_p_otkr.png', confidence=0.9)


def zakryt():
    zakryt0 = pyautogui.locateCenterOnScreen('img/zakryt.png', confidence=0.9)
    # print(zakryt0)
    if zakryt0 is not None:
        zakryt = pyautogui.locateCenterOnScreen('img/zakryt.png', confidence=0.9)
        # print(zakryt)
        pyautogui.moveTo(zakryt, duration=1, tween=pyautogui.easeInOutQuad)
        pyautogui.click(zakryt)
        sleep(son)


def bonus():
    # кнопка добавить
    pos_bonus = pyautogui.locateCenterOnScreen('img/dobavit.png', confidence=0.8)
    pyautogui.moveTo(pos_bonus, duration=1, tween=pyautogui.easeInOutQuad)
    sleep(son)
    pyautogui.click(pos_bonus)
    sleep(son * 2)
    # кнопка забрать
    bonus = pyautogui.locateCenterOnScreen('img/zabrat.png', confidence=0.9)
    if bonus != None:
        pyautogui.moveTo(bonus, duration=1, tween=pyautogui.easeInOutQuad)
        pyautogui.click()
        print('Бщнус найден')
    else:
        print('Бщнус не найден')
    # кнопка закрыть
    zakryt()
    zakryt()
    # save_to_File()


def zapusk():
    p_my = 0
    paus = 0

    def spec_predlog():
        sz = 0
        spec = pyautogui.locateCenterOnScreen('img/spec_predlog.png', confidence=0.96)
        if spec is not None:
            s_p_zakr = pyautogui.locateCenterOnScreen('img/s_p_zakr.png', confidence=0.96)
            while s_p_zakr is not None and sz <= 5:
                sleep(son * 2)
                s_p_zakr = pyautogui.locateCenterOnScreen('img/s_p_zakr.png', confidence=0.96)
                sz += 1
            pyautogui.click(s_p_zakr)

    def authorization():  # авторизация при необходимости
        sleep(son * 2)
        pos_autoriz = pyautogui.locateCenterOnScreen('img/b_autoriz.png', confidence=0.8)
        if pos_autoriz is not None:
            pyautogui.moveTo(pos_autoriz, duration=1, tween=pyautogui.easeInOutQuad)
            pyautogui.click(pos_autoriz)
            sleep(son * 2)

    # клик по кнопке "мои игры"
    def _my_game():
        pos_my_game = pyautogui.locateCenterOnScreen('img/my_game1.png', confidence=0.8)
        pos_my_game1 = pyautogui.locateCenterOnScreen('img/my_game2.png', confidence=0.8)
        while pos_my_game is None and pos_my_game1 is None:
            sleep(0.5)
            pos_my_game = pyautogui.locateCenterOnScreen('img/my_game1.png', confidence=0.8)
            print(pos_my_game)
            pos_my_game1 = pyautogui.locateCenterOnScreen('img/my_game2.png', confidence=0.8)
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
        pos_autoriz = pyautogui.locateCenterOnScreen('img/b_autoriz.png', confidence=0.8)
        if pos_autoriz is not None:
            authorization()

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


    authorization()
    _my_game()
    klik_icon_game()
    geograf()
    spec_predlog()


def shmon():
    global sum_vip
    vi = 10  # задаёт количество обнаружений
    analiz = 0
    vizit = 0

    def vna4flo():
        begin = pyautogui.locateCenterOnScreen('img/b_begin.png', confidence=0.96)
        if begin is not None:  # если увидел
            pyautogui.moveTo(begin, duration=1, tween=pyautogui.easeInOutQuad)
            print(' перемотка в начало ')
            sleep(son)
            pyautogui.click(begin)
            print('клик в начало ' + str(begin))
        pyautogui.moveTo(50, 600, duration=1, tween=pyautogui.easeInOutQuad)
        sleep(son)

    def vip_detected():
        sleep(son)
        pos_vip = pyautogui.locateCenterOnScreen('img/b_vip.png', region=oblast, confidence=0.8)
        pyautogui.moveTo(pos_vip, duration=1, tween=pyautogui.easeInOutQuad)
        pyautogui.click(pos_vip)
        print('клик по VIP ' + str(pos_vip))
        sleep(son)

    def dom_detected():
        sleep(son)
        dom = pyautogui.locateCenterOnScreen('img/b_dom.png', confidence=0.9)
        pyautogui.moveTo(dom, duration=1, tween=pyautogui.easeInOutQuad)
        pyautogui.click(dom)
        print('клик по дом ' + str(dom))
        sleep(son)

    def dom_not_detected():
        sleep(son)
        pos_vip = pyautogui.locateCenterOnScreen('img/b_vip.png', region=oblast, confidence=0.8)
        pyautogui.click(pos_vip)
        print("повтор клик по дом")
        sleep(son)

    def obysk():
        obysk = pyautogui.locateCenterOnScreen('img/b_obysk.png', confidence=0.8)
        if obysk is not None:
            pyautogui.moveTo(obysk, duration=1, tween=pyautogui.easeInOutQuad)
            pyautogui.click(obysk)
            print("клик обыск" + str(obysk))
        else:
            print(' уже обыскан ')

    def new_analysis():
        sleep(son)
        ar_right = pyautogui.locateCenterOnScreen('img/b_arrow_right.png', confidence=0.8)
        pyautogui.moveTo(ar_right, duration=1, tween=pyautogui.easeInOutQuad)
        pyautogui.click(ar_right)
        sleep(son)

    def end_obysk():
        pyautogui.moveTo(200, 670)
        sleep(son)
        vyxod = pyautogui.locateCenterOnScreen('img/b_vyxod.png', confidence=0.9)
        pyautogui.moveTo(vyxod, duration=1, tween=pyautogui.easeInOutQuad)
        pyautogui.click(vyxod)
        print('клик на выход')
        pyautogui.moveTo(200, 670, duration=2, tween=pyautogui.easeInOutQuad)

    vna4flo()
    while vizit < vi:
        pos_vip = pyautogui.locateCenterOnScreen('img/b_vip.png', region=oblast, confidence=0.8)
        analiz += 1
        pd = 0
        er = 0
        if pos_vip is not None:
            vizit += 1
            vip_detected()
            print('VIP № ' + str(vizit) + ' найден')
            dom = pyautogui.locateCenterOnScreen('img/b_dom.png', confidence=0.9)
            while dom is None and pd <= 25:
                pd += 1
                er += 1
                dom_not_detected()
                print('Дом не найден, повтор поиска №' + str(pd) + 'всего ошибок ' + str(er))
                dom = pyautogui.locateCenterOnScreen('img/b_dom.png', confidence=0.9)
            print(' дом найден')
            dom_detected()
            obysk()
        if vizit < vi:
            new_analysis()
    end_obysk()
    print('Проанализировано ' + str(analiz) + ' изображений. Найдено ' + str(vizit) + ' VIP ')
    sum_vip = vizit


# нажать по ссылке
def moveTo_click(pos_klick, z_p_k):
    # z_p_k задержка перед кликом
    # print('moveTo_click', pos_klick)
    sleep(0.3)
    pyautogui.moveTo(pos_klick, duration=0.1, tween=pyautogui.easeInOutQuad)
    # print('должен быть клик')
    sleep(z_p_k)
    pyautogui.click(pos_klick)
    sleep(0.18)