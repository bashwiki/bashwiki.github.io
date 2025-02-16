# [Linux] Bash hostname użycie: wyświetlanie lub ustawianie nazwy hosta

## Przegląd
Polecenie `hostname` w systemie Linux służy do wyświetlania lub ustawiania nazwy hosta systemu. Nazwa hosta to unikalna etykieta przypisana do urządzenia w sieci, która identyfikuje je w komunikacji z innymi urządzeniami.

## Użycie
Podstawowa składnia polecenia `hostname` jest następująca:

```bash
hostname [opcje] [argumenty]
```

## Częste opcje
- `-a`, `--alias`: Wyświetla alias hosta.
- `-f`, `--fqdn`: Wyświetla w pełni kwalifikowaną nazwę domenową (FQDN).
- `-i`, `--ip-address`: Wyświetla adres IP przypisany do hosta.
- `-s`, `--short`: Wyświetla krótką nazwę hosta.

## Przykłady
1. Aby wyświetlić aktualną nazwę hosta:
   ```bash
   hostname
   ```

2. Aby ustawić nową nazwę hosta:
   ```bash
   sudo hostname nowa_nazwa
   ```

3. Aby wyświetlić w pełni kwalifikowaną nazwę domenową:
   ```bash
   hostname -f
   ```

4. Aby wyświetlić adres IP przypisany do hosta:
   ```bash
   hostname -i
   ```

5. Aby wyświetlić krótką nazwę hosta:
   ```bash
   hostname -s
   ```

## Wskazówki
- Używaj polecenia `sudo`, aby zmienić nazwę hosta, ponieważ wymaga to uprawnień administratora.
- Po zmianie nazwy hosta, rozważ ponowne uruchomienie systemu, aby upewnić się, że zmiana została zastosowana we wszystkich usługach.
- Sprawdź plik `/etc/hostname`, aby upewnić się, że nowa nazwa hosta została poprawnie zapisana.