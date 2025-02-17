# [Linux] Bash netstat Verwendung: Netzwerkverbindungen anzeigen

## Übersicht
Der Befehl `netstat` wird verwendet, um Netzwerkverbindungen, Routing-Tabellen, Schnittstellenstatistiken und andere Netzwerkinformationen anzuzeigen. Er ist ein nützliches Werkzeug zur Diagnose von Netzwerkproblemen und zur Überwachung von Verbindungen auf einem System.

## Verwendung
Die grundlegende Syntax des Befehls lautet:

```bash
netstat [Optionen] [Argumente]
```

## Häufige Optionen
- `-a`: Zeigt alle Verbindungen und Listening-Ports an.
- `-t`: Zeigt nur TCP-Verbindungen an.
- `-u`: Zeigt nur UDP-Verbindungen an.
- `-n`: Zeigt IP-Adressen und Portnummern numerisch an, anstatt sie in Namen aufzulösen.
- `-l`: Zeigt nur die Listening-Ports an.
- `-p`: Zeigt die PID und den Namen des Prozesses, der die Verbindung hält.

## Häufige Beispiele
Hier sind einige praktische Beispiele für die Verwendung von `netstat`:

1. **Alle aktiven Verbindungen anzeigen:**
   ```bash
   netstat -a
   ```

2. **Nur TCP-Verbindungen anzeigen:**
   ```bash
   netstat -t
   ```

3. **Nur Listening-Ports anzeigen:**
   ```bash
   netstat -l
   ```

4. **Verbindungen mit numerischen Adressen anzeigen:**
   ```bash
   netstat -n
   ```

5. **Verbindungen mit Prozessinformationen anzeigen:**
   ```bash
   netstat -p
   ```

## Tipps
- Verwenden Sie `netstat` zusammen mit `grep`, um gezielt nach bestimmten Verbindungen oder Ports zu suchen. Beispiel:
  ```bash
  netstat -tuln | grep 80
  ```
- Kombinieren Sie Optionen, um spezifischere Informationen zu erhalten. Zum Beispiel:
  ```bash
  netstat -tulnp
  ```
- Beachten Sie, dass `netstat` in einigen modernen Linux-Distributionen durch `ss` ersetzt wurde, das ähnliche Funktionen bietet, aber schneller und effizienter ist.