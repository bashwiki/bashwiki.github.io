# [Linux] Bash bc Verwendung: Ein Taschenrechner für die Kommandozeile

## Übersicht
Der Befehl `bc` (Basic Calculator) ist ein leistungsfähiger Taschenrechner, der in der Kommandozeile von Unix-ähnlichen Betriebssystemen verwendet wird. Er ermöglicht die Durchführung von mathematischen Berechnungen mit hoher Präzision und unterstützt sowohl Ganzzahlen als auch Fließkommazahlen.

## Verwendung
Die grundlegende Syntax des Befehls lautet:

```bash
bc [Optionen] [Argumente]
```

## Häufige Optionen
- `-l`: Lädt die mathematische Bibliothek, die zusätzliche Funktionen wie trigonometrische und logarithmische Berechnungen bereitstellt.
- `-q`: Schaltet die Ausgabe von Begrüßungsnachrichten ab und startet `bc` im "quiet" Modus.
- `-e`: Führt die angegebenen Befehle direkt aus und beendet `bc` danach.

## Häufige Beispiele
Hier sind einige praktische Beispiele für die Verwendung von `bc`:

1. **Einfache Addition**
   ```bash
   echo "3 + 5" | bc
   ```
   Ausgabe: `8`

2. **Fließkomma-Berechnung**
   ```bash
   echo "scale=2; 10 / 3" | bc
   ```
   Ausgabe: `3.33`

3. **Verwendung der mathematischen Bibliothek**
   ```bash
   echo "scale=4; s(1)" | bc -l
   ```
   Ausgabe: `0.8415`

4. **Berechnung mit Variablen**
   ```bash
   echo "a=5; b=10; a * b" | bc
   ```
   Ausgabe: `50`

5. **Komplexe Berechnung**
   ```bash
   echo "scale=3; (2 + 3) * (5 - 2) / 2" | bc
   ```
   Ausgabe: `7.500`

## Tipps
- Verwenden Sie `scale`, um die Anzahl der Dezimalstellen in den Ergebnissen zu steuern.
- Nutzen Sie die mathematische Bibliothek mit `-l`, um erweiterte Funktionen zu verwenden.
- Speichern Sie häufig verwendete Berechnungen in einer Datei und führen Sie sie mit `bc dateiname` aus, um Zeit zu sparen.