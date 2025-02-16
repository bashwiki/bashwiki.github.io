# [Linux] Bash umask gebruik: Beheer van standaard bestandspermissies

## Overzicht
De `umask`-opdracht in Bash wordt gebruikt om de standaard bestandspermissies te beheren voor nieuwe bestanden en mappen die worden aangemaakt. Het bepaalt welke permissies niet mogen worden toegewezen aan nieuwe bestanden en directories.

## Gebruik
De basis syntaxis van de `umask`-opdracht is als volgt:

```bash
umask [opties] [argumenten]
```

## Veelvoorkomende opties
- `-S`: Toont de umask in symbolische vorm.
- `-p`: Toont de huidige umask-waarde in een uitvoerbare vorm.

## Veelvoorkomende voorbeelden

1. **Bekijk de huidige umask-waarde:**
   ```bash
   umask
   ```

2. **Stel een nieuwe umask-waarde in:**
   ```bash
   umask 027
   ```

3. **Toon de umask in symbolische vorm:**
   ```bash
   umask -S
   ```

4. **Stel umask in en controleer de waarde:**
   ```bash
   umask 002
   umask
   ```

## Tips
- Zorg ervoor dat je de umask-waarde begrijpt voordat je deze wijzigt, omdat dit invloed heeft op de toegankelijkheid van bestanden voor andere gebruikers.
- Het is handig om de umask-waarde in je shell-configuratiebestand (zoals `.bashrc` of `.bash_profile`) in te stellen, zodat deze automatisch wordt toegepast bij het openen van een nieuwe terminalsessie.
- Test de umask-instellingen door nieuwe bestanden en mappen te maken om te zien hoe de permissies worden toegepast.