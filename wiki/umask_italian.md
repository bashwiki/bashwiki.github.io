# [Linux] Bash umask utilizzo: Imposta i permessi predefiniti per i file e le directory

## Overview
Il comando `umask` in Bash è utilizzato per impostare i permessi predefiniti per i nuovi file e directory creati. La maschera dei permessi determina quali permessi saranno negati ai file e alle directory appena creati.

## Usage
La sintassi di base del comando `umask` è la seguente:

```bash
umask [options] [arguments]
```

## Common Options
- `-S`: Mostra la maschera dei permessi in formato simbolico.
- `-p`: Mostra la maschera dei permessi corrente in formato simbolico, utile per visualizzare i permessi senza modificarli.

## Common Examples
Ecco alcuni esempi pratici di utilizzo del comando `umask`:

1. **Visualizzare la maschera dei permessi corrente**:
   ```bash
   umask
   ```

2. **Impostare una nuova maschera dei permessi**:
   Impostiamo la maschera per negare i permessi di scrittura per il gruppo e gli altri:
   ```bash
   umask 022
   ```

3. **Visualizzare la maschera dei permessi in formato simbolico**:
   ```bash
   umask -S
   ```

4. **Ripristinare la maschera predefinita**:
   Per ripristinare la maschera predefinita (077), puoi eseguire:
   ```bash
   umask 077
   ```

## Tips
- È buona pratica controllare la maschera dei permessi prima di creare file sensibili, per garantire che i permessi siano impostati correttamente.
- Ricorda che la maschera `umask` è applicata solo ai file e alle directory creati dopo la sua impostazione. Non influisce sui file già esistenti.
- Puoi aggiungere il comando `umask` nel tuo file di configurazione della shell (come `.bashrc` o `.bash_profile`) per impostare automaticamente la maschera desiderata all'avvio della sessione.