# [Linux] Bash echo utilizare: Afișează text pe ecran

## Overview
Comanda `echo` în Bash este utilizată pentru a afișa text sau variabile pe ecran. Este o unealtă simplă, dar extrem de utilă pentru a verifica valori, a genera ieșiri sau a crea mesaje informative.

## Usage
Sintaxa de bază a comenzii `echo` este următoarea:

```bash
echo [opțiuni] [argumente]
```

## Common Options
Iată câteva opțiuni comune pentru comanda `echo`:

- `-n`: Nu adaugă un caracter de linie nouă la sfârșitul ieșirii.
- `-e`: Activează interpretarea secvențelor de escape (de exemplu, `\n` pentru o linie nouă).
- `-E`: Dezactivează interpretarea secvențelor de escape (aceasta este opțiunea implicită).

## Common Examples
Iată câteva exemple practice ale utilizării comenzii `echo`:

1. Afișarea unui text simplu:
   ```bash
   echo "Salut, lume!"
   ```

2. Afișarea unei variabile:
   ```bash
   nume="Ion"
   echo "Numele meu este $nume."
   ```

3. Afișarea textului fără o linie nouă la sfârșit:
   ```bash
   echo -n "Aceasta este o propoziție fără linie nouă."
   ```

4. Utilizarea secvențelor de escape:
   ```bash
   echo -e "Primul rând\nAl doilea rând"
   ```

5. Afișarea textului cu caractere speciale:
   ```bash
   echo "Caractere speciale: \$ \` \""
   ```

## Tips
- Folosiți `-n` pentru a evita linia nouă dacă doriți să continuați pe aceeași linie.
- Utilizați `-e` pentru a adăuga formatare în ieșirea dvs., cum ar fi linii noi sau taburi.
- Fiți atenți la utilizarea variabilelor; asigurați-vă că le precedați cu `$` pentru a le evalua corect.