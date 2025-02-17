# [Linux] Bash xmlstarlet utilizzo: Strumento per manipolare file XML

## Overview
Il comando `xmlstarlet` è uno strumento potente per la manipolazione di file XML. Permette di eseguire operazioni come la trasformazione, la validazione e la ricerca di dati all'interno di documenti XML, rendendolo utile per sviluppatori e amministratori di sistema.

## Usage
La sintassi di base del comando `xmlstarlet` è la seguente:

```bash
xmlstarlet [opzioni] [argomenti]
```

## Common Options
Ecco alcune opzioni comuni per `xmlstarlet`:

- `xmlstarlet sel`: Seleziona nodi da un documento XML.
- `xmlstarlet ed`: Modifica un documento XML esistente.
- `xmlstarlet val`: Valida un documento XML contro uno schema.
- `xmlstarlet tr`: Trasforma un documento XML utilizzando un foglio di stile XSLT.
- `xmlstarlet fo`: Formatta un documento XML per una migliore leggibilità.

## Common Examples

### Selezionare nodi
Per selezionare nodi specifici da un file XML, puoi usare il comando `sel`:

```bash
xmlstarlet sel -t -m "//elemento" -v "." -n file.xml
```

### Modificare un documento XML
Per aggiungere un nuovo nodo a un documento XML, utilizza il comando `ed`:

```bash
xmlstarlet ed -a "/radice" -t -n "nuovoElemento" -v "valore" file.xml
```

### Validare un documento XML
Per validare un file XML contro uno schema XSD, usa il comando `val`:

```bash
xmlstarlet val -e schema.xsd file.xml
```

### Trasformare un documento XML
Per trasformare un file XML usando un foglio di stile XSLT, puoi utilizzare il comando `tr`:

```bash
xmlstarlet tr foglio.xslt file.xml
```

### Formattare un documento XML
Per formattare un documento XML per una migliore leggibilità, usa il comando `fo`:

```bash
xmlstarlet fo file.xml
```

## Tips
- Assicurati di avere una copia di backup dei tuoi file XML prima di eseguire modifiche.
- Utilizza il comando `--help` per visualizzare tutte le opzioni disponibili e ottenere ulteriori dettagli.
- Sperimenta con piccole modifiche per comprendere meglio come funziona `xmlstarlet` prima di applicare cambiamenti a file più complessi.