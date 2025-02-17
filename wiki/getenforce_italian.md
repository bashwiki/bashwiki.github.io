# [Linux] Bash getenforce utilizzo: Controlla lo stato di SELinux

## Overview
Il comando `getenforce` viene utilizzato per verificare lo stato attuale di SELinux (Security-Enhanced Linux). Questo strumento fornisce informazioni su come SELinux è configurato nel sistema, indicando se è in modalità "Enforcing", "Permissive" o "Disabled".

## Usage
La sintassi di base del comando è la seguente:

```bash
getenforce [opzioni]
```

## Common Options
Il comando `getenforce` non ha molte opzioni, ma ecco quelle più comuni:

- **Nessuna opzione**: Restituisce lo stato attuale di SELinux.
  
## Common Examples

Ecco alcuni esempi pratici dell'uso del comando `getenforce`:

1. **Controllare lo stato di SELinux**:
   ```bash
   getenforce
   ```
   Questo comando restituirà uno dei seguenti stati: `Enforcing`, `Permissive` o `Disabled`.

2. **Utilizzare in uno script**:
   ```bash
   if [ "$(getenforce)" == "Enforcing" ]; then
       echo "SELinux è attivo."
   else
       echo "SELinux non è attivo."
   fi
   ```
   Questo script verifica se SELinux è in modalità "Enforcing" e stampa un messaggio appropriato.

## Tips
- È utile eseguire `getenforce` come parte di uno script di avvio per garantire che SELinux sia configurato correttamente.
- Se stai riscontrando problemi di accesso, controlla lo stato di SELinux con `getenforce` per determinare se potrebbe essere la causa.
- Ricorda che per modificare le impostazioni di SELinux, dovrai utilizzare altri comandi come `setenforce` o modificare i file di configurazione.