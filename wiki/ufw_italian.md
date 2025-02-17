# [Linux] Bash ufw Utilizzo: Gestire il firewall

## Overview
Il comando `ufw` (Uncomplicated Firewall) è un'interfaccia per gestire il firewall di Linux in modo semplice e intuitivo. È progettato per semplificare la configurazione delle regole del firewall, consentendo agli utenti di proteggere i propri sistemi da accessi non autorizzati.

## Usage
La sintassi di base del comando `ufw` è la seguente:

```bash
ufw [opzioni] [argomenti]
```

## Common Options
Ecco alcune opzioni comuni per il comando `ufw`:

- `enable`: Abilita il firewall.
- `disable`: Disabilita il firewall.
- `status`: Mostra lo stato attuale del firewall.
- `allow [port]`: Permette il traffico sulla porta specificata.
- `deny [port]`: Negare il traffico sulla porta specificata.
- `delete [rule]`: Rimuove una regola specificata.

## Common Examples
Ecco alcuni esempi pratici dell'uso di `ufw`:

### Abilitare il firewall
```bash
sudo ufw enable
```

### Disabilitare il firewall
```bash
sudo ufw disable
```

### Controllare lo stato del firewall
```bash
sudo ufw status
```

### Permettere il traffico sulla porta 22 (SSH)
```bash
sudo ufw allow 22
```

### Negare il traffico sulla porta 80 (HTTP)
```bash
sudo ufw deny 80
```

### Rimuovere una regola
```bash
sudo ufw delete allow 22
```

## Tips
- Assicurati di testare le regole del firewall in un ambiente sicuro prima di applicarle in produzione.
- Utilizza `ufw status verbose` per ottenere informazioni dettagliate sulle regole attive.
- Ricorda di abilitare il firewall dopo aver configurato le regole per garantire la protezione del tuo sistema.