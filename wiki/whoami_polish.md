# [Linux] Bash whoami użycie: Zwraca nazwę aktualnego użytkownika

## Overview
Polecenie `whoami` w systemie Linux służy do wyświetlania nazwy aktualnie zalogowanego użytkownika. Jest to przydatne narzędzie, które pozwala szybko sprawdzić, na którym koncie użytkownika pracujemy w danym momencie.

## Usage
Podstawowa składnia polecenia `whoami` jest następująca:

```bash
whoami [opcje]
```

## Common Options
Polecenie `whoami` nie ma wielu opcji, ale oto kilka, które mogą być przydatne:

- **--help**: Wyświetla pomoc dotyczącą polecenia.
- **--version**: Wyświetla wersję polecenia.

## Common Examples
Oto kilka praktycznych przykładów użycia polecenia `whoami`:

1. **Wyświetlenie nazwy aktualnego użytkownika**:
   ```bash
   whoami
   ```

2. **Wyświetlenie pomocy**:
   ```bash
   whoami --help
   ```

3. **Sprawdzenie wersji polecenia**:
   ```bash
   whoami --version
   ```

## Tips
- Używaj `whoami` w skryptach, aby dynamicznie uzyskiwać nazwę użytkownika, co może być przydatne w różnych operacjach.
- Możesz łączyć `whoami` z innymi poleceniami, aby uzyskać bardziej złożone informacje, na przykład:
  ```bash
  echo "Aktualny użytkownik to: $(whoami)"
  ```
- Pamiętaj, że `whoami` zwraca tylko nazwę użytkownika, a nie inne informacje, takie jak ID użytkownika czy grupa.