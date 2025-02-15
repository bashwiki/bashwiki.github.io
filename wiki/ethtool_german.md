# [리눅스] Bash ethtool 사용법

## Übersicht
Der Befehl `ethtool` ist ein leistungsfähiges Kommandozeilenwerkzeug in Linux, das verwendet wird, um die Eigenschaften und Einstellungen von Ethernet-Netzwerkgeräten zu überprüfen und zu konfigurieren. Mit `ethtool` können Ingenieure und Entwickler Informationen über die Netzwerkverbindung abrufen, wie z.B. die Geschwindigkeit, den Duplex-Modus, die unterstützten Funktionen und vieles mehr. Es ist ein unverzichtbares Werkzeug für die Netzwerkdiagnose und -optimierung.

## Verwendung
Die grundlegende Syntax des `ethtool`-Befehls lautet:

```bash
ethtool [OPTIONEN] <Schnittstelle>
```

Hierbei ist `<Schnittstelle>` der Name des Netzwerkinterfaces, das Sie untersuchen oder konfigurieren möchten (z.B. `eth0`, `ens33`).

### Häufige Optionen:
- `-i`: Zeigt Treiberinformationen für das angegebene Netzwerkinterface an.
- `-s`: Ermöglicht das Setzen von Einstellungen wie Geschwindigkeit und Duplex-Modus.
- `-p`: Blinkt die LEDs des Netzwerkinterfaces für eine bestimmte Zeit, um das Interface physisch zu identifizieren.
- `-a`: Zeigt die Auto-Negotiation-Einstellungen an.
- `-T`: Zeigt die unterstützten Transceiver-Einstellungen an.

## Beispiele
### Beispiel 1: Informationen über ein Netzwerkinterface abrufen
Um grundlegende Informationen über das Netzwerkinterface `eth0` abzurufen, verwenden Sie den folgenden Befehl:

```bash
ethtool eth0
```

Dieser Befehl gibt Details wie die Geschwindigkeit, den Duplex-Modus und die unterstützten Funktionen des Interfaces aus.

### Beispiel 2: Treiberinformationen anzeigen
Um die Treiberinformationen für das Interface `ens33` zu erhalten, verwenden Sie:

```bash
ethtool -i ens33
```

Dieser Befehl zeigt Informationen über den verwendeten Treiber, die Version und andere relevante Details an.

## Tipps
- Stellen Sie sicher, dass Sie über die erforderlichen Berechtigungen verfügen, um `ethtool` auszuführen. In vielen Fällen müssen Sie den Befehl als Root-Benutzer oder mit `sudo` ausführen.
- Verwenden Sie `ethtool -p <Schnittstelle>`, um ein Netzwerkinterface schnell zu identifizieren, wenn Sie mehrere Interfaces haben.
- Überprüfen Sie regelmäßig die Einstellungen Ihrer Netzwerkinterfaces mit `ethtool`, um sicherzustellen, dass sie optimal konfiguriert sind und keine Probleme auftreten.
- Nutzen Sie die `man`-Seite (`man ethtool`), um eine vollständige Liste der Optionen und deren Beschreibungen zu erhalten.