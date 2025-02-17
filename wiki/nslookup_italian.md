# [Linux] Bash nslookup utilizzo: Risolvere nomi di dominio in indirizzi IP

## Overview
Il comando `nslookup` è uno strumento utile per interrogare i server DNS al fine di ottenere informazioni sui nomi di dominio, come gli indirizzi IP associati. È comunemente utilizzato per diagnosticare problemi di rete e per verificare la configurazione DNS.

## Usage
La sintassi di base del comando `nslookup` è la seguente:

```bash
nslookup [opzioni] [argomenti]
```

## Common Options
Ecco alcune opzioni comuni per `nslookup`:

- `-type=tipo`: Specifica il tipo di record DNS da cercare (ad esempio, A, AAAA, MX).
- `-timeout=secondi`: Imposta il tempo di attesa per una risposta dal server DNS.
- `-debug`: Abilita la modalità di debug per visualizzare informazioni dettagliate sulla richiesta DNS.
- `-port=numero`: Specifica la porta da utilizzare per la richiesta DNS (di default è la porta 53).

## Common Examples
Ecco alcuni esempi pratici di utilizzo del comando `nslookup`:

1. **Ottenere l'indirizzo IP di un dominio:**

   ```bash
   nslookup example.com
   ```

2. **Cercare un record MX per un dominio:**

   ```bash
   nslookup -type=MX example.com
   ```

3. **Utilizzare un server DNS specifico:**

   ```bash
   nslookup example.com 8.8.8.8
   ```

4. **Visualizzare informazioni dettagliate sulla richiesta:**

   ```bash
   nslookup -debug example.com
   ```

5. **Cercare un record AAAA (IPv6):**

   ```bash
   nslookup -type=AAAA example.com
   ```

## Tips
- Assicurati di avere una connessione Internet attiva quando utilizzi `nslookup`, poiché il comando richiede l'accesso a un server DNS.
- Utilizza l'opzione `-debug` per ottenere informazioni più dettagliate, specialmente quando stai cercando di risolvere problemi di configurazione DNS.
- Se stai testando più domini, considera di scrivere uno script per automatizzare le chiamate a `nslookup` e raccogliere i risultati in un file.