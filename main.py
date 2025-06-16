"""
projekt_1.py: první projekt do Engeto Online Python Akademie

author: Pavol Medo
email: palimedo@gmail.com
"""
TEXTS = [
    """Situated about 10 miles west of Kemmerer,
    Fossil Butte is a ruggedly impressive
    topographic feature that rises sharply
    some 1000 feet above Twin Creek Valley
    to an elevation of more than 7500 feet
    above sea level. The butte is located just
    north of US 30 and the Union Pacific Railroad,
    which traverse the valley.""",
    """At the base of Fossil Butte are the bright
    red, purple, yellow and gray beds of the Wasatch
    Formation. Eroded portions of these horizontal
    beds slope gradually upward from the valley floor
    and steepen abruptly. Overlying them and extending
    to the top of the butte are the much steeper
    buff-to-white beds of the Green River Formation,
    which are about 300 feet thick.""",
    """The monument contains 8198 acres and protects
    a portion of the largest deposit of freshwater fish
    fossils in the world. The richest fossil fish deposits
    are found in multiple limestone layers, which lie some
    100 feet below the top of the butte. The fossils
    represent several varieties of perch, as well as
    other freshwater genera and herring similar to those
    in modern oceans. Other fish such as paddlefish,
    garpike and stingray are also present."""
]

#################### přihlašovací jméno a heslo ####################

uzivatele = {"Petr": "123",
             "Pavel": "heslo123",
             "Michal": "heslo124",
             "Lenka": "hes123"
}

uzivatel_jmeno = input("Zadej jmeno: ")
uzivatel_heslo = input("Zadej heslo: ")
cara = "-" * 44

if uzivatel_jmeno not in uzivatele:
    print("Neregistrovaný uživatel, ukončuji program..")
    quit()

elif uzivatel_heslo != uzivatele[uzivatel_jmeno]:
    print("Nesprávné heslo, ukončuji program..")
    quit()

else:
    print(
f"""uživatel:{uzivatel_jmeno}
heslo:{uzivatel_heslo}
{cara}
Vítej v aplikaci, {uzivatel_jmeno}
Máme k analýze 3 texty.
""", end=""
)
    
print(cara)

#################### výběr mezi 3 texty ####################

while True:
    txt_cislo = input("Zadej číslo mezi 1 a 3 pro výběr: ")
    
    if not txt_cislo.isdigit():
        print("Není číslo")
        continue
    
    txt_cislo = int(txt_cislo)
    
    if not 1 <= txt_cislo <= 3:
        print("Nesprávné číslo")
        continue
    
    break

#################### statistiky ####################

vybrany_txt = TEXTS[txt_cislo - 1]
slova = vybrany_txt.split()

pocet_slov = len(slova)
pocet_zacatecni_pismena = 0
pocet_velka_pismena = 0
pocet_mala_pismena = 0
pocet_cisel = 0
suma_cisel = 0

for slovo in slova:
    if slovo.istitle():
        pocet_zacatecni_pismena += 1
    
    if slovo.isupper():
        pocet_velka_pismena += 1
    
    if slovo.islower():
        pocet_mala_pismena += 1
    
    if slovo.isnumeric():
        pocet_cisel += 1
        suma_cisel += int(slovo)

print(cara)
print(f"Počet slov: {pocet_slov}")
print(f"Počet slov začínajících velkým písmenem: {pocet_zacatecni_pismena}")
print(f"Počet slov psaných velkými písmeny: {pocet_velka_pismena}")
print(f"Počet slov psaných malými písmeny: {pocet_mala_pismena}")
print(f"Počet čísel: {pocet_cisel}")
print(f"Suma všech čísel: {suma_cisel}")
print(cara)

#################### sloupcový graf // četnost různých délek slov v textu ####################

delka_slov = {}

print(f"{"DÉLKA":>5} | {"VÝSKYT":<17}| {"ČÍSLO":<5}")
print(cara)

for slovo in slova:
    slovo_ciste = slovo.strip(".,")
    delka = len(slovo_ciste)
    delka_slov[delka] = delka_slov.get(delka, 0) + 1

for delka in sorted(delka_slov):
    pocet = delka_slov[delka]
    hvezdicky = "*" * pocet
    print(f"{delka:>5} | {hvezdicky:<17}| {pocet:<5}")




    

    