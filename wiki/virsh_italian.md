# [Linux] Bash virsh uso: Gestire macchine virtuali

## Overview
Il comando `virsh` è uno strumento da riga di comando utilizzato per gestire macchine virtuali attraverso l'interfaccia di virtualizzazione libvirt. Permette agli utenti di creare, modificare, avviare e fermare macchine virtuali, oltre a fornire informazioni dettagliate sulle stesse.

## Usage
La sintassi di base del comando `virsh` è la seguente:

```bash
virsh [opzioni] [argomenti]
```

## Common Options
Ecco alcune opzioni comuni per il comando `virsh`:

- `list`: Elenca le macchine virtuali attive.
- `start <nome_vm>`: Avvia una macchina virtuale specificata.
- `shutdown <nome_vm>`: Spegne una macchina virtuale in modo controllato.
- `destroy <nome_vm>`: Ferma forzatamente una macchina virtuale.
- `define <file.xml>`: Crea una macchina virtuale da un file di configurazione XML.
- `edit <nome_vm>`: Modifica la configurazione di una macchina virtuale.

## Common Examples
Ecco alcuni esempi pratici di utilizzo del comando `virsh`:

- **Elencare le macchine virtuali attive:**
  ```bash
  virsh list
  ```

- **Avviare una macchina virtuale chiamata "vm1":**
  ```bash
  virsh start vm1
  ```

- **Spegnere una macchina virtuale chiamata "vm1":**
  ```bash
  virsh shutdown vm1
  ```

- **Fermare forzatamente una macchina virtuale chiamata "vm1":**
  ```bash
  virsh destroy vm1
  ```

- **Creare una macchina virtuale da un file XML:**
  ```bash
  virsh define /path/to/vm.xml
  ```

- **Modificare la configurazione di una macchina virtuale chiamata "vm1":**
  ```bash
  virsh edit vm1
  ```

## Tips
- Assicurati di avere i permessi necessari per gestire le macchine virtuali, poiché alcune operazioni richiedono privilegi di amministratore.
- Utilizza `virsh help` per visualizzare un elenco completo dei comandi e delle opzioni disponibili.
- Fai sempre un backup della configurazione delle macchine virtuali prima di apportare modifiche significative.