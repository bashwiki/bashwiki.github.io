# [Linux] Bash docker użycie: Zarządzanie kontenerami aplikacji

## Overview
Polecenie `docker` jest narzędziem do zarządzania kontenerami aplikacji. Umożliwia tworzenie, uruchamianie i zarządzanie kontenerami, które są lekkimi, przenośnymi środowiskami do uruchamiania aplikacji. Docker pozwala na łatwe wdrażanie aplikacji w różnych środowiskach bez obaw o problemy z zależnościami.

## Usage
Podstawowa składnia polecenia `docker` wygląda następująco:

```bash
docker [options] [arguments]
```

## Common Options
Oto kilka powszechnie używanych opcji dla polecenia `docker`:

- `run`: Uruchamia nowy kontener.
- `ps`: Wyświetla listę uruchomionych kontenerów.
- `stop`: Zatrzymuje działający kontener.
- `rm`: Usuwa zatrzymany kontener.
- `images`: Wyświetla listę dostępnych obrazów.

## Common Examples
Oto kilka praktycznych przykładów użycia polecenia `docker`:

1. **Uruchomienie nowego kontenera**:
   ```bash
   docker run -d --name my_container nginx
   ```
   Uruchamia nowy kontener z obrazem Nginx w trybie odłączonym.

2. **Wyświetlenie uruchomionych kontenerów**:
   ```bash
   docker ps
   ```
   Pokazuje listę wszystkich aktualnie działających kontenerów.

3. **Zatrzymanie kontenera**:
   ```bash
   docker stop my_container
   ```
   Zatrzymuje kontener o nazwie `my_container`.

4. **Usunięcie kontenera**:
   ```bash
   docker rm my_container
   ```
   Usuwa zatrzymany kontener o nazwie `my_container`.

5. **Wyświetlenie dostępnych obrazów**:
   ```bash
   docker images
   ```
   Pokazuje listę wszystkich dostępnych obrazów na lokalnej maszynie.

## Tips
- Zawsze używaj opcji `-d` przy uruchamianiu kontenerów, jeśli chcesz, aby działały w tle.
- Regularnie sprawdzaj dostępne obrazy i kontenery, aby utrzymać porządek w swoim środowisku Docker.
- Używaj etykiet (tags) dla obrazów, aby łatwiej zarządzać wersjami aplikacji.