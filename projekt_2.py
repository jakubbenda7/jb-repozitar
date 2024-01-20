"""
projekt_2.py: druhý projekt do Engeto Online Python Akademie
author: Jakub Benda
email: jakub.benda55@gmail.com  
discord: jakubbenda7
"""

oddelovac="-----------------------------------------------"

print("Zdravím!")
print(oddelovac)
print("Vygeneroval jsem pro Vás 4 náhodná čísla.\n"
"Pojďme si zahrát hru bulls and cows.")
print(oddelovac)

import random
import time

def ctyrmistne_cislo():
    cislo = ""
    while len(cislo) < 4:
        cislo_2 = str(random.randint(0, 9))
        if len(cislo) == 0 and cislo_2 == "0":
            continue
        if not cislo_2 in cislo:
            cislo += cislo_2
    return cislo

n_v_c = ctyrmistne_cislo()


start_time = time.time()
pocet_pokusu_hrace = 0

while True:
    cislo_hrace = input("Zadejte číslo:")
    bulls = 0
    cows = 0
    print(oddelovac)

    if len(cislo_hrace) == 4 and cislo_hrace.isdigit() and cislo_hrace[0] != "0" and len(set(cislo_hrace)) == len(cislo_hrace):
        pocet_pokusu_hrace += 1
        for i in range(len(n_v_c)):
            if cislo_hrace[i] in n_v_c:
                if cislo_hrace[i] == n_v_c[i]:
                    bulls += 1
                else:
                    cows += 1
        print("Cows:", cows, "Bulls:", bulls)
        if bulls == 4:
            end_time = time.time()
            elapsed_time = end_time - start_time
            print(f"Vyhrál si! Uhodl si správné číslo za {pocet_pokusu_hrace} pokusů a za {elapsed_time:.2f} sekundy.")
            break
    else: 
        print("Číslo musí mít 4 znaky, nesmí obsahovat jiné znaky než čísla, nesmí obsahovat duplicity\n", 
              "a nesmí začínat nulou. Zadej nové číslo.")
        
   
    