# [리눅스] Bash netstat 사용법

## Übersicht
Der Befehl `netstat` (Network Statistics) ist ein nützliches Tool in der Bash, das Netzwerkverbindungen, Routing-Tabellen, Schnittstellenstatistiken und andere Netzwerkinformationen anzeigt. Er wird häufig von Ingenieuren und Entwicklern verwendet, um den Status von Netzwerkverbindungen zu überwachen und Probleme zu diagnostizieren.

## Verwendung
Die grundlegende Syntax des Befehls lautet:

```bash
netstat [Optionen]
```

Einige gängige Optionen sind:

- `-a`: Zeigt alle Verbindungen und Listening-Ports an.
- `-t`: Zeigt nur TCP-Verbindungen an.
- `-u`: Zeigt nur UDP-Verbindungen an.
- `-n`: Zeigt Adressen und Portnummern numerisch an, anstatt sie aufzulösen.
- `-l`: Zeigt nur die Ports an, die auf eingehende Verbindungen warten.

## Beispiele
Hier sind einige praktische Beispiele zur Verwendung des Befehls `netstat`:

1. **Alle aktiven Verbindungen anzeigen**:
   ```bash
   netstat -a
   ```
   Dieser Befehl zeigt alle aktiven Netzwerkverbindungen sowie die Ports, die auf eingehende Verbindungen warten.

2. **Nur TCP-Verbindungen anzeigen**:
   ```bash
   netstat -t -n
   ```
   Mit diesem Befehl werden nur die aktiven TCP-Verbindungen angezeigt, wobei die Adressen und Portnummern numerisch dargestellt werden.

## Tipps
- Verwenden Sie die Option `-p`, um den Prozess anzuzeigen, der die Verbindung hält. Dies kann hilfreich sein, um herauszufinden, welche Anwendung eine bestimmte Verbindung verwendet.
- Kombinieren Sie `netstat` mit `grep`, um nach bestimmten Verbindungen oder Ports zu filtern. Zum Beispiel:
  ```bash
  netstat -tuln | grep 80
  ```
  Dieser Befehl zeigt alle Verbindungen auf Port 80 an.
- Beachten Sie, dass `netstat` in einigen modernen Linux-Distributionen durch `ss` ersetzt wird, das ähnliche, aber erweiterte Funktionen bietet.