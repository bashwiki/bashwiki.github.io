# [리눅스] Bash true 사용법

## Übersicht
Der Befehl `true` ist ein einfacher Bash-Befehl, der immer mit dem Exit-Status 0 (Erfolg) zurückkehrt. Er wird häufig in Skripten verwendet, um eine erfolgreiche Bedingung zu simulieren oder als Platzhalter in Situationen, in denen ein Befehl erforderlich ist, aber keine Aktion ausgeführt werden soll. Der Hauptzweck von `true` besteht darin, die Ausführung von Skripten oder Befehlen zu steuern, ohne tatsächlich etwas zu tun.

## Verwendung
Die grundlegende Syntax des Befehls `true` ist sehr einfach:

```bash
true
```

Es gibt keine speziellen Optionen oder Argumente, die mit `true` verwendet werden können. Der Befehl hat keine Parameter und führt keine Operationen aus.

## Beispiele

### Beispiel 1: Verwendung in einer Bedingung
In diesem Beispiel verwenden wir `true` in einer `if`-Bedingung, um eine immer wahre Bedingung zu simulieren:

```bash
if true; then
    echo "Diese Bedingung ist immer wahr."
fi
```

Die Ausgabe dieses Skripts wird immer sein:

```
Diese Bedingung ist immer wahr.
```

### Beispiel 2: Platzhalter in einer Schleife
Hier verwenden wir `true` als Platzhalter in einer `while`-Schleife, die unendlich läuft:

```bash
while true; do
    echo "Die Schleife läuft unendlich."
    sleep 1
done
```

In diesem Fall wird die Schleife jede Sekunde eine Nachricht ausgeben, bis sie manuell gestoppt wird.

## Tipps
- Verwenden Sie `true` in Skripten, wenn Sie einen Befehl benötigen, der immer erfolgreich ist, um die Logik zu vereinfachen.
- `true` kann nützlich sein, um Platzhalter für zukünftige Befehle zu erstellen, die später hinzugefügt werden sollen.
- Kombinieren Sie `true` mit anderen Befehlen in Skripten, um die Ausführung zu steuern, ohne dass eine tatsächliche Aktion erforderlich ist.

Der Befehl `true` ist ein einfaches, aber nützliches Werkzeug in der Bash, das in vielen Skripten und Automatisierungsaufgaben verwendet werden kann.