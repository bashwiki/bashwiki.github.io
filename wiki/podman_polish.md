# [Linux] Bash podman użycie: Zarządzanie kontenerami bez demona

## Overview
Podman to narzędzie do zarządzania kontenerami, które umożliwia tworzenie, uruchamianie i zarządzanie kontenerami oraz obrazami kontenerów. Jest to alternatywa dla Dockera, ale działa bez potrzeby uruchamiania demona, co zwiększa bezpieczeństwo i elastyczność.

## Usage
Podstawowa składnia polecenia podman wygląda następująco:

```bash
podman [opcje] [argumenty]
```

## Common Options
Oto kilka powszechnie używanych opcji w poleceniu podman:

- `run`: Uruchamia nowy kontener.
- `ps`: Wyświetla listę uruchomionych kontenerów.
- `images`: Wyświetla dostępne obrazy kontenerów.
- `pull`: Pobiera obraz kontenera z rejestru.
- `rm`: Usuwa zatrzymany kontener.

## Common Examples
Oto kilka praktycznych przykładów użycia polecenia podman:

1. **Uruchomienie nowego kontenera:**
   ```bash
   podman run -d --name my_container nginx
   ```

2. **Wyświetlenie uruchomionych kontenerów:**
   ```bash
   podman ps
   ```

3. **Pobranie obrazu kontenera:**
   ```bash
   podman pull alpine
   ```

4. **Usunięcie zatrzymanego kontenera:**
   ```bash
   podman rm my_container
   ```

5. **Wyświetlenie dostępnych obrazów:**
   ```bash
   podman images
   ```

## Tips
- Używaj opcji `-d` (detached) podczas uruchamiania kontenera, aby działał w tle.
- Regularnie sprawdzaj dostępne obrazy i kontenery, aby utrzymać porządek w systemie.
- Zawsze używaj opcji `--name`, aby nadać kontenerom unikalne nazwy, co ułatwia ich zarządzanie.