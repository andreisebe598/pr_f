# ☕ Sistem de Management Cafenea

![Python Version](https://img.shields.io/badge/python-3.8%2B-blue)
![Status](https://img.shields.io/badge/status-active-success)
![License](https://img.shields.io/badge/license-MIT-green)

Un sistem complet de management pentru cafenele, dezvoltat în Python, care permite gestionarea clienților, angajaților, produselor, comenzilor și generarea de rapoarte financiare detaliate.

## 📋 Cuprins

- [Funcționalități Principale](#-funcționalități-principale)
- [Cerințe Sistem](#-cerințe-sistem)
- [Instalare](#-instalare)
- [Utilizare](#-utilizare)
- [Structura Proiectului](#-structura-proiectului)
- [Exemple](#-exemple)
- [Troubleshooting](#-troubleshooting)

## 🚀 Funcționalități Principale

### 👥 Gestionare Clienți
- ✅ Adăugare clienți noi cu informații complete
- ✅ Căutare clienți după ID sau nume
- ✅ Modificare date clienți existenți
- ✅ Ștergere clienți
- ✅ Vizualizare listă completă clienți
- ✅ Înregistrare băuturi preferate

### 👨‍💼 Gestionare Angajați
- ✅ Adăugare angajați cu detalii salariu și post
- ✅ Căutare angajați după diverse criterii
- ✅ Actualizare informații angajați
- ✅ Ștergere angajați din sistem
- ✅ Raportare performanță angajați

### 🍰 Gestionare Produse
- ✅ Catalog complet de produse (cafele, băuturi, dulciuri)
- ✅ Gestionare stoc și prețuri
- ✅ Adăugare produse noi
- ✅ Modificare detalii produse
- ✅ Tracking costuri achiziție vs preț vânzare

### 📦 Gestionare Comenzi
- ✅ Creare comenzi noi cu validare
- ✅ Asociere automată client-angajat
- ✅ Selecție multiplă produse
- ✅ Calcul automat total comandă
- ✅ Actualizare automată stoc
- ✅ Istoric complet comenzi

### 📊 Rapoarte Financiare
- ✅ Raport cheltuieli totale
- ✅ Raport încasări cu top produse
- ✅ Raport profit net și marjă
- ✅ Raport pe ultimul an
- ✅ Raport total complet
- ✅ Rapoarte personalizate pe perioadă
- ✅ Export rapoarte în JSON
- ✅ Statistici detaliate pe angajați și clienți

## 💻 Cerințe Sistem

### Software Necesar
- **Python**: 3.8 sau mai nou
- **Sistem de operare**: Windows, macOS, Linux

### Dependențe Python
```txt
colorama>=0.4.6
pathlib (inclus în Python 3.4+)
```

## 📥 Instalare

### Pasul 1: Clonare/Download Proiect
```bash
# Clonează repository-ul (dacă este pe Git)
git clone https://github.com/username/cafenea-management.git
cd cafenea-management

# SAU descarcă și extrage ZIP-ul
```

### Pasul 2: Instalare Dependențe
```bash
# Instalează colorama
pip install colorama

# SAU folosește requirements.txt (dacă există)
pip install -r requirements.txt
```

### Pasul 3: Verificare Structură
Asigură-te că ai următoarea structură de foldere:
```
proiect/
├── models/
├── commands/
├── json/          # Se va crea automat dacă nu există
└── main.py
```

### Pasul 4: Creare Directoare JSON (opțional)
```bash
mkdir -p json/rapoarte
```

## 🎮 Utilizare

### Rulare Aplicație
```bash
python main.py
```

### Meniu Principal
La rulare, vei vedea meniul principal cu opțiuni:
```
========================================
    SISTEM MANAGEMENT CAFENEA
========================================
1. Gestionare Clienti
2. Gestionare Angajati
3. Gestionare Produse
4. Gestionare Comenzi
5. Rapoarte Financiare
0. Iesire
========================================
```

### Flux de Lucru Recomandat

#### 1️⃣ Prima Utilizare
1. Adaugă angajați (Meniu 2)
2. Adaugă produse (Meniu 3)
3. Adaugă clienți (Meniu 1)
4. Creează comenzi (Meniu 4)
5. Generează rapoarte (Meniu 5)

#### 2️⃣ Utilizare Zilnică
1. Verifică stoc produse
2. Adaugă comenzi noi
3. Generează raport zilnic
4. Actualizează stoc după aprovizionare

## 📁 Structura Proiectului

```
proiect/
│
├── models/                      # 📦 Modele de date
│   ├── clienti.py              # Clasa Client
│   ├── angajati.py             # Clasa Angajat
│   ├── produse.py              # Clasa Produs
│   ├── comenzi.py              # Clasa Comanda
│   └── rapoarte.py             # Clasa Raport
│
├── commands/                    # 🎯 Logica de business
│   ├── comenzi_clienti.py      # Operațiuni clienți
│   ├── comenzi_angajati.py     # Operațiuni angajați
│   ├── comenzi_produse.py      # Operațiuni produse
│   ├── comenzi_comanda.py      # Operațiuni comenzi
│   └── comenzi_rapoarte.py     # Generare rapoarte
│
├── json/                        # 💾 Persistență date
│   ├── clienti.json            # Date clienți
│   ├── angajati.json           # Date angajați
│   ├── produse.json            # Date produse
│   ├── comenzi.json            # Date comenzi
│   └── rapoarte/               # Rapoarte salvate
│       ├── raport_cheltuieli.json
│       ├── raport_incasari.json
│       └── raport_profit.json
│
└── main.py                      # 🚀 Punct de intrare aplicație
```

### Descriere Module

#### 📦 Models (Modele de Date)
Conțin clasele simple de date cu metode `__str__`, `to_dict()`, `from_dict()`:
- **clienti.py**: Structura datelor pentru clienți
- **angajati.py**: Structura datelor pentru angajați
- **produse.py**: Structura datelor pentru produse
- **comenzi.py**: Structura datelor pentru comenzi
- **rapoarte.py**: Structura datelor pentru rapoarte

#### 🎯 Commands (Logica de Business)
Conțin toată logica aplicației, validări și operațiuni:
- **comenzi_clienti.py**: CRUD operațiuni pentru clienți
- **comenzi_angajati.py**: CRUD operațiuni pentru angajați
- **comenzi_produse.py**: CRUD operațiuni pentru produse
- **comenzi_comanda.py**: Gestionare comenzi complexe
- **comenzi_rapoarte.py**: Calcule și generare rapoarte

#### 💾 JSON (Persistență)
Fișiere JSON pentru salvarea permanentă a datelor

## 📸 Exemple

### Exemplu: Adăugare Client
```
--- Adaugare Client ---
Nume: Ion Popescu
Gen (Masculin, Feminin, Nespecificat): Masculin
Varsta: 28
Bautura preferata: Cappuccino

✓ Clientul Ion Popescu a fost adaugat cu succes!
```

### Exemplu: Creare Comandă
```
--- Adaugare comanda ---
ID-ul clientului: 1
ID-ul angajatului: 1
ID produs de adaugat (sau 'stop'): 1
Cantitatea dorita: 2
✓ Produs adaugat: Espresso - Cantitate: 2

ID produs de adaugat (sau 'stop'): stop
Data comenzii (YYYY-MM-DD sau 't' pentru azi): t

✓ Comanda #1 a fost adaugata cu succes!
```

### Exemplu: Raport Profit
```
--- Raport Profit ---

💰 REZUMAT FINANCIAR
----------------------------------------
Total incasari         1,500.00 RON
Total cheltuieli         800.00 RON
----------------------------------------
PROFIT NET              700.00 RON
Marja de profit (%)      46.67%

👥 Comenzi per Angajat:
Ion Popescu                     5
Maria Ionescu                   3
```

## 🔧 Troubleshooting

### ❌ Eroare: "ModuleNotFoundError: No module named 'colorama'"
**Soluție:**
```bash
pip install colorama
```

### ❌ Eroare: "FileNotFoundError: json/clienti.json"
**Soluție:**
Creează directorul `json/` în rădăcina proiectului:
```bash
mkdir json
mkdir json/rapoarte
```
Aplicația va crea automat fișierele JSON la prima utilizare.

### ❌ Eroare: "KeyError: 'id_angajat'"
**Soluție:**
Fișierele JSON au o structură veche. Șterge fișierele JSON și lasă aplicația să le recreeze:
```bash
rm json/*.json
```

### ❌ Meniul nu afișează culori
**Soluție:**
Pe Windows, colorama ar putea necesita inițializare suplimentară. Asigură-te că ai:
```python
from colorama import init
init(autoreset=True)
```

### ⚠️ Performanță lentă cu multe date
**Soluție:**
- Limitează numărul de comenzi afișate
- Arhivează comenzile vechi într-un fișier separat
- Folosește indexare pentru căutări rapide


## 📚 Documentație Suplimentară

- [📖 Documentație Tehnică](DOCUMENTATION.md) - Arhitectură și detalii tehnice
- [👤 User Guide](USER_GUIDE.md) - Ghid complet pentru utilizatori
- [👨‍💻 Developer Guide](DEVELOPER_GUIDE.md) - Ghid pentru dezvoltatori
- [📋 API Reference](API_REFERENCE.md) - Referință completă API

---

<div align="center">
  <p>Dezvoltat cu ❤️ pentru cafele și cod</p>
  <p>⭐ Dacă îți place proiectul, oferă-i un star!</p>
</div>