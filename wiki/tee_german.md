# [리눅스] Bash tee 사용법

## Übersicht
Der `tee`-Befehl in Bash ist ein nützliches Werkzeug, das den Inhalt von Standard-Eingaben (stdin) sowohl auf der Standard-Ausgabe (stdout) als auch in eine oder mehrere Dateien schreibt. Dies ermöglicht es Entwicklern und Ingenieuren, Daten gleichzeitig anzuzeigen und zu speichern, was besonders hilfreich ist, wenn man Protokolle oder Ausgaben von Befehlen überwachen möchte.

## Verwendung
Die grundlegende Syntax des `tee`-Befehls lautet:

```bash
tee [OPTIONEN] [DATEI...]
```

### Häufige Optionen:
- `-a`, `--append`: Fügt die Ausgabe an die angegebene Datei an, anstatt sie zu überschreiben.
- `-i`, `--ignore-interrupts`: Ignoriert Interrupt-Signale.
- `--help`: Zeigt eine Hilfemeldung an und beendet den Befehl.
- `--version`: Gibt die Version des `tee`-Befehls aus.

## Beispiele
Hier sind einige praktische Beispiele, die zeigen, wie man den `tee`-Befehl verwendet:

1. **Einfaches Beispiel**: Ausgabe eines Befehls in eine Datei schreiben und gleichzeitig auf dem Bildschirm anzeigen.

```bash
echo "Hallo Welt" | tee ausgabe.txt
```
In diesem Beispiel wird der Text "Hallo Welt" sowohl auf dem Bildschirm angezeigt als auch in die Datei `ausgabe.txt` geschrieben.

2. **Anfügen an eine Datei**: Die Ausgabe eines Befehls an eine bestehende Datei anhängen.

```bash
echo "Zusätzliche Zeile" | tee -a ausgabe.txt
```
Hier wird der Text "Zusätzliche Zeile" an die Datei `ausgabe.txt` angehängt, ohne den vorherigen Inhalt zu überschreiben.

## Tipps
- Verwenden Sie die `-a`-Option, wenn Sie sicherstellen möchten, dass bestehende Daten in einer Datei nicht verloren gehen.
- Kombinieren Sie `tee` mit anderen Befehlen in einer Pipeline, um die Ausgabe zu speichern und gleichzeitig weiterzuverarbeiten.
- Nutzen Sie `tee` in Skripten, um Protokolle zu erstellen, während das Skript ausgeführt wird, was die Fehlersuche erleichtert.

Mit diesen Informationen sind Sie gut gerüstet, um den `tee`-Befehl effektiv in Ihren Bash-Skripten und -Befehlen zu nutzen.