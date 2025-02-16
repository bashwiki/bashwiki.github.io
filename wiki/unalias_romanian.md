# [Linux] Bash unalias utilizare: Elimină aliasurile din sesiunea curentă

## Overview
Comanda `unalias` este utilizată în Bash pentru a elimina aliasurile definite anterior. Aceasta permite utilizatorilor să revină la comportamentul standard al comenzilor, fără a fi influențați de aliasurile personalizate.

## Usage
Sintaxa de bază a comenzii `unalias` este următoarea:

```bash
unalias [options] [arguments]
```

## Common Options
- `-a`: Elimină toate aliasurile definite.
- `-p`: Afișează toate aliasurile curente fără a le elimina.

## Common Examples

1. **Eliminarea unui alias specific**:
   Dacă ai definit un alias pentru comanda `ll`, îl poți elimina astfel:
   ```bash
   unalias ll
   ```

2. **Eliminarea tuturor aliasurilor**:
   Pentru a elimina toate aliasurile din sesiunea curentă, folosește opțiunea `-a`:
   ```bash
   unalias -a
   ```

3. **Afișarea aliasurilor curente**:
   Dacă vrei să vezi toate aliasurile definite înainte de a le elimina, poți folosi:
   ```bash
   unalias -p
   ```

## Tips
- Asigură-te că știi ce aliasuri vrei să elimini, deoarece `unalias` nu poate fi folosit pentru a recupera aliasurile șterse.
- Poți adăuga comanda `unalias` în fișierul tău de configurare `.bashrc` pentru a elimina automat anumite aliasuri la fiecare sesiune de terminal.
- Verifică aliasurile curente folosind comanda `alias` înainte de a decide să le elimini.