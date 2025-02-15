# [리눅스] Bash cd 사용법

## Übersicht
Der Befehl `cd` (change directory) ist ein grundlegender Befehl in der Bash-Shell, der verwendet wird, um das aktuelle Arbeitsverzeichnis zu ändern. Er ermöglicht es Benutzern, zwischen verschiedenen Verzeichnissen im Dateisystem zu navigieren, was für die Ausführung von Befehlen und Skripten in spezifischen Verzeichnissen unerlässlich ist.

## Verwendung
Die grundlegende Syntax des `cd`-Befehls lautet:

```bash
cd [OPTIONEN] [VERZEICHNIS]
```

### Häufige Optionen:
- `..`: Wechselt in das übergeordnete Verzeichnis.
- `-`: Wechselt zurück zum vorherigen Verzeichnis.
- `~`: Wechselt in das Home-Verzeichnis des aktuellen Benutzers.

## Beispiele
1. **Wechseln in ein spezifisches Verzeichnis**:
   Um in ein Verzeichnis namens `Dokumente` zu wechseln, verwenden Sie den folgenden Befehl:

   ```bash
   cd Dokumente
   ```

2. **Wechseln in das übergeordnete Verzeichnis**:
   Um in das übergeordnete Verzeichnis des aktuellen Verzeichnisses zu wechseln, verwenden Sie:

   ```bash
   cd ..
   ```

3. **Zurück zum vorherigen Verzeichnis**:
   Um zum vorherigen Verzeichnis zurückzukehren, verwenden Sie:

   ```bash
   cd -
   ```

## Tipps
- Nutzen Sie die Tabulator-Taste zur automatischen Vervollständigung von Verzeichnisnamen, um Tippfehler zu vermeiden und die Eingabe zu beschleunigen.
- Verwenden Sie den Befehl `pwd` (print working directory), um das aktuelle Verzeichnis anzuzeigen, bevor Sie den `cd`-Befehl verwenden.
- Wenn Sie häufig zwischen bestimmten Verzeichnissen wechseln, können Sie Aliase in Ihrer Shell-Konfigurationsdatei (`.bashrc` oder `.bash_profile`) erstellen, um den Wechsel zu erleichtern.