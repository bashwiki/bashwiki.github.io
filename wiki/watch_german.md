# [Linux] Bash watch Verwendung: Aktualisieren von Befehlsausgaben in Echtzeit

## Übersicht
Der Befehl `watch` wird verwendet, um die Ausgabe eines bestimmten Befehls in regelmäßigen Abständen zu aktualisieren. Dies ist besonders nützlich, um Änderungen in der Ausgabe eines Befehls zu überwachen, ohne den Befehl manuell erneut eingeben zu müssen.

## Verwendung
Die grundlegende Syntax des Befehls lautet:

```bash
watch [Optionen] [Befehl]
```

## Häufige Optionen
- `-n <Sekunden>`: Legt das Intervall in Sekunden fest, in dem der Befehl aktualisiert wird. Standardmäßig ist es 2 Sekunden.
- `-d`: Hebt die Unterschiede zwischen den aufeinanderfolgenden Ausgaben hervor.
- `-t`: Entfernt den Titel und die Zeitstempel aus der Anzeige, um eine sauberere Ausgabe zu erhalten.

## Häufige Beispiele
Hier sind einige praktische Beispiele zur Verwendung des `watch`-Befehls:

1. **Überwachung des freien Speicherplatzes:**
   ```bash
   watch df -h
   ```

2. **Überwachung von Prozessen:**
   ```bash
   watch -n 1 ps aux
   ```

3. **Überwachung von Änderungen in einem Verzeichnis:**
   ```bash
   watch -d ls -l /path/to/directory
   ```

4. **Überwachung der CPU-Auslastung:**
   ```bash
   watch -n 5 mpstat
   ```

## Tipps
- Verwenden Sie die `-d`-Option, um schnell Änderungen in der Ausgabe zu erkennen.
- Passen Sie das Aktualisierungsintervall mit der `-n`-Option an, um die Systemressourcen zu schonen oder um schnellere Updates zu erhalten.
- Kombinieren Sie `watch` mit anderen Befehlen, um spezifische Informationen zu überwachen, z.B. `watch -n 2 'grep ERROR /var/log/syslog'`, um Fehlerprotokolle in Echtzeit zu beobachten.