# [Linux] Bash htop Verwendung: Systemüberwachung in Echtzeit

## Übersicht
Der Befehl `htop` ist ein interaktives Prozess-Viewer-Tool für Unix-basierte Systeme. Es bietet eine benutzerfreundliche Oberfläche zur Überwachung von Systemressourcen und Prozessen in Echtzeit, einschließlich CPU-, Speicher- und Swap-Nutzung.

## Verwendung
Die grundlegende Syntax des Befehls lautet:

```bash
htop [Optionen] [Argumente]
```

## Häufige Optionen
- `-h`, `--help`: Zeigt die Hilfe und eine Liste der Optionen an.
- `-s`, `--sort`: Ermöglicht das Sortieren der Prozesse nach verschiedenen Kriterien (z. B. CPU, Speicher).
- `-p`, `--pid`: Zeigt nur die Prozesse mit den angegebenen Prozess-IDs an.
- `--tree`: Zeigt die Prozesse in einer Baumstruktur an, um die Hierarchie darzustellen.

## Häufige Beispiele
- **Einfaches Starten von htop:**
  ```bash
  htop
  ```
  
- **Sortieren nach CPU-Nutzung:**
  ```bash
  htop -s PERCENT_CPU
  ```

- **Prozesse eines bestimmten Benutzers anzeigen:**
  ```bash
  htop -u benutzername
  ```

- **Nur bestimmte Prozess-IDs anzeigen:**
  ```bash
  htop -p 1234,5678
  ```

- **Prozesse in Baumstruktur anzeigen:**
  ```bash
  htop --tree
  ```

## Tipps
- Verwenden Sie die Funktionstasten (F1 bis F10) für schnellen Zugriff auf verschiedene Funktionen, wie Hilfe (F1) oder das Beenden von Prozessen (F9).
- Nutzen Sie die Filterfunktion (F3), um gezielt nach Prozessen zu suchen.
- Passen Sie die Anzeige an, indem Sie die Spalten mit der Taste F2 (Setup) konfigurieren, um nur die benötigten Informationen anzuzeigen.