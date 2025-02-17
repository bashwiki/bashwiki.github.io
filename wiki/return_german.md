# [Linux] Bash return Verwendung: Gibt den Rückgabewert eines Skripts oder Befehls zurück

## Übersicht
Der `return`-Befehl in Bash wird verwendet, um einen Rückgabewert aus einer Funktion zurückzugeben. Dies ist besonders nützlich, um den Status einer Funktion zu überprüfen oder um Fehlercodes zu kommunizieren.

## Verwendung
Die grundlegende Syntax des `return`-Befehls lautet:

```bash
return [options] [status]
```

## Häufige Optionen
- `status`: Eine Ganzzahl, die den Rückgabewert angibt. Standardmäßig ist dies 0, was Erfolg bedeutet.

## Häufige Beispiele

### Beispiel 1: Rückgabewert einer Funktion
```bash
my_function() {
    return 5
}

my_function
echo $?  # Gibt 5 aus
```

### Beispiel 2: Rückgabewert basierend auf einer Bedingung
```bash
check_file() {
    if [[ -f "$1" ]]; then
        return 0  # Datei existiert
    else
        return 1  # Datei existiert nicht
    fi
}

check_file "test.txt"
echo $?  # Gibt 0 oder 1 aus, je nach Ergebnis
```

### Beispiel 3: Verwendung in einer Schleife
```bash
for i in {1..5}; do
    if [[ $i -eq 3 ]]; then
        return 0  # Beende die Funktion, wenn i 3 ist
    fi
done
```

## Tipps
- Verwenden Sie `return` in Funktionen, um den Status oder Fehlercodes klar zu kommunizieren.
- Nutzen Sie `$?`, um den Rückgabewert des letzten ausgeführten Befehls oder der Funktion zu überprüfen.
- Halten Sie Rückgabewerte im Bereich von 0 bis 255, da dies die Standardgrenze für Rückgabewerte in Bash ist.