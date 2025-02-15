# [리눅스] Bash who 사용법

## Overview
Il comando `who` in Bash è utilizzato per visualizzare l'elenco degli utenti attualmente connessi al sistema. Fornisce informazioni utili come il nome dell'utente, il terminale utilizzato, la data e l'ora di accesso e, in alcuni casi, l'indirizzo IP o il nome host dell'utente. Questo comando è particolarmente utile per gli amministratori di sistema e gli sviluppatori che desiderano monitorare l'attività degli utenti nel sistema.

## Usage
La sintassi di base del comando `who` è la seguente:

```bash
who [opzioni]
```

### Opzioni comuni:
- `-a`: Mostra tutte le informazioni disponibili, inclusi gli utenti disconnessi.
- `-b`: Mostra l'ultima volta che il sistema è stato avviato.
- `-q`: Mostra solo i nomi degli utenti connessi e il conteggio totale.
- `--help`: Mostra un messaggio di aiuto con le opzioni disponibili.

## Examples
Ecco alcuni esempi pratici su come utilizzare il comando `who`.

1. **Visualizzare gli utenti connessi**:
   ```bash
   who
   ```
   Questo comando mostrerà un elenco di tutti gli utenti attualmente connessi al sistema, insieme alle informazioni relative al terminale e all'orario di accesso.

2. **Mostrare informazioni dettagliate**:
   ```bash
   who -a
   ```
   Utilizzando l'opzione `-a`, questo comando fornirà un output più dettagliato, inclusi gli utenti disconnessi e altre informazioni utili.

## Tips
- Utilizza `who` insieme ad altri comandi come `grep` per filtrare i risultati. Ad esempio, per trovare un utente specifico:
  ```bash
  who | grep nome_utente
  ```
- Se desideri monitorare continuamente gli accessi degli utenti, puoi combinare `who` con `watch`:
  ```bash
  watch who
  ```
  Questo comando aggiornerà automaticamente l'elenco degli utenti ogni 2 secondi.
- Ricorda che il comando `who` può mostrare informazioni sensibili sugli utenti, quindi è consigliabile utilizzarlo con attenzione, specialmente in ambienti condivisi.