# [Linux] Bash netstat użycie: Wyświetlanie statystyk sieciowych

## Overview
Polecenie `netstat` jest używane do wyświetlania informacji o połączeniach sieciowych, tabelach routingu, interfejsach sieciowych oraz statystykach protokołów. Umożliwia monitorowanie aktywności sieciowej oraz diagnozowanie problemów z połączeniami.

## Usage
Podstawowa składnia polecenia `netstat` jest następująca:

```bash
netstat [opcje] [argumenty]
```

## Common Options
- `-a`: Wyświetla wszystkie połączenia i porty nasłuchujące.
- `-t`: Pokazuje tylko połączenia TCP.
- `-u`: Pokazuje tylko połączenia UDP.
- `-n`: Wyświetla adresy i numery portów w formacie numerycznym.
- `-l`: Wyświetla tylko porty nasłuchujące.
- `-p`: Pokazuje identyfikatory procesów (PID) oraz nazwy programów korzystających z portów.

## Common Examples
1. Wyświetlenie wszystkich aktywnych połączeń:
   ```bash
   netstat -a
   ```

2. Wyświetlenie tylko połączeń TCP:
   ```bash
   netstat -t
   ```

3. Wyświetlenie portów nasłuchujących:
   ```bash
   netstat -l
   ```

4. Wyświetlenie adresów i portów w formacie numerycznym:
   ```bash
   netstat -n
   ```

5. Wyświetlenie połączeń z identyfikatorami procesów:
   ```bash
   netstat -p
   ```

## Tips
- Używaj opcji `-n`, aby przyspieszyć wyświetlanie wyników, ponieważ unika to rozwiązywania nazw hostów.
- Regularnie monitoruj połączenia, aby wykrywać nieautoryzowane lub podejrzane aktywności w sieci.
- Połączenie `netstat -tuln` jest przydatne do szybkiego sprawdzenia, które porty są nasłuchujące na serwerze.