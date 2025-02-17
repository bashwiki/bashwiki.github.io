# [Linux] Bash ps Verwendung: Prozesse anzeigen

## Übersicht
Der Befehl `ps` (process status) wird verwendet, um Informationen über aktuell laufende Prozesse im System anzuzeigen. Er bietet eine Momentaufnahme der aktiven Prozesse und deren Status, was bei der Überwachung und Verwaltung von Systemressourcen hilfreich ist.

## Verwendung
Die grundlegende Syntax des Befehls lautet:

```bash
ps [Optionen] [Argumente]
```

## Häufige Optionen
- `-e`: Zeigt alle Prozesse an.
- `-f`: Führt eine vollständige Formatierung der Ausgabe durch.
- `-u [Benutzer]`: Zeigt die Prozesse eines bestimmten Benutzers an.
- `-aux`: Zeigt alle Prozesse im ausführlichen Format an.
- `--sort`: Sortiert die Ausgabe nach einem bestimmten Kriterium, z.B. `--sort=-%mem` für die Speicherauslastung.

## Häufige Beispiele
Hier sind einige praktische Beispiele zur Verwendung des `ps`-Befehls:

1. Alle laufenden Prozesse anzeigen:
   ```bash
   ps -e
   ```

2. Prozesse im ausführlichen Format anzeigen:
   ```bash
   ps aux
   ```

3. Prozesse eines bestimmten Benutzers anzeigen:
   ```bash
   ps -u username
   ```

4. Prozesse nach Speicherauslastung sortieren:
   ```bash
   ps aux --sort=-%mem
   ```

5. Eine vollständige Prozessliste mit Hierarchie anzeigen:
   ```bash
   ps -ef --forest
   ```

## Tipps
- Verwenden Sie `ps aux | grep [Prozessname]`, um nach einem bestimmten Prozess zu suchen.
- Kombinieren Sie `ps` mit anderen Befehlen wie `less`, um die Ausgabe besser durchblättern zu können: `ps aux | less`.
- Nutzen Sie die Option `-o`, um spezifische Informationen anzuzeigen, z.B. `ps -eo pid,comm` für die Prozess-ID und den Befehl.