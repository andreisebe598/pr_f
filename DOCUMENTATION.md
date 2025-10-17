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

###