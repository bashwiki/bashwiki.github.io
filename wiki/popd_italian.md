# [Linux] Bash popd uso equivalente: Rimuove la directory dalla stack

## Overview
Il comando `popd` è utilizzato per rimuovere la directory superiore dalla stack delle directory. Questo comando è particolarmente utile quando si naviga tra diverse directory utilizzando `pushd`, poiché consente di tornare rapidamente alla directory precedente.

## Usage
La sintassi di base del comando è la seguente:

```bash
popd [options]
```

## Common Options
- `-n`: Non cambia la directory corrente, ma rimuove la directory dalla stack.
- `+n`: Rimuove la directory specificata dalla stack, dove `n` è l'indice della directory nella stack.

## Common Examples

### Esempio 1: Rimuovere la directory superiore dalla stack
```bash
pushd /home/utente/progetto
pushd /home/utente/documenti
popd
```
In questo esempio, `popd` rimuove `/home/utente/documenti` dalla stack e torna a `/home/utente/progetto`.

### Esempio 2: Usare l'opzione -n
```bash
pushd /home/utente/progetto
pushd /home/utente/documenti
popd -n
```
Qui, `popd -n` rimuove `/home/utente/documenti` dalla stack senza cambiare la directory corrente.

### Esempio 3: Usare l'opzione +n
```bash
pushd /home/utente/progetto
pushd /home/utente/documenti
pushd /home/utente/immagini
popd +1
```
In questo caso, `popd +1` rimuove `/home/utente/documenti` dalla stack, mantenendo la directory corrente su `/home/utente/immagini`.

## Tips
- Utilizza `pushd` e `popd` insieme per una navigazione efficiente tra le directory.
- Controlla la stack delle directory corrente con il comando `dirs` per avere un'idea chiara di dove ti trovi.
- Ricorda che l'uso di `popd` senza argomenti rimuove sempre la directory superiore dalla stack.