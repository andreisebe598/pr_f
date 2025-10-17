from commands.comenzi_clienti import Comenzi_Clienti
from commands.comenzi_produse import Comenzi_Produse
from commands.comenzi_comanda import Comenzi_Comanda
from commands.comenzi_angajati import Comenzi_Angajati
from commands.comenzi_rapoarte import Comenzi_Rapoarte
from colorama import Fore, Style

manager_angajati = Comenzi_Angajati(Comenzi_Angajati.incarcare_json("json/angajati.json"))
manager_produse = Comenzi_Produse(Comenzi_Produse.incarcare_json("json/produse.json"))
manager_clienti = Comenzi_Clienti(Comenzi_Clienti.citire_json("json/clienti.json"))
manager_comenzi = Comenzi_Comanda(Comenzi_Comanda.incarcare_json("json/comenzi.json"))
manager_rapoarte = Comenzi_Rapoarte(Comenzi_Comanda.incarcare_json("json/comenzi.json"))

def Afisare_UI():
    print(Fore.GREEN + Style.BRIGHT +"\n=================== Meniu Cafenea ===================")
    print(Fore.BLUE + "1. Setari angajati")
    print(Fore.YELLOW + "2. Setari produse")
    print(Fore.RED + "3. Setari clienti")
    print(Fore.BLUE + "4. Setari comenzi")
    print(Fore.YELLOW + "5. Setari rapoarte")
    print(Fore.RED + "6. Iesire")

def Afisare_UI_Angajati():
    print(Fore.GREEN + Style.BRIGHT +"\n=================== Meniu Angajati ===================")
    print(Fore.BLUE + "1. Adauga angajat")
    print(Fore.YELLOW + "2. Sterge angajat")
    print(Fore.RED + "3. Afisare angajat in functie de ID")
    print(Fore.BLUE + "4. Afisare angajat in functie de nume")
    print(Fore.YELLOW + "5. Afisare lista intreaga angajati")
    print(Fore.RED + "6. Modificare date angajat")
    print(Fore.BLUE + "7. Inapoi")

def Meniu_Angajati():
    while True:
        Afisare_UI_Angajati()
        opt = int(input(Fore.CYAN + "\nSelecteaza o optiune: "))
        match opt:
            case 1:
                manager_angajati.adauga_angajat()
            case 2:
                manager_angajati.sterge_angajat()
            case 3:
                manager_angajati.cauta_angajat()
            case 4:
                manager_angajati.cauta_angajat_nume()
            case 5:
                manager_angajati.afisare_angajati()
            case 6:
                manager_angajati.modifica_angajat()
            case 7:
                break 
            case _:
                print(Fore.RED + "Introdu o optiune valida!")

def Afisare_UI_Produse():
    print(Fore.GREEN + Style.BRIGHT +"\n=================== Meniu Produse ===================")
    print(Fore.BLUE + "1. Adauga produs")
    print(Fore.YELLOW + "2. Sterge produs")
    print(Fore.RED + "3. Afisare produs in functie de ID")
    print(Fore.BLUE + "4. Afisare produs in functie de nume")
    print(Fore.YELLOW + "5. Afisare lista intreaga produse")
    print(Fore.RED + "6. Modificare date produs")
    print(Fore.BLUE + "7. Inapoi")

def Meniu_Produse():
    while True:
        Afisare_UI_Produse()
        opt = int(input(Fore.CYAN + "\nSelecteaza o optiune: "))
        match opt:
            case 1:
                manager_produse.adauga_produs()
            case 2:
                manager_produse.sterge_produs()
            case 3:
                manager_produse.cauta_produs()
            case 4:
                manager_produse.cauta_produs_nume()
            case 5:
                manager_produse.afisare_produse()
            case 6:
                manager_produse.modifica_date()
            case 7:
                break 
            case _:
                print(Fore.RED + "Introdu o optiune valida!")

