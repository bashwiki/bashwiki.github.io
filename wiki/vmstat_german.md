# [리눅스] Bash vmstat 사용법

## Übersicht
Der Befehl `vmstat` (Virtual Memory Statistics) ist ein nützliches Werkzeug in der Linux-Umgebung, das Informationen über das System und die Speichernutzung bereitstellt. Es zeigt Statistiken zu Prozessen, Speicher, Paging, Block-I/O, Traps und CPU-Aktivitäten an. Der Hauptzweck von `vmstat` ist es, einen Überblick über die Systemleistung zu geben und Engpässe in der Ressourcennutzung zu identifizieren.

## Verwendung
Die Grundsyntax des Befehls `vmstat` lautet:

```bash
vmstat [OPTIONEN] [INTERVAL] [ANZAHL]
```

### Häufige Optionen:
- `-a`: Zeigt alle Speicherinformationen an, einschließlich freiem und belegtem Speicher.
- `-m`: Zeigt Informationen über den Speicherverbrauch von Slab-Cache-Objekten an.
- `-s`: Gibt eine Zusammenfassung der Speichernutzung in einer Tabelle aus.
- `INTERVAL`: Gibt den Zeitraum (in Sekunden) an, in dem die Statistiken aktualisiert werden sollen.
- `ANZAHL`: Gibt an, wie oft die Statistiken angezeigt werden sollen.

## Beispiele
### Beispiel 1: Grundlegende Nutzung
Um alle 2 Sekunden die Systemstatistiken anzuzeigen, verwenden Sie den folgenden Befehl:

```bash
vmstat 2
```

### Beispiel 2: Detaillierte Speichernutzung
Um eine detaillierte Übersicht über die Speichernutzung zu erhalten, können Sie den Befehl mit der Option `-a` verwenden:

```bash
vmstat -a 2 5
```
Dieser Befehl zeigt alle 2 Sekunden die Statistiken für insgesamt 5 Iterationen an.

## Tipps
- Verwenden Sie `vmstat` in Kombination mit anderen Überwachungstools wie `top` oder `htop`, um ein umfassenderes Bild der Systemleistung zu erhalten.
- Achten Sie auf die CPU-Auslastung und den Speicherverbrauch, um potenzielle Engpässe frühzeitig zu erkennen.
- Speichern Sie die Ausgabe von `vmstat` in einer Datei zur späteren Analyse, indem Sie den Befehl wie folgt umleiten:

```bash
vmstat 2 > vmstat_output.txt
```

Durch die Anwendung dieser Tipps und die Nutzung von `vmstat` können Ingenieure und Entwickler die Leistung ihrer Systeme effektiv überwachen und optimieren.