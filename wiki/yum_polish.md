# [Linux] Bash yum użycie: Zarządzanie pakietami w systemie

## Overview
Polecenie `yum` (Yellowdog Updater, Modified) jest narzędziem do zarządzania pakietami w systemach opartych na Red Hat, takich jak CentOS i Fedora. Umożliwia instalację, aktualizację oraz usuwanie oprogramowania, a także zarządzanie repozytoriami pakietów.

## Usage
Podstawowa składnia polecenia `yum` wygląda następująco:

```bash
yum [opcje] [argumenty]
```

## Common Options
Oto kilka powszechnie używanych opcji dla polecenia `yum`:

- `install`: Instaluje pakiet.
- `remove`: Usuwa pakiet.
- `update`: Aktualizuje zainstalowane pakiety do najnowszych wersji.
- `search`: Wyszukuje pakiety w repozytoriach.
- `info`: Wyświetla informacje o pakiecie.
- `list`: Wyświetla listę dostępnych pakietów.

## Common Examples
Poniżej znajdują się przykłady użycia polecenia `yum`:

### Instalacja pakietu
Aby zainstalować pakiet, użyj polecenia:

```bash
yum install nazwa_pakietu
```

### Usunięcie pakietu
Aby usunąć zainstalowany pakiet, użyj:

```bash
yum remove nazwa_pakietu
```

### Aktualizacja wszystkich pakietów
Aby zaktualizować wszystkie zainstalowane pakiety, wykonaj:

```bash
yum update
```

### Wyszukiwanie pakietu
Aby wyszukać pakiet w repozytoriach, użyj:

```bash
yum search fraza
```

### Wyświetlanie informacji o pakiecie
Aby uzyskać szczegółowe informacje o pakiecie, użyj:

```bash
yum info nazwa_pakietu
```

## Tips
- Zawsze sprawdzaj dostępność aktualizacji przed instalacją nowych pakietów, aby uniknąć konfliktów.
- Używaj opcji `-y`, aby automatycznie potwierdzać instalacje i aktualizacje, co może przyspieszyć proces.
- Regularnie czyszcz pakiety i pamięć podręczną za pomocą `yum clean all`, aby zwolnić miejsce na dysku.