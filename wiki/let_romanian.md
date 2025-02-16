# [Linux] Bash let utilizare: Efectuarea de calcule aritmetice

## Overview
Comanda `let` în Bash este utilizată pentru a efectua calcule aritmetice simple. Aceasta permite evaluarea expresiilor aritmetice și atribuirea rezultatelor variabilelor.

## Usage
Sintaxa de bază a comenzii `let` este următoarea:

```bash
let [opțiuni] [argumente]
```

## Common Options
- `-n`: Verifică dacă expresia este validă, dar nu o evaluează.
- `-e`: Evaluează expresia și returnează un cod de ieșire care indică succesul (0) sau eșecul (1).

## Common Examples
1. **Adunarea a două numere:**
   ```bash
   let suma=5+10
   echo $suma  # Output: 15
   ```

2. **Scăderea:**
   ```bash
   let diferenta=20-5
   echo $diferenta  # Output: 15
   ```

3. **Înmulțirea:**
   ```bash
   let produs=4*3
   echo $produs  # Output: 12
   ```

4. **Împărțirea:**
   ```bash
   let cat=20/4
   echo $cat  # Output: 5
   ```

5. **Combinarea operațiunilor:**
   ```bash
   let rezultat=10+5*2-3
   echo $rezultat  # Output: 17
   ```

## Tips
- Asigurați-vă că variabilele sunt definite înainte de a le utiliza în calcule.
- Utilizați paranteze pentru a controla ordinea operațiunilor în expresiile complexe.
- `let` este o opțiune bună pentru calcule simple, dar pentru expresii mai complexe, luați în considerare utilizarea comenzii `expr` sau a aritmeticii extinse cu `(( ... ))`.