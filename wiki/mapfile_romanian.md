# [Linux] Bash mapfile utilizare: Citirea fișierelor într-un tablou

## Overview
Comanda `mapfile` în Bash este utilizată pentru a citi liniile dintr-un fișier și a le stoca într-un tablou. Aceasta este o modalitate eficientă de a manipula datele din fișiere text, permițându-vă să accesați fiecare linie ca un element al unui tablou.

## Usage
Sintaxa de bază a comenzii `mapfile` este următoarea:

```bash
mapfile [opțiuni] [argumente]
```

## Common Options
- `-t`: Elimină caracterele de sfârșit de linie din fiecare linie citită.
- `-n NUM`: Citește un număr specificat de linii.
- `-O NUM`: Specifică indexul de început pentru tabloul rezultat.

## Common Examples

### Exemplul 1: Citirea unui fișier într-un tablou
Pentru a citi un fișier numit `exemplu.txt` într-un tablou numit `linii`, folosiți următoarea comandă:

```bash
mapfile linii < exemplu.txt
```

### Exemplul 2: Eliminarea caracterelor de sfârșit de linie
Dacă doriți să citiți un fișier și să eliminați caracterele de sfârșit de linie, utilizați opțiunea `-t`:

```bash
mapfile -t linii < exemplu.txt
```

### Exemplul 3: Citirea unui număr specificat de linii
Pentru a citi doar primele 5 linii dintr-un fișier, utilizați opțiunea `-n`:

```bash
mapfile -n 5 linii < exemplu.txt
```

### Exemplul 4: Specificarea indexului de început
Dacă doriți să începeți stocarea liniilor în tabloul `linii` de la un index specificat, folosiți opțiunea `-O`:

```bash
mapfile -O 10 linii < exemplu.txt
```

## Tips
- Asigurați-vă că fișierul pe care doriți să-l citiți există și are permisiuni de citire.
- Utilizați `echo "${linii[@]}"` pentru a vizualiza conținutul tabloului după ce ați citit fișierul.
- `mapfile` este util în scripturi pentru a prelucra datele din fișiere mari fără a le încărca complet în memorie.