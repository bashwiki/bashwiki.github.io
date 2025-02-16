# [Linux] Bash uptime użycie: Wyświetla czas działania systemu

## Overview
Polecenie `uptime` w systemie Linux służy do wyświetlania czasu działania systemu, a także informacji o obciążeniu procesora oraz liczbie użytkowników aktualnie zalogowanych do systemu. Dzięki temu można szybko ocenić, jak długo system działa bez przerwy oraz jakie jest jego obciążenie.

## Usage
Podstawowa składnia polecenia `uptime` jest następująca:

```bash
uptime [opcje]
```

## Common Options
Oto kilka powszechnie używanych opcji dla polecenia `uptime`:

- `-p` : Wyświetla czas działania systemu w bardziej czytelnej formie.
- `-s` : Wyświetla czas, w którym system został uruchomiony.

## Common Examples

### Przykład 1: Podstawowe użycie
Aby wyświetlić czas działania systemu oraz obciążenie procesora, wystarczy wpisać:

```bash
uptime
```

### Przykład 2: Czytelna forma czasu działania
Aby uzyskać czas działania systemu w bardziej przystępnej formie, użyj opcji `-p`:

```bash
uptime -p
```

### Przykład 3: Czas uruchomienia systemu
Aby zobaczyć dokładny czas, w którym system został uruchomiony, można użyć opcji `-s`:

```bash
uptime -s
```

## Tips
- Regularnie sprawdzaj czas działania systemu, aby monitorować stabilność i dostępność usług.
- Używaj opcji `-p`, aby uzyskać bardziej zrozumiałe informacje o czasie działania, zwłaszcza w środowiskach, gdzie niektórzy użytkownicy mogą nie być zaznajomieni z formatem wyjściowym.
- W połączeniu z innymi narzędziami, takimi jak `top` lub `htop`, możesz uzyskać pełniejszy obraz obciążenia systemu i jego wydajności.