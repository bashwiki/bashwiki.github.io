# [리눅스] Bash tput 사용법

## Übersicht
Der Befehl `tput` ist ein nützliches Kommandozeilenwerkzeug in Unix-ähnlichen Betriebssystemen, das es ermöglicht, Terminal-Eigenschaften zu steuern und zu ändern. Es wird häufig verwendet, um die Anzeige von Text im Terminal zu formatieren, indem es Funktionen wie das Ändern von Farben, das Bewegen des Cursors und das Löschen von Bildschirmen bereitstellt. `tput` greift auf die Terminfo-Datenbank zu, um die richtigen Steuersequenzen für das jeweilige Terminal zu ermitteln.

## Verwendung
Die grundlegende Syntax des Befehls `tput` lautet:

```bash
tput [OPTION] [ARGUMENTE]
```

Einige häufig verwendete Optionen sind:

- `setaf`: Setzt die Vordergrundfarbe.
- `setab`: Setzt die Hintergrundfarbe.
- `clear`: Löscht den Bildschirm.
- `cup`: Bewegt den Cursor zu einer bestimmten Position (Zeile, Spalte).
- `bold`: Aktiviert den fetten Text.

## Beispiele
Hier sind einige praktische Beispiele, wie `tput` verwendet werden kann:

1. **Textfarbe ändern**:
   Um die Vordergrundfarbe auf grün zu setzen und dann "Hallo Welt" auszugeben, verwenden Sie den folgenden Befehl:

   ```bash
   tput setaf 2; echo "Hallo Welt"; tput sgr0
   ```

   In diesem Beispiel setzt `tput setaf 2` die Vordergrundfarbe auf grün, und `tput sgr0` setzt alle Attribute zurück.

2. **Cursorposition ändern**:
   Um den Cursor auf die Zeile 5 und die Spalte 10 zu bewegen und dort "Text" auszugeben, verwenden Sie:

   ```bash
   tput cup 5 10; echo "Text"
   ```

   Hierbei bewegt `tput cup 5 10` den Cursor an die angegebene Position, bevor der Text ausgegeben wird.

## Tipps
- Verwenden Sie `tput sgr0` am Ende Ihrer Befehle, um sicherzustellen, dass alle Textattribute zurückgesetzt werden. Dies verhindert, dass nachfolgender Text in der gleichen Formatierung angezeigt wird.
- Testen Sie die verschiedenen Farben und Attribute in Ihrem Terminal, um ein Gefühl für die Möglichkeiten von `tput` zu bekommen.
- In Skripten kann `tput` verwendet werden, um die Benutzeroberfläche zu verbessern und die Lesbarkeit von Ausgaben zu erhöhen, insbesondere in interaktiven Anwendungen.