# [리눅스] Bash iostat 사용법

## Übersicht
Der Befehl `iostat` ist ein leistungsstarkes Tool, das in der Linux-Umgebung verwendet wird, um Informationen über die CPU-Last und die Ein-/Ausgabe (I/O) Statistiken von Speichermedien zu überwachen. Es ist Teil des Pakets `sysstat` und wird häufig von Systemadministratoren und Entwicklern verwendet, um die Leistung von Systemen zu analysieren und Engpässe zu identifizieren.

## Verwendung
Die grundlegende Syntax des Befehls `iostat` lautet:

```bash
iostat [OPTIONEN] [INTERVAL] [ANZAHL]
```

### Häufige Optionen:
- `-c`: Zeigt nur die CPU-Statistiken an.
- `-d`: Zeigt nur die I/O-Statistiken für die Geräte an.
- `-x`: Zeigt erweiterte Statistiken für die Geräte an.
- `-m`: Gibt die Statistiken in Megabyte pro Sekunde aus.
- `-p [DEVICE]`: Zeigt Statistiken für ein bestimmtes Gerät an.

## Beispiele
### Beispiel 1: Grundlegende Nutzung
Um die CPU- und I/O-Statistiken alle 2 Sekunden anzuzeigen, verwenden Sie den folgenden Befehl:

```bash
iostat 2
```

### Beispiel 2: Erweiterte Statistiken für ein bestimmtes Gerät
Um erweiterte Statistiken für das Gerät `sda` anzuzeigen, können Sie den folgenden Befehl verwenden:

```bash
iostat -x -p sda 2 5
```

Dieser Befehl zeigt alle 2 Sekunden für 5 Intervalle die erweiterten Statistiken für das Gerät `sda` an.

## Tipps
- Verwenden Sie die Option `-m`, um die Ausgabe in Megabyte pro Sekunde zu erhalten, was die Interpretation der I/O-Statistiken erleichtert.
- Kombinieren Sie `iostat` mit anderen Monitoring-Tools wie `top` oder `vmstat`, um ein umfassenderes Bild der Systemleistung zu erhalten.
- Überwachen Sie die Statistiken über längere Zeiträume, um Trends zu erkennen und potenzielle Engpässe frühzeitig zu identifizieren.