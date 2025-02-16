# [Linux] Bash xmlstarlet gebruik: XML-bestanden bewerken en analyseren

## Overzicht
Het `xmlstarlet` commando is een krachtige tool voor het verwerken van XML-bestanden. Het stelt gebruikers in staat om XML-data te transformeren, te valideren, en te analyseren met behulp van een eenvoudige commandoregelinterface.

## Gebruik
De basis syntaxis van het `xmlstarlet` commando is als volgt:

```bash
xmlstarlet [opties] [argumenten]
```

## Veelvoorkomende Opties
- `ed`: Bewerk een XML-document.
- `sel`: Selecteer gegevens uit een XML-document.
- `val`: Valideer een XML-document tegen een DTD of XSD.
- `tr`: Transformeer een XML-document met behulp van XSLT.
- `fo`: Formatteer een XML-document voor betere leesbaarheid.

## Veelvoorkomende Voorbeelden

### XML Gegevens Selecteren
Om specifieke elementen uit een XML-bestand te selecteren, gebruik je de `sel` optie:

```bash
xmlstarlet sel -t -m "//boek" -v "titel" -n boeken.xml
```

### XML Gegevens Bewerken
Om een element in een XML-bestand te bewerken, gebruik je de `ed` optie:

```bash
xmlstarlet ed -u "//boek/titel" -v "Nieuwe Titel" boeken.xml
```

### XML Valideren
Om een XML-bestand te valideren tegen een XSD-schema, gebruik je de `val` optie:

```bash
xmlstarlet val -e -s schema.xsd boeken.xml
```

### XML Transformeren
Om een XML-bestand te transformeren met een XSLT-bestand, gebruik je de `tr` optie:

```bash
xmlstarlet tr transform.xsl input.xml > output.xml
```

## Tips
- Zorg ervoor dat je altijd een back-up maakt van je originele XML-bestanden voordat je bewerkingen uitvoert.
- Gebruik de `--help` optie om meer informatie te krijgen over de beschikbare opties en hun gebruik.
- Experimenteer met verschillende XPath-expressies om je gegevens effectief te selecteren en te manipuleren.