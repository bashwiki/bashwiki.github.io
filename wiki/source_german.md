# [Linux] Bash source Verwendung: Skripte ausführen und Umgebungsvariablen laden

## Übersicht
Der `source` Befehl in Bash wird verwendet, um ein Skript in die aktuelle Shell-Umgebung zu laden und auszuführen. Dies bedeutet, dass alle Variablen und Funktionen, die im Skript definiert sind, in der aktuellen Shell verfügbar sind, ohne eine neue Shell zu starten.

## Verwendung
Die grundlegende Syntax des `source` Befehls lautet:

```bash
source [Optionen] [Argumente]
```

Alternativ kann der Befehl auch mit einem Punkt (`.`) verwendet werden:

```bash
. [Optionen] [Argumente]
```

## Häufige Optionen
- `-h`, `--help`: Zeigt die Hilfe für den Befehl an.
- `-V`, `--version`: Gibt die Versionsnummer des Bash-Interpreters aus.

## Häufige Beispiele

### Beispiel 1: Ein einfaches Skript ausführen
Angenommen, Sie haben ein Skript namens `mein_skript.sh`, das einige Umgebungsvariablen definiert:

```bash
source mein_skript.sh
```

### Beispiel 2: Ein Skript mit Punkt ausführen
Sie können das gleiche Skript auch mit einem Punkt ausführen:

```bash
. mein_skript.sh
```

### Beispiel 3: Variablen aus einem Skript verwenden
Wenn `mein_skript.sh` eine Variable `MEINE_VAR` definiert, können Sie sie nach dem Ausführen des Skripts verwenden:

```bash
echo $MEINE_VAR
```

### Beispiel 4: Skript aus einem anderen Verzeichnis ausführen
Wenn sich das Skript in einem anderen Verzeichnis befindet, geben Sie den vollständigen Pfad an:

```bash
source /pfad/zum/skript/mein_skript.sh
```

## Tipps
- Verwenden Sie `source`, um sicherzustellen, dass Änderungen an Umgebungsvariablen sofort in der aktuellen Shell wirksam werden.
- Achten Sie darauf, dass das Skript ausführbare Berechtigungen hat, wenn Sie es direkt ausführen möchten.
- Nutzen Sie die `-h` Option, um schnell Hilfe zu erhalten, falls Sie sich unsicher über die Verwendung des Befehls sind.