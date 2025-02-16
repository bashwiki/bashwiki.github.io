# [Linux] Bash groupmod gebruik: Groepsinstellingen wijzigen

## Overzicht
Het `groupmod` commando wordt gebruikt om bestaande groepen in een Linux-systeem te wijzigen. Met dit commando kun je de naam van een groep veranderen of de groeps-ID (GID) aanpassen.

## Gebruik
De basis syntaxis van het `groupmod` commando is als volgt:

```bash
groupmod [opties] [argumenten]
```

## Veelvoorkomende Opties
- `-n, --new-name`: Wijzig de naam van de groep.
- `-g, --gid`: Wijzig de groeps-ID (GID) van de groep.
- `-o, --non-unique`: Sta toe dat een niet-unieke GID wordt gebruikt (meerdere groepen kunnen dezelfde GID hebben).

## Veelvoorkomende Voorbeelden

### Voorbeeld 1: Groepsnaam wijzigen
Om de naam van een groep van `oudenaam` naar `nieuwenaam` te wijzigen, gebruik je het volgende commando:

```bash
groupmod -n nieuwenaam oudenaam
```

### Voorbeeld 2: Groeps-ID wijzigen
Als je de GID van een groep wilt wijzigen naar `1001`, gebruik je:

```bash
groupmod -g 1001 groepsnaam
```

### Voorbeeld 3: Groepsnaam en GID tegelijk wijzigen
Je kunt ook zowel de naam als de GID van een groep tegelijk wijzigen:

```bash
groupmod -n nieuwenaam -g 1001 oudenaam
```

## Tips
- Zorg ervoor dat je voldoende rechten hebt (meestal root) om wijzigingen aan groepen aan te brengen.
- Controleer altijd de huidige groepsinstellingen met het `getent group` commando voordat je wijzigingen aanbrengt.
- Wees voorzichtig met het wijzigen van GID's, omdat dit invloed kan hebben op de bestandspermissies en toegang voor gebruikers die aan die groep zijn toegewezen.