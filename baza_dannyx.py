# имя станции = [имя для Print, поиск на карте, ID станции, если её не видно на карте,[задания]]

st_alexs = ['ст. Алексеевская', 'img/tonelli/k_Alexs.png', 'img/tonelli/s_Alexs.png', 0, []]
st_biblioteka = ['ст. Библиотека им. Ленина', 'img/tonelli/k_Biblioteka.png', 'img/tonelli/s_Biblioteka.png', 0, []]

st_borov = ['ст. Боровицкая', 'img/tonelli/k_Borov.png', 'img/tonelli/s_Borov.png', 'стрелка юг', []]

st_bulvar = ['ст. Цветной бульвар', 'img/tonelli/k_Cvetnoy.png', 'img/tonelli/s_Cvetnoy.png', 0, []]
st_vdnx = ['ст. ВДНХ', 'img/tonelli/k_VDNX.png', 'img/tonelli/s_VDNX.png', 0, []]

st_kiev = ['ст. Киевская', 'img/tonelli/k_Kiev.png', 'img/tonelli/s_Kiev.png', 0,
           ['img/45xp.png', 'img/68xp.png', 'img/68xp.png', 'img/90xp.png', 'img/90xp.png', 'img/113xp.png']]

st_kiev_a = ['ст. Киевская A', 'img/tonelli/k_Kiev_a.png', 'img/tonelli/s_Kiev_a.png', 0, [0]]
st_kitay = ['ст. Китай-город', 'img/tonelli/k_Kitay.png', 'img/tonelli/s_Kitay.png', 'стрелка север', []]
st_kropot = ['ст. Кропоткинская', 'img/tonelli/k_Kropotkin.png', 'img/tonelli/s_Kropotkin.png', 0, [0]]

st_most = ['ст. Кузнецкий мост', 'img/tonelli/k_Kuzneckiy.png', 'img/tonelli/s_Kuzneckiy.png', 0,
           ['img/23xp.png', 'img/23xp.png', 'img/45xp.png', 'img/45xp.png', 'img/68xp.png', 'img/68xp.png']]

st_novok = ['ст. Новокузнецкая', 'img/tonelli/k_Novokuznec.png', 'img/tonelli/s_Novokuznec.png', 0, []]
st_pavelec = ['ст. Павелецкая', 'img/tonelli/k_Pavelec.png', 'img/tonelli/s_Pavelec.png', 0, []]
st_pavelec_g = ['ст. Павелецкая ганза', 'img/tonelli/k_Pavelec_g.png', 'img/tonelli/s_Pavelec_g.png', 0, []]
st_park_g = ['ст. Парк культуры ганза', 'img/tonelli/k_Park_ganza.png', 'img/tonelli/s_Park_ganza.png', 0, [0]]
st_park_kr = ['ст. Парк культуры кр', 'img/tonelli/k_Park_kr.png', 'img/tonelli/s_Park_kr.png', 0, []]
st_polyanka = ['ст. Полянка', 'img/tonelli/k_Polyanka.png', 'img/tonelli/s_Polyanka.png', 0, []]
st_prospekt = ['ст. Проспект мира', 'img/tonelli/k_Prospekt.png', 'img/tonelli/s_Prospekt.png', 0, []]
st_pushkin = ['ст. Пушкинская', 'img/tonelli/k_Pushkin.png', 'img/tonelli/s_Pushkin.png', 0, []]
st_riga = ['ст. Рижская', 'img/tonelli/k_Rizgskaya.png', 'img/tonelli/s_Rizgskaya.png', 0, []]
st_suxarev = ['ст. Сухаревская', 'img/tonelli/k_Suxarev.png', 'img/tonelli/s_Suxarev.png', 0, []]
st_teatr = ['ст. Театральная', 'img/tonelli/k_Teatr.png', 'img/tonelli/s_Teatr.png', 0, []]
st_tver = ['ст. Тверская', 'img/tonelli/k_Tver.png', 'img/tonelli/s_Tver.png', 0, []]
st_tretya = ['ст. Третьяковская', 'img/tonelli/k_Tretyakov.png', 'img/tonelli/s_Tretyakov.png', 'стрелка юг', [0]]
st_turgenev = ['ст. Тургеневская', 'img/tonelli/k_Turgenev.png', 'img/tonelli/s_Turgenev.png', 0, [0]]
st_chekhov = ['ст. Чеховская', 'img/tonelli/k_Chekhov.png', 'img/tonelli/s_Chekhov.png', 'стрелка север', [0]]

st_frunze = ['ст. Фрунзенская', 'img/tonelli/k_Frunze.png', 'img/tonelli/s_Frunze.png', 0, []]
st_communist = ['ст. Коммунистическая', 'img/tonelli/k_Communist.png', 'img/tonelli/s_Communist.png', 0, []]

list_of_stations = [st_alexs, st_biblioteka, st_borov, st_bulvar, st_vdnx, st_kiev, st_kiev_a, st_kitay, st_kropot, st_most, st_novok, st_pavelec,
                    st_pavelec_g, st_park_g, st_park_kr, st_polyanka, st_prospekt, st_pushkin, st_riga, st_suxarev, st_teatr, st_tver, st_tretya,
                    st_turgenev, st_chekhov, st_frunze, st_communist]

