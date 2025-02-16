# [Linux] Bash chmod utilizare: Modifică permisiunile fișierelor

## Overview
Comanda `chmod` este utilizată în sistemele de operare Unix și Linux pentru a schimba permisiunile fișierelor și directoarelor. Aceasta permite utilizatorilor să controleze cine poate citi, scrie sau executa un fișier.

## Usage
Sintaxa de bază a comenzii `chmod` este următoarea:

```bash
chmod [opțiuni] [argumente]
```

## Common Options
- `-R`: Aplică modificările recursiv în toate subdirectoarele.
- `u`: Se referă la utilizator (proprietar).
- `g`: Se referă la grup.
- `o`: Se referă la alții (toți ceilalți utilizatori).
- `a`: Se referă la toți utilizatorii (u, g, o).
- `+`: Adaugă permisiuni.
- `-`: Elimină permisiuni.
- `=`: Setează permisiunile exact.

## Common Examples
1. **Adăugarea permisiunii de execuție pentru utilizator:**
   ```bash
   chmod u+x script.sh
   ```

2. **Eliminarea permisiunii de scriere pentru grup:**
   ```bash
   chmod g-w document.txt
   ```

3. **Setarea permisiunilor pentru toți utilizatorii la citire:**
   ```bash
   chmod a+r fisier.txt
   ```

4. **Modificarea permisiunilor recursiv pentru un director:**
   ```bash
   chmod -R 755 /cale/catre/director
   ```

5. **Setarea permisiunilor exacte pentru un fișier:**
   ```bash
   chmod 644 fisier.txt
   ```

## Tips
- Verifică permisiunile curente ale fișierelor folosind comanda `ls -l`.
- Folosește opțiunea `-R` cu precauție, deoarece poate modifica permisiunile pentru toate fișierele și subdirectoarele.
- Este recomandat să folosești permisiuni stricte pentru fișierele sensibile, cum ar fi cheile private sau fișierele de configurare.