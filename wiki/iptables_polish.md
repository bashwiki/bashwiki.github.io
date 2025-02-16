# [Linux] Bash iptables Użycie: Zarządzanie regułami zapory sieciowej

## Przegląd
Polecenie `iptables` jest narzędziem do zarządzania regułami zapory sieciowej w systemach Linux. Umożliwia użytkownikom kontrolowanie ruchu sieciowego poprzez definiowanie reguł, które określają, jakie pakiety danych mogą być akceptowane, odrzucane lub przekierowywane.

## Użycie
Podstawowa składnia polecenia `iptables` jest następująca:

```bash
iptables [opcje] [argumenty]
```

## Częste opcje
- `-A` : Dodaje nową regułę do łańcucha.
- `-D` : Usuwa regułę z łańcucha.
- `-L` : Wyświetla wszystkie reguły w łańcuchach.
- `-F` : Czyści wszystkie reguły w łańcuchach.
- `-P` : Ustawia politykę domyślną dla łańcucha.
- `-I` : Wstawia regułę na początku łańcucha.

## Częste przykłady
1. **Wyświetlenie wszystkich reguł:**
   ```bash
   iptables -L
   ```

2. **Dodanie reguły zezwalającej na ruch HTTP:**
   ```bash
   iptables -A INPUT -p tcp --dport 80 -j ACCEPT
   ```

3. **Usunięcie reguły blokującej ruch SSH:**
   ```bash
   iptables -D INPUT -p tcp --dport 22 -j DROP
   ```

4. **Ustawienie domyślnej polityki na odrzucenie ruchu przychodzącego:**
   ```bash
   iptables -P INPUT DROP
   ```

5. **Czyszczenie wszystkich reguł:**
   ```bash
   iptables -F
   ```

## Wskazówki
- Zawsze twórz kopię zapasową swoich reguł przed ich modyfikacją, aby móc przywrócić poprzednie ustawienia w razie potrzeby.
- Testuj nowe reguły w środowisku testowym przed wdrożeniem ich na serwerze produkcyjnym.
- Używaj opcji `-v` dla bardziej szczegółowych informacji o ruchu sieciowym, co może pomóc w diagnozowaniu problemów.