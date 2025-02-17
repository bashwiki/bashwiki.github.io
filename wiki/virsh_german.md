# [Linux] Bash virsh Verwendung: Verwaltung von virtuellen Maschinen

## Übersicht
Der `virsh`-Befehl ist ein Kommandozeilenwerkzeug zur Verwaltung von virtuellen Maschinen, die mit der Virtualisierungssoftware libvirt betrieben werden. Mit `virsh` können Benutzer virtuelle Maschinen erstellen, starten, stoppen und verwalten, sowie Informationen über die virtuellen Maschinen abrufen.

## Verwendung
Die grundlegende Syntax des `virsh`-Befehls lautet:

```bash
virsh [Optionen] [Argumente]
```

## Häufige Optionen
- `--help`: Zeigt die Hilfe für den Befehl an.
- `list`: Listet alle aktiven virtuellen Maschinen auf.
- `start <VM-Name>`: Startet eine angegebene virtuelle Maschine.
- `shutdown <VM-Name>`: Fährt eine angegebene virtuelle Maschine herunter.
- `destroy <VM-Name>`: Stoppt und entfernt eine virtuelle Maschine sofort.
- `define <XML-Datei>`: Definiert eine neue virtuelle Maschine basierend auf der bereitgestellten XML-Datei.

## Häufige Beispiele
Hier sind einige praktische Beispiele für die Verwendung von `virsh`:

1. **Liste der aktiven virtuellen Maschinen anzeigen:**
   ```bash
   virsh list
   ```

2. **Eine virtuelle Maschine starten:**
   ```bash
   virsh start meine_vm
   ```

3. **Eine virtuelle Maschine herunterfahren:**
   ```bash
   virsh shutdown meine_vm
   ```

4. **Eine virtuelle Maschine sofort stoppen:**
   ```bash
   virsh destroy meine_vm
   ```

5. **Eine neue virtuelle Maschine definieren:**
   ```bash
   virsh define /pfad/zur/meine_vm.xml
   ```

## Tipps
- Verwenden Sie `virsh --help`, um eine vollständige Liste der verfügbaren Befehle und Optionen zu erhalten.
- Speichern Sie häufig verwendete Befehle in einem Skript, um die Verwaltung Ihrer virtuellen Maschinen zu automatisieren.
- Überprüfen Sie regelmäßig den Status Ihrer virtuellen Maschinen, um sicherzustellen, dass sie ordnungsgemäß funktionieren.