# [리눅스] Bash true 사용법

## Overview
Il comando `true` è un comando di shell in Bash che non fa nulla e restituisce sempre un codice di uscita di successo (0). È comunemente utilizzato in script e comandi per indicare che un'operazione è stata completata con successo, senza eseguire alcuna azione. Questo comando è utile in vari contesti, come nei cicli o nelle condizioni, dove è necessario un comando che non influisca sul flusso di esecuzione.

## Usage
La sintassi di base del comando `true` è molto semplice:

```bash
true
```

Non ci sono opzioni comuni associate al comando `true`, poiché il suo scopo è semplicemente quello di restituire un codice di uscita di successo senza ulteriori parametri.

## Examples
Ecco alcuni esempi pratici su come utilizzare il comando `true`.

### Esempio 1: Utilizzo in un ciclo
Puoi utilizzare `true` in un ciclo `while` per creare un ciclo infinito che può essere interrotto da un comando esterno:

```bash
while true; do
    echo "Questo ciclo continuerà fino a quando non verrà interrotto."
    sleep 1
done
```

### Esempio 2: Condizione di successo
Puoi utilizzare `true` per testare una condizione in uno script:

```bash
if true; then
    echo "La condizione è vera!"
else
    echo "Questo non verrà mai stampato."
fi
```

## Tips
- Utilizza `true` quando hai bisogno di un comando che non faccia nulla ma che restituisca un codice di uscita di successo. Questo può essere utile per testare il flusso di lavoro nei tuoi script.
- In combinazione con `false`, puoi creare script di test per verificare il comportamento di altre parti del tuo codice in base ai codici di uscita.
- Ricorda che `true` è un comando molto leggero e non consuma risorse, quindi è ideale per l'uso in script complessi dove la semplicità è fondamentale.