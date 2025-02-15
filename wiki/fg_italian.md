# [리눅스] Bash fg 사용법

## Overview
Il comando `fg` in Bash è utilizzato per riportare un processo in esecuzione in background al primo piano (foreground). Questo è particolarmente utile quando si desidera interagire direttamente con un processo che è stato avviato in background, consentendo all'utente di fornire input o visualizzare output in tempo reale.

## Usage
La sintassi di base del comando `fg` è la seguente:

```bash
fg [job_spec]
```

- `job_spec`: Specifica quale processo portare in primo piano. Può essere un numero di lavoro (ad esempio, `%1`, `%2`, ecc.) o un nome di processo.

Se non viene fornito alcun argomento, `fg` porterà in primo piano l'ultimo processo in background.

## Examples
### Esempio 1: Riportare l'ultimo processo in background
Supponiamo di avere avviato un processo in background, ad esempio un editor di testo:

```bash
nano myfile.txt &
```

Per riportare questo processo in primo piano, basta digitare:

```bash
fg
```

### Esempio 2: Riportare un processo specifico in primo piano
Se hai più processi in background, puoi specificare quale riportare in primo piano. Ad esempio, se hai avviato due processi in background:

```bash
sleep 100 &
sleep 200 &
```

Puoi riportare il primo processo in primo piano con:

```bash
fg %1
```

## Tips
- Utilizza il comando `jobs` per visualizzare l'elenco dei processi in background e i loro numeri di lavoro prima di utilizzare `fg`.
- Ricorda che quando un processo è in primo piano, puoi interromperlo con `Ctrl + C` o metterlo in background di nuovo con `Ctrl + Z`, seguito da `bg`.
- Se un processo non risponde come previsto, verifica che non ci siano conflitti di input/output con altri processi in esecuzione.