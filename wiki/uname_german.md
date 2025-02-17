# [Linux] Bash uname Verwendung: Systeminformationen anzeigen

## Übersicht
Der Befehl `uname` wird verwendet, um Informationen über das Betriebssystem und die Hardware des Systems anzuzeigen. Er liefert grundlegende Informationen, die für die Systemadministration und Fehlersuche nützlich sein können.

## Verwendung
Die grundlegende Syntax des Befehls lautet:

```bash
uname [Optionen]
```

## Häufige Optionen
- `-a`: Zeigt alle verfügbaren Informationen an.
- `-s`: Gibt den Namen des Betriebssystems aus.
- `-n`: Zeigt den Netzwerk-Hostnamen des Systems an.
- `-r`: Gibt die Kernel-Version aus.
- `-v`: Zeigt die Versionsnummer des Kernels an.
- `-m`: Gibt den Maschinen-Typ aus (z.B. x86_64).
- `-p`: Gibt den Prozessor-Typ aus (wenn verfügbar).
- `-i`: Gibt die Hardware-Plattform aus (wenn verfügbar).
- `-o`: Gibt den Namen des Betriebssystem-Anbieters aus.

## Häufige Beispiele
Hier sind einige praktische Beispiele für die Verwendung von `uname`:

1. **Alle Informationen anzeigen:**
   ```bash
   uname -a
   ```

2. **Nur den Namen des Betriebssystems anzeigen:**
   ```bash
   uname -s
   ```

3. **Kernel-Version anzeigen:**
   ```bash
   uname -r
   ```

4. **Maschinen-Typ anzeigen:**
   ```bash
   uname -m
   ```

5. **Netzwerk-Hostnamen anzeigen:**
   ```bash
   uname -n
   ```

## Tipps
- Verwenden Sie `uname -a`, um eine umfassende Übersicht über Ihr System zu erhalten.
- Kombinieren Sie `uname` mit anderen Befehlen, um Skripte zu erstellen, die auf spezifische Systeminformationen reagieren.
- Beachten Sie, dass einige Optionen möglicherweise nicht auf allen Systemen verfügbar sind, abhängig von der verwendeten Linux-Distribution.