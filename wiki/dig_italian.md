# [Linux] Bash dig Utilizzo: Strumento per interrogare server DNS

## Overview
Il comando `dig` (Domain Information Groper) è uno strumento utilizzato per interrogare i server DNS e ottenere informazioni dettagliate sui nomi di dominio. È particolarmente utile per diagnosticare problemi di risoluzione DNS e per raccogliere informazioni sui record DNS.

## Usage
La sintassi di base del comando `dig` è la seguente:

```bash
dig [opzioni] [argomenti]
```

## Common Options
Ecco alcune opzioni comuni per il comando `dig`:

- `@server`: Specifica un server DNS da interrogare.
- `-t tipo`: Specifica il tipo di record DNS da cercare (ad esempio, A, MX, TXT).
- `+short`: Restituisce un output più conciso, mostrando solo le informazioni essenziali.
- `+trace`: Segue il percorso della risoluzione DNS, mostrando ogni passaggio.

## Common Examples
Ecco alcuni esempi pratici dell'uso del comando `dig`:

1. **Interrogare un record A di un dominio:**
   ```bash
   dig example.com
   ```

2. **Interrogare un server DNS specifico:**
   ```bash
   dig @8.8.8.8 example.com
   ```

3. **Cercare un record MX (Mail Exchange):**
   ```bash
   dig -t MX example.com
   ```

4. **Ottenere un output conciso:**
   ```bash
   dig +short example.com
   ```

5. **Seguire il percorso della risoluzione DNS:**
   ```bash
   dig +trace example.com
   ```

## Tips
- Utilizza l'opzione `+short` per ottenere risultati più rapidi e leggibili, specialmente se stai cercando solo indirizzi IP.
- Se stai diagnosticando problemi di DNS, l'opzione `+trace` può aiutarti a capire dove si verifica il problema.
- Prova a interrogare diversi server DNS per confrontare i risultati e verificare la coerenza delle informazioni.