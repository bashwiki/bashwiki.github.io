# [Linux] Bash id użycie: wyświetlanie informacji o użytkowniku

## Overview
Polecenie `id` w systemie Linux służy do wyświetlania informacji o bieżącym użytkowniku lub o użytkowniku wskazanym jako argument. Pokazuje identyfikator użytkownika (UID), identyfikator grupy (GID) oraz przynależność do grup.

## Usage
Podstawowa składnia polecenia `id` jest następująca:

```bash
id [opcje] [argumenty]
```

## Common Options
- `-u`: Wyświetla tylko UID użytkownika.
- `-g`: Wyświetla tylko GID grupy.
- `-G`: Wyświetla wszystkie GID, do których należy użytkownik.
- `-n`: Wyświetla nazwy zamiast identyfikatorów.
- `-r`: Wyświetla rzeczywiste identyfikatory użytkowników i grup.

## Common Examples
1. Wyświetlenie informacji o bieżącym użytkowniku:
   ```bash
   id
   ```

2. Wyświetlenie tylko UID bieżącego użytkownika:
   ```bash
   id -u
   ```

3. Wyświetlenie tylko GID bieżącej grupy:
   ```bash
   id -g
   ```

4. Wyświetlenie wszystkich GID, do których należy użytkownik:
   ```bash
   id -G
   ```

5. Wyświetlenie informacji o innym użytkowniku (np. `username`):
   ```bash
   id username
   ```

6. Wyświetlenie nazw grup zamiast identyfikatorów:
   ```bash
   id -nG
   ```

## Tips
- Używaj opcji `-n`, aby uzyskać bardziej czytelne wyniki, gdy interesują Cię nazwy grup.
- Możesz używać polecenia `id` w skryptach, aby sprawdzić uprawnienia użytkowników przed wykonaniem operacji wymagających określonych uprawnień.
- Pamiętaj, że `id` może być użyteczne w diagnostyce problemów z uprawnieniami w systemie.