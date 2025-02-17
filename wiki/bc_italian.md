# [Linux] Bash bc utilizzo: Calcolatrice arbitraria

## Overview
Il comando `bc` è un linguaggio di calcolo arbitrario che consente di eseguire operazioni matematiche direttamente dalla riga di comando. È utile per effettuare calcoli complessi e per la manipolazione di numeri in formato decimale.

## Usage
La sintassi di base del comando `bc` è la seguente:

```bash
bc [options] [arguments]
```

## Common Options
- `-l`: Carica la libreria matematica standard, che include funzioni matematiche come seno, coseno e radice quadrata.
- `-q`: Esegue `bc` in modalità silenziosa, disabilitando il messaggio di benvenuto.
- `-e`: Permette di eseguire comandi specificati direttamente dalla riga di comando.

## Common Examples
Ecco alcuni esempi pratici dell'uso di `bc`:

### Esempio 1: Calcolo semplice
Per eseguire un semplice calcolo, come la somma di due numeri:

```bash
echo "5 + 3" | bc
```

### Esempio 2: Divisione con precisione
Per eseguire una divisione e ottenere un risultato con decimali:

```bash
echo "scale=2; 10 / 3" | bc
```

### Esempio 3: Utilizzo della libreria matematica
Per calcolare la radice quadrata di un numero utilizzando la libreria matematica:

```bash
echo "scale=4; sqrt(16)" | bc -l
```

### Esempio 4: Operazioni complesse
Per eseguire un'espressione più complessa:

```bash
echo "scale=3; (2 + 3) * (5 - 2) / 2" | bc
```

## Tips
- Utilizza `scale` per definire il numero di cifre decimali nel risultato.
- Ricorda che `bc` tratta i numeri come interi per impostazione predefinita, quindi specifica `scale` per ottenere risultati decimali.
- Puoi salvare le espressioni in un file e utilizzare `bc` per eseguire calcoli complessi in batch.