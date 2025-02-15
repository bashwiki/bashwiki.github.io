# [리눅스] Bash sysctl 사용법

## Übersicht

Der Befehl `sysctl` wird in Linux-Systemen verwendet, um Kernelparameter zur Laufzeit zu lesen und zu ändern. Er ermöglicht es Benutzern, verschiedene Aspekte des Kernels zu konfigurieren, ohne das System neu starten zu müssen. Dies ist besonders nützlich für die Optimierung der Systemleistung und die Anpassung des Verhaltens des Kernels an spezifische Anforderungen.

## Verwendung

Die grundlegende Syntax des `sysctl`-Befehls lautet:

```bash
sysctl [OPTIONEN] [PARAMETER]
```

### Häufige Optionen:

- `-a`, `--all`: Zeigt alle verfügbaren Kernelparameter an.
- `-n`, `--quiet`: Gibt nur den Wert des angegebenen Parameters aus, ohne den Parameter selbst anzuzeigen.
- `-w`, `--write`: Ändert den Wert eines Kernelparameters. Dies erfordert in der Regel Root-Rechte.
- `-p`, `--load`: Lädt die Parameter aus einer Datei, typischerweise `/etc/sysctl.conf`.

## Beispiele

### Beispiel 1: Alle Kernelparameter anzeigen

Um alle aktuellen Kernelparameter anzuzeigen, verwenden Sie den folgenden Befehl:

```bash
sysctl -a
```

### Beispiel 2: Einen Kernelparameter ändern

Um den Wert des Parameters `vm.swappiness` auf 10 zu setzen, verwenden Sie den folgenden Befehl:

```bash
sudo sysctl -w vm.swappiness=10
```

## Tipps

- Stellen Sie sicher, dass Sie über die erforderlichen Berechtigungen verfügen, um Kernelparameter zu ändern. In der Regel sind Root-Rechte erforderlich.
- Änderungen, die mit `sysctl -w` vorgenommen werden, sind nicht persistent und gehen nach einem Neustart verloren. Um Änderungen dauerhaft zu machen, fügen Sie die Parameter in die Datei `/etc/sysctl.conf` ein und laden Sie sie mit `sysctl -p`.
- Verwenden Sie `sysctl -n`, um den Wert eines Parameters zu überprüfen, ohne zusätzliche Informationen anzuzeigen. Dies ist nützlich für Skripte, in denen nur der Wert benötigt wird.