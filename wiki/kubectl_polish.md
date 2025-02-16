# [Linux] Bash kubectl Użycie: zarządzanie klastrami Kubernetes

## Overview
`kubectl` to narzędzie wiersza poleceń, które pozwala na interakcję z klastrami Kubernetes. Umożliwia użytkownikom zarządzanie aplikacjami kontenerowymi, monitorowanie ich stanu oraz wykonywanie różnych operacji na zasobach Kubernetes.

## Usage
Podstawowa składnia polecenia `kubectl` wygląda następująco:

```bash
kubectl [opcje] [argumenty]
```

## Common Options
- `get`: Pobiera informacje o zasobach.
- `apply`: Zastosowuje zmiany z pliku konfiguracyjnego.
- `delete`: Usuwa zasoby.
- `describe`: Wyświetla szczegółowe informacje o zasobie.
- `logs`: Wyświetla logi kontenera.

## Common Examples
1. **Pobieranie listy podów:**
   ```bash
   kubectl get pods
   ```

2. **Zastosowanie zmian z pliku YAML:**
   ```bash
   kubectl apply -f deployment.yaml
   ```

3. **Usunięcie poda:**
   ```bash
   kubectl delete pod nazwa-poda
   ```

4. **Wyświetlenie szczegółów poda:**
   ```bash
   kubectl describe pod nazwa-poda
   ```

5. **Wyświetlenie logów kontenera:**
   ```bash
   kubectl logs nazwa-poda
   ```

## Tips
- Używaj opcji `-n` do określenia przestrzeni nazw, jeśli pracujesz w wielu przestrzeniach.
- Sprawdzaj status zasobów za pomocą `kubectl get all`, aby uzyskać pełny przegląd.
- Zawsze testuj zmiany w środowisku deweloperskim przed wdrożeniem ich w produkcji.