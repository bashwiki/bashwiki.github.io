# [리눅스] Bash pushd 사용법

## Overview
Il comando `pushd` è utilizzato nella shell Bash per gestire la directory corrente e la stack delle directory. La sua funzione principale è quella di cambiare la directory corrente e, contemporaneamente, memorizzare la directory precedente in una pila. Questo permette di navigare facilmente tra le directory senza perdere il riferimento a quelle già visitate.

## Usage
La sintassi di base del comando `pushd` è la seguente:

```bash
pushd [directory]
```

### Opzioni comuni:
- **directory**: Specifica la directory nella quale si desidera spostarsi. Se non viene fornita alcuna directory, `pushd` scambia la directory corrente con quella in cima alla pila.

## Examples
### Esempio 1: Spostarsi in una directory specifica
Supponiamo di voler passare alla directory `/home/utente/progetti`:

```bash
pushd /home/utente/progetti
```

Dopo aver eseguito questo comando, la directory corrente sarà `/home/utente/progetti`, e la directory precedente sarà memorizzata nella pila.

### Esempio 2: Tornare alla directory precedente
Se desideri tornare alla directory precedente che hai appena lasciato, puoi utilizzare il comando `popd`:

```bash
popd
```

Questo comando ti riporterà alla directory che era in cima alla pila, ripristinando la tua posizione precedente.

## Tips
- Utilizza `dirs` per visualizzare la pila delle directory attualmente memorizzate. Questo ti permette di vedere rapidamente quali directory hai visitato.
- Ricorda che puoi usare `pushd` senza argomenti per scambiare la directory corrente con quella in cima alla pila, facilitando la navigazione avanti e indietro tra le directory.
- È utile combinare `pushd` con script o comandi complessi per mantenere il contesto della directory durante l'esecuzione di operazioni multiple.