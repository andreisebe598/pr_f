# 📖 Documentație Tehnică - Sistem Management Cafenea

## 📋 Cuprins

1. [Arhitectura Sistemului](#arhitectura-sistemului)
2. [Design Patterns](#design-patterns)
3. [Structura Modulelor](#structura-modulelor)
4. [Structuri JSON](#structuri-json)
5. [Fluxuri de Date](#fluxuri-de-date)
6. [Best Practices](#best-practices)

---

## 🏗️ Arhitectura Sistemului

### Model-Command Pattern

Proiectul folosește **Model-Command Pattern** (o variantă a MVC) pentru separarea responsabilităților:

```
┌─────────────────────────────────────────────────────┐
│                    MAIN.PY                          │
│              (Interfață Utilizator)                 │
└────────────────────┬────────────────────────────────┘
                     │
                     ▼
┌─────────────────────────────────────────────────────┐
│                  COMMANDS/                          │
│            (Business Logic Layer)                   │
│  ┌──────────────────────────────────────────────┐  │
│  │ comenzi_clienti.py                           │  │
│  │ comenzi_angajati.py                          │  │
│  │ comenzi_produse.py                           │  │
│  │ comenzi_comanda.py                           │  │
│  │ comenzi_rapoarte.py                          │  │
│  └──────────────────┬───────────────────────────┘  │
└─────────────────────┼───────────────────────────────┘
                      │
                      ▼
┌─────────────────────────────────────────────────────┐
│                   MODELS/                           │
│              (Data Layer - DTOs)                    │
│  ┌──────────────────────────────────────────────┐  │
│  │ clienti.py    (Client)                       │  │
│  │ angajati.py   (Angajat)                      │  │
│  │ produse.py    (Produs)                       │  │
│  │ comenzi.py    (Comanda)                      │  │
│  │ rapoarte.py   (Raport)                       │  │
│  └──────────────────┬───────────────────────────┘  │
└─────────────────────┼───────────────────────────────┘
                      │
                      ▼
┌─────────────────────────────────────────────────────┐
│                    JSON/                            │
│           (Persistence Layer)                       │
│  ┌──────────────────────────────────────────────┐  │
│  │ clienti.json                                 │  │
│  │ angajati.json                                │  │
│  │ produse.json                                 │  │
│  │ comenzi.json                                 │  │
│  │ rapoarte/*.json                              │  │
│  └──────────────────────────────────────────────┘  │
└─────────────────────────────────────────────────────┘
```

### Separarea Responsabilităților

| Layer | Responsabilitate | Exemple |
|-------|------------------|---------|
| **Models** | Structuri de date simple (DTOs) | `Client`, `Angajat`, `Produs` |
| **Commands** | Logică business, validări, CRUD | `Comenzi_Clienti`, `Comenzi_Angajati` |
| **JSON** | Persistență date | Fișiere `.json` |
| **Main** | Interfață utilizator, meniuri | `main.py` |

---

## 🎨 Design Patterns

### 1. **Data Transfer Object (DTO) Pattern**

Toate clasele din `models/` sunt DTO-uri simple:

```python
class Client:
    def __init__(self, id_client, nume, gen, varsta, bautura_preferata):
        self.id_client = id_client
        self.nume = nume
        self.gen = gen
        self.varsta = varsta
        self.bautura_preferata = bautura_preferata
    
    def to_dict(self):
        # Serializare pentru JSON
        return {...}
    
    @staticmethod
    def from_dict(data):
        # Deserializare din JSON
        return Client(...)
```

**Avantaje:**
- ✅ Separare clară date vs logică
- ✅ Ușor de serializat/deserializat
- ✅ Testare simplificată

### 2. **Repository Pattern**

Clasele `Comenzi_*` acționează ca repository-uri:

```python
class Comenzi_Clienti:
    @staticmethod
    def salvare_json(file_path, data):
        # Salvare în persistență
        
    @staticmethod
    def citire_json(file_path):
        # Citire din persistență
```

**Avantaje:**
- ✅ Abstractizare persistență
- ✅ Ușor de schimbat baza de date (JSON → SQL)
- ✅ Operațiuni CRUD centralizate

### 3. **Factory Pattern** (Parțial)

Metodele `from_dict()` acționează ca factory methods:

```python
@staticmethod
def from_dict(data):
    return Client(
        data.get("id_client") or data.get("id"),
        data["nume"],
        # ...
    )
```

---

## 📦 Structura Modulelor

### Models Layer

#### `clienti.py` - Clasa Client

**Atribute:**
| Atribut | Tip | Descriere |
|---------|-----|-----------|
| `id_client` | int | Identificator unic |
| `nume` | str | Nume complet client |
| `gen` | str | Masculin/Feminin/Nespecificat |
| `varsta` | int | Vârsta clientului |
| `bautura_preferata` | str | Băutura preferată |

**Metode:**
- `__init__()` - Constructor
- `__str__()` - Reprezentare string
- `to_dict()` - Serializare JSON
- `from_dict(data)` - Deserializare JSON

#### `angajati.py` - Clasa Angajat

**Atribute:**
| Atribut | Tip | Descriere |
|---------|-----|-----------|
| `id_angajat` | int | Identificator unic |
| `nume` | str | Nume familie |
| `prenume` | str | Prenume |
| `salariu` | float | Salariu lunar |
| `post` | str | Poziție (Barista, Manager, etc.) |

#### `produse.py` - Clasa Produs

**Atribute:**
| Atribut | Tip | Descriere |
|---------|-----|-----------|
| `id_produs` | int | Identificator unic |
| `denumire` | str | Nume produs |
| `categorie` | str | Categorie (Cafele, Bauturi, etc.) |
| `pret_vanzare` | float | Preț vânzare către client |
| `cost_achizitie` | float | Cost achiziție |
| `cantitate` | int | Stoc disponibil |

#### `comenzi.py` - Clasa Comanda

**Atribute:**
| Atribut | Tip | Descriere |
|---------|-----|-----------|
| `id_comanda` | int | Identificator unic |
| `id_client` | int | ID client care a făcut comanda |
| `id_angajat` | int | ID angajat care a procesat |
| `produse` | list[dict] | Lista produse comandate |
| `data` | str | Data și ora comenzii |

**Structură produs în comandă:**
```python
{
    "produs": Produs,     # Obiect Produs
    "cantitate": int      # Cantitate comandată
}
```

#### `rapoarte.py` - Clasa Raport

**Atribute:**
| Atribut | Tip | Descriere |
|---------|-----|-----------|
| `perioada_start` | str | Data început perioadă |
| `perioada_end` | str | Data sfârșit perioadă |
| `numar_comenzi` | int | Total comenzi |
| `total_incasari` | float | Total vânzări |
| `total_cheltuieli` | float | Total costuri |
| `total_profit` | float | Profit net |

### Commands Layer

#### `comenzi_clienti.py` - Operațiuni Clienți

**Metode Principale:**
```python
def adaugare_client(self)           # Adaugă client nou
def sterge_client(self)             # Șterge client după ID
def cauta_client(self)              # Caută după ID
def cauta_client_nume(self)         # Caută după nume
def afisare_clienti(self)           # Afișează toți clienții
def modifica_date(self)             # Modifică date client
```

**Metode Statice:**
```python
@staticmethod
def salvare_json(file_path, data)   # Salvează în JSON
@staticmethod
def citire_json(file_path)          # Încarcă din JSON
```

#### `comenzi_produse.py` - Operațiuni Produse

**Atribute Clasă:**
```python
categorii_produse = ["Cafele", "Bauturi Calde", "Bauturi Reci", "Soft Drinks", "Dulciuri"]
cafele = ["Espresso", "Cappuccino", "Americano", ...]
bauturi_calde = ["Ciocolata calda", "Chai latte", ...]
# etc.
```

**Metode:**
- Operațiuni CRUD complete
- Validare categorii și produse
- Gestionare stoc

#### `comenzi_comanda.py` - Operațiuni Comenzi

**Caracteristici:**
- Validare existență client și angajat
- Selecție multiplă produse
- Verificare stoc disponibil
- Actualizare automată cantități
- Calcul total comandă

#### `comenzi_rapoarte.py` - Generare Rapoarte

**Metode Publice:**
```python
def afisare_cheltuieli(self)            # Raport cheltuieli
def afisare_incasari(self)              # Raport încasări + top produse
def afisare_profit(self)                # Raport profit + performanță
def afisare_raport_ultimul_an(self)     # Raport ultim an
def afisare_raport_total(self)          # Raport complet
def afisare_raport_personalizat(self)   # Raport perioadă custom
```

**Metode Helper (Private):**
```python
def _calculeaza_totale(comenzi)         # Calcule financiare
def _get_comenzi_per_angajat(comenzi)   # Statistici angajați
def _get_comenzi_per_client(comenzi)    # Statistici clienți
def _get_produse_vandute(comenzi)       # Statistici produse
def _get_top_produse(comenzi, top=5)    # Top N produse
def _parseaza_data(data_str)            # Parsing date
def _filtreaza_comenzi_perioada(...)    # Filtrare pe perioadă
```

---

## 📄 Structuri JSON

### clienti.json
```json
[
  {
    "id_client": 1,
    "nume": "Ion Popescu",
    "gen": "Masculin",
    "varsta": 28,
    "bautura_preferata": "Cappuccino"
  }
]
```

### angajati.json
```json
[
  {
    "id_angajat": 1,
    "nume": "Marinescu",
    "prenume": "Maria",
    "salariu": 3500.0,
    "post": "Barista"
  }
]
```

### produse.json
```json
[
  {
    "id_produs": 1,
    "denumire": "Espresso",
    "categorie": "Cafele",
    "pret_vanzare": 10.0,
    "cost_achizitie": 3.0,
    "cantitate": 100
  }
]
```

### comenzi.json
```json
[
  {
    "id_comanda": 1,
    "id_client": 1,
    "id_angajat": 1,
    "produse": [
      {
        "id_produs": 1,
        "denumire": "Espresso",
        "pret_vanzare": 10.0,
        "cost_achizitie": 3.0,
        "cantitate": 2
      }
    ],
    "data": "17 October 2025 14:30:00"
  }
]
```

### rapoarte/*.json
```json
{
  "perioada_start": "2025-01-01",
  "perioada_end": "2025-12-31",
  "numar_comenzi": 150,
  "total_incasari": 25000.0,
  "total_cheltuieli": 12000.0,
  "total_profit": 13000.0
}
```

---

## 🔄 Fluxuri de Date

### Flux Adăugare Comandă

```
┌──────────────┐
│  Utilizator  │
└──────┬───────┘
       │ introduce date
       ▼
┌────────────────────────────┐
│ comenzi_comanda.py         │
│ adaugare_comanda()         │
└──────┬─────────────────────┘
       │ validează client
       ▼
┌────────────────────────────┐
│ Verifică în clienti.json   │
└──────┬─────────────────────┘
       │ validează angajat
       ▼
┌────────────────────────────┐
│ Verifică în angajati.json  │
└──────┬─────────────────────┘
       │ validează produse
       ▼
┌────────────────────────────┐
│ Verifică stoc produse.json │
└──────┬─────────────────────┘
       │ actualizează stoc
       ▼
┌────────────────────────────┐
│ Actualizează produse.json  │
└──────┬─────────────────────┘
       │ salvează comandă
       ▼
┌────────────────────────────┐
│ Salvează în comenzi.json   │
└────────────────────────────┘
```

### Flux Generare Raport

```
┌──────────────┐
│  Utilizator  │
└──────┬───────┘
       │ selectează tip raport
       ▼
┌────────────────────────────┐
│ comenzi_rapoarte.py        │
│ afisare_*()                │
└──────┬─────────────────────┘
       │ încarcă comenzi
       ▼
┌────────────────────────────┐
│ Citește comenzi.json       │
└──────┬─────────────────────┘
       │ filtrează pe perioadă
       ▼
┌────────────────────────────┐
│ _filtreaza_comenzi_...()   │
└──────┬─────────────────────┘
       │ calculează totale
       ▼
┌────────────────────────────┐
│ _calculeaza_totale()       │
└──────┬─────────────────────┘
       │ afișează rezultate
       ▼
┌────────────────────────────┐
│ Console Output (colorat)   │
└──────┬─────────────────────┘
       │ (opțional) salvează
       ▼
┌────────────────────────────┐
│ json/rapoarte/*.json       │
└────────────────────────────┘
```

---

## ✅ Best Practices

### 1. Separarea Responsabilităților (SoC)
```python
# ❌ Greșit: Logică în model
class Client:
    def save_to_database(self):
        # Nu! Logica nu aparține modelului

# ✅ Corect: Model simplu, logică în Commands
class Client:
    def to_dict(self):
        return self.__dict__

class Comenzi_Clienti:
    def salvare_json(self, client):
        # Logica de salvare aici
```

### 2. Validare Date
```python
# Validare la nivel de Commands
def adaugare_produs(self):
    pret_vanzare = float(input("Pret vanzare: "))
    cost_achizitie = float(input("Cost achizitie: "))
    
    if pret_vanzare < cost_achizitie:
        print("Eroare: Pretul trebuie sa fie > costul")
        return
```

### 3. Gestionare Erori
```python
try:
    with open(file_path, 'r') as f:
        data = json.load(f)
except FileNotFoundError:
    print(f"Fisierul {file_path} nu exista")
    return []
except json.JSONDecodeError:
    print("Format JSON invalid")
    return []
```

### 4. Compatibilitate Backwards (from_dict)
```python
@staticmethod
def from_dict(data):
    # Suportă multiple formate de chei
    id_client = data.get("id_client") or data.get("id")
    bautura = data.get("bautura_preferata") or data.get("bautura_preferat")
    
    return Client(id_client, data["nume"], ...)
```

### 5. Metode Statice pentru Utilități
```python
class Comenzi_Rapoarte:
    @staticmethod
    def salvare_json(file_path, raport):
        # Poate fi apelată fără instanță
        with open(file_path, 'w') as f:
            json.dump(raport.to_dict(), f)
```

### 6. Naming Conventions
```python
# Classes: PascalCase
class Comenzi_Clienti:
    pass

# Methods: snake_case
def adaugare_client(self):
    pass

# Private methods: _snake_case
def _calculeaza_totale(self):
    pass

# Constants: UPPER_SNAKE_CASE
CATEGORII_PRODUSE = [...]
```

### 7. DRY Principle (Don't Repeat Yourself)
```python
# ❌ Greșit: Cod duplicat
def afisare_cheltuieli(self):
    total = 0
    for comanda in self.comenzi:
        for item in comanda.produse:
            total += item["produs"].cost_achizitie * item["cantitate"]

def afisare_incasari(self):
    total = 0
    for comanda in self.comenzi:
        for item in comanda.produse:
            total += item["produs"].pret_vanzare * item["cantitate"]

# ✅ Corect: Metodă reutilizabilă
def _calculeaza_totale(self, comenzi_lista):
    total_incasari = 0
    total_cheltuieli = 0
    for comanda in comenzi_lista:
        for item in comanda.produse:
            total_incasari += item["produs"].pret_vanzare * item["cantitate"]
            total_cheltuieli += item["produs"].cost_achizitie * item["cantitate"]
    return total_incasari, total_cheltuieli, total_incasari - total_cheltuieli
```

---

## 🔐 Securitate și Validări

### Input Validation
```python
# Validare vârstă
varsta = int(input("Varsta: "))
if varsta < 0 or varsta > 150:
    print("Varsta invalida")
    return

# Validare preț
if pret_vanzare < 0:
    print("Pretul nu poate fi negativ")
    return

# Validare categorie
if categorie not in self.categorii_produse:
    print("Categorie invalida")
    return
```

### Sanitization
```python
# Curățare input
nume = input("Nume: ").strip()
if not nume:
    print("Numele nu poate fi gol")
    return
```

---

## 📊 Performanță și Optimizări

### 1. Lazy Loading
```python
class Comenzi_Rapoarte:
    def __init__(self):
        # Încarcă doar când este necesar
        self.comenzi = None
        self.clienti = None
    
    def _load_comenzi(self):
        if self.comenzi is None:
            self.comenzi = Comenzi_Comanda.incarcare_json("json/comenzi.json")
```

### 2. Caching Rezultate
```python
# Pentru rapoarte frecvente
self._cache_raport_zilnic = None
self._cache_data = None

def get_raport_zilnic(self):
    azi = datetime.now().date()
    if self._cache_data == azi:
        return self._cache_raport_zilnic
    # Calculează și salvează în cache
```

### 3. Indexare pentru Căutări
```python
# Creează index pentru căutări rapide
self._index_clienti = {c.id_client: c for c in self.clienti}

# Căutare O(1) în loc de O(n)
client = self._index_clienti.get(id_client)
```

---

## 🧪 Testing Guidelines

### Unit Testing Structure
```python
import unittest
from models.clienti import Client

class TestClient(unittest.TestCase):
    def setUp(self):
        self.client = Client(1, "Test", "M", 25, "Espresso")
    
    def test_to_dict(self):
        expected = {
            "id_client": 1,
            "nume": "Test",
            "gen": "M",
            "varsta": 25,
            "bautura_preferata": "Espresso"
        }
        self.assertEqual(self.client.to_dict(), expected)
    
    def test_from_dict(self):
        data = {"id_client": 1, "nume": "Test", ...}
        client = Client.from_dict(data)
        self.assertEqual(client.nume, "Test")
```

### Integration Testing
```python
class TestComenziClienti(unittest.TestCase):
    def test_salvare_si_incarcare(self):
        # Creează client
        client = Client(1, "Test", "M", 25, "Espresso")
        
        # Salvează
        Comenzi_Clienti.salvare_json("test.json", [client])
        
        # Încarcă
        clienti = Comenzi_Clienti.citire_json("test.json")
        
        # Verifică
        self.assertEqual(len(clienti), 1)
        self.assertEqual(clienti[0].nume, "Test")
```

---

## 🔄 Migrare și Versioning

### Schema Versioning
```json
{
  "version": "1.0",
  "data": [...]
}
```

### Migration Scripts
```python
def migrate_v1_to_v2(old_data):
    """Migrează datele de la versiunea 1 la 2"""
    new_data = []
    for item in old_data:
        # Adaugă câmpuri noi
        item["email"] = None
        item["telefon"] = None
        new_data.append(item)
    return new_data
```

---

## 📈 Scalabilitate

### Considerații pentru Creștere

#### 1. Trecere la Bază de Date SQL
```python
# Structură actuală
class Comenzi_Clienti:
    @staticmethod
    def salvare_json(file_path, data):
        with open(file_path, 'w') as f:
            json.dump([c.to_dict() for c in data], f)

# Migrare la SQL (exemplu)
class Comenzi_Clienti:
    @staticmethod
    def salvare_db(data):
        conn = sqlite3.connect('cafenea.db')
        cursor = conn.cursor()
        for client in data:
            cursor.execute(
                "INSERT INTO clienti VALUES (?, ?, ?, ?, ?)",
                (client.id_client, client.nume, ...)
            )
        conn.commit()
```

#### 2. API REST
```python
# Transformare în API endpoint
from flask import Flask, jsonify

@app.route('/api/clienti', methods=['GET'])
def get_clienti():
    clienti = Comenzi_Clienti.citire_json("json/clienti.json")
    return jsonify([c.to_dict() for c in clienti])
```

#### 3. Paginare Rezultate
```python
def afisare_clienti(self, page=1, per_page=10):
    start = (page - 1) * per_page
    end = start + per_page
    clienti_pagina = self.clienti[start:end]
```

---

## 🛠️ Extensibilitate

### Adăugare Funcționalități Noi

#### 1. Noul Model
```python
# models/reduceri.py
class Reducere:
    def __init__(self, id_reducere, cod, procent, valabil_pana):
        self.id_reducere = id_reducere
        self.cod = cod
        self.procent = procent
        self.valabil_pana = valabil_pana
```

#### 2. Nou Command
```python
# commands/comenzi_reduceri.py
class Comenzi_Reduceri:
    def __init__(self):
        self.reduceri = self.incarcare_json("json/reduceri.json")
    
    def adaugare_reducere(self):
        # Implementare
        pass
```

#### 3. Integrare în Sistem
```python
# comenzi_comanda.py - modificare
def adaugare_comanda(self):
    # ... cod existent ...
    
    # Nou: Aplicare reducere
    cod_reducere = input("Cod reducere (Enter pentru skip): ")
    if cod_reducere:
        reducere = self.reduceri.get_reducere(cod_reducere)
        if reducere:
            total = total * (1 - reducere.procent / 100)
```

---

## 📱 Interfețe Alternative

### 1. GUI cu Tkinter
```python
import tkinter as tk
from tkinter import ttk

class CafeneaGUI:
    def __init__(self):
        self.root = tk.Tk()
        self.comenzi_clienti = Comenzi_Clienti()
        
    def create_widgets(self):
        # Butoane pentru operațiuni
        tk.Button(text="Adauga Client", 
                  command=self.show_add_client_dialog).pack()
```

### 2. Web Interface cu Flask
```python
from flask import Flask, render_template, request

app = Flask(__name__)
comenzi_clienti = Comenzi_Clienti()

@app.route('/clienti')
def clienti():
    clienti = comenzi_clienti.clienti
    return render_template('clienti.html', clienti=clienti)
```

---

## 🔍 Debugging și Logging

### Setup Logging
```python
import logging

logging.basicConfig(
    filename='cafenea.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

class Comenzi_Comanda:
    def adaugare_comanda(self):
        logging.info(f"Adaugare comanda pentru client {id_client}")
        try:
            # operațiuni
            logging.info(f"Comanda {id_comanda} adaugata cu succes")
        except Exception as e:
            logging.error(f"Eroare adaugare comanda: {e}")
```

### Debug Mode
```python
DEBUG = True

def debug_print(message):
    if DEBUG:
        print(f"[DEBUG] {message}")

# Utilizare
debug_print(f"Numar comenzi incarcate: {len(self.comenzi)}")
```

---

## 📚 Resurse Suplimentare

### Documentație Dependențe
- **Colorama**: https://pypi.org/project/colorama/
- **Pathlib**: https://docs.python.org/3/library/pathlib.html
- **JSON**: https://docs.python.org/3/library/json.html
- **Datetime**: https://docs.python.org/3/library/datetime.html

### Design Patterns
- **Repository Pattern**: https://martinfowler.com/eaaCatalog/repository.html
- **DTO Pattern**: https://martinfowler.com/eaaCatalog/dataTransferObject.html

### Python Best Practices
- **PEP 8**: https://peps.python.org/pep-0008/
- **PEP 257**: https://peps.python.org/pep-0257/ (Docstrings)

---

## 🎯 Viitor și Roadmap

### Funcționalități Planificate
- [ ] Sistem de autentificare utilizatori
- [ ] Backup automat date
- [ ] Export rapoarte PDF
- [ ] Notificări stoc scăzut
- [ ] Integrare plăți online
- [ ] Aplicație mobilă
- [ ] Dashboard analitică avansată
- [ ] Sistem de fidelizare clienți

### Îmbunătățiri Tehnice
- [ ] Migrare la PostgreSQL
- [ ] Implementare cache Redis
- [ ] API RESTful complet
- [ ] Unit tests 80%+ coverage
- [ ] CI/CD pipeline
- [ ] Docker containerization
- [ ] Kubernetes deployment

---

<div align="center">

**[⬅️ Înapoi la README](README.md)** | **[User Guide ➡️](USER_GUIDE.md)**

*Documentație tehnică v1.0 - Actualizat 17 Octombrie 2025*

</div>