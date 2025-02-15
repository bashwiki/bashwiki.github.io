# [리눅스] Bash umask 사용법

## Übersicht
Der Befehl `umask` in Bash ist ein wichtiges Werkzeug zur Steuerung der Standardberechtigungen für neu erstellte Dateien und Verzeichnisse. Die Hauptfunktion von `umask` besteht darin, die Berechtigungen zu definieren, die von den Standardwerten abgezogen werden, wenn eine Datei oder ein Verzeichnis erstellt wird. Dies ermöglicht es Benutzern, die Sicherheit ihrer Dateien zu erhöhen, indem sie den Zugriff auf diese Dateien einschränken.

## Verwendung
Die grundlegende Syntax des `umask`-Befehls lautet:

```bash
umask [OPTIONEN] [WERT]
```

### Optionen
- **WERT**: Ein oktaler Wert, der die Berechtigungen angibt, die von den Standardberechtigungen abgezogen werden sollen. Zum Beispiel:
  - `022`: Entfernt die Schreibberechtigung für die Gruppe und andere.
  - `077`: Entfernt alle Berechtigungen für die Gruppe und andere.
- Wenn kein Wert angegeben wird, zeigt `umask` den aktuellen Wert an.

## Beispiele

### Beispiel 1: Aktuellen umask-Wert anzeigen
Um den aktuellen `umask`-Wert zu überprüfen, verwenden Sie einfach:

```bash
umask
```

### Beispiel 2: umask-Wert setzen
Um den `umask`-Wert auf `027` zu setzen, was bedeutet, dass die Gruppe keine Berechtigungen hat und andere Benutzer nur Leseberechtigungen haben, führen Sie den folgenden Befehl aus:

```bash
umask 027
```

Nach dem Setzen dieses Wertes werden neu erstellte Dateien standardmäßig die Berechtigungen `640` (rw-r-----) und neue Verzeichnisse `750` (rwxr-x---) haben.

## Tipps
- Überprüfen Sie regelmäßig Ihren `umask`-Wert, um sicherzustellen, dass er den Sicherheitsanforderungen Ihres Projekts entspricht.
- Setzen Sie `umask` in Ihren Shell-Startdateien (z. B. `.bashrc` oder `.bash_profile`), um sicherzustellen, dass der Wert bei jeder neuen Sitzung angewendet wird.
- Seien Sie vorsichtig beim Setzen von `umask` auf sehr restriktive Werte, da dies die Funktionalität von Anwendungen beeinträchtigen kann, die auf bestimmte Berechtigungen angewiesen sind.