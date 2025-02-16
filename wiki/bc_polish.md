# [Linux] Bash bc użycie: Kalkulator wiersza poleceń

## Overview
Polecenie `bc` to kalkulator wiersza poleceń, który umożliwia wykonywanie obliczeń arytmetycznych oraz operacji na liczbach zmiennoprzecinkowych. Jest to narzędzie przydatne dla programistów i administratorów systemów, którzy potrzebują szybko przeprowadzić obliczenia w skryptach lub w terminalu.

## Usage
Podstawowa składnia polecenia `bc` jest następująca:

```bash
bc [opcje] [argumenty]
```

## Common Options
- `-l`: Włącza bibliotekę matematyczną, co umożliwia korzystanie z funkcji matematycznych, takich jak sinus, cosinus, logarytm itp.
- `-q`: Uruchamia `bc` w trybie cichym, co oznacza, że nie wyświetla powitania.
- `-h`: Wyświetla pomoc i dostępne opcje.

## Common Examples
### Proste obliczenia
Aby wykonać proste obliczenia, można użyć polecenia `echo` w połączeniu z `bc`:

```bash
echo "5 + 3" | bc
```

### Obliczenia z użyciem zmiennych
Możesz również używać zmiennych w obliczeniach:

```bash
echo "a=5; b=3; a * b" | bc
```

### Użycie biblioteki matematycznej
Aby korzystać z funkcji matematycznych, użyj opcji `-l`:

```bash
echo "scale=2; s=sin(1); s" | bc -l
```

### Obliczenia z precyzją
Możesz ustawić precyzję obliczeń za pomocą `scale`:

```bash
echo "scale=4; 10 / 3" | bc
```

## Tips
- Używaj `scale`, aby kontrolować liczbę miejsc po przecinku w wynikach.
- Warto zapoznać się z funkcjami dostępnymi w bibliotece matematycznej, aby rozszerzyć możliwości obliczeniowe.
- Możesz zapisać skrypty `bc` w plikach tekstowych i uruchamiać je, co ułatwia złożone obliczenia.