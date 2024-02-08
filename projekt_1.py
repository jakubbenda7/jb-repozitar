"""
projekt_1.py: první projekt do Engeto Online Python Akademie
author: Jakub Benda 
email: jakub.benda55@gmail.com
discord: jakubbenda7
"""
TEXTS = ['''
Situated about 10 miles west of Kemmerer,
Fossil Butte is a ruggedly impressive
topographic feature that rises sharply
some 1000 feet above Twin Creek Valley
to an elevation of more than 7500 feet
above sea level. The butte is located just
north of US 30N and the Union Pacific Railroad,
which traverse the valley.\n ''',
'''At the base of Fossil Butte are the bright
red, purple, yellow and gray beds of the Wasatch
Formation. Eroded portions of these horizontal
beds slope gradually upward from the valley floor
and steepen abruptly. Overlying them and extending
to the top of the butte are the much steeper
buff-to-white beds of the Green River Formation,
which are about 300 feet thick.\n''',
'''The monument contains 8198 acres and protects
a portion of the largest deposit of freshwater fish
fossils in the world. The richest fossil fish deposits
are found in multiple limestone layers, which lie some
100 feet below the top of the butte. The fossils
represent several varieties of perch, as well as
other freshwater genera and herring similar to those
in modern oceans. Other fish such as paddlefish,
garpike and stingray are also present.\n'''
]
oddelovac = "----------------------------------------"
registrovani_uzivatele = {"bob" : "123", "ann" : "pass123", "mike" : "password123", "liz" : "pass123"}
prihlasovaci_jmeno = input("Zadejte Vaše přihlašovací jméno:")
heslo = input("Zadejte Vaše přihlašovací heslo:")
if registrovani_uzivatele.get(prihlasovaci_jmeno) == heslo:
    print("Vítej v textovém analyzátoru!\n""Máme 3 textové soubory k zanalyzování")
    print(oddelovac)
else:
    print("Nesprávné přihlašovací údaje!\n""Ukončuji program")
    exit()
    
for i, text in enumerate(TEXTS, start=1):
    print(f"Text {i}: {text}")

vyber = input("Zadejte číslo textu, který jste si vybral:")
if not vyber.isdigit():
    print ("Zadali jste neplatné číslo, program bude ukončen!")
    quit()
vyber = int(vyber)
if vyber < 1 or vyber > len(TEXTS):
    print ("Zadali jste neplatné číslo, program bude ukončen!")
    quit()
    
vybrany_text = TEXTS[vyber - 1]
max_cetnost= None
def sloupcovy_graf(text):
    delka_slov = [len(slovo) for slovo in text]
    
    udaje_o_delce = {}
    for delka in delka_slov:
        if delka in udaje_o_delce:
            udaje_o_delce[delka] += 1
        else:
            udaje_o_delce[delka] = 1    
    max_delka = max(udaje_o_delce.keys())
    global max_cetnost
    max_cetnost = max(udaje_o_delce.values())
    graf = ""    
    for i in range(1, max_delka + 1):
        cetnost = udaje_o_delce.get(i, 0)
        graf += f"{i} \t| {'*' * cetnost:<{max_cetnost}}\t| {cetnost}\n"
        
    return graf
    
slova = [slovo.strip(". , : ;") for slovo in vybrany_text.split()]
slova_psana_s_prvnim_velkym_pismenem = [slovo for slovo in slova if slovo.istitle()]
slova_psana_velkymi_pismeny = [slovo for slovo in slova if slovo.isupper() and slovo.isalpha()]
slova_psana_malymi_pismeny = [slovo for slovo in slova if slovo.islower() and slovo.isalpha]
soucet = [slovo for slovo in slova if slovo.isnumeric()]
hodnoty = [int(slovo) for slovo in soucet]
celkova_suma = sum(hodnoty)
graf_textu = sloupcovy_graf(slova)

print(f"Vybraný text obsahuje {len(slova)} slov.")
print(f"Vybraný text obsahuje {len(slova_psana_s_prvnim_velkym_pismenem)} slov začínajících velkým písmenem.")
print(f"Vybraný text obsahuje {len(slova_psana_velkymi_pismeny)} slov psaných velkými písmeny.")
print(f"Vybraný text obsahuje {len(slova_psana_malymi_pismeny)} slov psaných velkými písmeny.")
print(f"Vybraný text obsahuje {len(soucet)} čísel.")
print(f"Součet čísel ve vybraném textu je: {celkova_suma}")
print(oddelovac)
if max_cetnost > 13:
    print("POČ \t|  VÝSKYT\t\t|ČÍSLEM")
else:
    print("POČ \t|  VÝSKYT\t|ČÍSLEM")
print(oddelovac)
print(graf_textu)

    
