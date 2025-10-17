from models.rapoarte import Raport
from commands.comenzi_comanda import Comenzi_Comanda
from commands.comenzi_clienti import Comenzi_Clienti
from commands.comenzi_angajati import Comenzi_Angajati
from colorama import Fore, Style, init
from datetime import datetime, timedelta
import json
from pathlib import Path

init(autoreset=True)

class Comenzi_Rapoarte:
    def __init__(self, comenzi=None, clienti=None, angajati=None):
        self.comenzi = comenzi if comenzi else Comenzi_Comanda.incarcare_json("json/comenzi.json")
        self.clienti = clienti if clienti else Comenzi_Clienti.citire_json("json/clienti.json")
        self.angajati = angajati if angajati else Comenzi_Angajati.incarcare_json("json/angajati.json")
    
    @staticmethod
    def salvare_json(file_path, raport):
        with open(file_path, 'w', encoding='utf-8') as f:
            json.dump(raport.to_dict(), f, indent=4, ensure_ascii=False)
        print(Fore.GREEN + f"Raportul a fost salvat in '{file_path}'")
    
    @staticmethod
    def incarcare_json(file_path):
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                data = json.load(f)
                return Raport.from_dict(data)
        except FileNotFoundError:
            print(Fore.RED + f"Fisierul {file_path} nu a fost gasit.")
            return None
    
    def _calculeaza_totale(self, comenzi_lista):
        total_incasari = 0
        total_cheltuieli = 0
        
        for comanda in comenzi_lista:
            for item in comanda.produse:
                produs = item["produs"]
                cantitate = item["cantitate"]
                total_incasari += produs.pret_vanzare * cantitate
                total_cheltuieli += produs.cost_achizitie * cantitate
        
        total_profit = total_incasari - total_cheltuieli
        return total_incasari, total_cheltuieli, total_profit
    
    def _get_comenzi_per_angajat(self, comenzi_lista):
        comenzi_per_angajat = {}
        for comanda in comenzi_lista:
            id_angajat = comanda.id_angajat
            if id_angajat not in comenzi_per_angajat:
                comenzi_per_angajat[id_angajat] = 0
            comenzi_per_angajat[id_angajat] += 1
        return comenzi_per_angajat
    
    def _get_comenzi_per_client(self, comenzi_lista):
        comenzi_per_client = {}
        for comanda in comenzi_lista:
            id_client = comanda.id_client
            if id_client not in comenzi_per_client:
                comenzi_per_client[id_client] = 0
            comenzi_per_client[id_client] += 1
        return comenzi_per_client
    
    def _get_produse_vandute(self, comenzi_lista):
        produse_vandute = {}
        for comanda in comenzi_lista:
            for item in comanda.produse:
                produs = item["produs"]
                cantitate = item["cantitate"]
                
                id_produs = produs.id_produs
                if id_produs not in produse_vandute:
                    produse_vandute[id_produs] = {
                        "denumire": produs.denumire,
                        "cantitate": 0,
                        "incasari": 0
                    }
                
                produse_vandute[id_produs]["cantitate"] += cantitate
                produse_vandute[id_produs]["incasari"] += produs.pret_vanzare * cantitate
        
        return produse_vandute
    
    def _get_top_produse(self, comenzi_lista, top=5):
        produse = self._get_produse_vandute(comenzi_lista)
        sorted_produse = sorted(produse.items(), key=lambda x: x[1]["cantitate"], reverse=True)
        return sorted_produse[:top]
    
    def _parseaza_data(self, data_str):
        formate = [
            "%d %B %Y %H:%M:%S",
            "%Y-%m-%d",
            "%d/%m/%Y",
            "%d-%m-%Y"
        ]
        
        for fmt in formate:
            try:
                return datetime.strptime(data_str, fmt)
            except (ValueError, TypeError):
                continue
        return None
    
    def _filtreaza_comenzi_perioada(self, data_start=None, data_end=None):
        comenzi_filtrate = []
        
        for comanda in self.comenzi:
            data_comanda = self._parseaza_data(comanda.data)
            
            if data_comanda is None:
                continue
            
            if data_start is None and data_end is None:
                comenzi_filtrate.append(comanda)
                continue
            
            if data_start and data_comanda < data_start:
                continue
            if data_end and data_comanda > data_end:
                continue
                
            comenzi_filtrate.append(comanda)
        
        return comenzi_filtrate
    
    # =================== 1. Afișare Cheltuieli ===================
    def afisare_cheltuieli(self):
        print(Fore.CYAN + Style.BRIGHT + "\n--- Raport Cheltuieli ---")
        
        total_incasari, total_cheltuieli, total_profit = self._calculeaza_totale(self.comenzi)
        numar_comenzi = len(self.comenzi)
        
        print(f"\n{'Descriere':<40} {'Valoare (RON)':>15}")
        print("-" * 56)
        print(f"{'Total cheltuieli (costuri achizitie)':<40} {Fore.RED}{total_cheltuieli:>14.2f}")
        print(f"{'Numar comenzi procesate':<40} {numar_comenzi:>15}")
        
        if numar_comenzi > 0:
            medie_cheltuieli = total_cheltuieli / numar_comenzi
            print(f"{'Cheltuieli medii per comanda':<40} {medie_cheltuieli:>14.2f}")
        
        print(Fore.YELLOW + "\n💡 Acestea sunt costurile de achizitie pentru produsele vandute.")
        
        salvare = input(Fore.YELLOW + "\nDoresti sa salvezi acest raport? (da/nu): ").strip().lower()
        if salvare in ['da', 'd', 'yes', 'y']:
            Path("json/reports").mkdir(parents=True, exist_ok=True)
            raport = Raport(None, None, numar_comenzi, total_incasari, total_cheltuieli, total_profit)
            self.salvare_json("json/reports/raport_cheltuieli.json", raport)
    
    def afisare_incasari(self):
        print(Fore.CYAN + Style.BRIGHT + "\n--- Raport Incasari ---")
        
        total_incasari, total_cheltuieli, total_profit = self._calculeaza_totale(self.comenzi)
        numar_comenzi = len(self.comenzi)
        
        print(f"\n{'Descriere':<40} {'Valoare (RON)':>15}")
        print("-" * 56)
        print(f"{'Total incasari (vanzari)':<40} {Fore.GREEN}{total_incasari:>14.2f}")
        print(f"{'Numar comenzi procesate':<40} {numar_comenzi:>15}")
        
        if numar_comenzi > 0:
            medie_incasari = total_incasari / numar_comenzi
            print(f"{'Valoare medie per comanda':<40} {medie_incasari:>14.2f}")
        
        print(Fore.CYAN + Style.BRIGHT + "\nTop 5 Produse Vandute:")
        top_produse = self._get_top_produse(self.comenzi, 5)
        
        if top_produse:
            print(f"\n{'Produs':<30} {'Cantitate':>12} {'Incasari (RON)':>15}")
            print("-" * 58)
            for id_produs, info in top_produse:
                print(f"{info['denumire']:<30} {info['cantitate']:>12} {Fore.GREEN}{info['incasari']:>14.2f}")
        else:
            print(Fore.YELLOW + "Nu exista date disponibile.")
        
        salvare = input(Fore.YELLOW + "\nDoresti sa salvezi acest raport? (da/nu): ").strip().lower()
        if salvare in ['da', 'd', 'yes', 'y']:
            Path("json/reports").mkdir(parents=True, exist_ok=True)
            raport = Raport(None, None, numar_comenzi, total_incasari, total_cheltuieli, total_profit)
            self.salvare_json("json/reports/raport_incasari.json", raport)
    
    def afisare_profit(self):
        print(Fore.CYAN + Style.BRIGHT + "\n--- Raport Profit ---")
        
        total_incasari, total_cheltuieli, total_profit = self._calculeaza_totale(self.comenzi)
        numar_comenzi = len(self.comenzi)
        
        print(f"\n{'Descriere':<40} {'Valoare (RON)':>15}")
        print("-" * 56)
        print(f"{'Total incasari':<40} {Fore.GREEN}{total_incasari:>14.2f}")
        print(f"{'Total cheltuieli':<40} {Fore.RED}{total_cheltuieli:>14.2f}")
        print("-" * 56)
        
        culoare_profit = Fore.GREEN if total_profit >= 0 else Fore.RED
        print(f"{'PROFIT NET':<40} {culoare_profit}{Style.BRIGHT}{total_profit:>14.2f}")
        
        if total_incasari > 0:
            marja_profit = (total_profit / total_incasari) * 100
            print(f"{'Marja de profit (%)':<40} {marja_profit:>14.2f}%")
        
        print(f"\n{'Numar comenzi procesate':<40} {numar_comenzi:>15}")
        
        if numar_comenzi > 0:
            profit_mediu = total_profit / numar_comenzi
            print(f"{'Profit mediu per comanda':<40} {profit_mediu:>14.2f}")
        
        print(Fore.CYAN + Style.BRIGHT + "\nComenzi per Angajat: ")
        comenzi_angajati = self._get_comenzi_per_angajat(self.comenzi)
        
        if comenzi_angajati:
            print(f"\n{'Angajat':<40} {'Nr. Comenzi':>15}")
            print("-" * 56)
            
            for id_angajat, nr_comenzi in sorted(comenzi_angajati.items(), key=lambda x: x[1], reverse=True):
                angajat = next((a for a in self.angajati if a.id_angajat == id_angajat), None)
                nume_angajat = f"{angajat.nume} {angajat.prenume}" if angajat else f"ID: {id_angajat}"
                print(f"{nume_angajat:<40} {nr_comenzi:>15}")
        
        salvare = input(Fore.YELLOW + "\nDoresti sa salvezi acest raport? (da/nu): ").strip().lower()
        if salvare in ['da', 'd', 'yes', 'y']:
            Path("json/reports").mkdir(parents=True, exist_ok=True)
            raport = Raport(None, None, numar_comenzi, total_incasari, total_cheltuieli, total_profit)
            self.salvare_json("json/reports/raport_profit.json", raport)
    
    def afisare_raport_ultimul_an(self):
        print(Fore.CYAN + Style.BRIGHT + "\n--- Raport Ultimul An ---")
        
        data_end = datetime.now()
        data_start = data_end - timedelta(days=365)
        
        print(Fore.YELLOW + f"Perioada: {data_start.strftime('%d/%m/%Y')} - {data_end.strftime('%d/%m/%Y')}")
        
        comenzi_filtrate = self._filtreaza_comenzi_perioada(data_start, data_end)
        
        total_incasari, total_cheltuieli, total_profit = self._calculeaza_totale(comenzi_filtrate)
        numar_comenzi = len(comenzi_filtrate)
        
        print(f"\n{'Indicator':<40} {'Valoare':>15}")
        print("-" * 56)
        print(f"{'Numar comenzi':<40} {numar_comenzi:>15}")
        print(f"{'Total incasari (RON)':<40} {Fore.GREEN}{total_incasari:>14.2f}")
        print(f"{'Total cheltuieli (RON)':<40} {Fore.RED}{total_cheltuieli:>14.2f}")
        
        culoare_profit = Fore.GREEN if total_profit >= 0 else Fore.RED
        print(f"{'Profit net (RON)':<40} {culoare_profit}{total_profit:>14.2f}")
        
        if numar_comenzi > 0:
            medie_comanda = total_incasari / numar_comenzi
            print(f"{'Valoare medie comanda (RON)':<40} {medie_comanda:>14.2f}")
        
        salvare = input(Fore.YELLOW + "\nDoresti sa salvezi acest raport? (da/nu): ").strip().lower()
        if salvare in ['da', 'd', 'yes', 'y']:
            Path("json/reports").mkdir(parents=True, exist_ok=True)
            raport = Raport(
                data_start.strftime('%d/%m/%Y'),
                data_end.strftime('%d/%m/%Y'),
                numar_comenzi,
                total_incasari,
                total_cheltuieli,
                total_profit
            )
            self.salvare_json("json/reports/raport_ultimul_an.json", raport)
    
    def afisare_raport_total(self):

        print(Fore.CYAN + Style.BRIGHT + "\n--- Raport Total - Toate Comenzile ---")
        
        if len(self.comenzi) == 0:
            print(Fore.YELLOW + "\n Nu exista comenzi in sistem.")
            return
        
        total_incasari, total_cheltuieli, total_profit = self._calculeaza_totale(self.comenzi)
        numar_comenzi = len(self.comenzi)

        print(Fore.CYAN + Style.BRIGHT + "\n--- Rezumat ---")
        print("-" * 56)
        print(f"{'Indicator':<40} {'Valoare':>15}")
        print("-" * 56)
        print(f"{'Total incasari (RON)':<40} {Fore.GREEN}{total_incasari:>14.2f}")
        print(f"{'Total cheltuieli (RON)':<40} {Fore.RED}{total_cheltuieli:>14.2f}")
        
        culoare_profit = Fore.GREEN if total_profit >= 0 else Fore.RED
        print(f"{'Profit net (RON)':<40} {culoare_profit}{Style.BRIGHT}{total_profit:>14.2f}")
        
        if total_incasari > 0:
            marja = (total_profit / total_incasari) * 100
            print(f"{'Marja de profit (%)':<40} {marja:>14.2f}%")
        
        print(Fore.CYAN + Style.BRIGHT + "\n--- Statistici Comenzi ---")
        print("-" * 56)
        print(f"{'Numar total comenzi':<40} {numar_comenzi:>15}")
        medie_comanda = total_incasari / numar_comenzi if numar_comenzi > 0 else 0
        print(f"{'Valoare medie comanda (RON)':<40} {medie_comanda:>14.2f}")

        print(Fore.CYAN + Style.BRIGHT + "\n--- Top 5 produse ---")
        print("-" * 70)
        top_produse = self._get_top_produse(self.comenzi, 5)
        
        if top_produse:
            print(f"{'Produs':<35} {'Cantitate':>12} {'Incasari (RON)':>18}")
            print("-" * 70)
            for id_produs, info in top_produse:
                print(f"{info['denumire']:<35} {info['cantitate']:>12} {Fore.GREEN}{info['incasari']:>17.2f}")
        
        print(Fore.CYAN + Style.BRIGHT + "\n--- Top 5 Clienti (dupa numar de comenzi) ---")
        print("-" * 56)
        comenzi_clienti = self._get_comenzi_per_client(self.comenzi)
        
        if comenzi_clienti:
            top_clienti = sorted(comenzi_clienti.items(), key=lambda x: x[1], reverse=True)[:5]
            print(f"{'Client':<40} {'Nr. Comenzi':>15}")
            print("-" * 56)
            
            for id_client, nr_comenzi_client in top_clienti:
                client = next((c for c in self.clienti if c.id_client == id_client), None)
                nume_client = client.nume if client else f"ID: {id_client}"
                print(f"{nume_client:<40} {nr_comenzi_client:>15}")
        
        print(Fore.CYAN + Style.BRIGHT + "\n--- Raport Angajati ---")
        print("-" * 56)
        comenzi_angajati = self._get_comenzi_per_angajat(self.comenzi)
        
        if comenzi_angajati:
            print(f"{'Angajat':<40} {'Nr. Comenzi':>15}")
            print("-" * 56)
            
            for id_angajat, nr_comenzi_angajat in sorted(comenzi_angajati.items(), key=lambda x: x[1], reverse=True):
                angajat = next((a for a in self.angajati if a.id_angajat == id_angajat), None)
                nume_angajat = f"{angajat.nume} {angajat.prenume}" if angajat else f"ID: {id_angajat}"
                print(f"{nume_angajat:<40} {nr_comenzi_angajat:>15}")
        
        salvare = input(Fore.YELLOW + "\nDoresti sa salvezi acest raport? (da/nu): ").strip().lower()
        if salvare in ['da', 'd', 'yes', 'y']:
            Path("json/reports").mkdir(parents=True, exist_ok=True)
            raport = Raport(None, None, numar_comenzi, total_incasari, total_cheltuieli, total_profit)
            self.salvare_json("json/reports/raport_total.json", raport)
    
    def afisare_raport_personalizat(self):
        print(Fore.CYAN + Style.BRIGHT + "\n--- Raport Personalizat ---")
        print(Fore.YELLOW + "Formatul datei: YYYY-MM-DD (ex: 2025-01-01)")
        print(Fore.YELLOW + "Lasa gol pentru a include toate comenzile.")
        
        data_start_str = input("\nData de inceput: ").strip()
        data_end_str = input("Data de sfarsit: ").strip()
        
        data_start = None
        data_end = None
        
        if data_start_str:
            data_start = self._parseaza_data(data_start_str)
            if not data_start:
                print(Fore.RED + "Formatul datei de inceput este invalid!")
                return
        
        if data_end_str:
            data_end = self._parseaza_data(data_end_str)
            if not data_end:
                print(Fore.RED + "Formatul datei de sfarsit este invalid!")
                return
            data_end = data_end.replace(hour=23, minute=59, second=59)
        
        print(Fore.YELLOW + f"\nPerioara: {data_start_str if data_start_str else 'Inceput'} - {data_end_str if data_end_str else 'Prezent'}")
        
        comenzi_filtrate = self._filtreaza_comenzi_perioada(data_start, data_end)
        
        if len(comenzi_filtrate) == 0:
            print(Fore.YELLOW + "\n Nu exista comenzi pentru perioada selectata.")
            return
        
        total_incasari, total_cheltuieli, total_profit = self._calculeaza_totale(comenzi_filtrate)
        numar_comenzi = len(comenzi_filtrate)
        
        print(f"\n{'Indicator':<40} {'Valoare':>15}")
        print("-" * 56)
        print(f"{'Numar comenzi':<40} {numar_comenzi:>15}")
        print(f"{'Total incasari (RON)':<40} {Fore.GREEN}{total_incasari:>14.2f}")
        print(f"{'Total cheltuieli (RON)':<40} {Fore.RED}{total_cheltuieli:>14.2f}")
        
        culoare_profit = Fore.GREEN if total_profit >= 0 else Fore.RED
        print(f"{'Profit net (RON)':<40} {culoare_profit}{total_profit:>14.2f}")
        
        if numar_comenzi > 0:
            medie_comanda = total_incasari / numar_comenzi
            print(f"{'Valoare medie comanda (RON)':<40} {medie_comanda:>14.2f}")
        
        salvare = input(Fore.YELLOW + "\nDoresti sa salvezi acest raport? (da/nu): ").strip().lower()
        if salvare in ['da', 'd', 'yes', 'y']:
            Path("json/reports").mkdir(parents=True, exist_ok=True)
            raport = Raport(
                data_start_str if data_start_str else None,
                data_end_str if data_end_str else None,
                numar_comenzi,
                total_incasari,
                total_cheltuieli,
                total_profit
            )
            nume_fisier = input(Fore.CYAN + "Nume fisier (Enter pentru 'raport_personalizat.json'): ").strip()
            if not nume_fisier:
                nume_fisier = "raport_personalizat.json"
            if not nume_fisier.endswith('.json'):
                nume_fisier += '.json'
            
            self.salvare_json(f"json/reports/{nume_fisier}", raport)