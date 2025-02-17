# [Linux] Bash column uso: [formattare l'output in colonne]

## Overview
Il comando `column` in Bash è utilizzato per formattare l'output di testo in colonne ordinate. Questo è particolarmente utile quando si desidera visualizzare dati tabulari in modo chiaro e leggibile.

## Usage
La sintassi di base del comando è la seguente:

```bash
column [options] [arguments]
```

## Common Options
- `-t`: Allinea i dati in colonne, separando automaticamente i campi in base agli spazi.
- `-s`: Specifica un delimitatore personalizzato per separare i campi (ad esempio, una virgola).
- `-n`: Disabilita l'allineamento delle colonne, mantenendo il testo originale.

## Common Examples
Ecco alcuni esempi pratici dell'uso del comando `column`:

1. **Allineare l'output in colonne**:
   ```bash
   cat file.txt | column -t
   ```

2. **Utilizzare un delimitatore personalizzato**:
   ```bash
   cat file.csv | column -s, -t
   ```

3. **Visualizzare l'output di un comando in colonne**:
   ```bash
   ls -l | column -t
   ```

4. **Disabilitare l'allineamento**:
   ```bash
   echo -e "Nome Età\nAlice 30\nBob 25" | column -n
   ```

## Tips
- Quando si utilizza il delimitatore `-s`, assicurati che il delimitatore non sia presente nei dati per evitare confusione.
- Puoi combinare `column` con altri comandi Unix per migliorare la leggibilità dell'output.
- Prova a utilizzare `column` con file di log o output di comandi complessi per ottenere una visualizzazione più chiara.