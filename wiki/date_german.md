# [Linux] Bash date Verwendung: Aktuelles Datum und Uhrzeit anzeigen

## Übersicht
Der Befehl `date` wird verwendet, um das aktuelle Datum und die Uhrzeit im Terminal anzuzeigen. Er kann auch verwendet werden, um das Datum in verschiedenen Formaten darzustellen oder um das Systemdatum zu ändern.

## Verwendung
Die grundlegende Syntax des Befehls lautet:

```bash
date [Optionen] [Argumente]
```

## Häufige Optionen
- `+FORMAT`: Gibt das Datum in einem benutzerdefinierten Format aus.
- `-u`: Zeigt die Zeit in UTC (Koordinierte Weltzeit) an.
- `-d STRING`: Gibt das Datum an, das durch die angegebene Zeichenfolge beschrieben wird.
- `-s STRING`: Setzt das Systemdatum und die Uhrzeit auf die angegebene Zeichenfolge.

## Häufige Beispiele
- Aktuelles Datum und Uhrzeit anzeigen:
    ```bash
    date
    ```

- Datum im Format "Tag-Monat-Jahr" anzeigen:
    ```bash
    date +"%d-%m-%Y"
    ```

- Aktuelle Zeit in UTC anzeigen:
    ```bash
    date -u
    ```

- Ein Datum in der Zukunft anzeigen (z.B. 5 Tage später):
    ```bash
    date -d "+5 days"
    ```

- Systemdatum auf ein bestimmtes Datum setzen (z.B. 1. Januar 2023):
    ```bash
    sudo date -s "2023-01-01 00:00:00"
    ```

## Tipps
- Verwenden Sie die `man date`-Anweisung, um die vollständige Dokumentation und alle verfügbaren Optionen zu sehen.
- Experimentieren Sie mit verschiedenen Formatzeichen, um das Datum nach Ihren Wünschen anzupassen.
- Seien Sie vorsichtig beim Setzen des Systemdatums, da dies Auswirkungen auf geplante Aufgaben und Protokolle haben kann.