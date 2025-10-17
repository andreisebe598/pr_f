from models.produse import Produs
from colorama import Style, Fore
import json
from colorama import Fore

class Comenzi_Produse:
    categorii_produse = ["Cafele", "Bauturi Calde", "Bauturi Reci", "Soft Drinks", "Dulciuri"]

    cafele = ["Espresso", "Espresso Lung", "Espresso Decaf", "Espresso Nachiatto", "Espresso Con Panna", "Americano", "Cappuccino", "Caffe Latte", "Flat White"]
    bauturi_calde = ["Ciocolata calda", "Chai latte", "Ceai"]
    bauturi_reci = ["Iced Coffee", "Greek Frappe", "Ness Frappe", "Espresso Tonic", "Milkshake", "Smoothie"]
    soft_drinks = ["Coca-Cola", "Fanta", "Sprite", "Pepsi", "Apa Plata", "Apa Minerala", "RedBull"]
    dulciuri = ["Negresa", "Fursec American", "Briosa", "Biscuite cu ovaz", "Mini Croissant", "Biscuiti Vegani", "Salam de Biscuiti", "Arahide", "Ciocolata de Casa"]

    def __init__(self, produse=None):
        self.produse = produse if produse else []

    # =================== Salvare informatii in fisier JSON ===================
    @staticmethod
    def salvare_json(file_path, data):
        with open(file_path, "w") as f:
            json.dump([p.__dict__ for p in data], f, indent=4)

    # =================== Incarcare informatii din fisier JSON ===================
    @staticmethod
    def incarcare_json(file_path):
        produse = []
        try:
            with open(file_path, "r") as f:
                data = json.load(f)
                produse = []
                for p in data:
                    produs = Produs(
                        id_produs=p["id_produs"],
                        denumire=p["denumire"],
                        categorie=p.get("categorie", ""),
                        pret_vanzare=p.get("pret_vanzare", 0),
                        cost_achizitie=p.get("cost_achizitie", 0),
                        cantitate=p.get("cantitate", 1)
                    )
                    produse.append(produs)
                return produse
        except FileNotFoundError:
            print(f"Fisierul {file_path} nu exista.")
        return produse
    
    # =================== 1. Adauga Produs ===================
    def adauga_produs(self):

        print(Fore.CYAN + Style.BRIGHT + "\n--- Adauga produs ---")
        id = len(self.produse) + 1
        nume = input("Nume produs: ")
        if nume not in self.cafele + self.bauturi_calde + self.bauturi_reci + self.soft_drinks + self.dulciuri:
            print(Fore.RED + "Eroare: Produsul nu exista in lista de produse.")
            return
        categorie = input("Categorie produsului: ")
        if categorie not in self.categorii_produse:
            print(Fore.RED + "Eroare: Categorie invalida.")
            return
        cost_achizitie = float(input("Costul de achizitie: "))
        if cost_achizitie < 0:
            print(Fore.RED + "Eroare: Costul de achizitie nu poate fi negativ.")
            return
        pret_vanzare = float(input("Pretul de vanzare: "))
        if pret_vanzare < cost_achizitie:
            print(Fore.RED + "Eroare: Pretul de vanzare trebuie sa fie mai mare ca pretul de achizitie.")
            return
        cantitate = int(input("Cantitatea: "))
        if cantitate < 0:
            print(Fore.RED + "Eroare: Cantitatea nu poate fi negativa.")
            return

        id = max([p.id for p in self.produse], default=0) + 1
        produs = Produs(id, nume, categorie,pret_vanzare, cost_achizitie, cantitate)
        self.produse.append(produs)
        self.salvare_json("json/produse.json", self.produse)
        print(Fore.GREEN + f"\nProdusul '{nume}' a fost adaugat cu succes.")
    
    # =================== 2. Sterge Produs ===================
    def sterge_produs(self):
        print(Fore.CYAN + Style.BRIGHT + "\n--- Sterge produs ---")
        try:
            id = int(input("ID produs: "))
            produs = next((p for p in self.produse if p.id == id), None)
            if produs:
                self.produse.remove(produs)
                self.salvare_json("json/produse.json", self.produse)
                print(Fore.GREEN + f"\nProdusul '{produs.nume}' a fost sters cu succes.")
            else:
                print(Fore.RED + "Eroare: Produsul nu exista.")
        except ValueError:
            print(Fore.RED + "Eroare: ID-ul trebuie sa fie un numar.")

    # =================== 3. Cauta produs in functie de ID ===================
    def cauta_produs(self):
        print(Fore.CYAN + Style.BRIGHT + "\n--- Cauta produs ---")
        try:
            id = int(input("ID produs: "))
            produs = next((p for p in self.produse if p.id == id), None)
            if produs:
                print(produs)
            else:
                print(Fore.RED + "Eroare: Produsul nu exista.")
        except ValueError:
            print(Fore.RED + "Eroare: ID-ul trebuie sa fie un numar.")

    # =================== 4. Cauta produs in functie de nume ===================
    def cauta_produs_nume(self):
        print(Fore.CYAN + Style.BRIGHT + "\n--- Cauta produs ---")
        nume = input("Nume produs: ")
        produs = next((p for p in self.produse if p.nume == nume), None)
        if produs:
            print(produs)
        else:
            print(Fore.RED + "Eroare: Produsul nu exista.")

    # =================== 5. Afiseaza toate produsele ===================
    def afisare_produse(self):
        print(Fore.CYAN + Style.BRIGHT + "\n--- Lista Produse ---")
        if not self.produse:
            print(Fore.RED + "Nu exista produse inregistrate.")
        else:
            for produs in self.produse:
                print(produs)

    # =================== 6. Modificare date produse ===================
    def modifica_date(self):
        print(Fore.CYAN + Style.BRIGHT + "\n--- Modificare date produs ---")
        try:
            id = int(input("ID produs: "))
            produs = next((p for p in self.produse if p.id == id), None)
            if produs:
                print("Datele produsului (Apasa ENTER pentru a lasa aceleasi date):")
                print(produs)
                print("Introduceti noile date:")
                nume = input("Nume: ")
                if not nume:
                    nume = produs.nume
                if nume not in self.cafele + self.bauturi_calde + self.bauturi_reci + self.soft_drinks + self.dulciuri:
                    print(Fore.RED + "Eroare: Produsul nu exista in lista de produse.")
                    return
                categorie = input("Categorie: ")
                if not categorie:
                    categorie = produs.categorie
                if categorie not in self.categorii_produse:
                    print(Fore.RED + "Eroare: Categorie invalida.")
                    return
                cost_achizitie = float(input("Costul de achizitie: "))
                if not cost_achizitie:
                    cost_achizitie = produs.cost_achizitie
                if cost_achizitie < 0:
                    print(Fore.RED + "Eroare: Costul de achizitie nu poate fi negativ.")
                    return
                pret_vanzare = float(input("Pretul de vanzare: "))
                if not pret_vanzare:
                    pret_vanzare = produs.pret_vanzare
                if pret_vanzare < cost_achizitie:
                    print(Fore.RED + "Eroare: Pretul de vanzare trebuie sa fie mai mare ca pretul de achizitie.")
                    return
                cantitate = int(input("Cantitatea: "))
                if not cantitate:
                    cantitate = produs.cantitate
                if cantitate < 0:
                    print(Fore.RED + "Eroare: Cantitatea nu poate fi negativa.")
                    return

                produs.nume = nume
                produs.categorie = categorie
                produs.cost_achizitie = cost_achizitie
                produs.pret_vanzare = pret_vanzare
                produs.cantitate = cantitate

                self.salvare_json("json/produse.json", self.produse)
                print(Fore.GREEN + f"\nDatele produsului #{id} au fost modificate cu succes.")
        except ValueError:
            print(Fore.RED + "Eroare: ID-ul trebuie sa fie un numar.")



    
