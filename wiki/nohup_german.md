# [리눅스] Bash nohup 사용법

## Übersicht
Der Befehl `nohup` (kurz für "no hang up") wird in der Bash verwendet, um Prozesse zu starten, die unabhängig von der aktuellen Sitzung weiterlaufen. Dies ist besonders nützlich, wenn Sie einen langen Prozess ausführen möchten, der nicht unterbrochen werden soll, selbst wenn Sie sich von der Shell abmelden oder die Verbindung zum Terminal verlieren. `nohup` leitet die Standardausgabe und die Standardfehlerausgabe des Prozesses standardmäßig in eine Datei namens `nohup.out`, es sei denn, Sie geben eine andere Ausgabedatei an.

## Verwendung
Die grundlegende Syntax des `nohup`-Befehls lautet:

```bash
nohup Befehl [Argumente] &
```

### Optionen
- `Befehl`: Der auszuführende Befehl oder das Skript.
- `[Argumente]`: Optional, die Argumente, die an den Befehl übergeben werden.
- `&`: Führt den Befehl im Hintergrund aus, sodass Sie die Shell weiterhin verwenden können.

## Beispiele
### Beispiel 1: Ein einfaches Skript im Hintergrund ausführen
Angenommen, Sie haben ein Skript namens `mein_script.sh`, das lange läuft. Sie können es mit `nohup` wie folgt ausführen:

```bash
nohup ./mein_script.sh &
```

Die Ausgabe wird in die Datei `nohup.out` geschrieben, und das Skript läuft im Hintergrund weiter, auch wenn Sie sich abmelden.

### Beispiel 2: Ein Befehl mit spezifischer Ausgabedatei
Wenn Sie die Ausgabe in eine spezifische Datei umleiten möchten, können Sie dies wie folgt tun:

```bash
nohup ./mein_script.sh > meine_ausgabe.log 2>&1 &
```

Hierbei wird die Standardausgabe und der Standardfehler in die Datei `meine_ausgabe.log` geschrieben.

## Tipps
- Überprüfen Sie regelmäßig die `nohup.out`-Datei oder die von Ihnen angegebene Ausgabedatei, um sicherzustellen, dass Ihr Prozess wie erwartet läuft.
- Verwenden Sie den Befehl `jobs`, um alle Hintergrundprozesse zu sehen, die in Ihrer aktuellen Shell-Sitzung laufen.
- Nutzen Sie `disown`, um einen Hintergrundprozess von der aktuellen Shell zu trennen, sodass er weiterläuft, auch wenn die Shell geschlossen wird.
- Stellen Sie sicher, dass Sie die Berechtigungen für das Skript oder den Befehl, den Sie ausführen möchten, korrekt gesetzt haben, um Ausführungsfehler zu vermeiden.