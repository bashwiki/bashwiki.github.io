# [리눅스] Bash cmake 사용법

## Übersicht
Der Befehl `cmake` ist ein plattformübergreifendes Build-System, das verwendet wird, um die Kompilierung von Softwareprojekten zu steuern. Es ermöglicht Entwicklern, Projekte durch die Verwendung von Konfigurationsdateien (CMakeLists.txt) zu erstellen, die die benötigten Informationen über Quellcode, Abhängigkeiten und Build-Optionen enthalten. CMake generiert dann die entsprechenden Makefiles oder Projektdateien für verschiedene Build-Umgebungen.

## Verwendung
Die grundlegende Syntax des `cmake`-Befehls lautet:

```bash
cmake [Optionen] [Pfad_zum_Quellverzeichnis]
```

### Häufige Optionen:
- `-B <Verzeichnis>`: Gibt das Verzeichnis an, in dem die Build-Dateien generiert werden sollen.
- `-S <Verzeichnis>`: Gibt das Verzeichnis an, das die Quelldateien enthält.
- `-D <Name=Value>`: Definiert eine CMake-Variable mit einem bestimmten Wert.
- `--build <Verzeichnis>`: Baut das Projekt im angegebenen Verzeichnis.
- `--target <Ziel>`: Gibt ein spezifisches Ziel an, das gebaut werden soll.

## Beispiele
### Beispiel 1: Einfaches Projekt erstellen
Um ein einfaches CMake-Projekt zu erstellen, navigieren Sie in das Verzeichnis Ihres Projekts und führen Sie den folgenden Befehl aus:

```bash
cmake -S . -B build
```
Dieser Befehl generiert die Build-Dateien im Unterverzeichnis `build`.

### Beispiel 2: Projekt mit benutzerdefinierten Optionen bauen
Wenn Sie eine benutzerdefinierte Option für Ihr Projekt festlegen möchten, können Sie dies wie folgt tun:

```bash
cmake -S . -B build -DCMAKE_BUILD_TYPE=Release
cmake --build build
```
Hier wird das Projekt im `Release`-Modus gebaut.

## Tipps
- Stellen Sie sicher, dass Sie die CMakeLists.txt-Datei korrekt konfiguriert haben, bevor Sie den `cmake`-Befehl ausführen, da diese Datei die Anweisungen für den Build-Prozess enthält.
- Verwenden Sie die Option `-D`, um Variablen zu definieren, die in Ihrer CMakeLists.txt verwendet werden können, um den Build-Prozess anzupassen.
- Es ist eine gute Praxis, separate Build-Verzeichnisse zu verwenden, um die Quellverzeichnisse sauber zu halten und um die Möglichkeit zu haben, verschiedene Build-Konfigurationen (z.B. Debug und Release) zu verwalten.