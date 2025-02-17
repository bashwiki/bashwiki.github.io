# [Linux] Bash who uso: Visualizza gli utenti connessi

## Overview
Il comando `who` in Bash viene utilizzato per visualizzare gli utenti attualmente connessi al sistema. Mostra informazioni come il nome dell'utente, il terminale utilizzato, la data e l'ora di accesso.

## Usage
La sintassi di base del comando `who` è la seguente:

```bash
who [opzioni] [argomenti]
```

## Common Options
- `-a`: Mostra tutte le informazioni disponibili, inclusi gli utenti inattivi.
- `-b`: Mostra l'ultima volta che il sistema è stato avviato.
- `-q`: Mostra solo i nomi degli utenti connessi e il numero totale di utenti.
- `--help`: Mostra un messaggio di aiuto con le opzioni disponibili.

## Common Examples
Ecco alcuni esempi pratici dell'uso del comando `who`:

1. **Visualizzare gli utenti connessi:**
   ```bash
   who
   ```

2. **Mostrare informazioni complete sugli utenti:**
   ```bash
   who -a
   ```

3. **Visualizzare l'ultima volta che il sistema è stato avviato:**
   ```bash
   who -b
   ```

4. **Mostrare solo i nomi degli utenti connessi:**
   ```bash
   who -q
   ```

## Tips
- Usa `who` regolarmente per monitorare chi è connesso al tuo sistema, specialmente in ambienti multi-utente.
- Combina `who` con altri comandi come `grep` per filtrare risultati specifici. Ad esempio:
  ```bash
  who | grep nome_utente
  ```
- Ricorda che `who` mostra solo gli utenti attivi; per una panoramica più completa, considera di usare anche il comando `w`.