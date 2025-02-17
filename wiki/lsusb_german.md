# [Linux] Bash lsusb Verwendung: Zeigt USB-Geräte an

## Übersicht
Der Befehl `lsusb` wird verwendet, um Informationen über USB-Geräte, die an ein Linux-System angeschlossen sind, anzuzeigen. Er listet alle erkannten USB-Geräte auf und bietet detaillierte Informationen über deren Eigenschaften.

## Verwendung
Die grundlegende Syntax des Befehls lautet:

```bash
lsusb [Optionen] [Argumente]
```

## Häufige Optionen
- `-v`: Zeigt detaillierte Informationen über die USB-Geräte an.
- `-t`: Zeigt die USB-Geräte in einer Baumstruktur an.
- `-s <Bus:Device>`: Zeigt Informationen nur für das angegebene USB-Gerät an.
- `-d <Vendor:Product>`: Filtert die Ausgabe nach dem angegebenen Hersteller- und Produkt-ID.

## Häufige Beispiele
Um alle angeschlossenen USB-Geräte anzuzeigen, verwenden Sie einfach:

```bash
lsusb
```

Um detaillierte Informationen über alle USB-Geräte anzuzeigen, verwenden Sie:

```bash
lsusb -v
```

Um die USB-Geräte in einer Baumstruktur darzustellen, verwenden Sie:

```bash
lsusb -t
```

Um Informationen zu einem bestimmten USB-Gerät anzuzeigen, verwenden Sie die Bus- und Geräte-ID:

```bash
lsusb -s 001:002
```

Um die Ausgabe auf ein bestimmtes Gerät zu filtern, verwenden Sie die Hersteller- und Produkt-ID:

```bash
lsusb -d 1234:5678
```

## Tipps
- Verwenden Sie `lsusb -v`, um tiefere Einblicke in die Eigenschaften der USB-Geräte zu erhalten, insbesondere wenn Sie Probleme mit einem Gerät diagnostizieren müssen.
- Kombinieren Sie `lsusb` mit anderen Befehlen wie `grep`, um die Ausgabe nach bestimmten Geräten oder Eigenschaften zu filtern.
- Überprüfen Sie regelmäßig die angeschlossenen USB-Geräte, insbesondere nach dem Anschluss neuer Hardware, um sicherzustellen, dass sie korrekt erkannt werden.