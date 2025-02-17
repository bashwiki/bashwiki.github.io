# [Linux] Bash systemctl utilizzo: Gestire i servizi di sistema

## Overview
Il comando `systemctl` è uno strumento fondamentale per gestire il sistema e i servizi su sistemi operativi Linux che utilizzano systemd come sistema di init. Permette di avviare, fermare, riavviare e controllare lo stato dei servizi, oltre a gestire i target e le unità di sistema.

## Usage
La sintassi di base del comando `systemctl` è la seguente:

```bash
systemctl [opzioni] [argomenti]
```

## Common Options
Ecco alcune opzioni comuni per `systemctl`:

- `start`: Avvia un'unità (servizio).
- `stop`: Ferma un'unità.
- `restart`: Riavvia un'unità.
- `status`: Mostra lo stato di un'unità.
- `enable`: Abilita un'unità per l'avvio automatico al boot.
- `disable`: Disabilita un'unità dall'avvio automatico al boot.
- `list-units`: Elenca tutte le unità attive.

## Common Examples
Ecco alcuni esempi pratici dell'uso di `systemctl`:

- Avviare un servizio:
    ```bash
    sudo systemctl start nome_servizio
    ```

- Fermare un servizio:
    ```bash
    sudo systemctl stop nome_servizio
    ```

- Riavviare un servizio:
    ```bash
    sudo systemctl restart nome_servizio
    ```

- Controllare lo stato di un servizio:
    ```bash
    systemctl status nome_servizio
    ```

- Abilitare un servizio all'avvio:
    ```bash
    sudo systemctl enable nome_servizio
    ```

- Disabilitare un servizio dall'avvio:
    ```bash
    sudo systemctl disable nome_servizio
    ```

- Elencare tutte le unità attive:
    ```bash
    systemctl list-units --type=service
    ```

## Tips
- Utilizza `sudo` per eseguire comandi che richiedono privilegi di amministratore.
- Controlla sempre lo stato di un servizio dopo averlo avviato o fermato per assicurarti che funzioni correttamente.
- Usa `systemctl list-units` per avere una panoramica dei servizi attivi e del loro stato.
- Ricorda che le modifiche alle unità richiedono spesso un riavvio del servizio per avere effetto.