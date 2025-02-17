# [Linux] Bash times Verwendung: Zeigt die CPU-Zeit der Shell an

## Übersicht
Der Befehl `times` wird in der Bash verwendet, um die CPU-Zeit anzuzeigen, die von der aktuellen Shell und ihren Kindprozessen verbraucht wurde. Dies kann nützlich sein, um die Leistung von Skripten oder Befehlen zu überwachen.

## Verwendung
Die grundlegende Syntax des Befehls ist:

```bash
times [options] [arguments]
```

## Häufige Optionen
Der Befehl `times` hat keine speziellen Optionen, die häufig verwendet werden. Er gibt einfach die CPU-Zeit aus, die von der Shell und ihren Prozessen verwendet wurde.

## Häufige Beispiele

### Beispiel 1: Einfache Verwendung
Um die CPU-Zeit der aktuellen Shell anzuzeigen, geben Sie einfach `times` ein:

```bash
times
```

### Beispiel 2: Verwendung in einem Skript
Wenn Sie ein Skript ausführen und die CPU-Zeit am Ende anzeigen möchten, können Sie `times` am Ende des Skripts hinzufügen:

```bash
#!/bin/bash
# Einfache Berechnung
for i in {1..1000000}; do
  echo $i > /dev/null
done

# Zeige die CPU-Zeit an
times
```

### Beispiel 3: Verwendung nach mehreren Befehlen
Sie können `times` auch nach der Ausführung mehrerer Befehle verwenden, um die gesamte CPU-Zeit zu sehen:

```bash
echo "Starte Berechnungen..."
sleep 2
echo "Berechnungen abgeschlossen."
times
```

## Tipps
- Verwenden Sie `times` am Ende von Skripten, um die Gesamtzeit zu erfassen, die für die Ausführung benötigt wurde.
- Beachten Sie, dass `times` nur die CPU-Zeit anzeigt und keine Informationen über die tatsächliche Laufzeit oder andere Leistungsmetriken liefert.
- Nutzen Sie `times` in Kombination mit anderen Befehlen zur Leistungsüberwachung, um Engpässe in Skripten zu identifizieren.