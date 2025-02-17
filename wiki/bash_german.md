# [Linux] Bash bash Verwendung: Befehle in der Kommandozeile ausführen

## Übersicht
Der Bash-Befehl ist eine Kommandozeilen-Schnittstelle, die es Benutzern ermöglicht, Befehle auszuführen, Skripte zu schreiben und die Systemumgebung zu steuern. Bash steht für "Bourne Again SHell" und ist eine der am häufigsten verwendeten Shells in Linux- und Unix-ähnlichen Betriebssystemen.

## Verwendung
Die grundlegende Syntax des Bash-Befehls lautet:

```bash
bash [Optionen] [Argumente]
```

## Häufige Optionen
- `-c`: Führt einen Befehl aus, der als Argument übergeben wird.
- `-i`: Startet die Shell im interaktiven Modus.
- `-l`: Startet die Shell als Login-Shell.
- `-s`: Liest Befehle von der Standardeingabe.

## Häufige Beispiele
Hier sind einige praktische Beispiele für die Verwendung von Bash:

1. **Ein einfaches Skript ausführen**:
   ```bash
   bash mein_skript.sh
   ```

2. **Einen Befehl direkt ausführen**:
   ```bash
   bash -c 'echo "Hallo Welt!"'
   ```

3. **Interaktive Shell starten**:
   ```bash
   bash -i
   ```

4. **Ein Skript mit Argumenten ausführen**:
   ```bash
   bash mein_skript.sh arg1 arg2
   ```

## Tipps
- Verwenden Sie `bash -i`, um eine interaktive Shell zu starten, wenn Sie mehrere Befehle nacheinander eingeben möchten.
- Nutzen Sie die Tab-Vervollständigung, um Befehle und Dateinamen schneller einzugeben.
- Speichern Sie häufig verwendete Befehle in Skripten, um die Effizienz zu steigern und Tippfehler zu vermeiden.