# [Linux] Bash iostat Verwendung: Überwachung der Systemleistung

## Übersicht
Der Befehl `iostat` wird verwendet, um die Input/Output-Statistiken von Systemgeräten und Partitionen zu überwachen. Er hilft dabei, die Leistung von Festplatten und anderen Speichermedien zu analysieren, indem er Informationen über die Nutzung und die Auslastung bereitstellt.

## Verwendung
Die grundlegende Syntax des Befehls lautet:

```bash
iostat [Optionen] [Argumente]
```

## Häufige Optionen
- `-c`: Zeigt CPU-Nutzungsstatistiken an.
- `-d`: Zeigt Geräte-Statistiken an.
- `-x`: Zeigt erweiterte Statistiken für Geräte an.
- `-m`: Gibt die Ausgabe in Megabyte pro Sekunde aus.
- `-t`: Fügt einen Zeitstempel zur Ausgabe hinzu.

## Häufige Beispiele
Hier sind einige praktische Beispiele für die Verwendung von `iostat`:

1. **Einfacher Befehl zur Anzeige der CPU-Statistiken:**
   ```bash
   iostat -c
   ```

2. **Geräte-Statistiken anzeigen:**
   ```bash
   iostat -d
   ```

3. **Erweiterte Statistiken für alle Geräte anzeigen:**
   ```bash
   iostat -x
   ```

4. **Statistiken alle 5 Sekunden anzeigen:**
   ```bash
   iostat -d 5
   ```

5. **Ausgabe in Megabyte pro Sekunde:**
   ```bash
   iostat -m
   ```

## Tipps
- Verwenden Sie die Option `-t`, um Zeitstempel zu Ihrer Ausgabe hinzuzufügen, was die Analyse über längere Zeiträume erleichtert.
- Kombinieren Sie Optionen, um detailliertere Informationen zu erhalten, z.B. `iostat -c -d -x`.
- Überwachen Sie regelmäßig die I/O-Statistiken, um Engpässe in der Systemleistung frühzeitig zu erkennen.