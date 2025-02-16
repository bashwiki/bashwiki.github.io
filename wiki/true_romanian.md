# [Linux] Bash true utilizare: Comandă care returnează întotdeauna adevărat

## Overview
Comanda `true` în Bash este o comandă simplă care returnează întotdeauna un cod de ieșire 0, ceea ce indică faptul că a fost executată cu succes. Este adesea folosită în scripturi pentru a indica faptul că o operațiune a avut succes sau pentru a umple locuri în comenzi complexe.

## Usage
Sintaxa de bază a comenzii `true` este următoarea:

```bash
true [opțiuni]
```

## Common Options
Comanda `true` nu are opțiuni specifice, deoarece scopul său principal este de a returna un cod de ieșire 0. Totuși, poate fi utilizată în combinație cu alte comenzi care acceptă opțiuni.

## Common Examples

1. **Utilizarea `true` într-un script**:
   ```bash
   #!/bin/bash
   if true; then
       echo "Aceasta este întotdeauna adevărat."
   fi
   ```

2. **Utilizarea `true` cu comanda `&&`**:
   ```bash
   true && echo "Aceasta va fi afișată deoarece true a returnat 0."
   ```

3. **Utilizarea `true` în bucle**:
   ```bash
   while true; do
       echo "Aceasta va continua să ruleze până când este oprită."
       sleep 1
   done
   ```

4. **Umplerea unui loc în comenzi complexe**:
   ```bash
   command1 || true
   ```

## Tips
- Folosiți `true` în scripturi pentru a evita erorile în lanțuri de comenzi.
- Este util în bucle infinite sau în condiții care necesită o evaluare constantă.
- Comanda `true` este rapidă și eficientă, având un impact minim asupra performanței scripturilor.