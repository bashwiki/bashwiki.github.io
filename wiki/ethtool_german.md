# [Linux] Bash ethtool Verwendung: Netzwerkschnittstelleninformationen anzeigen und konfigurieren

## Übersicht
Der `ethtool`-Befehl ist ein leistungsstarkes Werkzeug zur Anzeige und Konfiguration von Netzwerkschnittstellen in Linux. Er ermöglicht es Benutzern, Informationen über Ethernet-Geräte abzurufen und verschiedene Parameter wie Geschwindigkeit, Duplex-Modus und andere Einstellungen zu ändern.

## Verwendung
Die grundlegende Syntax des `ethtool`-Befehls lautet:

```bash
ethtool [Optionen] [Argumente]
```

## Häufige Optionen
- `-s`: Setzt die Parameter der Netzwerkschnittstelle.
- `-i`: Zeigt Informationen über den Treiber der Netzwerkschnittstelle an.
- `-p`: Blinkt die LED der angegebenen Schnittstelle für eine bestimmte Zeit.
- `-a`: Zeigt die Auto-Negotiation-Einstellungen an.
- `-t`: Führt einen Selbsttest der Netzwerkschnittstelle durch.

## Häufige Beispiele
Um Informationen über eine Netzwerkschnittstelle anzuzeigen, verwenden Sie:

```bash
ethtool eth0
```

Um den Treiber der Netzwerkschnittstelle anzuzeigen, verwenden Sie:

```bash
ethtool -i eth0
```

Um die LED der Schnittstelle für 10 Sekunden blinken zu lassen, verwenden Sie:

```bash
ethtool -p eth0 10
```

Um die Auto-Negotiation-Einstellungen anzuzeigen, verwenden Sie:

```bash
ethtool -a eth0
```

Um die Geschwindigkeit und den Duplex-Modus einer Schnittstelle zu ändern, verwenden Sie:

```bash
ethtool -s eth0 speed 100 duplex full
```

## Tipps
- Stellen Sie sicher, dass Sie über die erforderlichen Berechtigungen verfügen, um `ethtool` auszuführen, da einige Optionen Administratorrechte benötigen.
- Verwenden Sie `man ethtool`, um die vollständige Dokumentation und alle verfügbaren Optionen zu lesen.
- Testen Sie Änderungen an der Netzwerkschnittstelle in einer sicheren Umgebung, um unerwartete Verbindungsprobleme zu vermeiden.