# [리눅스] Bash ufw 사용법

## Overview
`ufw` (Uncomplicated Firewall) è un'interfaccia per la gestione del firewall di Linux, progettata per semplificare la configurazione delle regole del firewall. Il suo obiettivo principale è fornire un modo facile e intuitivo per gestire le impostazioni del firewall, rendendo più accessibile la protezione delle macchine Linux contro accessi non autorizzati.

## Usage
La sintassi di base del comando `ufw` è la seguente:

```bash
ufw [opzioni] [comando]
```

Alcune delle opzioni e dei comandi più comuni includono:

- `enable`: Abilita il firewall.
- `disable`: Disabilita il firewall.
- `allow [porta]`: Consente il traffico sulla porta specificata.
- `deny [porta]`: Negare il traffico sulla porta specificata.
- `status`: Mostra lo stato attuale del firewall e le regole attive.
- `reset`: Ripristina tutte le regole del firewall alle impostazioni predefinite.

## Examples
Ecco alcuni esempi pratici su come utilizzare `ufw`:

1. **Abilitare il firewall**:
   ```bash
   sudo ufw enable
   ```
   Questo comando attiva il firewall, iniziando a filtrare il traffico in base alle regole configurate.

2. **Consentire il traffico sulla porta 22 (SSH)**:
   ```bash
   sudo ufw allow 22
   ```
   Questo comando consente il traffico sulla porta 22, che è comunemente utilizzata per le connessioni SSH.

3. **Controllare lo stato del firewall**:
   ```bash
   sudo ufw status
   ```
   Questo comando mostra lo stato attuale del firewall e le regole attive.

## Tips
- **Controlla sempre lo stato del firewall**: Prima di apportare modifiche, è utile controllare lo stato attuale del firewall per evitare conflitti.
- **Utilizza il comando `verbose`**: Quando esegui comandi come `allow` o `deny`, puoi aggiungere l'opzione `verbose` per ottenere informazioni dettagliate sulle azioni intraprese.
- **Fai attenzione alle regole di accesso remoto**: Se stai configurando un server remoto, assicurati di consentire l'accesso SSH prima di abilitare il firewall, altrimenti potresti bloccarti fuori.
- **Backup delle regole**: Prima di eseguire un `reset`, considera di salvare le regole attuali per poterle ripristinare in seguito se necessario.