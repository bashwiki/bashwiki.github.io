# [리눅스] Bash blkid 사용법

## Overview
Il comando `blkid` è uno strumento di utilità in Linux utilizzato per identificare e visualizzare le informazioni sui dispositivi di blocco, come le partizioni del disco e i dispositivi di archiviazione. Il suo scopo principale è quello di fornire dettagli come l'UUID (Universally Unique Identifier), il tipo di filesystem e altre informazioni utili per la gestione dei dispositivi di archiviazione. Questo comando è particolarmente utile per gli amministratori di sistema e gli sviluppatori che devono gestire e configurare i dispositivi di archiviazione.

## Usage
La sintassi di base del comando `blkid` è la seguente:

```bash
blkid [opzioni] [file]
```

### Opzioni comuni:
- `-o` o `--output`: Specifica il formato di output. Può essere impostato su `value`, `full`, `list`, ecc.
- `-s` o `--match-tag`: Filtra l'output per mostrare solo le informazioni relative al tag specificato.
- `-p` o `--probe`: Forza la scansione dei dispositivi anche se non sono stati modificati.
- `-c` o `--cache`: Specifica un file di cache da utilizzare per memorizzare le informazioni sui dispositivi.

## Examples
### Esempio 1: Visualizzare tutte le informazioni sui dispositivi di blocco
Per visualizzare tutte le informazioni sui dispositivi di blocco presenti nel sistema, è possibile eseguire il comando senza alcuna opzione:

```bash
blkid
```

Questo comando restituirà un elenco di tutti i dispositivi di blocco, insieme ai loro UUID e tipi di filesystem.

### Esempio 2: Ottenere solo l'UUID di un dispositivo specifico
Se si desidera ottenere solo l'UUID di un dispositivo specifico, ad esempio `/dev/sda1`, si può utilizzare il comando come segue:

```bash
blkid -s UUID /dev/sda1
```

Questo comando mostrerà solo l'UUID del dispositivo `/dev/sda1`.

## Tips
- È consigliabile eseguire `blkid` con i privilegi di superutente (utilizzando `sudo`) per garantire l'accesso completo a tutte le informazioni sui dispositivi.
- Utilizzare l'opzione `-o value` per ottenere un output più pulito e facilmente leggibile, specialmente quando si desidera utilizzare le informazioni in script o automazioni.
- Se si notano discrepanze nelle informazioni, provare a utilizzare l'opzione `-p` per forzare una nuova scansione dei dispositivi.