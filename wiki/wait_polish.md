# [Linux] Bash wait użycie: Czekanie na zakończenie procesów

## Overview
Polecenie `wait` w Bash służy do czekania na zakończenie procesów potomnych. Umożliwia synchronizację skryptów, zapewniając, że skrypt nie przejdzie do następnego kroku, dopóki określony proces nie zakończy swojego działania.

## Usage
Podstawowa składnia polecenia `wait` jest następująca:

```bash
wait [options] [arguments]
```

## Common Options
- `-n`: Czeka na zakończenie dowolnego procesu potomnego.
- `PID`: Czeka na zakończenie procesu o podanym identyfikatorze PID.

## Common Examples

### Przykład 1: Czekanie na zakończenie konkretnego procesu
```bash
sleep 5 &
pid=$!
wait $pid
echo "Proces zakończony!"
```
W tym przykładzie uruchamiamy proces `sleep 5` w tle i czekamy na jego zakończenie.

### Przykład 2: Czekanie na wszystkie procesy potomne
```bash
for i in {1..3}; do
    sleep $i &
done
wait
echo "Wszystkie procesy zakończone!"
```
Tutaj uruchamiamy trzy procesy `sleep` w tle i czekamy na zakończenie wszystkich z nich.

### Przykład 3: Użycie opcji -n
```bash
sleep 2 &
sleep 3 &
wait -n
echo "Jedno z procesów zakończone!"
```
W tym przypadku czekamy na zakończenie dowolnego z dwóch uruchomionych procesów.

## Tips
- Używaj `wait` w skryptach, aby zapewnić, że wszystkie procesy zakończą się przed kontynuowaniem dalszych działań.
- Możesz użyć `wait` w połączeniu z innymi poleceniami, aby zbudować bardziej złożone skrypty, które wymagają synchronizacji.
- Pamiętaj, że `wait` działa tylko dla procesów potomnych uruchomionych w tym samym skrypcie lub powłoce.