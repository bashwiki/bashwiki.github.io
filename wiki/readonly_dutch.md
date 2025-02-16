# [Linux] Bash readonly gebruik: Beperk variabelen tot alleen-lezen

## Overzicht
De `readonly` opdracht in Bash wordt gebruikt om variabelen als alleen-lezen te markeren. Dit betekent dat, eenmaal ingesteld, de waarde van de variabele niet meer kan worden gewijzigd. Dit is handig om ervoor te zorgen dat belangrijke waarden niet per ongeluk worden overschreven.

## Gebruik
De basis syntaxis van de `readonly` opdracht is als volgt:

```bash
readonly [opties] [argumenten]
```

## Veelvoorkomende Opties
- `-p`: Toont een lijst van alle alleen-lezen variabelen in de huidige shell.

## Veelvoorkomende Voorbeelden

### Voorbeeld 1: Een variabele instellen als alleen-lezen
```bash
my_var="Dit is een test"
readonly my_var
```
In dit voorbeeld wordt `my_var` ingesteld als alleen-lezen. Pogingen om het later te wijzigen zullen een foutmelding geven.

### Voorbeeld 2: Lijst van alleen-lezen variabelen weergeven
```bash
readonly -p
```
Dit commando toont alle variabelen die momenteel als alleen-lezen zijn gemarkeerd in de shell.

### Voorbeeld 3: Proberen een alleen-lezen variabele te wijzigen
```bash
my_var="Nog een test"
readonly my_var
my_var="Wijziging"  # Dit zal een foutmelding geven
```
Hier zal de poging om `my_var` te wijzigen resulteren in een foutmelding omdat de variabele als alleen-lezen is ingesteld.

## Tips
- Gebruik `readonly` voor belangrijke configuratie-instellingen die niet mogen worden gewijzigd tijdens de uitvoering van een script.
- Controleer regelmatig de lijst van alleen-lezen variabelen met `readonly -p` om te begrijpen welke waarden beschermd zijn.
- Wees voorzichtig bij het instellen van variabelen als alleen-lezen, vooral in grotere scripts, om onverwachte fouten te voorkomen.