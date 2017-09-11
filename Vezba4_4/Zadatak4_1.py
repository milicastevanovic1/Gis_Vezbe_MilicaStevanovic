# -*- coding: utf-8 -*-

obavestenje1 = int(raw_input(" --Za čitanje sadržaja datoteke uneti 1 \n"
                             " --Za upisivanje sadržaja u datoteku uneti 2\n"))
if obavestenje1 == 1:
    obavestenje2 = int(input(" --Za čitanje celokupnog sadržaja datoteke odjednom, uneti 1\n"
                             " --Za čitanje sadržaja datoteke red po red, uneti 2\n"))
    if obavestenje2 == 1:
        f = open('Ulazni_Podaci.txt', 'r')
        print(f.read())
        f.close()
    elif obavestenje2 == 2:
        f = open('Ulazni_Podaci.txt', 'r')
        f.seek(0)
        br = 1
        for i in f.readlines():
            print(str(br) + ". red: " + str(i))
            br += 1
        f.close()
    else:
        print("Ne odgovara zahtevu!")
elif obavestenje1 == 2:
    obavestenje2 = int(input("-- Za dodavanje sadržaja datoteke na postojeći, uneti 1\n"
                             "-- Za prepisivanje postojećeg sadržaja datoteke, uneti 2\n"))
    if obavestenje2 == 1:
        t = str(input("Uneti tekst za upisivanje u datoteku (pod znacima navoda):\n"))
        f = open('Ulazni_Podaci.txt', 'a')
        f.write(t)
        f.close()
    elif obavestenje2 == 2:
        t = str(input("Uneti tekst za upisivanje u datoteku (pod znacima navoda):\n"))
        f = open('Ulazni_Podaci.txt', 'w')
        f.write(t)
        f.close()
    else:
        print("Ne odgovara zahtevu!")
else:
    print("Ne odgovara zahtevu!")