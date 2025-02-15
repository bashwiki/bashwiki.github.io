# [리눅스] Bash jq 사용법

## Übersicht
`jq` ist ein leistungsstarkes Kommandozeilenwerkzeug zur Verarbeitung von JSON-Daten. Es ermöglicht Entwicklern und Ingenieuren, JSON-Daten zu analysieren, zu filtern, zu transformieren und zu formatieren. Mit `jq` können Sie komplexe Datenstrukturen einfach manipulieren und die gewünschten Informationen extrahieren.

## Verwendung
Die grundlegende Syntax von `jq` lautet:

```bash
jq [OPTIONEN] 'FILTER' DATEI
```

### Häufige Optionen:
- `-c`: Gibt die Ausgabe im kompakten Format zurück, ohne Zeilenumbrüche.
- `-r`: Gibt die Ausgabe als rohe Zeichenkette zurück, anstatt sie in Anführungszeichen zu setzen.
- `-f DATEI`: Liest Filter aus einer Datei anstelle von der Kommandozeile.

## Beispiele
### Beispiel 1: Einfaches Filtern
Angenommen, Sie haben eine JSON-Datei namens `daten.json` mit folgendem Inhalt:

```json
{
  "name": "Max",
  "alter": 30,
  "stadt": "Berlin"
}
```

Um den Namen aus dieser Datei zu extrahieren, können Sie den folgenden Befehl verwenden:

```bash
jq '.name' daten.json
```

Die Ausgabe wäre:

```
"Max"
```

### Beispiel 2: Komplexe Abfrage
Wenn Sie eine Liste von Objekten haben, z.B. in `personen.json`:

```json
[
  { "name": "Max", "alter": 30 },
  { "name": "Anna", "alter": 25 },
  { "name": "Tom", "alter": 35 }
]
```

Um nur die Namen der Personen, die älter als 30 Jahre sind, zu erhalten, verwenden Sie:

```bash
jq '.[] | select(.alter > 30) | .name' personen.json
```

Die Ausgabe wäre:

```
"Tom"
```

## Tipps
- Nutzen Sie die `-r` Option, wenn Sie die Ausgabe in einem Skript weiterverarbeiten möchten, um unerwünschte Anführungszeichen zu vermeiden.
- Experimentieren Sie mit verschiedenen Filtern, um die Flexibilität von `jq` voll auszuschöpfen. Die Dokumentation bietet viele Beispiele und Erklärungen zu komplexeren Abfragen.
- Verwenden Sie `jq` in Kombination mit anderen Unix-Tools wie `curl`, um Daten von APIs direkt zu verarbeiten.