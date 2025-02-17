# [Linux] Bash env Verwendung: Umgebungsvariablen anzeigen und ändern

## Übersicht
Der Befehl `env` wird verwendet, um die Umgebungsvariablen eines Systems anzuzeigen oder neue Umgebungsvariablen für die Ausführung eines Befehls festzulegen. Dies ist besonders nützlich, um die Umgebung zu modifizieren, in der Programme ausgeführt werden.

## Verwendung
Die grundlegende Syntax des Befehls lautet:

```bash
env [Optionen] [Befehle]
```

## Häufige Optionen
- `-i`: Startet eine leere Umgebung, ohne bestehende Umgebungsvariablen zu erben.
- `-u VAR`: Entfernt die angegebene Umgebungsvariable `VAR`.
- `VAR=WERT`: Setzt eine Umgebungsvariable `VAR` auf den angegebenen `WERT` für den folgenden Befehl.

## Häufige Beispiele

### 1. Anzeigen aller Umgebungsvariablen
Um alle aktuellen Umgebungsvariablen anzuzeigen, können Sie einfach `env` ohne Argumente verwenden:

```bash
env
```

### 2. Ausführen eines Befehls mit einer neuen Umgebungsvariable
Um einen Befehl mit einer neuen Umgebungsvariable auszuführen, verwenden Sie die folgende Syntax:

```bash
VAR=WERT command
```

Beispiel:

```bash
MY_VAR=Hello env
```

### 3. Entfernen einer Umgebungsvariable
Um eine Umgebungsvariable zu entfernen, verwenden Sie die `-u` Option:

```bash
env -u MY_VAR command
```

### 4. Starten einer leeren Umgebung
Um einen Befehl in einer leeren Umgebung auszuführen, verwenden Sie die `-i` Option:

```bash
env -i command
```

## Tipps
- Verwenden Sie `env` in Skripten, um sicherzustellen, dass die richtigen Umgebungsvariablen gesetzt sind, bevor Sie einen Befehl ausführen.
- Seien Sie vorsichtig beim Entfernen von Umgebungsvariablen, da dies das Verhalten von Programmen beeinflussen kann.
- Nutzen Sie die `-i` Option, um sicherzustellen, dass keine unerwünschten Umgebungsvariablen geerbt werden, was besonders in Testumgebungen nützlich ist.