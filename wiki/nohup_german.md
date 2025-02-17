# [Linux] Bash nohup Verwendung: Prozesse im Hintergrund ausführen

## Übersicht
Der `nohup`-Befehl (no hang up) wird verwendet, um Prozesse im Hintergrund auszuführen, sodass sie nicht beendet werden, wenn die Sitzung geschlossen wird. Dies ist besonders nützlich, wenn Sie lang laufende Prozesse starten und sicherstellen möchten, dass sie weiterlaufen, auch wenn Sie sich vom Terminal abmelden.

## Verwendung
Die grundlegende Syntax des Befehls lautet:

```bash
nohup [Optionen] [Befehle] &
```

Das `&` am Ende des Befehls sorgt dafür, dass der Prozess im Hintergrund ausgeführt wird.

## Häufige Optionen
- `-h`: Zeigt die Hilfe für den Befehl an.
- `-v`: Aktiviert den ausführlichen Modus, um mehr Informationen über den Prozess zu erhalten.
- `--version`: Gibt die Versionsnummer von nohup aus.

## Häufige Beispiele
Hier sind einige praktische Beispiele für die Verwendung von `nohup`:

1. **Ein einfaches Skript im Hintergrund ausführen:**
   ```bash
   nohup ./mein_skript.sh &
   ```

2. **Einen Python-Server im Hintergrund starten:**
   ```bash
   nohup python3 -m http.server 8000 &
   ```

3. **Ein lang laufendes Backup-Skript ausführen und die Ausgabe in eine Datei umleiten:**
   ```bash
   nohup ./backup.sh > backup.log 2>&1 &
   ```

4. **Einen Prozess mit einer spezifischen Priorität im Hintergrund starten:**
   ```bash
   nohup nice -n 19 ./lang_laufender_prozess &
   ```

## Tipps
- Verwenden Sie `nohup` in Kombination mit `&`, um sicherzustellen, dass der Prozess im Hintergrund läuft.
- Leiten Sie die Ausgabe in eine Datei um, um die Protokollierung zu erleichtern und spätere Überprüfungen zu ermöglichen.
- Überprüfen Sie regelmäßig die Ausgabedatei, um sicherzustellen, dass der Prozess wie erwartet läuft.