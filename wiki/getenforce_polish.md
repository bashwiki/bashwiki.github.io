# [Linux] Bash getenforce użycie: Sprawdza status SELinux

## Overview
Polecenie `getenforce` służy do sprawdzania aktualnego statusu SELinux (Security-Enhanced Linux) na systemie operacyjnym. Wyświetla, czy SELinux jest włączony, wyłączony, czy działa w trybie wymuszania.

## Usage
Podstawowa składnia polecenia `getenforce` jest następująca:

```bash
getenforce [opcje]
```

## Common Options
`getenforce` nie ma wielu opcji, ale oto kilka, które mogą być użyteczne:

- `-h`, `--help`: Wyświetla pomoc dotyczącą polecenia.
- `-V`, `--version`: Wyświetla wersję polecenia.

## Common Examples

1. **Sprawdzenie statusu SELinux:**
   Aby sprawdzić, w jakim stanie znajduje się SELinux, wystarczy wpisać:
   ```bash
   getenforce
   ```

2. **Wyświetlenie pomocy:**
   Aby uzyskać więcej informacji na temat polecenia, użyj:
   ```bash
   getenforce --help
   ```

3. **Sprawdzenie wersji:**
   Aby sprawdzić wersję polecenia, wpisz:
   ```bash
   getenforce --version
   ```

## Tips
- Regularnie sprawdzaj status SELinux, aby upewnić się, że system jest odpowiednio zabezpieczony.
- Jeśli SELinux jest wyłączony, rozważ jego włączenie dla lepszej ochrony systemu.
- Używaj `getenforce` w skryptach, aby automatycznie dostosowywać zachowanie aplikacji w zależności od statusu SELinux.