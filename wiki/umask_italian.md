# [리눅스] Bash umask 사용법

## Panoramica
Il comando `umask` in Bash è utilizzato per impostare il valore di maschera dei permessi predefiniti per i nuovi file e directory creati nel sistema. La maschera dei permessi determina quali permessi (lettura, scrittura, esecuzione) vengono negati ai file e alle directory appena creati. In sostanza, `umask` controlla i permessi di accesso iniziali per gli utenti e i gruppi.

## Utilizzo
La sintassi di base del comando `umask` è la seguente:

```bash
umask [opzioni] [maschera]
```

### Opzioni comuni
- **-S**: Mostra la maschera dei permessi in forma simbolica.
- **-p**: Mostra la maschera dei permessi corrente in forma simbolica, utile per visualizzare i permessi senza modificarli.

## Esempi
### Esempio 1: Visualizzare la maschera corrente
Per visualizzare la maschera dei permessi attuale, puoi semplicemente eseguire:

```bash
umask
```

Questo comando restituirà un valore numerico che rappresenta la maschera dei permessi attuale.

### Esempio 2: Impostare una nuova maschera
Se desideri impostare una nuova maschera, ad esempio per negare i permessi di scrittura per il gruppo e altri utenti, puoi utilizzare:

```bash
umask 022
```

In questo caso, i nuovi file creati avranno permessi di `rw-r--r--`, mentre le nuove directory avranno permessi di `rwxr-xr-x`.

## Suggerimenti
- È buona pratica controllare la maschera dei permessi prima di creare file o directory, specialmente in ambienti condivisi, per garantire che i permessi siano configurati correttamente.
- Ricorda che la maschera dei permessi è applicata solo ai nuovi file e directory; non modifica i permessi di file o directory esistenti.
- Puoi aggiungere il comando `umask` nel tuo file di configurazione della shell (come `.bashrc` o `.bash_profile`) per impostare automaticamente la maschera desiderata all'avvio della sessione.