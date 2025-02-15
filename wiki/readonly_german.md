# [리눅스] Bash readonly 사용법

## Übersicht
Der Befehl `readonly` in Bash wird verwendet, um Variablen als schreibgeschützt zu deklarieren. Das bedeutet, dass einmal festgelegte Werte nicht mehr verändert werden können. Dies ist besonders nützlich, um sicherzustellen, dass kritische Variablen während der Ausführung eines Skripts nicht versehentlich geändert werden.

## Verwendung
Die grundlegende Syntax des `readonly`-Befehls lautet:

```bash
readonly VARIABLE_NAME=VALUE
```

oder um eine bereits definierte Variable schreibgeschützt zu machen:

```bash
readonly VARIABLE_NAME
```

### Optionen
- Es gibt keine speziellen Optionen für den `readonly`-Befehl, da er hauptsächlich dazu dient, Variablen zu deklarieren oder deren Schreibschutz aufzuheben.

## Beispiele
Hier sind einige praktische Beispiele zur Verwendung des `readonly`-Befehls:

### Beispiel 1: Eine neue schreibgeschützte Variable erstellen
```bash
readonly PI=3.14
echo $PI  # Ausgabe: 3.14
```
In diesem Beispiel wird die Variable `PI` mit dem Wert `3.14` erstellt und als schreibgeschützt deklariert. Ein Versuch, den Wert von `PI` zu ändern, führt zu einem Fehler.

### Beispiel 2: Eine bestehende Variable schreibgeschützt machen
```bash
MY_VAR="Hello"
readonly MY_VAR
MY_VAR="World"  # Fehler: cannot assign to readonly variable
```
Hier wird die Variable `MY_VAR` zuerst mit dem Wert "Hello" erstellt und dann als schreibgeschützt deklariert. Ein Versuch, den Wert auf "World" zu ändern, schlägt fehl.

## Tipps
- Verwenden Sie `readonly` für Variablen, die während der Ausführung eines Skripts nicht verändert werden sollen, um unbeabsichtigte Fehler zu vermeiden.
- Sie können die Liste der schreibgeschützten Variablen mit dem Befehl `declare -r` oder `declare -p` anzeigen.
- Beachten Sie, dass `readonly` nur für die aktuelle Shell-Sitzung gilt. Wenn Sie ein Skript beenden und erneut starten, müssen Sie die `readonly`-Deklarationen erneut vornehmen.