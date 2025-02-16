# [Linux] Bash printf utilizare: Afișează formate de text

## Overview
Comanda `printf` în Bash este utilizată pentru a formata și a afișa text pe ecran. Aceasta permite utilizatorilor să controleze modul în care sunt prezentate datele, oferind opțiuni avansate de formatare.

## Usage
Sintaxa de bază a comenzii `printf` este următoarea:

```bash
printf [opțiuni] [argumente]
```

## Common Options
- `-v`: Salvează rezultatul în variabilă în loc să-l afișeze pe ecran.
- `-f`: Specifică un format de ieșire.
- `%s`: Format pentru șiruri de caractere.
- `%d`: Format pentru numere întregi.
- `%f`: Format pentru numere în virgulă mobilă.

## Common Examples
1. Afișarea unui șir de caractere:
   ```bash
   printf "Salut, lume!\n"
   ```

2. Afișarea unui număr întreg:
   ```bash
   printf "Numărul este: %d\n" 42
   ```

3. Afișarea unui număr în virgulă mobilă:
   ```bash
   printf "Valoarea este: %.2f\n" 3.14159
   ```

4. Afișarea mai multor argumente:
   ```bash
   printf "Nume: %s, Vârstă: %d\n" "Ion" 30
   ```

5. Salvarea rezultatului într-o variabilă:
   ```bash
   printf -v mesaj "Salut, %s!" "Maria"
   echo "$mesaj"
   ```

## Tips
- Folosește `\n` pentru a adăuga o linie nouă în ieșire.
- Verifică formatul argumentelor pentru a evita erorile de afișare.
- Poți combina mai multe formate într-o singură comandă pentru a crea ieșiri complexe.