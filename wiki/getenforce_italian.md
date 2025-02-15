# [리눅스] Bash getenforce 사용법

## Overview
Il comando `getenforce` è utilizzato per visualizzare lo stato attuale della modalità di sicurezza SELinux (Security-Enhanced Linux) su un sistema Linux. SELinux è un modulo di sicurezza del kernel Linux che fornisce un controllo degli accessi obbligatorio. Il comando `getenforce` restituisce uno dei seguenti tre stati: `Enforcing`, `Permissive` o `Disabled`, che indicano rispettivamente se SELinux è attivo e sta applicando le politiche di sicurezza, se è in modalità permissiva (dove le violazioni delle politiche vengono registrate ma non bloccate), o se è disabilitato.

## Usage
La sintassi di base del comando `getenforce` è la seguente:

```bash
getenforce
```

Non ci sono opzioni comuni da utilizzare con questo comando, poiché il suo scopo principale è semplicemente restituire lo stato attuale di SELinux.

## Examples
Ecco alcuni esempi pratici su come utilizzare il comando `getenforce`.

### Esempio 1: Controllare lo stato di SELinux
Per verificare rapidamente lo stato di SELinux, basta eseguire:

```bash
getenforce
```

L'output potrebbe essere uno dei seguenti:
- `Enforcing`
- `Permissive`
- `Disabled`

### Esempio 2: Utilizzare in uno script
Puoi utilizzare `getenforce` all'interno di uno script Bash per prendere decisioni basate sullo stato di SELinux. Ecco un esempio:

```bash
#!/bin/bash

if [ "$(getenforce)" == "Enforcing" ]; then
    echo "SELinux è attivo e sta applicando le politiche di sicurezza."
else
    echo "SELinux non è in modalità enforcing."
fi
```

## Tips
- È buona prassi controllare lo stato di SELinux prima di eseguire applicazioni o servizi che potrebbero essere influenzati dalle politiche di sicurezza.
- Se stai sviluppando o testando software, considera di utilizzare la modalità `Permissive` per facilitare il debug, ma ricorda di passare a `Enforcing` per la produzione per garantire la sicurezza del sistema.
- Puoi combinare `getenforce` con altri comandi per automatizzare la gestione della sicurezza nel tuo ambiente di sviluppo o produzione.