def Afisare_UI_Clienti():
    print(Fore.GREEN + Style.BRIGHT +"\n=================== Meniu Clienti ===================")
    print(Fore.BLUE + "1. Adauga client")
    print(Fore.YELLOW + "2. Sterge client")
    print(Fore.RED + "3. Afisare client in functie de ID")
    print(Fore.BLUE + "4. Afisare client in functie de nume")
    print(Fore.YELLOW + "5. Afisare lista intreaga clienti")
    print(Fore.RED + "6. Modificare date client")
    print(Fore.BLUE + "7. Inapoi")

def Meniu_Clienti():
    while True:
        Afisare_UI_Clienti()
        opt = int(input(Fore.CYAN + "\nSelecteaza o optiune: "))
        match opt:
            case 1:
                manager_clienti.adaugare_client()
            case 2:
                manager_clienti.sterge_client()
            case 3:
                manager_clienti.afisare_client()
            case 4:
                manager_clienti.afisare_client_nume()
            case 5:
                manager_clienti.afisare_clienti()
            case 6:
                manager_clienti.modificare_date()
            case 7:
                break
            case _:
                print(Fore.RED + "Introdu o optiune valida!")

def Afisare_UI_Comenzi():
    print(Fore.GREEN + Style.BRIGHT +"\n=================== Meniu Comenzi ===================")
    print(Fore.BLUE + "1. Adauga comanda")
    print(Fore.YELLOW + "2. Sterge comanda")
    print(Fore.RED + "3. Afisare comanda in functie de ID")
    print(Fore.BLUE + "4. Afisare lista intreaga comenzi")
    print(Fore.RED + "5. Inapoi")

def Meniu_Comenzi():
    while True:
        Afisare_UI_Comenzi()
        opt = int(input(Fore.CYAN + "\nSelecteaza o optiune: "))
        match opt:
            case 1:
                manager_comenzi.adaugare_comanda()
            case 2:
                manager_comenzi.sterge_comanda()
            case 3:
                manager_comenzi.afisare_comanda()
            case 4:
                manager_comenzi.afisare_comenzi()
            case 5:
                break
            case _:
                print(Fore.RED + "Introdu o optiune valida!")

def Afisare_UI_Rapoarte():
    print(Fore.GREEN + Style.BRIGHT + "\n=================== Meniu Rapoarte ===================")
    print(Fore.BLUE + "1. Raport cheltuieli")
    print(Fore.YELLOW + "2. Raport incasari")
    print(Fore.RED + "3. Raport profit")
    print(Fore.BLUE + "4. Raport ultimul an")
    print(Fore.YELLOW + "5. Raport total")
    print(Fore.RED + "6. Raport personalizat")
    print(Fore.BLUE + "7. Inapoi")

def Meniu_Rapoarte():
    while True:
        Afisare_UI_Rapoarte()
        opt = int(input(Fore.CYAN + "\nSelecteaza o optiune: "))

        match opt:
            case 1:
                manager_rapoarte.afisare_cheltuieli()
            case 2:
                manager_rapoarte.afisare_incasari()
            case 3:
                manager_rapoarte.afisare_profit()
            case 4:
                manager_rapoarte.afisare_raport_ultimul_an()
            case 5:
                manager_rapoarte.afisare_raport_total()
            case 6:
                manager_rapoarte.afisare_raport_personalizat()
            case 7:
                break
            case _:
                print(Fore.RED + "Introdu o optiune valida!")

while True:
    Afisare_UI()
    optiune = int(input(Fore.CYAN + "\nSelecteaza o optiune: "))

    match optiune:
        case 1:
            Meniu_Angajati()
        case 2:
            Meniu_Produse()
        case 3:
            Meniu_Clienti()
        case 4:
            Meniu_Comenzi()
        case 5:
            Meniu_Rapoarte()
        case 6:
            print(Fore.RED + Style.BRIGHT + "La revedere!")
            break;
        case _:
            print(Fore.RED + "Introdu o optiune valida!")