# [Linux] Bash cmake Verwendung: Ein Werkzeug zur Erstellung von Softwareprojekten

## Übersicht
Der Befehl `cmake` ist ein plattformübergreifendes Build-System, das verwendet wird, um Softwareprojekte zu konfigurieren und zu erstellen. Es generiert die notwendigen Makefiles oder Projektdateien für verschiedene Build-Umgebungen, sodass Entwickler ihre Software einfach kompilieren können.

## Verwendung
Die grundlegende Syntax des Befehls lautet:

```bash
cmake [Optionen] [Argumente]
```

## Häufige Optionen
- `-S <Verzeichnis>`: Gibt das Quellverzeichnis an, das die CMakeLists.txt-Datei enthält.
- `-B <Verzeichnis>`: Gibt das Build-Verzeichnis an, in dem die Build-Dateien erstellt werden.
- `-G <Generator>`: Wählt den Build-Generator aus (z.B. "Unix Makefiles", "Ninja").
- `-D <Variable>=<Wert>`: Definiert eine CMake-Variable mit einem bestimmten Wert.
- `--build <Verzeichnis>`: Baut das Projekt im angegebenen Verzeichnis.

## Häufige Beispiele
Hier sind einige praktische Beispiele für die Verwendung von `cmake`:

1. **Ein einfaches Projekt erstellen:**
   ```bash
   cmake -S . -B build
   ```

2. **Ein Projekt mit einem spezifischen Generator erstellen:**
   ```bash
   cmake -S . -B build -G "Unix Makefiles"
   ```

3. **Eine CMake-Variable definieren:**
   ```bash
   cmake -S . -B build -D CMAKE_BUILD_TYPE=Release
   ```

4. **Das Projekt im Build-Verzeichnis kompilieren:**
   ```bash
   cmake --build build
   ```

## Tipps
- Stellen Sie sicher, dass Sie die CMakeLists.txt-Datei im Quellverzeichnis haben, da CMake diese Datei benötigt, um das Projekt zu konfigurieren.
- Nutzen Sie die Option `-D`, um benutzerdefinierte Konfigurationen einfach zu setzen, ohne die CMakeLists.txt zu ändern.
- Es ist eine gute Praxis, ein separates Build-Verzeichnis zu verwenden, um die Quellverzeichnisse sauber zu halten.