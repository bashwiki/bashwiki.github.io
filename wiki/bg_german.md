# [리눅스] Bash bg 사용법

## Übersicht
Der Befehl `bg` in Bash wird verwendet, um einen gestoppten Job im Hintergrund fortzusetzen. Dies ist besonders nützlich, wenn Sie einen Prozess gestartet haben, der die Kontrolle über das Terminal übernommen hat, und Sie ihn weiterlaufen lassen möchten, während Sie andere Befehle im Terminal ausführen können. Der Befehl `bg` ermöglicht es Ihnen, die Ausführung eines Jobs im Hintergrund fortzusetzen, ohne dass er das Terminal blockiert.

## Verwendung
Die grundlegende Syntax des Befehls `bg` lautet:

```bash
bg [Jobnummer]
```

- **Jobnummer**: Dies ist die Nummer des gestoppten Jobs, den Sie im Hintergrund fortsetzen möchten. Wenn Sie keine Jobnummer angeben, wird der zuletzt gestoppte Job verwendet.

### Häufige Optionen
- Es gibt keine speziellen Optionen für den Befehl `bg`, da er in der Regel in Verbindung mit der Jobkontrolle verwendet wird. Die Jobnummer kann durch den Befehl `jobs` ermittelt werden, der eine Liste aller aktuellen Jobs anzeigt.

## Beispiele
### Beispiel 1: Einen gestoppten Job im Hintergrund fortsetzen
Angenommen, Sie haben einen langen Prozess gestartet, der gestoppt wurde (z. B. durch Drücken von `Ctrl+Z`):

```bash
$ sleep 100
```

Sie drücken `Ctrl+Z`, um den Prozess zu stoppen. Um den Prozess im Hintergrund fortzusetzen, verwenden Sie:

```bash
$ bg %1
```

Hierbei ist `%1` die Jobnummer des gestoppten Prozesses, die Sie mit dem Befehl `jobs` überprüfen können.

### Beispiel 2: Den zuletzt gestoppten Job im Hintergrund fortsetzen
Wenn Sie nur einen Job gestoppt haben und ihn im Hintergrund fortsetzen möchten, können Sie einfach `bg` ohne Jobnummer verwenden:

```bash
$ bg
```

Dieser Befehl setzt den zuletzt gestoppten Job im Hintergrund fort.

## Tipps
- Verwenden Sie den Befehl `jobs`, um eine Übersicht über alle aktiven Jobs zu erhalten. Dies hilft Ihnen, die Jobnummern zu identifizieren, die Sie mit `bg` verwenden möchten.
- Seien Sie vorsichtig, wenn Sie mehrere Jobs im Hintergrund ausführen. Stellen Sie sicher, dass Sie die Kontrolle über die Jobs behalten, um unerwartete Ergebnisse zu vermeiden.
- Kombinieren Sie `bg` mit `disown`, um einen Job vollständig von der Shell zu trennen, sodass er nicht mehr an Ihr Terminal gebunden ist.