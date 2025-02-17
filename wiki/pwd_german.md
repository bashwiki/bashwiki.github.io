# [Linux] Bash pwd Verwendung: Zeigt das aktuelle Verzeichnis an

## Übersicht
Der Befehl `pwd` (print working directory) wird in der Bash verwendet, um das aktuelle Arbeitsverzeichnis anzuzeigen. Er gibt den vollständigen Pfad des Verzeichnisses zurück, in dem sich der Benutzer gerade befindet.

## Verwendung
Die grundlegende Syntax des Befehls ist wie folgt:

```bash
pwd [Optionen]
```

## Häufige Optionen
- `-L`: Zeigt den logischen Pfad des aktuellen Verzeichnisses an (Standardverhalten).
- `-P`: Zeigt den physischen Pfad des aktuellen Verzeichnisses an, wobei symbolische Links aufgelöst werden.

## Häufige Beispiele
Hier sind einige praktische Beispiele zur Verwendung des `pwd`-Befehls:

1. **Einfaches Anzeigen des aktuellen Verzeichnisses:**

   ```bash
   pwd
   ```

2. **Anzeigen des physischen Pfades:**

   ```bash
   pwd -P
   ```

3. **Anzeigen des logischen Pfades (Standardverhalten):**

   ```bash
   pwd -L
   ```

## Tipps
- Verwenden Sie `pwd` regelmäßig, um sich zu vergewissern, in welchem Verzeichnis Sie sich befinden, insbesondere wenn Sie mit mehreren Verzeichnissen arbeiten.
- Kombinieren Sie `pwd` mit anderen Befehlen, um Skripte zu erstellen, die den aktuellen Pfad dynamisch verwenden.