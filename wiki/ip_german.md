# [리눅스] Bash ip 사용법

## Übersicht
Der Befehl `ip` ist ein leistungsstarkes Tool zur Verwaltung von Netzwerkverbindungen in Linux-basierten Systemen. Er wird verwendet, um Netzwerkgeräte, IP-Adressen, Routing-Tabellen und andere netzwerkbezogene Einstellungen zu konfigurieren und anzuzeigen. Der `ip`-Befehl ist Teil des `iproute2`-Pakets und wird oft als moderner Ersatz für die älteren Befehle `ifconfig` und `route` angesehen.

## Verwendung
Die grundlegende Syntax des `ip`-Befehls lautet:

```
ip [OPTIONEN] BEFEHL [BEFEHL-OPTIONEN]
```

Hier sind einige häufig verwendete Optionen und Befehle:

- `link`: Verwaltet Netzwerkgeräte (z.B. aktivieren/deaktivieren von Schnittstellen).
- `addr`: Zeigt IP-Adressen an oder konfiguriert sie.
- `route`: Zeigt die Routing-Tabelle an oder konfiguriert Routen.
- `neigh`: Verwaltet die ARP-Tabelle (Address Resolution Protocol).

## Beispiele
### Beispiel 1: Anzeigen von Netzwerkgeräten
Um alle Netzwerkgeräte und deren Status anzuzeigen, verwenden Sie den folgenden Befehl:

```bash
ip link show
```

Dieser Befehl listet alle verfügbaren Netzwerkinterfaces auf, einschließlich ihrer Statusinformationen (aktiv/inaktiv).

### Beispiel 2: Hinzufügen einer IP-Adresse
Um einer Schnittstelle (z.B. `eth0`) eine IP-Adresse hinzuzufügen, verwenden Sie den folgenden Befehl:

```bash
ip addr add 192.168.1.100/24 dev eth0
```

Dieser Befehl weist der Schnittstelle `eth0` die IP-Adresse `192.168.1.100` mit einer Subnetzmaske von `255.255.255.0` zu.

## Tipps
- Verwenden Sie `ip -h`, um eine Hilfeübersicht über die verfügbaren Optionen und Befehle zu erhalten.
- Um die Änderungen an den Netzwerkgeräten dauerhaft zu machen, müssen Sie die entsprechenden Konfigurationsdateien Ihres Systems anpassen, da Änderungen über den `ip`-Befehl nicht persistent sind.
- Nutzen Sie `ip addr flush` gefolgt von dem Interface-Namen, um alle IP-Adressen von einem Interface zu entfernen, bevor Sie neue IPs hinzufügen.
- Der `ip`-Befehl kann auch in Skripten verwendet werden, um Netzwerkoperationen automatisiert durchzuführen.