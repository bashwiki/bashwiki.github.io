# [Linux] Bash readarray utilizare: Citirea liniilor dintr-un fișier într-un array

## Overview
Comanda `readarray` (sau `mapfile`) este utilizată în Bash pentru a citi liniile dintr-un fișier și a le stoca într-un array. Aceasta este utilă atunci când doriți să manipulați datele linie cu linie, fără a fi nevoie să le procesați manual.

## Usage
Sintaxa de bază a comenzii `readarray` este următoarea:

```bash
readarray [opțiuni] [nume_array]
```

## Common Options
- `-n NUM`: Specifică numărul de linii de citit.
- `-s NUM`: Sari peste un număr specificat de linii înainte de a începe citirea.
- `-t`: Elimină caracterul de newline de la sfârșitul fiecărei linii citite.

## Common Examples
### Exemplul 1: Citirea unui fișier într-un array
```bash
readarray -t my_array < my_file.txt
```
Acest exemplu citește toate liniile din `my_file.txt` și le stochează în array-ul `my_array`, eliminând caracterele de newline.

### Exemplul 2: Citirea unui număr specific de linii
```bash
readarray -n 5 my_array < my_file.txt
```
Aici, doar primele 5 linii din `my_file.txt` sunt citite și stocate în `my_array`.

### Exemplul 3: Sărind peste linii
```bash
readarray -s 2 -t my_array < my_file.txt
```
Acest exemplu sare primele 2 linii din `my_file.txt` și citește restul liniilor, stocându-le în `my_array`.

## Tips
- Asigurați-vă că fișierul pe care doriți să-l citiți există și are permisiuni de citire.
- Utilizați opțiunea `-t` pentru a evita problemele cauzate de caracterele de newline atunci când manipulați datele din array.
- Verificați dimensiunea array-ului folosind `echo ${#my_array[@]}` pentru a vă asigura că ați citit corect liniile dorite.