# кратчайший путь от Кузнецкого моста на Рижскую и обратно
most_riga = [st_pushkin, st_tver, st_teatr, st_novok, st_tretya, st_kitay, st_turgenev, st_suxarev,
             st_prospekt, st_riga]
riga_most = [st_prospekt, st_suxarev, st_turgenev, st_kitay, st_tretya, st_novok, st_teatr,
             st_tver, st_pushkin, st_most]

# кратчайший путь от Киевской до Кузнецкого моста и обратно
kiev_most = [st_park_g, st_park_kr, st_kropot, st_biblioteka, st_borov, st_chekhov, st_pushkin, st_most]
most_kiev = [st_pushkin, st_chekhov, st_borov, st_biblioteka, st_kropot, st_park_kr, st_park_g, st_kiev]

# кратчайший путь от Фрунзенской до Рижской и обратно
frunze_riga = [st_park_kr, st_kropot, st_biblioteka, st_borov, st_chekhov, st_tver, st_teatr, st_novok, st_tretya, st_kitay,
               st_turgenev, st_suxarev, st_prospekt, st_riga]
riga_frunze = [st_prospekt, st_suxarev, st_turgenev, st_kitay, st_tretya, st_novok, st_teatr,
               st_tver, st_chekhov, st_borov, st_biblioteka, st_kropot, st_park_kr, st_frunze]

# оббежать все станции в поисках подарков
bypass = [st_pushkin, st_tver, st_teatr, st_novok, st_pavelec, st_pavelec_g, st_pavelec, st_novok, st_tretya, st_kitay, st_turgenev, st_suxarev,
          st_prospekt, st_riga, st_alexs, st_vdnx,
          st_alexs, st_riga, st_prospekt, st_suxarev, st_turgenev, st_kitay, st_tretya, st_novok, st_teatr, st_tver, st_chekhov,
          st_bulvar, st_chekhov, st_borov, st_polyanka, st_borov, st_biblioteka, st_kropot, st_park_kr, st_frunze, st_communist,
          st_frunze, st_park_kr, st_park_g, st_kiev, st_kiev_a,
          st_kiev, st_park_g, st_park_kr, st_kropot, st_biblioteka, st_borov, st_chekhov, st_pushkin, st_most]

# за кикиморами в туннелях
most_kikimory = [st_pushkin, st_tver, st_teatr, st_novok, st_tretya, st_kitay,
                 st_turgenev, st_suxarev, st_prospekt, st_riga, st_prospekt, st_suxarev,
                 st_turgenev, st_suxarev, st_prospekt, st_riga, st_prospekt, st_suxarev,
                 st_turgenev, st_suxarev, st_prospekt, st_riga, st_prospekt, st_suxarev,
                 st_turgenev, st_suxarev, st_prospekt, st_riga, st_prospekt, st_suxarev,
                 st_turgenev, st_suxarev, st_prospekt, st_riga, st_prospekt, st_suxarev,
                 st_turgenev, st_kitay, st_tretya, st_novok, st_teatr, st_tver, st_pushkin, st_most]

frunze_kikimory = [st_park_kr, st_kropot, st_biblioteka, st_borov, st_chekhov, st_tver, st_teatr, st_novok, st_tretya, st_kitay,
                   st_turgenev, st_suxarev, st_prospekt, st_riga, st_prospekt, st_suxarev,
                   st_turgenev, st_suxarev, st_prospekt, st_riga, st_prospekt, st_suxarev,
                   st_turgenev, st_suxarev, st_prospekt, st_riga, st_prospekt, st_suxarev,
                   st_turgenev, st_suxarev, st_prospekt, st_riga, st_prospekt, st_suxarev,
                   st_turgenev, st_suxarev, st_prospekt, st_riga, st_prospekt, st_suxarev,
                   st_turgenev, st_kitay, st_tretya, st_novok, st_teatr, st_tver, st_chekhov, st_borov, st_biblioteka, st_kropot, st_park_kr, st_frunze]
# тест передвижения между туннелями
test_running = [st_park_kr, st_kropot, st_park_kr, st_frunze]

frunze_kiev = [st_park_kr, st_park_g, st_kiev]
kiev_frunze = [st_park_g, st_park_kr, st_frunze]

frunze_most = [st_park_kr, st_kropot, st_biblioteka, st_borov, st_chekhov, st_pushkin, st_most]
most_frunze = [st_pushkin, st_chekhov, st_borov, st_biblioteka, st_kropot, st_park_kr, st_frunze]

pauk_yascher = [st_communist, st_frunze, st_communist, st_frunze, st_communist, st_frunze, st_park_kr, st_frunze, st_park_kr, st_kropot, st_park_kr,
                st_kropot,
                st_park_kr, st_kropot, st_park_kr, st_park_g, st_kiev, st_park_g, st_kiev, st_park_g, st_kiev, st_park_g, st_park_kr, st_frunze]
