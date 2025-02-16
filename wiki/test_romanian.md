# [Linux] Bash test utilizare: Verificarea condițiilor

## Overview
Comanda `test` este utilizată în Bash pentru a evalua expresii condiționale. Aceasta returnează un cod de ieșire care indică dacă condiția specificată este adevărată sau falsă. Este frecvent utilizată în scripturi pentru a lua decizii bazate pe rezultatele evaluărilor.

## Usage
Sintaxa de bază a comenzii `test` este următoarea:

```bash
test [opțiuni] [argumente]
```

## Common Options
- `-e`: Verifică dacă un fișier există.
- `-f`: Verifică dacă un fișier este un fișier obișnuit.
- `-d`: Verifică dacă un director există.
- `-z`: Verifică dacă un șir de caractere este gol.
- `-n`: Verifică dacă un șir de caractere nu este gol.
- `=`: Compară două șiruri de caractere pentru a verifica dacă sunt egale.
- `-lt`, `-le`, `-gt`, `-ge`, `-eq`, `-ne`: Compară numere pentru a verifica relații de mai mic, mai mic sau egal, mai mare, mai mare sau egal, egal, diferit.

## Common Examples
1. Verificarea existenței unui fișier:
   ```bash
   test -e /path/catre/fișier.txt && echo "Fișierul există."
   ```

2. Verificarea unui director:
   ```bash
   test -d /path/catre/director && echo "Este un director."
   ```

3. Compararea a două șiruri de caractere:
   ```bash
   test "abc" = "abc" && echo "Șirurile sunt egale."
   ```

4. Verificarea unui șir gol:
   ```bash
   str=""
   test -z "$str" && echo "Șirul este gol."
   ```

5. Compararea a două numere:
   ```bash
   num1=5
   num2=10
   test $num1 -lt $num2 && echo "$num1 este mai mic decât $num2."
   ```

## Tips
- Utilizați `[` în loc de `test` pentru o sintaxă mai concisă, de exemplu: `[ -e /path/catre/fișier.txt ]`.
- Asigurați-vă că spațiile sunt corecte în jurul operatorilor, cum ar fi `=` sau `-lt`.
- Folosiți `&&` pentru a executa comenzi condiționat, în funcție de rezultatul evaluării `test`.