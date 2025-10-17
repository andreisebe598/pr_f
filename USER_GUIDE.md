# 👤 User Guide - Sistem Management Cafenea

## 📋 Cuprins

1. [Introducere](#introducere)
2. [Primii Pași](#primii-pași)
3. [Gestionare Clienți](#-gestionare-clienți)
4. [Gestionare Angajați](#-gestionare-angajați)
5. [Gestionare Produse](#-gestionare-produse)
6. [Gestionare Comenzi](#-gestionare-comenzi)
7. [Rapoarte Financiare](#-rapoarte-financiare)
8. [Scenarii Practice](#-scenarii-practice)
9. [Întrebări Frecvente (FAQ)](#-întrebări-frecvente)
10. [Sfaturi și Trucuri](#-sfaturi-și-trucuri)

---

## 📖 Introducere

Bine ai venit! Acest ghid te va ajuta să folosești sistemul de management pentru cafenea pas cu pas. Nu sunt necesare cunoștințe tehnice - totul este explicat simplu și clar.

### Ce Poți Face cu Acest Sistem?

✅ **Ține evidența clienților** tăi și preferințelor lor  
✅ **Gestionează angajații** și salariile acestora  
✅ **Administrează stocul** de produse  
✅ **Procesează comenzi** rapid și eficient  
✅ **Generează rapoarte** financiare detaliate  

---

## 🚀 Primii Pași

### Pornirea Aplicației

1. **Deschide terminalul/cmd** în folderul proiectului
2. **Rulează comanda:**
   ```bash
   python main.py
   ```
3. **Vei vedea meniul principal:**

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

### Prima Configurare

Pentru început, urmează acești pași în ordine:

#### 📝 Pasul 1: Adaugă Angajații
```
Selectează: 2 (Gestionare Angajati)
Apoi: 1 (Adaugare angajat)
```

#### 📦 Pasul 2: Adaugă Produsele
```
Selectează: 3 (Gestionare Produse)
Apoi: 1 (Adaugare produs)
```

#### 👥 Pasul 3: Adaugă Clienții
```
Selectează: 1 (Gestionare Clienti)
Apoi: 1 (Adaugare client)
```

#### 🛒 Pasul 4: Creează Prima Comandă
```
Selectează: 4 (Gestionare Comenzi)
Apoi: 1 (Adaugare comanda)
```

---

## 👥 Gestionare Clienți

### 1️⃣ Adăugare Client Nou

**Pași:**

1. Selectează `1` din meniul principal
2. Selectează `1` (Adaugare client)
3. Completează informațiile:

```
--- Adaugare Client ---
Nume: Ion Popescu
Gen (Masculin, Feminin, Nespecificat): Masculin
Varsta: 28
Bautura preferata: Cappuccino
```

**💡 Sfat:** Scrie băutura preferată exact cum apare în meniu pentru recomandări viitoare!

**✅ Rezultat:**
```
✓ Clientul Ion Popescu a fost adaugat cu succes!
```

### 2️⃣ Căutare Client

**După ID:**
```
Selectează: 2 (Cauta client)
ID client: 1

Rezultat:
1: Ion Popescu -> (Masculin, 28) - Bautura Preferata: Cappuccino
```

**După Nume:**
```
Selectează: 3 (Cauta client dupa nume)
Nume client: Ion Popescu
```

### 3️⃣ Modificare Date Client

```
Selectează: 5 (Modificare date)
ID client: 1

Datele clientului (Apasa ENTER pentru a lasa aceleasi date):
1: Ion Popescu -> (Masculin, 28) - Bautura Preferata: Cappuccino

Introduceti noile date:
Nume: [Enter pentru păstrare]
Gen: [Enter pentru păstrare]
Varsta: 29
Bautura preferata: Espresso

✓ Datele clientului #1 au fost modificate cu succes.
```

**⚠️ Notă:** Dacă apeși Enter fără să scrii nimic, valoarea rămâne neschimbată!

### 4️⃣ Ștergere Client

```
Selectează: 4 (Sterge client)
ID client: 1

✓ Clientul 'Ion Popescu' a fost sters cu succes.
```

⚠️ **ATENȚIE:** Ștergerea este permanentă! Verifică ID-ul înainte de confirmare.

### 5️⃣ Vizualizare Toți Clienții

```
Selectează: 6 (Afisare clienti)

--- Lista Clienti ---
1: Ion Popescu -> (Masculin, 28) - Bautura Preferata: Cappuccino
2: Maria Ionescu -> (Feminin, 32) - Bautura Preferata: Latte
3: Alex Georgescu -> (Nespecificat, 25) - Bautura Preferata: Americano
```

---

## 👨‍💼 Gestionare Angajați

### 1️⃣ Adăugare Angajat

```
--- Adaugare angajat ---
Nume: Popescu
Prenume: Ion
Salariu: 3500
Post: Barista

✓ Angajatul Ion Popescu a fost adaugat cu succes!
```

**📝 Posturi comune:**
- Barista
- Manager
- Casier
- Ospătar
- Bucătar

### 2️⃣ Căutare Angajat

**După ID:**
```
Selectează: 2 (Cauta angajat)
ID angajat: 1

1. Nume: Popescu Ion - Salariu: 3500 - Post: Barista
```

**După Nume:**
```
Selectează: 3 (Cauta angajat dupa nume)
Nume angajat: Popescu

1. Nume: Popescu Ion - Salariu: 3500 - Post: Barista
```

### 3️⃣ Modificare Date Angajat

Similar cu modificarea clienților - apasă Enter pentru a păstra valorile existente.

```
Selectează: 5 (Modificare date)
ID angajat: 1

Salariu: 3800  # Creștere salariu
Post: [Enter]  # Păstrează postul actual
```

### 4️⃣ Ștergere Angajat

```
Selectează: 4 (Sterge angajat)
ID angajat: 1

✓ Angajatul 'Ion Popescu' a fost sters cu succes.
```

---

## 🍰 Gestionare Produse

### 1️⃣ Adăugare Produs

```
--- Adauga produs ---
Nume produs: Espresso
Categorie produsului: Cafele
Costul de achizitie: 3.00
Pretul de vanzare: 10.00
Cantitatea: 100

✓ Produsul 'Espresso' a fost adaugat cu succes.
```

### 📋 Categorii Disponibile

| Categorie | Exemple de Produse |
|-----------|-------------------|
| **Cafele** | Espresso, Cappuccino, Americano, Latte |
| **Bauturi Calde** | Ciocolata calda, Chai latte, Ceai |
| **Bauturi Reci** | Iced Coffee, Frappe, Milkshake, Smoothie |
| **Soft Drinks** | Coca-Cola, Fanta, Sprite, Apa |
| **Dulciuri** | Negresa, Croissant, Briosa, Biscuiti |

### 📊 Liste Complete Produse

**Cafele:**
- Espresso
- Espresso Lung
- Espresso Decaf
- Espresso Macchiato
- Espresso Con Panna
- Americano
- Cappuccino
- Caffe Latte
- Flat White

**Bauturi Calde:**
- Ciocolata calda
- Chai latte
- Ceai

**Bauturi Reci:**
- Iced Coffee
- Greek Frappe
- Ness Frappe
- Espresso Tonic
- Milkshake
- Smoothie

**Soft Drinks:**
- Coca-Cola
- Fanta
- Sprite
- Pepsi
- Apa Plata
- Apa Minerala
- RedBull

**Dulciuri:**
- Negresa
- Fursec American
- Briosa
- Biscuite cu ovaz
- Mini Croissant
- Biscuiti Vegani
- Salam de Biscuiti
- Arahide
- Ciocolata de Casa

### 2️⃣ Verificare Stoc

```
Selectează: 5 (Afisare produse)

--- Lista Produse ---
Produs(ID: 1, Denumire: Espresso, Pret: 10.0, Stoc: 100)
Produs(ID: 2, Denumire: Cappuccino, Pret: 15.0, Stoc: 80)
```

**💡 Sfat:** Verifică stocul zilnic pentru a evita rupturi!

### 3️⃣ Actualizare Stoc

```
Selectează: 6 (Modificare date produs)
ID produs: 1

Cantitatea: 150  # Stoc nou după aprovizionare
```

### 4️⃣ Modificare Prețuri

```
Selectează: 6 (Modificare date produs)
ID produs: 1

Pretul de vanzare: 12.00  # Preț nou
```

⚠️ **Important:** Prețul de vânzare trebuie să fie mai mare decât costul de achiziție!

---

## 📦 Gestionare Comenzi

### 1️⃣ Creare Comandă Nouă

**Pași Detalați:**

```
--- Adaugare comanda ---

1. ID-ul clientului: 1
   ✓ Client găsit: Ion Popescu

2. ID-ul angajatului: 1
   ✓ Angajat găsit: Maria Ionescu (Barista)

3. Adăugare produse:
   
   ID produs de adaugat (sau 'stop'): 1
   Produs selectat: Espresso - Stoc: 100
   Cantitatea dorita: 2
   ✓ Produs adaugat: Espresso - Cantitate: 2
   
   ID produs de adaugat (sau 'stop'): 3
   Produs selectat: Croissant - Stoc: 50
   Cantitatea dorita: 1
   ✓ Produs adaugat: Croissant - Cantitate: 1
   
   ID produs de adaugat (sau 'stop'): stop

4. Data comenzii (YYYY-MM-DD sau 't' pentru azi): t

✓ Comanda #1 a fost adaugata cu succes pentru clientul Ion Popescu.
```

### ⚠️ Validări Automate

Sistemul verifică automat:
- ✅ Clientul există în sistem
- ✅ Angajatul există în sistem  
- ✅ Produsele există în inventar
- ✅ Stocul este suficient
- ✅ Cantitatea este pozitivă

**Exemplu de eroare:**
```
ID-ul clientului: 999
✗ Nu exista client cu acest ID.
```

### 2️⃣ Efecte Comandă

După plasarea comenzii:
- ✅ Stocul produselor scade automat
- ✅ Comanda este salvată în istoric
- ✅ Data și ora sunt înregistrate
- ✅ Asocierea client-angajat este salvată

---

## 📊 Rapoarte Financiare

### 1️⃣ Raport Cheltuieli

**Ce afișează:**
- Total cheltuieli (costuri achiziție)
- Număr comenzi procesate
- Cheltuieli medii per comandă

```
--- Raport Cheltuieli ---

Descriere                              Valoare (RON)
--------------------------------------------------------
Total cheltuieli (costuri achizitie)          800.25
Numar comenzi procesate                           10
Cheltuieli medii per comanda                   80.03

💡 Acestea sunt costurile de achizitie pentru produsele vandute.
```

### 2️⃣ Raport Încasări

**Ce afișează:**
- Total încasări (vânzări)
- Număr comenzi
- Valoare medie per comandă
- **Top 5 produse vândute**

```
--- Raport Incasari ---

Descriere                              Valoare (RON)
--------------------------------------------------------
Total incasari (vanzari)                    1,500.50
Numar comenzi procesate                           10
Valoare medie per comanda                     150.05

📈 Top 5 Produse Vandute:
Produs                      Cantitate    Incasari (RON)
----------------------------------------------------------
Espresso                           25            250.00
Cappuccino                         20            300.00
Croissant                          15            120.00
Americano                          12            120.00
Latte                              10            150.00
```

### 3️⃣ Raport Profit

**Ce afișează:**
- Total încasări
- Total cheltuieli
- **Profit net**
- Marjă de profit (%)
- Profit mediu per comandă
- **Performanță angajați**

```
--- Raport Profit ---

Descriere                              Valoare (RON)
--------------------------------------------------------
Total incasari                              1,500.50
Total cheltuieli                              800.25
--------------------------------------------------------
PROFIT NET                                    700.25
Marja de profit (%)                            46.68%

Numar comenzi procesate                           10
Profit mediu per comanda                       70.03

👥 Comenzi per Angajat:
Angajat                                 Nr. Comenzi
--------------------------------------------------------
Popescu Ion                                       6
Ionescu Maria                                     4
```

**💡 Interpretare:**
- **Marjă > 40%** = Foarte bine! 🎉
- **Marjă 30-40%** = Bine ✅
- **Marjă < 30%** = Atenție! Verifică prețurile ⚠️

### 4️⃣ Raport Ultimul An

Afișează toate datele pentru ultimele 365 de zile.

```
--- Raport Ultimul An ---
Perioada: 17/10/2024 - 17/10/2025

Indicator                                  Valoare
--------------------------------------------------------
Numar comenzi                                      150
Total incasari (RON)                         25,000.00
Total cheltuieli (RON)                       12,000.00
Profit net (RON)                             13,000.00
Valoare medie comanda (RON)                     166.67
```

### 5️⃣ Raport Total

**Cel mai complet raport** cu:
- Rezumat financiar complet
- Statistici comenzi
- Top 5 produse vândute
- Top 5 clienți fideli
- Performanță toți angajații

```
--- Raport Total - Toate Comenzile ---

💰 REZUMAT FINANCIAR
--------------------------------------------------------
Total incasari (RON)                         50,000.00
Total cheltuieli (RON)                       25,000.00
Profit net (RON)                             25,000.00
Marja de profit (%)                              50.00%

📦 STATISTICI COMENZI
--------------------------------------------------------
Numar total comenzi                                300
Valoare medie comanda (RON)                     166.67

🏆 TOP 5 PRODUSE VANDUTE
----------------------------------------------------------------------
Produs                          Cantitate       Incasari (RON)
----------------------------------------------------------------------
Espresso                              150                1,500.00
Cappuccino                            120                1,800.00
Americano                             100                1,000.00

👤 TOP 5 CLIENTI (dupa numar de comenzi)
--------------------------------------------------------
Client                                      Nr. Comenzi
--------------------------------------------------------
Ion Popescu                                          25
Maria Ionescu                                        20
Alex Georgescu                                       15

👥 PERFORMANTA ANGAJATI
--------------------------------------------------------
Angajat                                     Nr. Comenzi
--------------------------------------------------------
Popescu Ion                                          80
Ionescu Maria                                        70
Vasilescu George                                     50
```

### 6️⃣ Raport Personalizat

**Creează raport pentru orice perioadă:**

```
--- Raport Personalizat ---
Formatul datei: YYYY-MM-DD (ex: 2025-01-01)
Lasa gol pentru a include toate comenzile.

Data de inceput: 2025-10-01
Data de sfarsit: 2025-10-15

Perioada: 2025-10-01 - 2025-10-15

Indicator                                  Valoare
--------------------------------------------------------
Numar comenzi                                       25
Total incasari (RON)                          4,000.00
Total cheltuieli (RON)                        2,000.00
Profit net (RON)                              2,000.00
Valoare medie comanda (RON)                     160.00
```

### 💾 Salvare Rapoarte

După fiecare raport, poți salva rezultatele:

```
Doresti sa salvezi acest raport? (da/nu): da

✓ Raportul a fost salvat in 'json/rapoarte/raport_profit.json'
```

**Fișiere salvate automat:**
- `raport_cheltuieli.json`
- `raport_incasari.json`
- `raport_profit.json`
- `raport_ultimul_an.json`
- `raport_total.json`
- `raport_personalizat.json` (nume custom)

---

## 🎯 Scenarii Practice

### Scenariul 1: Deschiderea Zilei

```
1. Verifică stocul produselor (Meniu 3 → 5)
2. Pregătește produsele necesare
3. Înregistrează angajații prezenți
4. Gata de comenzi!
```

### Scenariul 2: Client Nou

```
1. Adaugă clientul (Meniu 1 → 1)
   - Notează băutura preferată
2. Creează prima comandă (Meniu 4 → 1)
3. Oferă reducere pentru prima comandă (viitor)
```

### Scenariul 3: Aprovizionare Stoc

```
1. Generează raport încasări (Meniu 5 → 2)
2. Vezi ce produse se vând mai bine
3. Actualizează stocul (Meniu 3 → 6)
   - Adaugă cantitate mare pentru produse populare
```

### Scenariul 4: Închiderea Zilei

```
1. Generează raport profit zilnic:
   - Raport personalizat (Meniu 5 → 6)
   - Data: azi - azi
2. Salvează raportul
3. Verifică performanța angajaților
4. Planifică ziua următoare
```

### Scenariul 5: Raport Lunar

```
1. Raport personalizat (Meniu 5 → 6)
2. Data de început: 2025-10-01
3. Data de sfârșit: 2025-10-31
4. Salvează raportul pentru contabilitate
5. Analizează:
   - Produse profitabile
   - Clienți fideli
   - Angajați performanți
```

---

## ❓ Întrebări Frecvente

### Q1: Pot șterge o comandă greșită?
**R:** Momentan nu există funcție de ștergere comenzi. Pentru comenzi greșite, creează o comandă negativă sau contactă suportul tehnic pentru editare manuală a fișierului JSON.

### Q2: Cum văd istoricul unui client?
**R:** Caută clientul după nume/ID, apoi verifică rapoartele pentru a vedea comenzile sale.

### Q3: Pot modifica o comandă după plasare?
**R:** Nu direct prin interfață. Comenzile sunt finale. Pentru modificări, contactează administratorul.

### Q4: Cum resetez stocul la zero?
**R:** Modifică produsul (Meniu 3 → 6) și setează cantitatea la 0.

### Q5: Rapoartele nu afișează date?
**R:** Verifică că:
- Ai creat cel puțin o comandă
- Fișierele JSON există în folder-ul `json/`
- Formatele datelor sunt corecte

### Q6: Cum exportalex un raport în Excel?
**R:** Momentan doar în JSON. Poți deschide JSON-ul și să-l copiezi într-un Excel sau să folosești un convertor online.

### Q7: Pot avea mai multe cafenele?
**R:** Nu în versiunea actuală. Fiecare instalare gestionează o singură locație.

### Q8: Cum fac backup la date?
**R:** Copiază întreg folder-ul `json/` într-o locație sigură. Restaurarea = copiază înapoi.

### Q9: Sistemul funcționează offline?
**R:** DA! Totul este local, fără nevoie de internet.

### Q10: Cum actualizez sistemul?
**R:** Descarcă noua versiune și înlocuiește fișierele Python. **NU** șterge folder-ul `json/`!

---

## 💡 Sfaturi și Trucuri

### 🎯 Pentru Eficiență

**1. Tastează rapid ID-urile**
- Memorează ID-urile produselor populare
- Exemplu: 1=Espresso, 2=Cappuccino

**2. Folosește băutura preferată**
- Întreabă clientul prima dată
- Salvează în sistem
- Oferă recomandări personalizate

**3. Verifică stocul săptămânal**
- Luni dimineața = verificare stoc
- Comandă produse înainte să termine

**4. Rapoarte regulate**
- Zilnic: Raport profit
- Săptămânal: Raport încasări
- Lunar: Raport total

### 📊 Pentru Analiză

**1. Monitorizează top produse**
- Identifică bestseller-ele
- Promovează produse cu marjă mare

**2. Urmărește performanța angajaților**
- Comenzi procesate
- Feedback clienți
- Premiază performanța

**3. Identifică clienți fideli**
- Top comenzi = clienți VIP
- Oferă beneficii speciale
- Program de loialitate (viitor)

### ⚠️ Erori Comune de Evitat

❌ **NU** șterge fișierele JSON manual  
❌ **NU** modifica JSON-urile direct (poți corupe datele)  
❌ **NU** uita să verifici stocul înainte de comenzi  
❌ **NU** seta prețuri mai mici decât costul  
❌ **NU** ștergi angajați cu comenzi active  

### ✅ Best Practices

✅ Backup zilnic al folder-ului `json/`  
✅ Verifică rapoartele săptămânal  
✅ Actualizează stocul imediat după aprovizionare  
✅ Formează angajații pe sistem  
✅ Notează feedback-ul clienților  
✅ Păstrează prețurile competitive  

<div align="center">

**[⬅️ Înapoi la README](README.md)**

*User Guide v1.0 - Actualizat 17 Octombrie 2025*

**Succes cu cafeneaua ta! ☕** 

</div>
