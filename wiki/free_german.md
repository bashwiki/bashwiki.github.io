# [Linux] Bash free Befehl: Zeigt den Speicherverbrauch an

## Übersicht
Der `free` Befehl in Bash wird verwendet, um Informationen über den Speicherverbrauch des Systems anzuzeigen. Er zeigt sowohl den physischen Speicher als auch den Swap-Speicher an und gibt einen Überblick über die Speichernutzung in Echtzeit.

## Verwendung
Die grundlegende Syntax des Befehls lautet:

```bash
free [Optionen] [Argumente]
```

## Häufige Optionen
- `-h`: Zeigt die Speichergrößen in einem menschenlesbaren Format (z.B. KB, MB, GB) an.
- `-m`: Gibt die Speicherdaten in Megabyte aus.
- `-g`: Gibt die Speicherdaten in Gigabyte aus.
- `-s <Sekunden>`: Aktualisiert die Anzeige alle angegebenen Sekunden.
- `-t`: Zeigt die Gesamtsumme von physischem und Swap-Speicher an.

## Häufige Beispiele
Hier sind einige praktische Beispiele für die Verwendung des `free` Befehls:

1. **Einfacher Speicherabruf**:
   ```bash
   free
   ```

2. **Speicher in menschenlesbarem Format anzeigen**:
   ```bash
   free -h
   ```

3. **Speicher in Megabyte anzeigen**:
   ```bash
   free -m
   ```

4. **Speicher in Gigabyte anzeigen**:
   ```bash
   free -g
   ```

5. **Speicher alle 5 Sekunden aktualisieren**:
   ```bash
   free -s 5
   ```

6. **Gesamtspeicher anzeigen**:
   ```bash
   free -t
   ```

## Tipps
- Verwenden Sie die `-h` Option, um die Ausgabe leichter lesbar zu machen, besonders wenn Sie mit großen Speichermengen arbeiten.
- Kombinieren Sie den `free` Befehl mit anderen Befehlen wie `watch`, um die Speicherverwendung in Echtzeit zu überwachen:
  ```bash
  watch free -h
  ```
- Nutzen Sie die `-s` Option, um regelmäßig den Speicherverbrauch zu überprüfen, was besonders nützlich ist, wenn Sie Leistungsprobleme diagnostizieren.