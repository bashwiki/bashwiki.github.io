# [Linux] Bash nice Verwendung: Prozesse priorisieren

## Übersicht
Der `nice` Befehl in Bash wird verwendet, um die Priorität eines Prozesses beim Ausführen zu steuern. Mit `nice` können Sie die CPU-Zeit, die ein Prozess erhält, beeinflussen, indem Sie ihm eine höhere oder niedrigere Priorität zuweisen. Dies ist besonders nützlich, um sicherzustellen, dass wichtige Prozesse genügend Ressourcen erhalten, während weniger wichtige Prozesse weniger CPU-Zeit beanspruchen.

## Verwendung
Die grundlegende Syntax des `nice` Befehls lautet:

```bash
nice [Optionen] [Befehl] [Argumente]
```

## Häufige Optionen
- `-n`, `--adjustment`: Legt die Priorität des Prozesses fest. Der Wert kann zwischen -20 (höchste Priorität) und 19 (niedrigste Priorität) liegen.
- `-h`, `--help`: Zeigt eine Hilfemeldung an.
- `-v`, `--version`: Gibt die Versionsnummer des `nice` Befehls aus.

## Häufige Beispiele
Hier sind einige praktische Beispiele für die Verwendung des `nice` Befehls:

1. **Einen Prozess mit Standardpriorität starten:**
   ```bash
   nice python mein_script.py
   ```

2. **Einen Prozess mit niedrigerer Priorität starten (z. B. 10):**
   ```bash
   nice -n 10 python mein_script.py
   ```

3. **Einen Prozess mit höherer Priorität starten (z. B. -5):**
   ```bash
   nice -n -5 python mein_script.py
   ```

4. **Die aktuelle Priorität eines Prozesses anzeigen:**
   ```bash
   ps -o pid,ni,cmd
   ```

## Tipps
- Verwenden Sie `nice`, um sicherzustellen, dass ressourcenintensive Prozesse die Systemleistung nicht beeinträchtigen.
- Überprüfen Sie die Priorität laufender Prozesse mit dem `ps` Befehl, um zu sehen, ob Anpassungen notwendig sind.
- Seien Sie vorsichtig beim Setzen einer hohen Priorität für Prozesse, da dies andere wichtige Prozesse negativ beeinflussen kann.