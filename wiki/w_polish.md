# [Linux] Bash w w: Wyświetlanie informacji o użytkownikach

## Overview
Polecenie `w` w systemie Linux służy do wyświetlania informacji o aktualnie zalogowanych użytkownikach oraz ich aktywności. Dzięki temu możesz szybko sprawdzić, kto jest zalogowany i co aktualnie robi.

## Usage
Podstawowa składnia polecenia `w` jest następująca:

```
w [opcje] [argumenty]
```

## Common Options
Oto kilka powszechnie używanych opcji polecenia `w`:

- `-h`: Ukrywa nagłówki w wyjściu.
- `-s`: Wyświetla skróconą wersję informacji.
- `-f`: Wyświetla pełne informacje o użytkownikach, w tym ich terminale.

## Common Examples

1. **Wyświetlenie podstawowych informacji o użytkownikach:**
   ```bash
   w
   ```

2. **Wyświetlenie informacji bez nagłówków:**
   ```bash
   w -h
   ```

3. **Wyświetlenie skróconej wersji informacji:**
   ```bash
   w -s
   ```

4. **Wyświetlenie pełnych informacji o użytkownikach:**
   ```bash
   w -f
   ```

## Tips
- Używaj opcji `-h`, jeśli chcesz szybko uzyskać informacje bez dodatkowych nagłówków.
- Regularnie sprawdzaj aktywność użytkowników na serwerze, aby monitorować obciążenie systemu.
- Możesz połączyć polecenie `w` z innymi narzędziami, takimi jak `grep`, aby filtrować wyniki według określonych kryteriów.