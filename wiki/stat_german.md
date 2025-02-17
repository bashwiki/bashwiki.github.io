# [Linux] Bash stat Verwendung: Zeigt Dateiinformationen an

## Übersicht
Der Befehl `stat` wird verwendet, um detaillierte Informationen über Dateien und Verzeichnisse im Dateisystem anzuzeigen. Dazu gehören Angaben wie Größe, Berechtigungen, Zeitstempel und mehr.

## Verwendung
Die grundlegende Syntax des Befehls lautet:

```bash
stat [Optionen] [Argumente]
```

## Häufige Optionen
- `-c` : Gibt die Ausgabe in einem benutzerdefinierten Format an.
- `-f` : Zeigt Informationen über das Dateisystem an, in dem die Datei gespeichert ist.
- `--format` : Ermöglicht die Angabe eines spezifischen Formats für die Ausgabe.
- `-t` : Gibt die Informationen in einer kompakten, tabellarischen Form aus.

## Häufige Beispiele
Hier sind einige praktische Beispiele für die Verwendung des `stat`-Befehls:

1. **Allgemeine Informationen über eine Datei anzeigen:**
   ```bash
   stat datei.txt
   ```

2. **Nur die Größe der Datei anzeigen:**
   ```bash
   stat -c %s datei.txt
   ```

3. **Informationen über das Dateisystem einer Datei anzeigen:**
   ```bash
   stat -f datei.txt
   ```

4. **Detaillierte Informationen in einem benutzerdefinierten Format anzeigen:**
   ```bash
   stat --format="Datei: %n, Größe: %s Bytes, Letzte Änderung: %y" datei.txt
   ```

5. **Kompakte Ausgabe der Dateiinformationen:**
   ```bash
   stat -t datei.txt
   ```

## Tipps
- Verwenden Sie die `--format`-Option, um die Ausgabe an Ihre Bedürfnisse anzupassen.
- Nutzen Sie die `-f`-Option, um schnell Informationen über das Dateisystem zu erhalten, ohne die Datei selbst zu betrachten.
- Kombinieren Sie `stat` mit anderen Befehlen in einer Pipeline, um die Informationen weiter zu verarbeiten oder zu filtern.