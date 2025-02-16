# [Linux] Bash pushd gebruik: Navigeren tussen directories

## Overzicht
De `pushd` opdracht in Bash wordt gebruikt om de huidige directory op de stack te plaatsen en vervolgens naar een andere directory te navigeren. Dit maakt het eenvoudig om tussen verschillende directories te schakelen zonder de oorspronkelijke locatie te verliezen.

## Gebruik
De basis syntaxis van de `pushd` opdracht is als volgt:

```bash
pushd [opties] [argumenten]
```

## Veelvoorkomende opties
- `+n`: Navigeert naar de n-de directory op de stack.
- `-n`: Navigeert naar de n-de directory op de stack, maar zonder deze toe te voegen aan de stack.

## Veelvoorkomende voorbeelden

1. **Navigeren naar een nieuwe directory en de huidige directory opslaan:**
   ```bash
   pushd /pad/naar/directory
   ```

2. **Teruggaan naar de vorige directory:**
   ```bash
   popd
   ```

3. **Navigeren naar de tweede directory op de stack:**
   ```bash
   pushd +1
   ```

4. **Navigeren naar de derde directory op de stack zonder deze toe te voegen:**
   ```bash
   pushd -2
   ```

## Tips
- Gebruik `dirs` om de huidige stack van directories te bekijken.
- Combineer `pushd` met `popd` om efficiënt te navigeren zonder je huidige locatie te verliezen.
- Wees voorzichtig met het gebruik van `pushd` in scripts, omdat het de stack kan beïnvloeden en verwarring kan veroorzaken als je niet goed oplet.