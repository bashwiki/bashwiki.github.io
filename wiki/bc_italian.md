# [리눅스] Bash bc 사용법

## Overview
Il comando `bc` (Basic Calculator) è un linguaggio di calcolo arbitrario che consente di eseguire operazioni matematiche in modo interattivo o tramite script. È particolarmente utile per ingegneri e sviluppatori che necessitano di effettuare calcoli complessi, poiché supporta operazioni con numeri interi e decimali, funzioni matematiche e variabili.

## Usage
La sintassi di base del comando `bc` è la seguente:

```bash
bc [opzioni] [file]
```

### Opzioni comuni:
- `-l`: Carica la libreria matematica standard, che fornisce funzioni matematiche come `sine`, `cosine`, `square root`, ecc.
- `-q`: Esegue `bc` in modalità silenziosa, disabilitando il messaggio di benvenuto.
- `-e`: Esegue un'espressione specificata direttamente dalla riga di comando.

## Examples
### Esempio 1: Calcolo semplice
Puoi avviare `bc` e inserire direttamente le espressioni matematiche:

```bash
echo "5 + 3" | bc
```
Output:
```
8
```

### Esempio 2: Utilizzo della libreria matematica
Utilizzando l'opzione `-l`, puoi calcolare funzioni matematiche:

```bash
echo "scale=2; sqrt(16)" | bc -l
```
Output:
```
4.00
```

## Tips
- Usa `scale` per definire il numero di cifre decimali nei risultati. Ad esempio, `scale=3; 1/3` restituirà `0.333`.
- Puoi salvare le espressioni in un file e quindi eseguire `bc` su quel file per calcoli più complessi. Ad esempio, crea un file `calcoli.txt` con il contenuto:
  ```
  a = 5
  b = 10
  a + b
  ```
  E poi esegui:
  ```bash
  bc calcoli.txt
  ```
- Ricorda che `bc` tratta i numeri come interi per impostazione predefinita, quindi assicurati di impostare `scale` se hai bisogno di risultati in virgola mobile.