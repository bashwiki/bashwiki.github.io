# [리눅스] Bash firewalld 사용법

## Overview
Il comando `firewalld` è un gestore di firewall dinamico per Linux, progettato per gestire le regole del firewall in modo semplice e flessibile. La sua principale funzione è quella di fornire un'interfaccia per configurare e gestire le politiche di sicurezza della rete, consentendo di aggiungere, rimuovere e modificare le regole del firewall senza dover riavviare il servizio. `firewalld` supporta zone e servizi, permettendo una gestione granulare della sicurezza della rete.

## Usage
La sintassi di base del comando `firewalld` è la seguente:

```bash
firewall-cmd [opzioni]
```

Alcune delle opzioni più comuni includono:

- `--zone=<zone>`: Specifica la zona in cui applicare le regole.
- `--add-service=<servizio>`: Aggiunge un servizio alla zona specificata.
- `--remove-service=<servizio>`: Rimuove un servizio dalla zona specificata.
- `--list-all`: Mostra tutte le configurazioni della zona attiva.
- `--permanent`: Applica le modifiche in modo permanente, senza perderle al riavvio del servizio.

## Examples
Ecco alcuni esempi pratici su come utilizzare `firewalld`.

### Esempio 1: Aggiungere un servizio
Per aggiungere il servizio HTTP alla zona pubblica, puoi utilizzare il seguente comando:

```bash
sudo firewall-cmd --zone=public --add-service=http --permanent
```

Dopo aver eseguito questo comando, è necessario ricaricare le configurazioni per applicare le modifiche:

```bash
sudo firewall-cmd --reload
```

### Esempio 2: Elencare le configurazioni della zona
Per visualizzare tutte le configurazioni della zona attiva, puoi utilizzare:

```bash
sudo firewall-cmd --list-all
```

Questo comando mostrerà informazioni dettagliate sulla zona attiva, inclusi i servizi e le porte aperte.

## Tips
- Assicurati di utilizzare l'opzione `--permanent` quando desideri che le modifiche siano persistenti dopo un riavvio del servizio.
- Utilizza `firewall-cmd --state` per verificare se `firewalld` è attivo e in esecuzione.
- È consigliabile testare le modifiche in un ambiente di sviluppo prima di applicarle in produzione per evitare interruzioni del servizio.
- Familiarizza con le zone di `firewalld` per gestire in modo efficace le diverse configurazioni di rete.