# [Linux] Bash lokalny <Użycie>: Zarządzanie zmiennymi lokalnymi w funkcjach

## Przegląd
Polecenie `local` w Bashu służy do definiowania zmiennych lokalnych wewnątrz funkcji. Zmienne te są widoczne tylko w obrębie funkcji, co pozwala uniknąć konfliktów z innymi zmiennymi o tej samej nazwie w szerszym zakresie.

## Użycie
Podstawowa składnia polecenia `local` wygląda następująco:

```bash
local [opcje] [argumenty]
```

## Częste opcje
- `name=value` - definiuje zmienną lokalną o nazwie `name` i przypisuje jej wartość `value`.
- `-n` - tworzy zmienną lokalną, która jest referencją do innej zmiennej.

## Przykłady
Oto kilka praktycznych przykładów użycia polecenia `local`:

### Przykład 1: Definiowanie zmiennej lokalnej
```bash
my_function() {
    local my_var="Hello, World!"
    echo $my_var
}

my_function  # Wydrukuje: Hello, World!
echo $my_var  # Nie wydrukuje nic, ponieważ my_var jest lokalne
```

### Przykład 2: Użycie zmiennej lokalnej w obliczeniach
```bash
calculate() {
    local num1=5
    local num2=10
    local sum=$((num1 + num2))
    echo "Suma: $sum"
}

calculate  # Wydrukuje: Suma: 15
```

### Przykład 3: Użycie opcji -n
```bash
set_global() {
    local -n ref_var=$1
    ref_var="Nowa wartość"
}

global_var=""
set_global global_var
echo $global_var  # Wydrukuje: Nowa wartość
```

## Wskazówki
- Używaj `local` w funkcjach, aby ograniczyć zasięg zmiennych i uniknąć niezamierzonych konfliktów.
- Zawsze definiuj zmienne lokalne w górnej części funkcji, aby zwiększyć czytelność kodu.
- Pamiętaj, że zmienne lokalne są usuwane po zakończeniu funkcji, co pomaga w zarządzaniu pamięcią.