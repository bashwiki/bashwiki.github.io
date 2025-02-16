# [Linux] Bash diff utilizare: Compararea fișierelor

## Overview
Comanda `diff` este utilizată pentru a compara conținutul a două fișiere text și a evidenția diferențele dintre ele. Aceasta este utilă pentru programatori și utilizatori care doresc să identifice modificările sau să analizeze variațiile între versiuni diferite ale unui fișier.

## Usage
Sintaxa de bază a comenzii `diff` este următoarea:

```bash
diff [opțiuni] [fișier1] [fișier2]
```

## Common Options
- `-u`: Afișează diferențele într-un format unificat, care este mai ușor de citit.
- `-i`: Ignoră diferențele de majuscule și minuscule.
- `-w`: Ignoră spațiile albe la începutul și la sfârșitul liniilor.
- `-r`: Compară recursiv directoare și subdirectoare.
- `-q`: Afișează doar dacă fișierele sunt diferite, fără a arăta diferențele.

## Common Examples
1. Compararea a două fișiere simple:
   ```bash
   diff fisier1.txt fisier2.txt
   ```

2. Compararea a două fișiere cu opțiunea de ignorare a majusculelor:
   ```bash
   diff -i fisier1.txt fisier2.txt
   ```

3. Afișarea diferențelor într-un format unificat:
   ```bash
   diff -u fisier1.txt fisier2.txt
   ```

4. Compararea recursivă a două directoare:
   ```bash
   diff -r director1/ director2/
   ```

5. Verificarea rapidă a diferențelor între fișiere:
   ```bash
   diff -q fisier1.txt fisier2.txt
   ```

## Tips
- Folosiți opțiunea `-u` pentru a obține un context mai bun al modificărilor, ceea ce poate fi util în revizuirea codului.
- Dacă lucrați cu fișiere mari, luați în considerare utilizarea opțiunii `-w` pentru a evita confuziile cauzate de spațiile albe.
- Pentru a salva rezultatul comparației într-un fișier, redirecționați ieșirea comenzii:
  ```bash
  diff fisier1.txt fisier2.txt > diferente.txt
  ```