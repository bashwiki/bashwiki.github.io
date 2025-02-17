# [Linux] Bash hostname Verwendung: Zeigt den Hostnamen des Systems an

## Übersicht
Der Befehl `hostname` wird verwendet, um den aktuellen Hostnamen des Systems anzuzeigen oder zu ändern. Der Hostname ist der Name, der einem Computer im Netzwerk zugewiesen ist, und wird häufig zur Identifizierung des Geräts verwendet.

## Verwendung
Die grundlegende Syntax des Befehls lautet:

```bash
hostname [Optionen] [Argumente]
```

## Häufige Optionen
- `-f`, `--fqdn`: Gibt den vollqualifizierten Domainnamen (FQDN) des Hosts zurück.
- `-s`, `--short`: Zeigt nur den kurzen Hostnamen an.
- `-i`, `--ip-address`: Gibt die IP-Adresse des Hosts zurück.
- `-A`, `--all-fqdns`: Listet alle FQDNs des Hosts auf.

## Häufige Beispiele
Hier sind einige praktische Beispiele für die Verwendung des Befehls `hostname`:

1. **Aktuellen Hostnamen anzeigen:**
   ```bash
   hostname
   ```

2. **Vollqualifizierten Domainnamen anzeigen:**
   ```bash
   hostname -f
   ```

3. **Kurzen Hostnamen anzeigen:**
   ```bash
   hostname -s
   ```

4. **IP-Adresse des Hosts anzeigen:**
   ```bash
   hostname -i
   ```

5. **Alle FQDNs des Hosts auflisten:**
   ```bash
   hostname -A
   ```

## Tipps
- Um den Hostnamen temporär zu ändern, können Sie einfach den Befehl `hostname neuer_hostname` verwenden. Beachten Sie, dass dies nach einem Neustart zurückgesetzt wird.
- Für eine dauerhafte Änderung des Hostnamens sollten Sie die Konfigurationsdatei `/etc/hostname` bearbeiten und den neuen Hostnamen dort eintragen.
- Überprüfen Sie nach Änderungen den Hostnamen mit dem Befehl `hostname`, um sicherzustellen, dass die Änderung erfolgreich war.