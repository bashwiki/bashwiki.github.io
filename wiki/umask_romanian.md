# [Linux] Bash umask utilizare: Setează permisiunile implicite pentru fișiere

## Overview
Comanda `umask` este utilizată pentru a seta masca de permisiuni implicite pentru fișierele și directoarele create de utilizator. Aceasta determină permisiunile care nu vor fi acordate fișierelor noi, influențând astfel securitatea și accesibilitatea acestora.

## Usage
Sintaxa de bază a comenzii `umask` este următoarea:

```bash
umask [opțiuni] [argumente]
```

## Common Options
- `-S`: Afișează masca de permisiuni într-un format simbolic.
- `-p`: Afișează masca de permisiuni curentă, fără a o modifica.

## Common Examples
1. **Afișarea mascii curente:**
   ```bash
   umask
   ```

2. **Setarea unei noi masti de permisiuni:**
   ```bash
   umask 027
   ```
   Aceasta va permite ca fișierele noi să aibă permisiuni de 640 (rw-r-----) și directoarele să aibă permisiuni de 750 (rwxr-x---).

3. **Afișarea mascii în format simbolic:**
   ```bash
   umask -S
   ```

4. **Restabilirea mascii implicite:**
   ```bash
   umask 0022
   ```
   Aceasta va seta permisiunile implicite pentru fișierele noi la 644 (rw-r--r--) și pentru directoare la 755 (rwxr-xr-x).

## Tips
- Este recomandat să verificați periodic masca de permisiuni pentru a vă asigura că nu permite accesul neautorizat la fișierele sensibile.
- Utilizați `umask` în scripturi pentru a controla permisiunile fișierelor create automat.
- Fiți atenți la setările de umask în medii partajate, deoarece acestea pot afecta accesul altor utilizatori la fișierele create.