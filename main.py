"""
projekt_1.py: první projekt do Engeto Online Python Akademie

author: Pavol Medo
email: palimedo@gmail.com
"""
TEXTS = [
    '''Situated about 10 miles west of Kemmerer,
    Fossil Butte is a ruggedly impressive
    topographic feature that rises sharply
    some 1000 feet above Twin Creek Valley
    to an elevation of more than 7500 feet
    above sea level. The butte is located just
    north of US 30 and the Union Pacific Railroad,
    which traverse the valley.''',
    '''At the base of Fossil Butte are the bright
    red, purple, yellow and gray beds of the Wasatch
    Formation. Eroded portions of these horizontal
    beds slope gradually upward from the valley floor
    and steepen abruptly. Overlying them and extending
    to the top of the butte are the much steeper
    buff-to-white beds of the Green River Formation,
    which are about 300 feet thick.''',
    '''The monument contains 8198 acres and protects
    a portion of the largest deposit of freshwater fish
    fossils in the world. The richest fossil fish deposits
    are found in multiple limestone layers, which lie some
    100 feet below the top of the butte. The fossils
    represent several varieties of perch, as well as
    other freshwater genera and herring similar to those
    in modern oceans. Other fish such as paddlefish,
    garpike and stingray are also present.'''
]

#################### přihlašovací jméno a heslo ####################

uzivatele = {"bob": "123",
             "ann": "pass123",
             "mike": "password123",
             "liz": "pass123"
}

uzivatel_jm = input("Zadej jmeno: ")
uzivatel_pass = input("Zadej heslo: ")
cara = "-" * 40

if uzivatel_jm not in uzivatele:
    print("unregistered user, terminating the program..")
    quit()

elif uzivatel_pass != uzivatele[uzivatel_jm]:
    print("Invalid password, terminating the program..")
    quit()

else:
    print(
f"""username:{uzivatel_jm}
password:{uzivatel_pass}
{cara}
Welcome to the app, {uzivatel_jm}
We have 3 texts to be analyzed.
""", end=""
)

#################### výběr mezi 3 texty ####################

print(cara)
txt_cislo = (input("Enter a number btw. 1 and 3 to select: "))

if txt_cislo.isdigit():
    txt_cislo = int(txt_cislo)
    if 1 <= txt_cislo <= 3:
        pass
    else:
        print("Invalid number")
        quit()
else:
    print("Not a number")
    quit()

#################### statistiky ####################

vybrany_txt = TEXTS[txt_cislo - 1]
slova = vybrany_txt.split()

pocet_slov = len(slova)
pocet_vp = 0
pocet_vlkp = 0
pocet_mp = 0
pocet_cisel = 0
suma_cisel = 0

for vp in slova:
    if vp.istitle():
        pocet_vp += 1

for vlkp in slova:
    if vlkp.isupper():
        pocet_vlkp += 1

for mp in slova:
    if mp.islower():
        pocet_mp += 1

for cislo in slova:
    if cislo.isnumeric():
        pocet_cisel += 1

for suma in slova:
    if suma.isnumeric():
        suma_cisel += int(suma)

print(cara)
print(f"There are {pocet_slov} words in the selected text.")
print(f"There are {pocet_vp} titlecase words.")
print(f"There are {pocet_vlkp} uppercase words.")
print(f"There are {pocet_mp} lowercase words.")
print(f"There are {pocet_cisel} numeric strings.")
print(f"The sum of all the numbers {suma_cisel}")
print(cara)

#################### sloupcový graf // četnost různých délek slov v textu ####################

delka_slov = {}

print("LEN| OCCURENES     |NR.")
print(cara)

for slovo in slova:
    slovo_ciste = slovo.strip(".,")
    delka = len(slovo_ciste)
    delka_slov[delka] = delka_slov.get(delka, 0) + 1

for delka in sorted(delka_slov):
    pocet = delka_slov[delka]
    hvezdicky = "*" * pocet
    print(f"{delka:>3}|{hvezdicky:<15}|{pocet}")




    

    