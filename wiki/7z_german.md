# [Linux] Bash 7z Verwendung: Dateien komprimieren und entpacken

## Übersicht
Der `7z`-Befehl ist ein leistungsstarkes Tool zur Dateikompression und -archivierung. Es unterstützt verschiedene Formate und ermöglicht das Erstellen, Entpacken und Verwalten von Archiven.

## Verwendung
Die grundlegende Syntax des Befehls lautet:

```
7z [Optionen] [Argumente]
```

## Häufige Optionen
- `a`: Fügt Dateien zu einem Archiv hinzu.
- `x`: Entpackt ein Archiv.
- `t`: Gibt den Typ des Archivs an.
- `l`: Listet den Inhalt eines Archivs auf.
- `d`: Löscht Dateien aus einem Archiv.

## Häufige Beispiele

### 1. Ein Archiv erstellen
Um ein neues Archiv zu erstellen und Dateien hinzuzufügen, verwenden Sie:

```bash
7z a meinArchiv.7z /pfad/zur/datei1 /pfad/zur/datei2
```

### 2. Ein Archiv entpacken
Um ein Archiv zu entpacken, verwenden Sie:

```bash
7z x meinArchiv.7z
```

### 3. Den Inhalt eines Archivs auflisten
Um den Inhalt eines Archivs anzuzeigen, verwenden Sie:

```bash
7z l meinArchiv.7z
```

### 4. Dateien aus einem Archiv löschen
Um eine Datei aus einem Archiv zu entfernen, verwenden Sie:

```bash
7z d meinArchiv.7z datei1
```

## Tipps
- Verwenden Sie die Option `-p`, um ein Passwort für Ihr Archiv festzulegen, z.B. `7z a -pMeinPasswort meinArchiv.7z /pfad/zur/datei`.
- Nutzen Sie die Option `-m0=Copy`, um Dateien ohne Kompression hinzuzufügen, was nützlich sein kann, wenn Sie die Geschwindigkeit priorisieren.
- Überprüfen Sie die Integrität Ihrer Archive mit der Option `t`, um sicherzustellen, dass sie nicht beschädigt sind.