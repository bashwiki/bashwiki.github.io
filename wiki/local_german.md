# [리눅스] Bash local 사용법

## Übersicht
Der Befehl `local` in Bash wird verwendet, um lokale Variablen innerhalb einer Funktion zu deklarieren. Diese Variablen sind nur innerhalb der Funktion sichtbar und existieren nicht außerhalb dieser. Der Hauptzweck des `local`-Befehls besteht darin, den Geltungsbereich von Variablen zu kontrollieren und Namenskonflikte zu vermeiden, die auftreten können, wenn mehrere Funktionen dieselben Variablennamen verwenden.

## Verwendung
Die grundlegende Syntax des `local`-Befehls lautet:

```bash
local [Optionen] Name[=Wert]
```

- `Name`: Der Name der Variablen, die lokal deklariert werden soll.
- `Wert`: (Optional) Der Wert, der der Variablen zugewiesen werden soll.

### Häufige Optionen
Der `local`-Befehl hat keine speziellen Optionen, die direkt verwendet werden. Er wird hauptsächlich in Funktionen verwendet, um Variablen zu deklarieren.

## Beispiele

### Beispiel 1: Einfache lokale Variable
Hier ist ein einfaches Beispiel, das zeigt, wie `local` verwendet wird, um eine lokale Variable in einer Funktion zu erstellen:

```bash
#!/bin/bash

meine_funktion() {
    local lokale_variable="Hallo, Welt!"
    echo $lokale_variable
}

meine_funktion
echo $lokale_variable  # Diese Zeile gibt nichts aus, da die Variable lokal ist.
```

In diesem Beispiel wird die Variable `lokale_variable` innerhalb der Funktion `meine_funktion` deklariert und ist außerhalb dieser Funktion nicht sichtbar.

### Beispiel 2: Verwendung mit Berechnungen
Hier ist ein weiteres Beispiel, das zeigt, wie `local` in einer Funktion verwendet werden kann, um Berechnungen durchzuführen:

```bash
#!/bin/bash

berechne_summe() {
    local zahl1=5
    local zahl2=10
    local summe=$((zahl1 + zahl2))
    echo "Die Summe ist: $summe"
}

berechne_summe
```

In diesem Beispiel werden die Variablen `zahl1`, `zahl2` und `summe` lokal innerhalb der Funktion `berechne_summe` deklariert.

## Tipps
- Verwenden Sie `local`, um den Geltungsbereich Ihrer Variablen zu steuern und unerwartete Konflikte mit globalen Variablen zu vermeiden.
- Es ist eine gute Praxis, Variablen innerhalb von Funktionen lokal zu deklarieren, es sei denn, es ist unbedingt erforderlich, dass sie global sind.
- Dokumentieren Sie die Verwendung von `local` in Ihren Funktionen, um die Lesbarkeit und Wartbarkeit Ihres Codes zu verbessern.