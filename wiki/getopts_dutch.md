# [Linux] Bash getopts gebruik: Verwerken van opties in shell-scripts

## Overzicht
De `getopts`-opdracht in Bash wordt gebruikt om opties en argumenten te verwerken in shell-scripts. Het maakt het eenvoudig om commandoregelopties te parseren, wat handig is voor het maken van flexibele en gebruiksvriendelijke scripts.

## Gebruik
De basisstructuur van de `getopts`-opdracht is als volgt:

```bash
getopts [options] [arguments]
```

## Veelvoorkomende Opties
Hier zijn enkele veelvoorkomende opties die je kunt gebruiken met `getopts`:

- `-a`: Specificeert dat de opties als een array moeten worden behandeld.
- `-o`: Definieert de opties die je wilt verwerken.
- `-l`: Biedt ondersteuning voor lange opties (bijvoorbeeld `--help`).

## Veelvoorkomende Voorbeelden

### Voorbeeld 1: Basisopties verwerken
Dit voorbeeld laat zien hoe je eenvoudige opties kunt verwerken met `getopts`.

```bash
#!/bin/bash

while getopts "ab:c:" opt; do
  case $opt in
    a)
      echo "Optie A geselecteerd"
      ;;
    b)
      echo "Optie B met waarde: $OPTARG"
      ;;
    c)
      echo "Optie C met waarde: $OPTARG"
      ;;
    \?)
      echo "Ongeldige optie: -$OPTARG" >&2
      ;;
  esac
done
```

### Voorbeeld 2: Opties met argumenten
In dit voorbeeld worden opties met bijbehorende argumenten verwerkt.

```bash
#!/bin/bash

while getopts "u:p:" opt; do
  case $opt in
    u)
      echo "Gebruikersnaam: $OPTARG"
      ;;
    p)
      echo "Wachtwoord: $OPTARG"
      ;;
    \?)
      echo "Ongeldige optie: -$OPTARG" >&2
      ;;
  esac
done
```

### Voorbeeld 3: Meerdere opties tegelijk
Hier is een voorbeeld waarin meerdere opties tegelijk worden verwerkt.

```bash
#!/bin/bash

while getopts "xyz" opt; do
  case $opt in
    x)
      echo "Optie X geselecteerd"
      ;;
    y)
      echo "Optie Y geselecteerd"
      ;;
    z)
      echo "Optie Z geselecteerd"
      ;;
    \?)
      echo "Ongeldige optie: -$OPTARG" >&2
      ;;
  esac
done
```

## Tips
- Gebruik duidelijke en betekenisvolle optieletters om de bruikbaarheid van je script te verbeteren.
- Vergeet niet om een helpoptie (`-h` of `--help`) toe te voegen voor gebruikers die meer informatie willen.
- Test je script met verschillende combinaties van opties om ervoor te zorgen dat het correct werkt.