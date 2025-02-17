# [Linux] Bash firewalld utilizzo: Gestire le regole del firewall

## Overview
Il comando `firewalld` è uno strumento di gestione del firewall in Linux che fornisce un'interfaccia per configurare e gestire le regole del firewall in modo dinamico. Utilizza zone e servizi per semplificare la configurazione della sicurezza di rete.

## Usage
La sintassi di base del comando `firewalld` è la seguente:

```bash
firewalld [opzioni] [argomenti]
```

## Common Options
- `--zone`: Specifica la zona da utilizzare per le regole del firewall.
- `--add-service`: Aggiunge un servizio a una zona.
- `--remove-service`: Rimuove un servizio da una zona.
- `--add-port`: Aggiunge una porta a una zona.
- `--remove-port`: Rimuove una porta da una zona.
- `--list-all`: Mostra tutte le regole e le configurazioni per una zona specifica.

## Common Examples

### Aggiungere un servizio a una zona
Per aggiungere il servizio HTTP alla zona pubblica, puoi usare il seguente comando:

```bash
firewall-cmd --zone=public --add-service=http
```

### Rimuovere un servizio da una zona
Per rimuovere il servizio SSH dalla zona privata:

```bash
firewall-cmd --zone=private --remove-service=ssh
```

### Aggiungere una porta specifica
Se desideri aprire la porta 8080 nella zona di lavoro:

```bash
firewall-cmd --zone=work --add-port=8080/tcp
```

### Visualizzare tutte le regole di una zona
Per vedere tutte le regole configurate nella zona pubblica:

```bash
firewall-cmd --zone=public --list-all
```

## Tips
- Assicurati di utilizzare il comando `--permanent` se desideri che le modifiche siano permanenti e non solo temporanee fino al riavvio del servizio.
- Usa `firewall-cmd --reload` dopo aver apportato modifiche permanenti per applicarle immediatamente.
- Controlla frequentemente le configurazioni del firewall per garantire che non ci siano regole indesiderate o obsolete.