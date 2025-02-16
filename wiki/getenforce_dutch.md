# [Linux] Bash getenforce gebruik: Controleer de huidige SELinux-status

## Overzicht
Het `getenforce` commando wordt gebruikt om de huidige status van SELinux (Security-Enhanced Linux) te controleren. Het geeft aan of SELinux is ingeschakeld en welke modus het momenteel draait: Enforcing, Permissive of Disabled.

## Gebruik
De basis syntaxis van het `getenforce` commando is als volgt:

```bash
getenforce [options]
```

## Veelvoorkomende opties
`getenforce` heeft geen uitgebreide opties, maar de belangrijkste zijn:

- `-h`, `--help`: Toont een helpbericht met informatie over het gebruik van het commando.

## Veelvoorkomende Voorbeelden

### Voorbeeld 1: Controleer de SELinux-status
Om de huidige status van SELinux te controleren, gebruik je eenvoudig:

```bash
getenforce
```

Dit zal een van de volgende waarden teruggeven:
- Enforcing
- Permissive
- Disabled

### Voorbeeld 2: Gebruik in een script
Je kunt `getenforce` gebruiken in een script om beslissingen te nemen op basis van de SELinux-status:

```bash
if [ "$(getenforce)" == "Enforcing" ]; then
    echo "SELinux is ingeschakeld."
else
    echo "SELinux is niet ingeschakeld."
fi
```

## Tips
- Gebruik `getenforce` regelmatig om de status van SELinux te controleren, vooral bij het oplossen van beveiligingsproblemen.
- Combineer `getenforce` met andere commando's zoals `setenforce` om de SELinux-modus dynamisch te wijzigen indien nodig.
- Houd er rekening mee dat wijzigingen in SELinux-instellingen vaak een herstart van diensten of systemen vereisen om effect te hebben.