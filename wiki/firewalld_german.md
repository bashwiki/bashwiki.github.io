# [Linux] Bash firewalld Verwendung: Verwaltung von Firewall-Regeln

## Übersicht
Der Befehl `firewalld` ist ein dynamisches Firewall-Management-Tool, das es Benutzern ermöglicht, Firewall-Regeln in Echtzeit zu verwalten. Es bietet eine benutzerfreundliche Schnittstelle zur Konfiguration von Netzwerksicherheitsrichtlinien und unterstützt sowohl IPv4- als auch IPv6-Netzwerke.

## Verwendung
Die grundlegende Syntax des `firewalld`-Befehls lautet:

```bash
firewalld [Optionen] [Argumente]
```

## Häufige Optionen
- `--zone`: Gibt die Zone an, in der die Regel angewendet werden soll.
- `--add-service`: Fügt einen Dienst zur angegebenen Zone hinzu.
- `--remove-service`: Entfernt einen Dienst aus der angegebenen Zone.
- `--add-port`: Öffnet einen bestimmten Port in der angegebenen Zone.
- `--remove-port`: Schließt einen bestimmten Port in der angegebenen Zone.
- `--list-all`: Listet alle aktuellen Regeln und Einstellungen für eine Zone auf.

## Häufige Beispiele
Hier sind einige praktische Beispiele zur Verwendung von `firewalld`:

### 1. Dienst zur Zone hinzufügen
Um den HTTP-Dienst zur öffentlichen Zone hinzuzufügen, verwenden Sie den folgenden Befehl:

```bash
firewall-cmd --zone=public --add-service=http
```

### 2. Dienst aus der Zone entfernen
Um den HTTP-Dienst aus der öffentlichen Zone zu entfernen, verwenden Sie:

```bash
firewall-cmd --zone=public --remove-service=http
```

### 3. Port öffnen
Um den Port 8080 in der öffentlichen Zone zu öffnen, verwenden Sie:

```bash
firewall-cmd --zone=public --add-port=8080/tcp
```

### 4. Port schließen
Um den Port 8080 in der öffentlichen Zone zu schließen, verwenden Sie:

```bash
firewall-cmd --zone=public --remove-port=8080/tcp
```

### 5. Alle Regeln auflisten
Um alle Regeln und Einstellungen der öffentlichen Zone anzuzeigen, verwenden Sie:

```bash
firewall-cmd --zone=public --list-all
```

## Tipps
- Stellen Sie sicher, dass Sie `firewalld` mit Root-Rechten ausführen, um Änderungen vorzunehmen.
- Verwenden Sie die Option `--permanent`, um Änderungen dauerhaft zu machen, z.B. `--add-service=http --permanent`.
- Überprüfen Sie regelmäßig Ihre Firewall-Regeln, um sicherzustellen, dass keine unerwünschten Dienste oder Ports geöffnet sind.