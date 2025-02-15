# [리눅스] Bash firewalld 사용법

## Übersicht
Der Befehl `firewalld` ist ein dynamisches Firewall-Verwaltungstool, das in vielen Linux-Distributionen verwendet wird. Es ermöglicht die Verwaltung von Netzwerkzugriffsregeln und -richtlinien, um den Datenverkehr zu steuern und die Sicherheit des Systems zu erhöhen. `firewalld` verwendet Zonen, um unterschiedliche Vertrauensstufen für Netzwerkverbindungen zu definieren, und unterstützt sowohl IPv4- als auch IPv6-Adressen.

## Verwendung
Die grundlegende Syntax des Befehls `firewalld` lautet:

```bash
firewalld [OPTIONEN]
```

Einige häufig verwendete Optionen sind:

- `--start`: Startet den Firewalld-Dienst.
- `--stop`: Stoppt den Firewalld-Dienst.
- `--reload`: Lädt die Firewall-Regeln neu, ohne den Dienst neu zu starten.
- `--zone=<zone>`: Gibt die Zone an, die für die Regel angewendet werden soll.
- `--add-service=<service>`: Fügt einen Dienst zur angegebenen Zone hinzu.
- `--remove-service=<service>`: Entfernt einen Dienst aus der angegebenen Zone.

## Beispiele
Hier sind einige praktische Beispiele zur Verwendung von `firewalld`:

1. **Starten des Firewalld-Dienstes**:
   ```bash
   sudo systemctl start firewalld
   ```

2. **Hinzufügen des HTTP-Dienstes zur öffentlichen Zone**:
   ```bash
   sudo firewall-cmd --zone=public --add-service=http --permanent
   ```

3. **Neuladen der Firewall-Regeln**:
   ```bash
   sudo firewall-cmd --reload
   ```

## Tipps
- Verwenden Sie die Option `--permanent`, um sicherzustellen, dass die Änderungen auch nach einem Neustart des Systems bestehen bleiben.
- Überprüfen Sie regelmäßig den Status Ihrer Firewall mit dem Befehl `firewall-cmd --state`, um sicherzustellen, dass der Dienst aktiv ist.
- Nutzen Sie `firewall-cmd --list-all`, um eine Übersicht über alle aktiven Zonen und deren Regeln zu erhalten.
- Testen Sie neue Regeln in einer sicheren Umgebung, bevor Sie sie in einer Produktionsumgebung anwenden, um unerwartete Unterbrechungen zu vermeiden.