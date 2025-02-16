# [Linux] Bash exit użycie: Zakończenie skryptu lub sesji

## Overview
Polecenie `exit` w Bashu służy do zakończenia bieżącego skryptu lub sesji powłoki. Można je wykorzystać do przekazania kodu zakończenia, co może być przydatne w przypadku skryptów, które są wywoływane przez inne programy.

## Usage
Podstawowa składnia polecenia `exit` jest następująca:

```bash
exit [options] [arguments]
```

## Common Options
- `n`: Opcjonalny argument, który określa kod zakończenia. Domyślnie jest to 0, co oznacza, że skrypt zakończył się pomyślnie.

## Common Examples

### Zakończenie skryptu z kodem 0
```bash
#!/bin/bash
echo "Zakończenie skryptu."
exit 0
```

### Zakończenie skryptu z kodem błędu
```bash
#!/bin/bash
echo "Wystąpił błąd."
exit 1
```

### Zakończenie sesji powłoki
Aby zakończyć bieżącą sesję powłoki, wystarczy wpisać:
```bash
exit
```

### Użycie w skrypcie z warunkiem
```bash
#!/bin/bash
if [ "$1" -lt 0 ]; then
    echo "Argument musi być liczbą nieujemną."
    exit 1
fi
echo "Argument jest poprawny."
exit 0
```

## Tips
- Zawsze używaj odpowiednich kodów zakończenia, aby ułatwić debugowanie skryptów.
- Używaj `exit` w połączeniu z warunkami, aby kontrolować przepływ skryptu.
- Pamiętaj, że kod zakończenia 0 oznacza sukces, a każdy inny kod oznacza błąd.