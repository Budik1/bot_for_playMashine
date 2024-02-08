# имя станции = [имя для Print, поиск на карте, ID станции, если её не видно на карте,[задания]]

alexs = ['ст. Алексеевская', 'img/tonelli/k_Alexs.png', 'img/tonelli/s_Alexs.png', 0]
biblioteka = ['ст. Библиотека им. Ленина', 'img/tonelli/k_Biblioteka.png', 'img/tonelli/s_Biblioteka.png', 0]

borov = ['ст. Боровицкая', 'img/tonelli/k_Borov.png', 'img/tonelli/s_Borov.png', 'стрелка юг']

bulvar = ['ст. Цветной бульвар', 'img/tonelli/k_Cvetnoy.png', 'img/tonelli/s_Cvetnoy.png', 0]
vdnx = ['ст. ВДНХ', 'img/tonelli/k_VDNX.png', 'img/tonelli/s_VDNX.png', 0]

kiev = ['ст. Киевская', 'img/tonelli/k_Kiev.png', 'img/tonelli/s_Kiev.png', 0,
        ['img/45xp.png', 'img/68xp.png', 'img/68xp.png', 'img/90xp.png', 'img/90xp.png', 'img/113xp.png']]

kiev_a = ['ст. Киевская A', 'img/tonelli/k_Kiev_a.png', 'img/tonelli/s_Kiev_a.png', 0]
kitay = ['ст. Китай-город', 'img/tonelli/k_Kitay.png', 'img/tonelli/s_Kitay.png', 'стрелка север']
kropot = ['ст. Кропоткинская', 'img/tonelli/k_Kropotkin.png', 'img/tonelli/s_Kropotkin.png', 0]

most = ['ст. Кузнецкий мост', 'img/tonelli/k_Kuzneckiy.png', 'img/tonelli/s_Kuzneckiy.png', 0,
        ['img/23xp.png', 'img/23xp.png', 'img/45xp.png', 'img/45xp.png', 'img/68xp.png', 'img/68xp.png']]

novok = ['ст. Новокузнецкая', 'img/tonelli/k_Novokuznec.png', 'img/tonelli/s_Novokuznec.png', 0]
pavelec = ['ст. Павелецкая', 'img/tonelli/k_Pavelec.png', 'img/tonelli/s_Pavelec.png', 0]
pavelec_g = ['ст. Павелецкая ганза', 'img/tonelli/k_Pavelec_g.png', 'img/tonelli/s_Pavelec_g.png', 0]
park_g = ['ст. Парк культуры ганза', 'img/tonelli/k_Park_ganza.png', 'img/tonelli/s_Park_ganza.png', 0]
park_kr = ['ст. Парк культуры кр', 'img/tonelli/k_Park_kr.png', 'img/tonelli/s_Park_kr.png', 0]
polyanka = ['ст. Полянка', 'img/tonelli/k_Polyanka.png', 'img/tonelli/s_Polyanka.png', 0]
prospekt = ['ст. Проспект мира', 'img/tonelli/k_Prospekt.png', 'img/tonelli/s_Prospekt.png', 0]
pushkin = ['ст. Пушкинская', 'img/tonelli/k_Pushkin.png', 'img/tonelli/s_Pushkin.png', 0]
riga = ['ст. Рижская', 'img/tonelli/k_Rizgskaya.png', 'img/tonelli/s_Rizgskaya.png', 0]
suxarev = ['ст. Сухаревская', 'img/tonelli/k_Suxarev.png', 'img/tonelli/s_Suxarev.png', 0]
teatr = ['ст. Театральная', 'img/tonelli/k_Teatr.png', 'img/tonelli/s_Teatr.png', 0]
tver = ['ст. Тверская', 'img/tonelli/k_Tver.png', 'img/tonelli/s_Tver.png', 0]
tretya = ['ст. Третьяковская', 'img/tonelli/k_Tretyakov.png', 'img/tonelli/s_Tretyakov.png', 'стрелка юг']
turgenev = ['ст. Тургеневская', 'img/tonelli/k_Turgenev.png', 'img/tonelli/s_Turgenev.png', 0]
сhekhov = ['ст. Чеховская', 'img/tonelli/k_Chekhov.png', 'img/tonelli/s_Chekhov.png', 'стрелка север']

