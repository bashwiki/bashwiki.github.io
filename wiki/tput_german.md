# [Linux] Bash tput Verwendung: Terminalsteuerung und -formatierung

## Übersicht
Der Befehl `tput` wird verwendet, um Terminal-Eigenschaften zu steuern und zu formatieren. Er ermöglicht es Benutzern, Textfarben, Cursorpositionen und andere Anzeigeparameter in einem Terminal zu ändern.

## Verwendung
Die grundlegende Syntax des Befehls lautet:

```bash
tput [Optionen] [Argumente]
```

## Häufige Optionen
- `setaf [Farbe]`: Setzt die Vordergrundfarbe des Textes.
- `setab [Farbe]`: Setzt die Hintergrundfarbe des Textes.
- `clear`: Löscht den Bildschirm.
- `cup [Zeile] [Spalte]`: Bewegt den Cursor zu einer bestimmten Zeile und Spalte.
- `bold`: Setzt den Text auf fett.

## Häufige Beispiele
Hier sind einige praktische Beispiele für die Verwendung von `tput`:

### Beispiel 1: Textfarbe ändern
Ändern Sie die Vordergrundfarbe des Textes auf Rot:

```bash
tput setaf 1
echo "Dieser Text ist rot."
tput sgr0  # Setzt die Farben zurück
```

### Beispiel 2: Hintergrundfarbe ändern
Ändern Sie die Hintergrundfarbe des Textes auf Blau:

```bash
tput setab 4
echo "Dieser Text hat einen blauen Hintergrund."
tput sgr0  # Setzt die Farben zurück
```

### Beispiel 3: Bildschirm löschen
Löschen Sie den Bildschirm:

```bash
tput clear
```

### Beispiel 4: Cursorposition ändern
Bewegen Sie den Cursor zur Zeile 5 und Spalte 10:

```bash
tput cup 5 10
echo "Hier ist der Text an Zeile 5, Spalte 10."
```

### Beispiel 5: Fetter Text
Geben Sie fetten Text aus:

```bash
tput bold
echo "Dieser Text ist fett."
tput sgr0  # Setzt die Formatierung zurück
```

## Tipps
- Verwenden Sie `tput sgr0`, um alle Formatierungen und Farben zurückzusetzen, bevor Sie neuen Text ausgeben.
- Experimentieren Sie mit verschiedenen Farbnummern, um die gewünschten Farben zu finden. Die Farbnummern reichen normalerweise von 0 bis 7 für Standardfarben.
- Kombinieren Sie mehrere `tput`-Befehle in einem Skript, um komplexe Terminalausgaben zu erstellen.