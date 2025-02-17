# [Linux] Bash exit Gebrauch: Beenden von Shell-Sitzungen

## Übersicht
Der Befehl `exit` wird in Bash verwendet, um eine Shell-Sitzung zu beenden. Er kann sowohl in interaktiven Shells als auch in Skripten eingesetzt werden, um den Exit-Status zurückzugeben, der angibt, ob die Sitzung erfolgreich war oder ob ein Fehler aufgetreten ist.

## Verwendung
Die grundlegende Syntax des Befehls lautet:

```bash
exit [options] [status]
```

## Häufige Optionen
- `status`: Ein ganzzahliger Wert, der den Exit-Status angibt. Ein Wert von `0` bedeutet in der Regel Erfolg, während jeder andere Wert einen Fehler darstellt.

## Häufige Beispiele
1. **Einfaches Beenden der Shell:**
   ```bash
   exit
   ```

2. **Beenden mit einem spezifischen Status:**
   ```bash
   exit 1
   ```

3. **Beenden eines Bash-Skripts:**
   ```bash
   #!/bin/bash
   echo "Das Skript wird beendet."
   exit 0
   ```

4. **Verwendung in einer Funktion:**
   ```bash
   meine_funktion() {
       echo "Fehler aufgetreten!"
       exit 1
   }
   meine_funktion
   ```

## Tipps
- Verwenden Sie `exit 0`, um anzuzeigen, dass ein Skript oder eine Funktion erfolgreich abgeschlossen wurde.
- Nutzen Sie spezifische Exit-Codes, um verschiedene Fehlerarten zu kennzeichnen, was die Fehlersuche erleichtert.
- In interaktiven Shells kann `exit` ohne Argumente verwendet werden, um die aktuelle Sitzung zu beenden.