frunze = ['ст. Фрунзенская', 'img/tonelli/k_Frunze.png', 'img/tonelli/s_Frunze.png', 0]
communist = ['ст. Коммунистическая', 'img/tonelli/k_Communist.png', 'img/tonelli/s_Communist.png', 0]

list_of_stations = [alexs, biblioteka, borov, bulvar, vdnx, kiev, kiev_a, kitay, kropot, most, novok, pavelec,
                    pavelec_g, park_g, park_kr, polyanka, prospekt, pushkin, riga, suxarev, teatr, tver, tretya,
                    turgenev, сhekhov, frunze, communist]

# кратчайший путь от Кузнецкого моста на Рижскую и обратно
most_riga = [pushkin, tver, teatr, novok, tretya, kitay, turgenev, suxarev,
             prospekt, riga]
riga_most = [prospekt, suxarev, turgenev, kitay, tretya, novok, teatr,
             tver, pushkin, most]

# кратчайший путь от Киевской до Кузнецкого моста и обратно
kiev_most = [park_g, park_kr, kropot, biblioteka, borov, сhekhov, pushkin, most]
most_kiev = [pushkin, сhekhov, borov, biblioteka, kropot, park_kr, park_g, kiev]

# кратчайший путь от Фрунзенской до Рижской и обратно
frunze_riga = [park_kr, kropot, biblioteka, borov, сhekhov, tver, teatr, novok, tretya, kitay,
               turgenev, suxarev, prospekt, riga]
riga_frunze = [prospekt, suxarev, turgenev, kitay, tretya, novok, teatr,
               tver, сhekhov, borov, biblioteka, kropot, park_kr, frunze]

# оббежать все станции в поисках подарков
bypass = [pushkin, tver, teatr, novok, pavelec, pavelec_g, pavelec, novok, tretya, kitay, turgenev, suxarev,
          prospekt, riga, alexs, vdnx,
          alexs, riga, prospekt, suxarev, turgenev, kitay, tretya, novok, teatr, tver, сhekhov,
          bulvar, сhekhov, borov, polyanka, borov, biblioteka, kropot, park_kr, frunze, communist,
          frunze, park_kr, park_g, kiev, kiev_a,
          kiev, park_g, park_kr, kropot, biblioteka, borov, сhekhov, pushkin, most]

# за кикиморами в туннелях
most_kikimory = [pushkin, tver, teatr, novok, tretya, kitay,
                 turgenev, suxarev, prospekt, riga, prospekt, suxarev,
                 turgenev, suxarev, prospekt, riga, prospekt, suxarev,
                 turgenev, suxarev, prospekt, riga, prospekt, suxarev,
                 turgenev, suxarev, prospekt, riga, prospekt, suxarev,
                 turgenev, suxarev, prospekt, riga, prospekt, suxarev,
                 turgenev, kitay, tretya, novok, teatr, tver, pushkin, most]

frunze_kikimory = [park_kr, kropot, biblioteka, borov, сhekhov, tver, teatr, novok, tretya, kitay,
                   turgenev, suxarev, prospekt, riga, prospekt, suxarev,
                   turgenev, suxarev, prospekt, riga, prospekt, suxarev,
                   turgenev, suxarev, prospekt, riga, prospekt, suxarev,
                   turgenev, suxarev, prospekt, riga, prospekt, suxarev,
                   turgenev, suxarev, prospekt, riga, prospekt, suxarev,
                   turgenev, kitay, tretya, novok, teatr, tver, сhekhov, borov, biblioteka, kropot, park_kr, frunze]
# тест передвижения между туннелями
test_running = [bulvar, сhekhov]

frunze_kiev = [park_kr, park_g, kiev]
kiev_frunze = [park_g, park_kr, frunze]

frunze_most = [park_kr, kropot, biblioteka, borov, сhekhov, pushkin, most]
most_frunze = [pushkin, сhekhov, borov, biblioteka, kropot, park_kr, frunze]

pauk_yascher = [communist, frunze, communist, frunze, communist, frunze, park_kr, frunze, park_kr, kropot, park_kr,
                kropot,
                park_kr, kropot, park_kr, park_g, kiev, park_g, kiev, park_g, kiev, park_g, park_kr, frunze]
