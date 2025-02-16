# [Linux] Bash shopt użycie: Zarządzanie opcjami powłoki

## Overview
Polecenie `shopt` w Bashu służy do zarządzania opcjami powłoki, które mogą wpływać na zachowanie powłoki i jej funkcji. Umożliwia włączanie i wyłączanie różnych opcji, co pozwala na dostosowanie środowiska pracy do indywidualnych potrzeb użytkownika.

## Usage
Podstawowa składnia polecenia `shopt` jest następująca:

```bash
shopt [opcje] [argumenty]
```

## Common Options
Oto kilka powszechnie używanych opcji dla `shopt`:

- `-s` : Włącza określoną opcję.
- `-u` : Wyłącza określoną opcję.
- `-p` : Wyświetla aktualny stan opcji.

## Common Examples

### Włączenie opcji `cdspell`
Opcja `cdspell` automatycznie poprawia literówki w poleceniach `cd`.

```bash
shopt -s cdspell
```

### Wyłączenie opcji `cdspell`
Aby wyłączyć tę opcję, użyj:

```bash
shopt -u cdspell
```

### Wyświetlenie wszystkich opcji
Aby zobaczyć wszystkie dostępne opcje i ich aktualny stan, użyj:

```bash
shopt
```

### Włączenie opcji `nullglob`
Opcja `nullglob` sprawia, że wzorce globbing, które nie pasują do żadnych plików, zwracają pustą listę zamiast samego wzorca.

```bash
shopt -s nullglob
```

## Tips
- Regularnie sprawdzaj dostępne opcje za pomocą `shopt` bez argumentów, aby dostosować środowisko do swoich potrzeb.
- Używaj opcji `-p`, aby zapisać aktualne ustawienia, co może być przydatne przy tworzeniu skryptów.
- Pamiętaj, że zmiany wprowadzone przez `shopt` są lokalne dla bieżącej sesji powłoki, chyba że dodasz je do swojego pliku konfiguracyjnego, takiego jak `.bashrc`.