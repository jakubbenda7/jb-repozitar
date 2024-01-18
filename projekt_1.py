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
    
print("Text 1: ",TEXTS[0])
print("Text 2: ",TEXTS[1])
print("Text 3: ",TEXTS[2])
vyber = int(input("Zadejte číslo textu, který jste si vybral:"))

#příprava textů- rozdělení

slova_1 = TEXTS[0].split()
slova_2 = TEXTS[1].split()
slova_3 = TEXTS[2].split()

#zanesení do listu, s kterým budu pracovat + odebrání nežádoucích znaků

text_1 = []
for slovo in slova_1:
    text_1.append(slovo.strip(".,:;"))
    
text_2 = []
for slovo in slova_2:
    text_2.append(slovo.strip(".,:;"))
    
text_3 = []
for slovo in slova_3:
    text_3.append(slovo.strip(".,:;"))
    

pocet_slov_1= [slovo for slovo in text_1] 
pocet_slov_2= [slovo for slovo in text_2] 
pocet_slov_3= [slovo for slovo in text_3]

slova_psana_s_prvnim_velkym_pismenem_1=[slovo for slovo in text_1 if slovo.istitle()]
slova_psana_s_prvnim_velkym_pismenem_2=[slovo for slovo in text_2 if slovo.istitle()]
slova_psana_s_prvnim_velkym_pismenem_3=[slovo for slovo in text_3 if slovo.istitle()]

slova_psana_velkymi_pismeny_1=[slovo for slovo in text_1 if slovo.isupper() and slovo.isalpha()]
slova_psana_velkymi_pismeny_2=[slovo for slovo in text_2 if slovo.isupper() and slovo.isalpha()]
slova_psana_velkymi_pismeny_3=[slovo for slovo in text_3 if slovo.isupper() and slovo.isalpha()]

slova_psana_s_malymy_pismeny_1=[slovo for slovo in text_1 if slovo.islower() and slovo.isalpha()]
slova_psana_s_malymy_pismeny_2=[slovo for slovo in text_2 if slovo.islower() and slovo.isalpha()]
slova_psana_s_malymy_pismeny_3=[slovo for slovo in text_3 if slovo.islower() and slovo.isalpha()]

cisla_1=[slovo for slovo in text_1 if slovo.isnumeric()]
cisla_2=[slovo for slovo in text_2 if slovo.isnumeric()]
cisla_3=[slovo for slovo in text_3 if slovo.isnumeric()]

soucet_1= [int(x) for x in text_1 if x.isnumeric()]
suma_1=sum(soucet_1) 

soucet_2= [int(x) for x in text_2 if x.isnumeric()]
suma_2=sum(soucet_2) 

soucet_3= [int(x) for x in text_3 if x.isnumeric()]
suma_3=sum(soucet_3) 

def sloupcovy_graf(text):
    delka_slov = [len(slovo) for slovo in text]
    
    udaje_o_delce={}
    for delka in delka_slov:
        if delka in udaje_o_delce:
            udaje_o_delce[delka] +=1
        else:
            udaje_o_delce[delka] =1
    max_delka = max(udaje_o_delce.keys())        
    for i in range(1, max_delka + 1):
        cetnost= udaje_o_delce.get(i,0)
        print(f"{i}| {'*' * cetnost} | {cetnost}")

if vyber == 1:
    print("Text 1 obsahuje ",len(text_1),"slov.")
    print("Text 1 obsahuje ",len(slova_psana_s_prvnim_velkym_pismenem_1),"slov s prvním velkým písmenem.")
    print("Text 1 obsahuje ",len(slova_psana_velkymi_pismeny_1),"slov psaných velkými písmeny.")
    print("Text 1 obsahuje ",len(slova_psana_s_malymy_pismeny_1),"slov psaných malými písmeny.")
    print("Text 1 obsahuje ",len(cisla_1),"čísel.")
    print("Součet čísel v textu 1 je", (suma_1))
    print(oddelovac)
    print("POČ|","  VÝSKYT","|ČÍSLEM")
    print(oddelovac)
    sloupcovy_graf(text_1)
elif vyber == 2:
    print("Text 2 obsahuje ",len(text_2),"slov.")
    print("Text 2 obsahuje ",len(slova_psana_s_prvnim_velkym_pismenem_2),"slov s prvním velkým písmenem.")
    print("Text 2 obsahuje ",len(slova_psana_velkymi_pismeny_2),"slov psaných velkými písmeny.")
    print("Text 2 obsahuje ",len(slova_psana_s_malymy_pismeny_2),"slov psaných malými písmeny.")
    print("Text 2 obsahuje ",len(cisla_2),"čísel.")
    print("Součet čísel v textu 2 je", (suma_2))
    print(oddelovac)
    print("POČ|","  VÝSKYT","|ČÍSLEM")
    print(oddelovac)
    sloupcovy_graf(text_2)
elif vyber == 3:
    print("Text 3 obsahuje ",len(text_3),"slov.")
    print("Text 3 obsahuje ",len(slova_psana_s_prvnim_velkym_pismenem_3),"slov s prvním velkým písmenem.")
    print("Text 3 obsahuje ",len(slova_psana_velkymi_pismeny_3),"slov psaných velkými písmeny.")
    print("Text 3 obsahuje ",len(slova_psana_s_malymy_pismeny_3),"slov psaných malými písmeny.")
    print("Text 3 obsahuje ",len(cisla_3),"čísel.")
    print("Součet čísel v textu 3 je", (suma_3))
    print(oddelovac)
    print("POČ|","  VÝSKYT","|ČÍSLEM")
    print(oddelovac)
    sloupcovy_graf(text_3)
else:
    print("Zadali jste neplatné číslo, program bude ukončen!")
    exit()


    