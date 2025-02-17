# [Linux] Bash jobs Verwendung: Zeigt aktive Jobs an

## Übersicht
Der Befehl `jobs` wird in der Bash verwendet, um eine Liste der aktuell laufenden und gestoppten Jobs im aktuellen Terminal anzuzeigen. Dies ist besonders nützlich, um den Status von Hintergrundprozessen zu überwachen.

## Verwendung
Die grundlegende Syntax des Befehls lautet:

```bash
jobs [Optionen]
```

## Häufige Optionen
- `-l`: Zeigt die Prozess-ID (PID) der Jobs an.
- `-n`: Zeigt nur die Jobs an, die seit dem letzten Aufruf von `jobs` geändert wurden.
- `-p`: Gibt nur die Prozess-IDs der Jobs aus.

## Häufige Beispiele
1. **Einfaches Anzeigen von Jobs:**
   ```bash
   jobs
   ```
   Dies zeigt eine Liste aller aktiven und gestoppten Jobs an.

2. **Jobs mit Prozess-IDs anzeigen:**
   ```bash
   jobs -l
   ```
   Diese Variante zeigt die Jobs zusammen mit ihren Prozess-IDs.

3. **Nur neue oder geänderte Jobs anzeigen:**
   ```bash
   jobs -n
   ```
   Hiermit werden nur die Jobs angezeigt, die seit dem letzten Befehl geändert wurden.

4. **Prozess-IDs der Jobs anzeigen:**
   ```bash
   jobs -p
   ```
   Dies gibt nur die Prozess-IDs der aktiven Jobs aus.

## Tipps
- Verwenden Sie `bg` und `fg`, um gestoppte Jobs im Hintergrund oder Vordergrund fortzusetzen.
- Überprüfen Sie regelmäßig Ihre Jobs, um sicherzustellen, dass keine wichtigen Prozesse im Hintergrund hängen bleiben.
- Kombinieren Sie `jobs` mit anderen Befehlen wie `kill`, um nicht mehr benötigte Prozesse zu beenden.