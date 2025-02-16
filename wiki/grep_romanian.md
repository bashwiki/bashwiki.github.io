# [Linux] Bash grep utilizare: Căutare de text în fișiere

## Overview
Comanda `grep` este un instrument puternic utilizat în Bash pentru a căuta și a filtra textul din fișiere. Aceasta permite utilizatorilor să găsească linii care conțin un anumit șir de caractere, făcându-l extrem de util pentru analiza fișierelor de log, scripturi și multe altele.

## Usage
Sintaxa de bază a comenzii `grep` este următoarea:

```
grep [opțiuni] [argumente]
```

## Common Options
Iată câteva opțiuni comune pentru `grep`, împreună cu explicații scurte:

- `-i`: Ignoră diferențele dintre literele mari și mici.
- `-v`: Afișează liniile care nu conțin șirul specificat.
- `-r`: Caută recursiv în directoare.
- `-n`: Afișează numerele de linie pentru liniile găsite.
- `-l`: Afișează doar numele fișierelor care conțin șirul căutat.

## Common Examples
Iată câteva exemple practice de utilizare a comenzii `grep`:

1. Căutarea unui șir de caractere într-un fișier:
   ```bash
   grep "text_cautat" fisier.txt
   ```

2. Căutarea unui șir de caractere fără a ține cont de literele mari și mici:
   ```bash
   grep -i "text_cautat" fisier.txt
   ```

3. Căutarea recursivă a unui șir în toate fișierele dintr-un director:
   ```bash
   grep -r "text_cautat" /cale/catre/director
   ```

4. Afișarea liniilor care nu conțin un anumit șir:
   ```bash
   grep -v "text_cautat" fisier.txt
   ```

5. Afișarea numelui fișierului care conține un șir specific:
   ```bash
   grep -l "text_cautat" *.txt
   ```

## Tips
- Folosește opțiunea `-n` pentru a identifica rapid liniile din fișiere, mai ales când lucrezi cu fișiere mari.
- Combină `grep` cu alte comenzi folosind pipe (`|`) pentru a filtra rezultatele. De exemplu:
  ```bash
  cat fisier.txt | grep "text_cautat"
  ```
- Salvează rezultatele căutării într-un fișier folosind redirecționarea:
  ```bash
  grep "text_cautat" fisier.txt > rezultate.txt
  ``` 

Acestea sunt doar câteva dintre modalitățile prin care poți utiliza comanda `grep` pentru a căuta și a analiza textul în fișiere.