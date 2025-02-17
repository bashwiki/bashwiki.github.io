# [Linux] Bash realpath Verwendung: Gibt den absoluten Pfad einer Datei oder eines Verzeichnisses zurück

## Übersicht
Der Befehl `realpath` wird verwendet, um den absoluten Pfad einer Datei oder eines Verzeichnisses zu ermitteln. Er löst symbolische Links auf und entfernt relative Pfadangaben, sodass der vollständige Pfad angezeigt wird.

## Verwendung
Die grundlegende Syntax des Befehls lautet:

```bash
realpath [Optionen] [Argumente]
```

## Häufige Optionen
- `-m`, `--canonicalize-missing`: Gibt den absoluten Pfad zurück, auch wenn die Datei oder das Verzeichnis nicht existiert.
- `-q`, `--quiet`: Unterdrückt Fehlermeldungen, wenn der Pfad nicht existiert.
- `-s`, `--strip`: Entfernt die letzten Teile des Pfades, die auf ein Verzeichnis verweisen.

## Häufige Beispiele
Hier sind einige praktische Beispiele für die Verwendung von `realpath`:

1. **Absoluten Pfad einer Datei anzeigen:**
   ```bash
   realpath meine_datei.txt
   ```

2. **Absoluten Pfad eines Verzeichnisses anzeigen:**
   ```bash
   realpath /home/benutzername/mein_verzeichnis/
   ```

3. **Absoluten Pfad mit symbolischen Links auflösen:**
   ```bash
   realpath /pfad/zu/symbolischem/link
   ```

4. **Absoluten Pfad einer nicht existierenden Datei anzeigen:**
   ```bash
   realpath -m nicht_existierende_datei.txt
   ```

5. **Absoluten Pfad ohne Fehlermeldungen anzeigen:**
   ```bash
   realpath -q nicht_existierende_datei.txt
   ```

## Tipps
- Verwenden Sie `realpath`, um sicherzustellen, dass Sie mit absoluten Pfaden arbeiten, insbesondere in Skripten, um Verwirrung zu vermeiden.
- Nutzen Sie die Option `-m`, wenn Sie mit temporären oder nicht vorhandenen Dateien arbeiten, um trotzdem den gewünschten Pfad zu erhalten.
- Kombinieren Sie `realpath` mit anderen Befehlen in einer Pipeline, um Pfade dynamisch zu verarbeiten.