from models.comenzi import Comanda
from commands.comenzi_clienti import Comenzi_Clienti
from commands.comenzi_produse import Comenzi_Produse
from commands.comenzi_angajati import Comenzi_Angajati
from colorama import Fore, Style
import json
import datetime

class Comenzi_Comanda:
    def __init__(self, comenzi=None, produse = None, angajati = None, clienti=None):
        self.clienti = Comenzi_Clienti.citire_json("json/clienti.json")
        self.angajati = Comenzi_Angajati.incarcare_json("json/angajati.json")
        self.produse = Comenzi_Produse.incarcare_json("json/produse.json")

        self.comenzi = comenzi if comenzi is not None else self.incarcare_json("json/comenzi.json")

    # =================== Salvare informatii in fisier JSON ===================
    @staticmethod
    def salvare_json(filename, data):
        with open(filename, 'w', encoding="utf-8") as f:
            json.dump([comanda.to_dict() for comanda in data], f, indent=4, ensure_ascii=False)

    # =================== Incarcare informatii din fisier JSON ===================
    @staticmethod
    def incarcare_json(filename):
        try:
            with open(filename, 'r', encoding="utf-8") as f:
                data = json.load(f)
                return [Comanda.from_dict(comanda) for comanda in data]
        except FileNotFoundError:
            return []
        
    # =================== 1. Adaugare comanda ===================
    def adaugare_comanda(self):
        print(Fore.CYAN + Style.BRIGHT + "\n--- Adaugare comanda ---")
        try:
            id_comanda = len(self.comenzi) + 1
            id_client = int(input("ID-ul clientului: "))
            client = None
            for c in self.clienti:
                if c.id_client == id_client:
                    client = c
                    break
            if not client:
                print(Fore.RED + "Nu exista client cu acest ID.")
                return
            id_angajat = int(input("ID-ul angajatului: "))
            angajat = None
            for a in self.angajati:
                if a.id_angajat == id_angajat:
                    angajat = a
                    break
            if not angajat:
                print(Fore.RED + "Nu exista angajat cu acest ID.")
                return
            produse_selectate = []
            while True:
                id_produs = input("ID produs de adaugat (sau 'stop' pentru a termina): ")
                if id_produs.lower() == "stop":
                    break
                try:
                    id_produs = int(id_produs)
                    produs = next((p for p in self.produse if p.id_produs == id_produs), None)
                    if produs:
                        print(Fore.YELLOW + f"Produs selectat: {produs.denumire} - Stoc: {produs.cantitate}")
                        cantitate = int(input("Cantitatea dorita: "))
                        if cantitate <= 0:
                            print(Fore.RED + "Cantitatea trebuie sa fie un numar pozitiv.")
                            continue
                        if cantitate > produs.cantitate:
                            print(Fore.RED + "Cantitatea dorita depaseste stocul disponibil.")
                            continue

                        produs.cantitate -= cantitate

                        produse_selectate.append({
                            "produs": produs,
                            "cantitate": cantitate
                        })

                        print(Fore.GREEN + f"Produs adaugat cu succes: {produs.denumire} - Cantitate: {cantitate}")
                    else:
                        print(Fore.RED + "Nu exista produs cu acest ID.")
                except ValueError:
                    print(Fore.RED + "ID-ul trebuie sa fie un numar.")

            if not produse_selectate:
                print(Fore.RED + "Nu ai selectat niciun produs. Comanda anulata.")
                return

            # Data comenzii
            data = input("Data comenzii (YYYY-MM-DD) sau 't' pentru data actuala: ")
            if data.lower() == "t":
                data = datetime.datetime.now().strftime("%d %B %Y %H:%M:%S")

            # Creare comanda
            comanda = Comanda(id_comanda, client, angajat, produse_selectate, data)
            self.comenzi.append(comanda)
            self.salvare_json("json/comenzi.json", self.comenzi)
            Comenzi_Produse.salvare_json("json/produse.json", self.produse)

            print(Fore.GREEN + f"\nComanda #{id_comanda} a fost adaugata cu succes pentru clientul {client.nume}.")
        except ValueError:
            print(Fore.RED + "ID-ul trebuie sa fie un numar.")

    # =================== 2. Sterge comanda ===================
    def sterge_comanda(self):
        print(Fore.CYAN + Style.BRIGHT + "\n--- Stergere comanda ---")
        id_comanda = int(input("ID-ul comenzii de sters: "))
        comanda = next((c for c in self.comenzi if c.id_comanda == id_comanda), None)
        if comanda:
            self.comenzi.remove(comanda)
            self.salvare_json("json/comenzi.json", self.comenzi)
            print(Fore.GREEN + f"Comanda #{id_comanda} a fost stearsa cu succes.")
        else:
            print(Fore.RED + f"Comanda #{id_comanda} nu exista.")

    # =================== 3. Afisare comanda in functie de ID ===================
    def afisare_comanda(self):
        print(Fore.CYAN + Style.BRIGHT + "\n--- Afisare comanda in functie de ID ---")
        id_comanda = int(input("ID-ul comenzii de afisat: "))
        comanda = next((c for c in self.comenzi if c.id_comanda == id_comanda), None)
        if comanda:
            print(Fore.GREEN + f"\nComanda #{id_comanda}:")
            print(comanda)
        else:
            print(Fore.RED + f"Comanda #{id_comanda} nu exista.")

    # =================== 4. Afisare lista intreaga comenzi ===================
    def afisare_comenzi(self):
        print(Fore.CYAN + Style.BRIGHT + "\n--- Afisare lista intreaga comenzi ---")
        if not self.comenzi:
            print(Fore.RED + "Nu exista comenzi.")
        else:
            for comanda in self.comenzi:
                print(comanda)
