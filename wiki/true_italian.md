# [Linux] Bash true uso equivalente: Restituisce sempre un valore di uscita vero

## Overview
Il comando `true` in Bash è un comando molto semplice che restituisce sempre un valore di uscita vero (0). È spesso utilizzato in script per indicare che un'operazione è andata a buon fine o per creare cicli infiniti.

## Usage
La sintassi di base del comando `true` è la seguente:

```
true [options] [arguments]
```

## Common Options
Il comando `true` non ha opzioni specifiche. La sua funzione principale è semplicemente quella di restituire un valore di uscita di 0.

## Common Examples

### Esempio 1: Utilizzo di true in uno script
Puoi utilizzare `true` in uno script per indicare che un'operazione è stata completata con successo.

```bash
#!/bin/bash
echo "Inizio dello script"
true
echo "Operazione completata con successo"
```

### Esempio 2: Creare un ciclo infinito
Il comando `true` è utile per creare un ciclo infinito.

```bash
while true; do
    echo "Questo è un ciclo infinito. Premi Ctrl+C per uscire."
    sleep 1
done
```

### Esempio 3: Utilizzo con comandi condizionali
Puoi utilizzare `true` per forzare un comando a restituire un valore di uscita vero.

```bash
if true; then
    echo "Questa condizione è sempre vera."
fi
```

## Tips
- Utilizza `true` per semplificare la logica nei tuoi script, specialmente quando hai bisogno di un comando che non faccia nulla ma restituisca un valore di uscita positivo.
- Ricorda che `true` è utile anche in combinazione con comandi come `&&` e `||` per controllare il flusso di esecuzione in base ai risultati di altri comandi.