# [Linux] Bash virsh użycie: zarządzanie maszynami wirtualnymi

## Overview
Polecenie `virsh` jest narzędziem wiersza poleceń, które umożliwia zarządzanie maszynami wirtualnymi w środowisku wirtualizacji opartym na technologii libvirt. Umożliwia użytkownikom tworzenie, uruchamianie, zatrzymywanie oraz konfigurowanie maszyn wirtualnych.

## Usage
Podstawowa składnia polecenia `virsh` jest następująca:

```bash
virsh [opcje] [argumenty]
```

## Common Options
- `list` - wyświetla listę aktywnych maszyn wirtualnych.
- `start <nazwa>` - uruchamia maszynę wirtualną o podanej nazwie.
- `shutdown <nazwa>` - zamyka maszynę wirtualną o podanej nazwie.
- `define <plik>` - definiuje nową maszynę wirtualną na podstawie pliku XML.
- `destroy <nazwa>` - natychmiastowo zatrzymuje maszynę wirtualną o podanej nazwie.

## Common Examples
- Aby wyświetlić listę aktywnych maszyn wirtualnych:
  ```bash
  virsh list
  ```

- Aby uruchomić maszynę wirtualną o nazwie "mojaVM":
  ```bash
  virsh start mojaVM
  ```

- Aby zamknąć maszynę wirtualną o nazwie "mojaVM":
  ```bash
  virsh shutdown mojaVM
  ```

- Aby zdefiniować nową maszynę wirtualną z pliku XML:
  ```bash
  virsh define /ścieżka/do/pliku.xml
  ```

- Aby natychmiastowo zatrzymać maszynę wirtualną o nazwie "mojaVM":
  ```bash
  virsh destroy mojaVM
  ```

## Tips
- Zawsze sprawdzaj status maszyny wirtualnej przed podjęciem działań, aby uniknąć niepotrzebnych błędów.
- Używaj opcji `--help`, aby uzyskać więcej informacji na temat dostępnych poleceń i opcji w `virsh`.
- Regularnie twórz kopie zapasowe plików konfiguracyjnych maszyn wirtualnych, aby móc je łatwo przywrócić w razie potrzeby.