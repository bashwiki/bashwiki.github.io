# [리눅스] Bash typeset 사용법

## Übersicht
Der Befehl `typeset` in Bash wird verwendet, um Variablen zu deklarieren und deren Eigenschaften festzulegen. Er ermöglicht es Entwicklern, Variablen als lokal oder global zu definieren und spezifische Attribute wie den Datentyp oder die Sichtbarkeit festzulegen. `typeset` ist besonders nützlich in Funktionen, um sicherzustellen, dass Variablen nicht versehentlich global verändert werden.

## Verwendung
Die grundlegende Syntax des `typeset`-Befehls lautet:

```bash
typeset [Optionen] [Variablenname[=Wert]]
```

### Häufige Optionen:
- `-i`: Deklariert die Variable als Ganzzahl. Alle Zuweisungen an diese Variable werden als Ganzzahlen interpretiert.
- `-r`: Macht die Variable schreibgeschützt. Änderungen an dieser Variable sind nicht möglich, nachdem sie einmal gesetzt wurde.
- `-a`: Deklariert die Variable als Array.
- `-x`: Exportiert die Variable in die Umgebung, sodass sie für untergeordnete Prozesse verfügbar ist.

## Beispiele
### Beispiel 1: Ganzzahl-Deklaration
```bash
typeset -i zahl=10
zahl=zahl+5
echo $zahl  # Ausgabe: 15
```
In diesem Beispiel wird die Variable `zahl` als Ganzzahl deklariert. Die Berechnung wird korrekt als Ganzzahl durchgeführt.

### Beispiel 2: Schreibgeschützte Variable
```bash
typeset -r konstant=100
echo $konstant  # Ausgabe: 100
konstant=200    # Fehler: kann nicht geändert werden
```
Hier wird die Variable `konstant` als schreibgeschützt deklariert. Ein Versuch, den Wert zu ändern, führt zu einem Fehler.

## Tipps
- Verwenden Sie `typeset` innerhalb von Funktionen, um die Sichtbarkeit von Variablen zu steuern und Konflikte mit globalen Variablen zu vermeiden.
- Nutzen Sie die verschiedenen Optionen, um die Variablenverwendung zu optimieren und sicherzustellen, dass die Variablen die gewünschten Eigenschaften haben.
- Beachten Sie, dass `typeset` in Bash spezifisch ist und nicht in anderen Shells wie `sh` oder `dash` verfügbar sein könnte.