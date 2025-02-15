# [리눅스] Bash export 사용법

## Übersicht
Der Befehl `export` in Bash wird verwendet, um Umgebungsvariablen zu erstellen oder zu ändern, die für untergeordnete Prozesse verfügbar sind. Wenn eine Variable mit `export` markiert wird, wird sie in die Umgebung des aktuellen Shell-Prozesses und aller von ihm gestarteten Prozesse übertragen. Dies ist besonders nützlich, wenn Sie Konfigurationen oder Einstellungen für Skripte oder Programme bereitstellen möchten, die in einer neuen Shell-Instanz ausgeführt werden.

## Verwendung
Die grundlegende Syntax des `export`-Befehls lautet:

```bash
export VARIABLE_NAME=VALUE
```

### Häufige Optionen
- `-p`: Zeigt alle exportierten Variablen an.
- `-n`: Entfernt die Exportmarkierung von einer Variablen, sodass sie nicht mehr in untergeordnete Prozesse weitergegeben wird.

## Beispiele
### Beispiel 1: Eine Umgebungsvariable setzen
Um eine Umgebungsvariable namens `MY_VAR` mit dem Wert `HelloWorld` zu setzen, verwenden Sie den folgenden Befehl:

```bash
export MY_VAR=HelloWorld
```

Sie können dann den Wert der Variablen in der aktuellen Shell überprüfen:

```bash
echo $MY_VAR
```

### Beispiel 2: Exportieren mehrerer Variablen
Sie können auch mehrere Variablen in einer einzigen Zeile exportieren:

```bash
export VAR1=value1 VAR2=value2
```

Um die exportierten Variablen anzuzeigen, können Sie den `-p` Schalter verwenden:

```bash
export -p
```

## Tipps
- Stellen Sie sicher, dass Sie `export` verwenden, bevor Sie ein Skript oder Programm starten, das auf die Umgebungsvariablen zugreifen muss.
- Um Umgebungsvariablen in einer Shell-Sitzung zu löschen, verwenden Sie den Befehl `unset`:

```bash
unset MY_VAR
```

- Es ist eine gute Praxis, Umgebungsvariablen in einer Konfigurationsdatei wie `.bashrc` oder `.bash_profile` zu definieren, um sicherzustellen, dass sie bei jedem Start einer neuen Shell-Sitzung verfügbar sind.