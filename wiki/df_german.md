# [리눅스] Bash df 사용법

## Übersicht
Der Befehl `df` (disk free) wird in der Bash verwendet, um Informationen über den verfügbaren und verwendeten Speicherplatz auf Dateisystemen anzuzeigen. Er bietet eine schnelle Möglichkeit, den Status des Speicherplatzes auf verschiedenen Laufwerken und Partitionen zu überprüfen, was besonders nützlich für Systemadministratoren und Entwickler ist, die die Speicherkapazität ihrer Systeme überwachen müssen.

## Verwendung
Die grundlegende Syntax des `df`-Befehls lautet:

```bash
df [OPTIONEN] [DATEISYSTEM]
```

### Häufige Optionen:
- `-h`: Gibt die Ausgabe in einem menschenlesbaren Format aus (z.B. in KB, MB oder GB).
- `-T`: Zeigt den Typ des Dateisystems an.
- `-a`: Zeigt auch die Dateisysteme an, die keinen Speicherplatz mehr zur Verfügung haben.
- `-i`: Zeigt Informationen über die Inodes an, anstatt über den Speicherplatz.

## Beispiele
### Beispiel 1: Grundlegende Verwendung
Um eine Übersicht über den Speicherplatz aller gemounteten Dateisysteme zu erhalten, können Sie einfach den Befehl `df` ohne Optionen verwenden:

```bash
df
```

### Beispiel 2: Menschenlesbare Ausgabe
Um die Ausgabe in einem verständlicheren Format zu erhalten, verwenden Sie die `-h`-Option:

```bash
df -h
```

Diese Ausgabe zeigt die Größe, den verwendeten Speicherplatz, den verfügbaren Speicherplatz und die Einhängepunkte in einem leicht lesbaren Format.

## Tipps
- Verwenden Sie die `-T`-Option, um den Typ des Dateisystems zu überprüfen, insbesondere wenn Sie mit verschiedenen Dateisystemen arbeiten.
- Kombinieren Sie `df` mit anderen Befehlen wie `grep`, um spezifische Informationen zu filtern. Zum Beispiel:

```bash
df -h | grep '/dev/sda1'
```

- Führen Sie `df` regelmäßig aus, um sicherzustellen, dass Ihr Speicherplatz nicht knapp wird, insbesondere auf Servern oder in produktiven Umgebungen.