# [Linux] Bash xmlstarlet Verwendung: XML-Daten verarbeiten und transformieren

## Übersicht
Das `xmlstarlet`-Kommando ist ein leistungsstarkes Werkzeug zur Verarbeitung von XML-Daten in der Kommandozeile. Es ermöglicht das Lesen, Bearbeiten, Transformieren und Validieren von XML-Dokumenten. Mit `xmlstarlet` können Benutzer XML-Daten einfach manipulieren und in verschiedene Formate umwandeln.

## Verwendung
Die grundlegende Syntax des Befehls lautet:

```bash
xmlstarlet [Optionen] [Argumente]
```

## Häufige Optionen
- `xml`: Gibt an, dass die Eingabe im XML-Format vorliegt.
- `sel`: Wählt Knoten aus einem XML-Dokument aus.
- `ed`: Bearbeitet ein XML-Dokument.
- `tr`: Transformiert XML-Daten mit XSLT.
- `val`: Validiert ein XML-Dokument gegen ein Schema.

## Häufige Beispiele

### 1. XML-Datei anzeigen
Um den Inhalt einer XML-Datei anzuzeigen, verwenden Sie den folgenden Befehl:

```bash
xmlstarlet xml <datei.xml>
```

### 2. Knoten auswählen
Um spezifische Knoten aus einer XML-Datei auszuwählen, können Sie den `sel`-Befehl verwenden:

```bash
xmlstarlet sel -t -m "//buch" -v "titel" -n <datei.xml>
```

### 3. XML-Daten bearbeiten
Um einen Knoten in einer XML-Datei zu bearbeiten, verwenden Sie den `ed`-Befehl:

```bash
xmlstarlet ed -u "//buch/titel" -v "Neuer Titel" <datei.xml>
```

### 4. XML transformieren
Um eine XML-Datei mit XSLT zu transformieren, verwenden Sie den `tr`-Befehl:

```bash
xmlstarlet tr <stylesheet.xsl> <datei.xml>
```

### 5. XML validieren
Um eine XML-Datei gegen ein Schema zu validieren, verwenden Sie den `val`-Befehl:

```bash
xmlstarlet val -e -s <schema.xsd> <datei.xml>
```

## Tipps
- Nutzen Sie die `--help`-Option, um eine vollständige Liste der verfügbaren Optionen und deren Beschreibungen zu erhalten.
- Testen Sie Ihre XML-Daten mit `xmlstarlet` in einer sicheren Umgebung, um sicherzustellen, dass Ihre Änderungen keine unerwünschten Effekte haben.
- Verwenden Sie Pipes, um `xmlstarlet` mit anderen Kommandozeilenwerkzeugen zu kombinieren, um komplexere Datenverarbeitungsaufgaben zu erledigen.