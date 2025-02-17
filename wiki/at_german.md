# [Linux] Bash bei at: Aufgaben zeitgesteuert ausführen

## Übersicht
Der `at`-Befehl wird verwendet, um einmalige Aufgaben zu einem bestimmten Zeitpunkt in der Zukunft auszuführen. Mit `at` können Sie Befehle oder Skripte planen, die zu einem festgelegten Zeitpunkt automatisch ausgeführt werden.

## Verwendung
Die grundlegende Syntax des `at`-Befehls lautet:

```bash
at [Optionen] [Zeit]
```

## Häufige Optionen
- `-f [Datei]`: Führt die Befehle aus der angegebenen Datei aus.
- `-m`: Sendet eine E-Mail, wenn der Job abgeschlossen ist, auch wenn keine Ausgabe erzeugt wurde.
- `-q [Warteschlange]`: Gibt die Warteschlange an, in der der Job ausgeführt werden soll (z.B. a, b, c).
- `-l`: Listet alle geplanten `at`-Jobs auf.
- `-d [Job-ID]`: Löscht den angegebenen Job.

## Häufige Beispiele

### Beispiel 1: Einfache Aufgabe planen
Um einen Befehl um 15:00 Uhr auszuführen, können Sie Folgendes verwenden:

```bash
echo "echo 'Hallo Welt'" | at 15:00
```

### Beispiel 2: Skript zu einem bestimmten Zeitpunkt ausführen
Um ein Skript namens `backup.sh` um 2 Uhr nachts auszuführen:

```bash
at 02:00 -f /pfad/zu/backup.sh
```

### Beispiel 3: Job für einen bestimmten Tag planen
Um einen Befehl für den nächsten Montag um 10:00 Uhr zu planen:

```bash
echo "python /pfad/zu/script.py" | at 10:00 Montag
```

### Beispiel 4: Geplante Jobs auflisten
Um alle geplanten `at`-Jobs anzuzeigen:

```bash
at -l
```

### Beispiel 5: Job löschen
Um einen Job mit der ID 5 zu löschen:

```bash
at -d 5
```

## Tipps
- Stellen Sie sicher, dass der `atd`-Dienst läuft, damit geplante Jobs ausgeführt werden können.
- Verwenden Sie die `-m`-Option, um Benachrichtigungen über den Abschluss Ihrer Jobs zu erhalten.
- Testen Sie Ihre Befehle zuerst in der Kommandozeile, bevor Sie sie mit `at` planen, um sicherzustellen, dass sie wie gewünscht funktionieren.