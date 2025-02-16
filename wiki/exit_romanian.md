# [Linux] Bash exit utilizare: Terminarea unui script sau a unei sesiuni

## Overview
Comanda `exit` în Bash este folosită pentru a termina un script sau o sesiune de terminal. Aceasta poate returna un cod de ieșire, care este un număr întreg ce indică succesul sau eșecul execuției.

## Usage
Sintaxa de bază a comenzii `exit` este următoarea:

```bash
exit [opțiuni] [argumente]
```

## Common Options
- `n`: Un număr întreg care reprezintă codul de ieșire. Dacă nu este specificat, codul de ieșire va fi acela al ultimei comenzi executate.

## Common Examples
1. **Terminarea unui script cu succes:**
   ```bash
   #!/bin/bash
   echo "Scriptul s-a terminat cu succes."
   exit 0
   ```

2. **Terminarea unui script cu o eroare:**
   ```bash
   #!/bin/bash
   echo "A apărut o eroare."
   exit 1
   ```

3. **Ieșirea dintr-o sesiune de terminal:**
   ```bash
   exit
   ```

4. **Ieșirea dintr-un script și returnarea unui cod de eroare:**
   ```bash
   #!/bin/bash
   if [ ! -f "fisier.txt" ]; then
       echo "Fisierul nu există."
       exit 2
   fi
   ```

## Tips
- Folosește `exit 0` pentru a indica o terminare cu succes și un cod diferit pentru a indica diferite tipuri de erori.
- Verifică întotdeauna codul de ieșire al ultimei comenzi cu `$?` pentru a te asigura că scriptul tău se comportă așa cum te aștepți.
- În scripturi mai complexe, este o bună practică să gestionezi codurile de ieșire pentru a facilita depanarea.