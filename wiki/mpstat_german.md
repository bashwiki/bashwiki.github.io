# [리눅스] Bash mpstat 사용법

## Übersicht
Der Befehl `mpstat` ist ein Tool zur Überwachung der CPU-Nutzung in Linux-Systemen. Es gehört zum Paket `sysstat` und bietet detaillierte Statistiken über die CPU-Auslastung, die es Entwicklern und Systemadministratoren ermöglicht, die Leistung von Prozessoren in Mehrkernsystemen zu analysieren. Mit `mpstat` können Sie Informationen über die CPU-Auslastung in Echtzeit abrufen und historische Daten analysieren.

## Verwendung
Die grundlegende Syntax des Befehls `mpstat` lautet:

```bash
mpstat [OPTIONEN] [INTERVAL] [ANZAHL]
```

### Häufige Optionen:
- `-P ALL`: Zeigt die Statistiken für alle CPUs an.
- `-u`: Zeigt die CPU-Auslastung in Prozent an.
- `-h`: Gibt die Ausgabe in einem menschenlesbaren Format aus.
- `-V`: Zeigt die Versionsnummer von `mpstat` an.

### Parameter:
- `INTERVAL`: Gibt die Zeitspanne in Sekunden an, in der die Statistiken aktualisiert werden sollen.
- `ANZAHL`: Gibt die Anzahl der gewünschten Aktualisierungen an.

## Beispiele
### Beispiel 1: CPU-Auslastung für alle CPUs anzeigen
Um die CPU-Auslastung für alle verfügbaren CPUs alle 2 Sekunden anzuzeigen, verwenden Sie den folgenden Befehl:

```bash
mpstat -P ALL 2
```

### Beispiel 2: CPU-Auslastung über einen bestimmten Zeitraum erfassen
Um die CPU-Auslastung alle 5 Sekunden für insgesamt 3 Intervalle zu überwachen, können Sie diesen Befehl verwenden:

```bash
mpstat 5 3
```

## Tipps
- Verwenden Sie die Option `-h`, um die Ausgabe leserlicher zu gestalten, insbesondere wenn Sie die Statistiken in Skripten oder Berichten verwenden möchten.
- Kombinieren Sie `mpstat` mit anderen Überwachungstools wie `top` oder `htop`, um eine umfassendere Analyse der Systemleistung zu erhalten.
- Überwachen Sie die CPU-Auslastung regelmäßig, um Engpässe oder unerwartete Lastspitzen frühzeitig zu erkennen und zu beheben.