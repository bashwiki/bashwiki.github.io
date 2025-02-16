# [Linux] Bash dmesg użycie: Wyświetlanie komunikatów jądra

## Przegląd
Polecenie `dmesg` służy do wyświetlania komunikatów jądra systemu operacyjnego. Umożliwia ono przeglądanie logów systemowych, które są generowane podczas rozruchu systemu oraz w trakcie jego działania. Dzięki temu można diagnozować problemy z urządzeniami oraz monitorować ich działanie.

## Użycie
Podstawowa składnia polecenia `dmesg` jest następująca:

```bash
dmesg [opcje] [argumenty]
```

## Częste opcje
- `-C` – Czyści bufor komunikatów jądra.
- `-c` – Wyświetla komunikaty i następnie je czyści.
- `-n <poziom>` – Ustawia poziom logowania komunikatów.
- `-T` – Wyświetla czas w formacie czytelnym dla człowieka.
- `-H` – Wyświetla komunikaty w formacie HTML.

## Częste przykłady
1. Wyświetlenie wszystkich komunikatów jądra:
   ```bash
   dmesg
   ```

2. Wyświetlenie komunikatów z czasem w formacie czytelnym:
   ```bash
   dmesg -T
   ```

3. Czyszczenie bufora komunikatów jądra:
   ```bash
   dmesg -C
   ```

4. Wyświetlenie komunikatów tylko o poziomie krytycznym:
   ```bash
   dmesg -n 1
   ```

5. Wyświetlenie komunikatów w formacie HTML:
   ```bash
   dmesg -H
   ```

## Wskazówki
- Regularnie przeglądaj komunikaty jądra, aby monitorować stan systemu i urządzeń.
- Używaj opcji `-T`, aby łatwiej interpretować czasy w logach.
- Pamiętaj, że niektóre komunikaty mogą być usunięte po wyczyszczeniu bufora, więc używaj opcji czyszczenia ostrożnie.
- Możesz przekierować wyjście `dmesg` do pliku, aby zachować logi do późniejszej analizy:
  ```bash
  dmesg > logi_jadra.txt
  ```