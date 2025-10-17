from models.angajati import Angajat
from colorama import Fore, Style
import json

class Comenzi_Angajati:
    functii_angajati = ["Casier","Barista", "Administrator", "Director"]

    def __init__(self, angajati=None):
        self.angajati = angajati if angajati else []

    # =================== Salvare informatii in fisier JSON ===================
    @staticmethod
    def salvare_json(filename, data):
        with open(filename, 'w', encoding="utf-8") as f:
            json.dump([angajat.to_dict() for angajat in data], f, indent=4, ensure_ascii=False)

    # =================== Incarcare informatii din fisier JSON ===================
    @staticmethod
    def incarcare_json(filename):
        angajati = []
        try:
            with open(filename, 'r', encoding="utf-8") as f:
                data = json.load(f)
                return [Angajat.from_dict(angajat_data) for angajat_data in data]
        except FileNotFoundError:
            print(Fore.RED + f"Fisierul {filename} nu exista.")
        return angajati 
    
    # =================== 1. Adaugare angajat ===================
    def adauga_angajat(self):
        print(Fore.CYAN + Style.BRIGHT + "\n--- Adaugare angajat ---")
        try:
            id = len(self.angajati) + 1
            nume = input("Numele angajatului: ")
            prenume = input("Prenumele angajatului: ")
            salariu = float(input("Salariul angajatului: "))
            post = input("Postul angajatului: ")

            if post not in self.functii_angajati:
                print(Fore.RED + "Postul trebuie sa fie una dintre urmatoarele: Casier, Barista, Administrator, Director")
                return

            angajat = Angajat(id, nume, prenume, salariu, post)
            self.angajati.append(angajat)
            self.salvare_json("json/angajati.json", self.angajati)
            print(Fore.GREEN + f"\nAngajatul {nume} {prenume} a fost adaugat cu succes!")
        except ValueError:
            print(Fore.RED + "Eroare: ID-ul trebuie sa fie un numar.")

    # =================== 2. Stergere angajat ===================
    def sterge_angajat(self):
        print(Fore.CYAN + Style.BRIGHT + "\n--- Stergere angajat ---")
        try:
            id = int(input("ID-ul angajatului de sters: "))
            angajat = next((a for a in self.angajati if a.id == id), None)
            if angajat:
                self.angajati.remove(angajat)
                self.salvare_json("json/angajati.json", self.angajati)
                print(Fore.GREEN + f"\nAngajatul #{id} a fost sters cu succes.")
            else:
                print(Fore.RED + "Eroare: Angajatul nu exista.")
        except ValueError:
            print(Fore.RED + "Eroare: ID-ul trebuie sa fie un numar.")

    # =================== 3. Cautare angajat in functie de ID ===================
    def cauta_angajat(self):
        print(Fore.CYAN + Style.BRIGHT + "\n--- Cautare angajat ---")
        try:
            id = int(input("ID-ul angajatului: "))
            angajat = next((a for a in self.angajati if a.id == id), None)
            if angajat:
                print(angajat)
            else:
                print(Fore.RED + "Eroare: Angajatul nu exista.")
        except ValueError:
            print(Fore.RED + "Eroare: ID-ul trebuie sa fie un numar.")

    # =================== 4. Cautare angajat in functie de nume ===================
    def cauta_angajat_nume(self):
        print(Fore.CYAN + Style.BRIGHT + "\n--- Cautare angajat ---")
        nume = input("Numele angajatului: ")
        angajat = next((a for a in self.angajati if a.nume == nume), None)
        if angajat:
            print(angajat)
        else:
            print(Fore.RED + "Eroare: Angajatul nu exista.")
    
    # =================== 5. Afisare angajati ===================
    def afisare_angajati(self):
        print(Fore.CYAN + Style.BRIGHT + "\n--- Lista angajati ---")
        if not self.angajati:
            print(Fore.RED + "Nu exista angajati inregistrati.")
        else:
            for angajat in self.angajati:
                print(angajat)
        
    # =================== 6. Modificare angajat ===================
    def modifica_angajat(self):
        print(Fore.CYAN + Style.BRIGHT + "\n--- Modificare angajat ---")
        try:
            id = int(input("ID-ul angajatului de modificat: "))
            angajat = next((a for a in self.angajati if a.id == id), None)
            if angajat:
                print("Datele angajatului (Apasa ENTER pentru a lasa aceleasi date):")
                print(angajat)
                print("Introduceti noile date:")
                nume = input("Numele angajatului: ")
                if not nume:
                    nume = angajat.nume
                prenume = input("Prenumele angajatului: ")
                if not prenume:
                    prenume = angajat.prenume
                salariu = float(input("Salariul angajatului: "))
                if not salariu:
                    salariu = angajat.salariu
                post = input("Postul angajatului: ")
                if not post:
                    post = angajat.post

                if post not in self.functii_angajati:
                    print(Fore.RED + "Postul trebuie sa fie una dintre urmatoarele: Casier, Barista, Administrator, Director")
                    return

                angajat.nume = nume
                angajat.prenume = prenume
                angajat.salariu = salariu
                angajat.post = post
                self.salvare_json("json/angajati.json", self.angajati)
                print(Fore.GREEN + f"\nAngajatul #{id} a fost modificat cu succes.")
            else:
                print(Fore.RED + "Eroare: Angajatul nu exista.")
        except ValueError:
            print(Fore.RED + "Eroare: ID-ul trebuie sa fie un numar.")