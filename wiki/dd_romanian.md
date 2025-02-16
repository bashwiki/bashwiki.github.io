# [Linux] Bash dd utilizare: Copierea și conversia datelor

## Overview
Comanda `dd` este un instrument puternic în Linux utilizat pentru copierea și conversia datelor. Aceasta poate fi folosită pentru a crea imagini ale discurilor, a copia fișiere sau a transforma formatele de date.

## Usage
Sintaxa de bază a comenzii `dd` este următoarea:

```bash
dd [opțiuni] [argumente]
```

## Common Options
- `if=`: Specifică fișierul de intrare (input file).
- `of=`: Specifică fișierul de ieșire (output file).
- `bs=`: Setează dimensiunea blocului (block size).
- `count=`: Numărul de blocuri de copiat.
- `status=`: Afișează informații despre progresul comenzii (ex: `none`, `noxfer`, `progress`).

## Common Examples
1. **Crearea unei imagini a unui disc:**
   ```bash
   dd if=/dev/sda of=/path/to/image.img bs=4M
   ```

2. **Restaurarea unei imagini pe un disc:**
   ```bash
   dd if=/path/to/image.img of=/dev/sda bs=4M
   ```

3. **Copierea unui fișier:**
   ```bash
   dd if=/path/to/source.file of=/path/to/destination.file
   ```

4. **Crearea unui fișier de dimensiune specifică:**
   ```bash
   dd if=/dev/zero of=/path/to/file.img bs=1M count=100
   ```

5. **Verificarea progresului în timpul copiei:**
   ```bash
   dd if=/dev/sda of=/path/to/image.img bs=4M status=progress
   ```

## Tips
- Folosește `bs=` pentru a îmbunătăți viteza de copiere, alegând o dimensiune a blocului optimă.
- Verifică întotdeauna calea fișierelor de intrare și ieșire pentru a evita pierderea datelor.
- Utilizează opțiunea `status=progress` pentru a monitoriza progresul, mai ales când lucrezi cu fișiere mari.