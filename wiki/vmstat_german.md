# [Linux] Bash vmstat Verwendung: Systemüberwachung und Leistungsanalyse

## Übersicht
Der Befehl `vmstat` (Virtual Memory Statistics) ist ein nützliches Werkzeug zur Überwachung von Systemressourcen in Echtzeit. Er liefert Informationen über den Zustand des Systems, einschließlich Speicher-, Prozess- und CPU-Nutzung, und hilft dabei, Engpässe oder Leistungsprobleme zu identifizieren.

## Verwendung
Die grundlegende Syntax des Befehls lautet:

```bash
vmstat [Optionen] [Argumente]
```

## Häufige Optionen
- `-a`: Zeigt alle Speicherstatistiken an, einschließlich freiem und belegtem Speicher.
- `-m`: Zeigt Informationen über den Speicherverbrauch von Slab-Cache-Objekten an.
- `-s`: Gibt eine zusammenfassende Übersicht über die Systemstatistiken aus.
- `-n`: Verhindert die Anzeige von Headerzeilen bei wiederholten Ausgaben.
- `delay`: Gibt an, wie oft (in Sekunden) die Statistiken aktualisiert werden sollen.
- `count`: Gibt die Anzahl der gewünschten Ausgaben an.

## Häufige Beispiele
Hier sind einige praktische Beispiele für die Verwendung von `vmstat`:

1. **Einfache Anzeige von Systemstatistiken:**
   ```bash
   vmstat
   ```

2. **Statistiken alle 5 Sekunden anzeigen:**
   ```bash
   vmstat 5
   ```

3. **Statistiken alle 5 Sekunden für 10 Iterationen anzeigen:**
   ```bash
   vmstat 5 10
   ```

4. **Speicherstatistiken anzeigen:**
   ```bash
   vmstat -a
   ```

5. **Zusammenfassende Systemstatistiken anzeigen:**
   ```bash
   vmstat -s
   ```

## Tipps
- Verwenden Sie `vmstat` in Kombination mit anderen Überwachungstools wie `top` oder `htop`, um eine umfassendere Analyse der Systemleistung zu erhalten.
- Achten Sie auf die Werte in der Spalte "us" (Benutzerzeit) und "sy" (Systemzeit), um die CPU-Auslastung besser zu verstehen.
- Nutzen Sie die Option `-n`, wenn Sie eine kontinuierliche Überwachung ohne wiederholte Headerzeilen wünschen, um die Ausgabe übersichtlicher zu gestalten.