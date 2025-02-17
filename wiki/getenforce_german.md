# [Linux] Bash getenforce Verwendung: Überprüfen des SELinux-Status

## Übersicht
Der Befehl `getenforce` wird verwendet, um den aktuellen Status von SELinux (Security-Enhanced Linux) auf einem Linux-System zu überprüfen. Er zeigt an, ob SELinux aktiviert ist und in welchem Modus es läuft (z. B. Enforcing, Permissive oder Disabled).

## Verwendung
Die grundlegende Syntax des Befehls lautet:

```bash
getenforce [Optionen]
```

## Häufige Optionen
- Es gibt keine speziellen Optionen für `getenforce`, da der Befehl einfach den aktuellen Status zurückgibt. 

## Häufige Beispiele
Hier sind einige praktische Beispiele für die Verwendung von `getenforce`:

1. **Überprüfen des SELinux-Status:**
   ```bash
   getenforce
   ```
   Dieser Befehl gibt den aktuellen Modus von SELinux zurück, z. B. `Enforcing`, `Permissive` oder `Disabled`.

2. **Verwendung in einem Skript:**
   ```bash
   if [ "$(getenforce)" == "Enforcing" ]; then
       echo "SELinux ist im Enforcing-Modus."
   else
       echo "SELinux ist nicht im Enforcing-Modus."
   fi
   ```
   Dieses Skript überprüft den SELinux-Status und gibt eine entsprechende Nachricht aus.

## Tipps
- Verwenden Sie `getenforce` regelmäßig, um sicherzustellen, dass SELinux im gewünschten Modus läuft, insbesondere auf Produktionssystemen.
- Kombinieren Sie `getenforce` mit anderen Befehlen, um Skripte zu erstellen, die auf den SELinux-Status reagieren.
- Beachten Sie, dass Änderungen am SELinux-Modus in der Regel einen Neustart oder eine Neuladen der Konfiguration erfordern, um wirksam zu werden.