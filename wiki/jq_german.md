# [Linux] Bash jq Verwendung: JSON-Daten verarbeiten

## Übersicht
Der `jq` Befehl ist ein leistungsstarkes Werkzeug zum Verarbeiten und Analysieren von JSON-Daten. Er ermöglicht es Benutzern, JSON-Daten zu filtern, zu transformieren und zu formatieren, was ihn zu einem unverzichtbaren Tool für die Arbeit mit APIs und Datenformaten macht.

## Verwendung
Die grundlegende Syntax des `jq` Befehls lautet:

```bash
jq [Optionen] [Argumente]
```

## Häufige Optionen
- `-c`: Gibt die Ausgabe in kompaktem Format aus.
- `-r`: Gibt die Ausgabe als rohe Zeichenfolge aus, ohne Anführungszeichen.
- `-f <datei>`: Führt die jq-Anweisungen aus einer Datei aus.
- `--arg <name> <wert>`: Setzt eine Variable, die in der jq-Anweisung verwendet werden kann.

## Häufige Beispiele
Hier sind einige praktische Beispiele für die Verwendung von `jq`:

1. **Einfaches Filtern von JSON-Daten:**
   ```bash
   echo '{"name": "Max", "age": 30}' | jq '.name'
   ```
   Ausgabe:
   ```
   "Max"
   ```

2. **Zugriff auf verschachtelte Daten:**
   ```bash
   echo '{"user": {"name": "Max", "age": 30}}' | jq '.user.name'
   ```
   Ausgabe:
   ```
   "Max"
   ```

3. **Filtern von Arrays:**
   ```bash
   echo '[{"name": "Max"}, {"name": "Lisa"}]' | jq '.[0].name'
   ```
   Ausgabe:
   ```
   "Max"
   ```

4. **Verwendung von Variablen:**
   ```bash
   echo '{"name": "Max", "age": 30}' | jq --arg name "Max" '.name == $name'
   ```
   Ausgabe:
   ```
   true
   ```

5. **Ausgabe im kompakten Format:**
   ```bash
   echo '{"name": "Max", "age": 30}' | jq -c '.'
   ```
   Ausgabe:
   ```
   {"name":"Max","age":30}
   ```

## Tipps
- Verwenden Sie die Option `-r`, wenn Sie die Ausgabe ohne Anführungszeichen benötigen, um die Verarbeitung in anderen Skripten zu erleichtern.
- Nutzen Sie die Möglichkeit, jq-Skripte in einer Datei zu speichern, um komplexe Abfragen zu organisieren und wiederzuverwenden.
- Experimentieren Sie mit der jq-Dokumentation, um die Vielzahl der Funktionen und Filter zu entdecken, die Ihnen zur Verfügung stehen.