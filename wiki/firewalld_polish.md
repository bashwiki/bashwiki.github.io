# [Linux] Bash firewalld użycie: Zarządzanie zaporą sieciową

## Przegląd
`firewalld` to narzędzie do zarządzania zaporą sieciową w systemach Linux, które umożliwia dynamiczne zarządzanie regułami zapory. Umożliwia łatwe dodawanie, usuwanie i modyfikowanie reguł bez potrzeby przerywania aktywnych połączeń.

## Użycie
Podstawowa składnia polecenia `firewalld` wygląda następująco:

```bash
firewalld [opcje] [argumenty]
```

## Częste opcje
- `--zone`: Określa strefę, do której mają być zastosowane reguły.
- `--add-service`: Dodaje usługę do określonej strefy.
- `--remove-service`: Usuwa usługę z określonej strefy.
- `--add-port`: Otwiera określony port w danej strefie.
- `--remove-port`: Zamyka określony port w danej strefie.
- `--list-all`: Wyświetla wszystkie reguły i usługi w danej strefie.

## Częste przykłady
1. **Dodawanie usługi do strefy:**
   ```bash
   firewall-cmd --zone=public --add-service=http
   ```

2. **Usuwanie usługi z strefy:**
   ```bash
   firewall-cmd --zone=public --remove-service=http
   ```

3. **Otwieranie portu:**
   ```bash
   firewall-cmd --zone=public --add-port=8080/tcp
   ```

4. **Zamykanie portu:**
   ```bash
   firewall-cmd --zone=public --remove-port=8080/tcp
   ```

5. **Wyświetlanie wszystkich reguł w strefie:**
   ```bash
   firewall-cmd --zone=public --list-all
   ```

## Wskazówki
- Zawsze sprawdzaj aktualny stan zapory przed wprowadzeniem zmian, używając `--list-all`.
- Używaj opcji `--permanent`, aby zmiany były trwałe po restarcie systemu.
- Regularnie przeglądaj i aktualizuj reguły zapory, aby zapewnić bezpieczeństwo systemu.