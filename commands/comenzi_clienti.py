from models.clienti import Client
from colorama import Fore, Back, Style
import json

lista_genuri = ["masculin", "feminin", "nespecificat"]
lista_bauturi = []

class Comenzi_Clienti():
    def __init__(self, clienti=None):
        self.clienti = clienti if clienti else []

    # =================== Salvare informatii in fisier JSON ===================

    @staticmethod
    def salvare_json(filename, data):
        with open(filename, 'w', encoding="utf-8") as f:
            json.dump([client.to_dict() for client in data], f, indent=4, ensure_ascii=False)

    # =================== Citire informatii din fisier JSON ===================
    @staticmethod
    def citire_json(filename):
        clienti = []
        try:
            with open(filename, 'r', encoding="utf-8") as f:
                data = json.load(f)
                for a in data:
                    clienti.append(Client.from_dict(a))
        except FileNotFoundError:
            print(Fore.RED + f"Fisierul {filename} nu exista.")
        return clienti
    
    # =================== 1. Adaugare client ===================
    def adaugare_client(self):
        print(Fore.CYAN + Style.BRIGHT + "\n--- Adaugare client ---")
        try:
            id = len(self.clienti) + 1
            nume = input("Nume: ")
            gen = input("Gen (Masculin, Feminin, Nespecificat): ")
            if gen.lower() not in lista_genuri:
                print(Fore.RED + "Eroare: Genul trebuie sa fie masculin, feminin sau nespecificat!")
                return
            varsta = int(input("Varsta: "))
            if varsta < 0 or varsta > 100:
                print(Fore.RED + "Eroare: Varsta trebuie sa fie una reala!")
                return
            bautura_preferata = input("Bautura preferata: ")

            client = Client(id, nume, gen, varsta, bautura_preferata)
            self.clienti.append(client)
            self.salvare_json("json/clienti.json", self.clienti)
            print(Fore.GREEN + f"\nClientul {nume} a fost adaugat cu succes!")
        except ValueError:
            print(Fore.RED + "Eroare: ID-ul trebuie sa fie un numar.")

    # =================== 2. Stergere client ===================
    def sterge_client(self):
        print(Fore.CYAN + Style.BRIGHT + "\n--- Stergere client ---")
        try:
            id = int(input("ID-ul clientului de sters: "))
            client = next((c for c in self.clienti if c.id_client == id), None)
            if client:
                self.clienti.remove(client)
                self.salvare_json("json/clienti.json", self.clienti)
                print(Fore.GREEN + f"\nClientul #{id} a fost sters cu succes.")
            else:
                print(Fore.RED + "Eroare: Clientul nu exista.")
        except ValueError:
            print(Fore.RED + "Eroare: ID-ul trebuie sa fie un numar.")

    # =================== 3. Afisare client in functie de ID ===================
    def afisare_client(self):
        print(Fore.CYAN + Style.BRIGHT + "\n--- Afisare client in functie de ID ---")
        try:
            id = int(input("ID-ul clientului: "))
            client = next((c for c in self.clienti if c.id_client == id), None)
            if client:
                print(client)
            else:
                print(Fore.RED + "Eroare: Clientul nu exista.")
        except ValueError:
            print(Fore.RED + "Eroare: ID-ul trebuie sa fie un numar.")
    
    # =================== 4. Afisare client in functie de nume ===================
    def afisare_client_nume(self):
        print(Fore.CYAN + Style.BRIGHT + "\n--- Afisare client in functie de nume ---")
        try:
            nume = input("Numele clientului: ")
            client = next((c for c in self.clienti if c.nume == nume), None)
            if client:
                print(client)
            else:
                print(Fore.RED + "Eroare: Clientul nu exista.")
        except ValueError:
            print("Eroare: Numele trebuie sa fie un sir de caractere")

    # =================== 5. Afisare lista clienti ===================
    def afisare_clienti(self):
        print(Fore.CYAN + Style.BRIGHT + "\n--- Lista clienti ---")
        if not self.clienti:
            print(Fore.RED + "Nu exista clienti inregistrati.")
        else:
            for client in self.clienti:
                print(client)

    # =================== 6. Modificare date client ===================
    def modificare_date(self):
        print(Fore.CYAN + Style.BRIGHT + "\n--- Modificare date client ---")
        try:
            id = int(input("ID-ul clientului: "))
            client = next((c for c in self.clienti if c.id_client == id), None)
            if client:
                print("Datele clientului (Apasa ENTER pentru a lasa aceleasi date):")
                print(client)
                print("Introduceti noile date:")
                nume = input("Nume: ")
                if not nume:
                    nume = client.nume
                gen = input("Gen (Masculin, Feminin, Nespecificat): ")
                if not gen:
                    gen = client.gen
                if gen.lower() not in lista_genuri:
                    print(Fore.RED + "Eroare: Genul trebuie sa fie masculin, feminin sau nespecificat!")
                    return
                varsta = int(input("Varsta: "))
                if not varsta:
                    varsta = client.varsta
                if varsta < 0 or varsta > 100:
                    print(Fore.RED + "Eroare: Varsta trebuie sa fie una reala!")
                    return
                bautura_preferata = input("Bautura preferata: ")

                client.nume = nume
                client.gen = gen
                client.varsta = varsta
                client.bautura_preferat = bautura_preferata

                self.salvare_json("json/clienti.json", self.clienti)
                print(Fore.GREEN + f"\nDatele clientului #{id} au fost modificate cu succes.")
            else:
                print(Fore.RED + "Eroare: Clientul nu exista.")
        except Exception as e:
            print(Fore.RED + f"Eroare: {e}")

            