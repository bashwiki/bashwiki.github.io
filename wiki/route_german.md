# [리눅스] Bash route 사용법

## Übersicht
Der Befehl `route` wird in Linux-Systemen verwendet, um die Routing-Tabelle des Systems anzuzeigen oder zu ändern. Die Routing-Tabelle ist eine Datenstruktur, die Informationen darüber enthält, wie Datenpakete an verschiedene Netzwerke weitergeleitet werden. Mit `route` können Ingenieure und Entwickler Netzwerkkonfigurationen verwalten und sicherstellen, dass Daten effizient zwischen verschiedenen Netzwerken übertragen werden.

## Verwendung
Die grundlegende Syntax des `route`-Befehls lautet:

```
route [OPTIONEN] [Befehl] [ZIEL] [GATEWAY] [PARAMETER]
```

### Häufige Optionen:
- `-n`: Zeigt die Routing-Tabelle in numerischer Form an, ohne die Hostnamen aufzulösen.
- `add`: Fügt eine neue Route zur Routing-Tabelle hinzu.
- `del`: Entfernt eine Route aus der Routing-Tabelle.
- `-net`: Gibt an, dass die Route zu einem Netzwerk und nicht zu einem einzelnen Host hinzugefügt oder entfernt wird.

## Beispiele
### Beispiel 1: Anzeigen der Routing-Tabelle
Um die aktuelle Routing-Tabelle anzuzeigen, können Sie den folgenden Befehl verwenden:

```bash
route -n
```

Dieser Befehl zeigt die Routing-Tabelle in numerischer Form an, was nützlich ist, um die IP-Adressen der Gateways und Netzwerke schnell zu überprüfen.

### Beispiel 2: Hinzufügen einer neuen Route
Um eine neue Route zu einem bestimmten Netzwerk hinzuzufügen, verwenden Sie den folgenden Befehl:

```bash
sudo route add -net 192.168.1.0/24 gw 192.168.1.1
```

In diesem Beispiel wird eine Route zum Netzwerk 192.168.1.0 mit der Subnetzmaske 255.255.255.0 hinzugefügt, wobei 192.168.1.1 als Gateway verwendet wird.

## Tipps
- Verwenden Sie die Option `-n`, um die Ausgabe zu beschleunigen, da die Namensauflösung umgangen wird.
- Seien Sie vorsichtig beim Hinzufügen oder Entfernen von Routen, da falsche Konfigurationen zu Netzwerkproblemen führen können.
- Überprüfen Sie regelmäßig die Routing-Tabelle, um sicherzustellen, dass alle Routen korrekt konfiguriert sind und keine unerwünschten Routen vorhanden sind.