# [Linux] Bash mpstat Verwendung: Überwachung der CPU-Auslastung

## Übersicht
Der Befehl `mpstat` wird verwendet, um die CPU-Auslastung in einem Linux-System zu überwachen. Er zeigt Statistiken für jede CPU oder für alle CPUs zusammen an und hilft dabei, die Leistung des Systems zu analysieren.

## Verwendung
Die grundlegende Syntax des Befehls lautet:

```bash
mpstat [Optionen] [Argumente]
```

## Häufige Optionen
- `-P ALL`: Zeigt Statistiken für alle CPUs an.
- `-u`: Zeigt die CPU-Auslastung in Prozent an.
- `-o JSON`: Gibt die Ausgabe im JSON-Format aus.
- `-h`: Zeigt die Hilfe und die verfügbaren Optionen an.

## Häufige Beispiele
Hier sind einige praktische Beispiele für die Verwendung von `mpstat`:

1. **CPU-Auslastung für alle CPUs anzeigen:**
   ```bash
   mpstat -P ALL
   ```

2. **CPU-Auslastung alle 5 Sekunden aktualisieren:**
   ```bash
   mpstat 5
   ```

3. **CPU-Auslastung im JSON-Format ausgeben:**
   ```bash
   mpstat -o JSON
   ```

4. **Nur die Auslastung der ersten CPU anzeigen:**
   ```bash
   mpstat -P 0
   ```

## Tipps
- Verwenden Sie `mpstat` in Kombination mit anderen Überwachungstools wie `top` oder `htop`, um ein umfassenderes Bild der Systemleistung zu erhalten.
- Überwachen Sie die CPU-Auslastung regelmäßig, um Engpässe frühzeitig zu erkennen und zu beheben.
- Nutzen Sie die JSON-Ausgabe, wenn Sie die Daten in eine Anwendung oder ein Skript integrieren möchten.