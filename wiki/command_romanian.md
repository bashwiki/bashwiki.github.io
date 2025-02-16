# [Linux] Bash command utilizare: [execută comenzi în fundal]

## Overview
Comanda `nohup` permite executarea unei comenzi în fundal, astfel încât aceasta să continue să ruleze chiar și după ce utilizatorul se deconectează de la sesiunea terminalului. Este utilă pentru procesele pe termen lung care nu trebuie întrerupte.

## Usage
Sintaxa de bază a comenzii `nohup` este următoarea:

```bash
nohup command [options] [arguments] &
```

## Common Options
- `&` - Rulează comanda în fundal.
- `nohup.out` - Fișierul implicit în care se redirecționează ieșirea standard și erorile, dacă nu se specifică altceva.
- `-p` - Permite specificarea unui PID (Process ID) pentru a verifica starea procesului.

## Common Examples
1. **Executarea unui script în fundal:**
   ```bash
   nohup ./script.sh &
   ```

2. **Executarea unei comenzi cu redirecționarea ieșirii:**
   ```bash
   nohup long_running_command > output.log 2>&1 &
   ```

3. **Verificarea procesului după deconectare:**
   ```bash
   nohup sleep 1000 &
   ```

4. **Executarea unui server web în fundal:**
   ```bash
   nohup python -m http.server 8000 &
   ```

## Tips
- Asigurați-vă că redirecționați ieșirea standard și erorile pentru a evita pierderea informațiilor importante.
- Verificați fișierul `nohup.out` pentru a vedea ieșirea procesului după ce a fost lansat.
- Utilizați comanda `jobs` pentru a lista procesele care rulează în fundal.