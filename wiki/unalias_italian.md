# [Linux] Bash unalias uso: Rimuovere alias dalla sessione corrente

## Overview
Il comando `unalias` in Bash viene utilizzato per rimuovere alias precedentemente definiti. Gli alias sono scorciatoie per comandi più lunghi e possono semplificare l'uso della shell. Tuttavia, a volte è necessario rimuovere un alias per ripristinare il comportamento predefinito di un comando.

## Usage
La sintassi di base del comando `unalias` è la seguente:

```bash
unalias [options] [arguments]
```

## Common Options
- `-a`: Rimuove tutti gli alias definiti nella sessione corrente.
- `-m`: Rimuove gli alias che corrispondono a un pattern specificato.

## Common Examples
Ecco alcuni esempi pratici dell'uso del comando `unalias`:

1. **Rimuovere un alias specifico**:
   Se hai definito un alias chiamato `ll` e desideri rimuoverlo, puoi eseguire:
   ```bash
   unalias ll
   ```

2. **Rimuovere tutti gli alias**:
   Per rimuovere tutti gli alias definiti nella sessione corrente, utilizza l'opzione `-a`:
   ```bash
   unalias -a
   ```

3. **Rimuovere alias che corrispondono a un pattern**:
   Se hai alias che iniziano con `g` e vuoi rimuoverli, puoi usare:
   ```bash
   unalias g*
   ```

## Tips
- È buona pratica controllare gli alias definiti con il comando `alias` prima di rimuoverli, per evitare di eliminare alias importanti.
- Ricorda che gli alias sono temporanei e vengono persi alla chiusura della sessione, a meno che non siano definiti nel file di configurazione della shell.
- Se desideri rendere permanenti le modifiche, considera di rimuovere gli alias dal file di configurazione della tua shell, come `.bashrc` o `.bash_profile`.