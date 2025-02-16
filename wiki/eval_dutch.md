# [Linux] Bash eval gebruik: Voer een commando uit dat is opgeslagen in een variabele

## Overzicht
De `eval`-opdracht in Bash voert een commando uit dat is opgeslagen in een variabele of dat als argument wordt doorgegeven. Het verwerkt de argumenten en voert de resulterende opdracht uit, wat handig kan zijn voor dynamische commando's.

## Gebruik
De basis syntaxis van de `eval`-opdracht is als volgt:

```bash
eval [opties] [argumenten]
```

## Veelvoorkomende opties
De `eval`-opdracht heeft geen specifieke opties, maar het is belangrijk om te weten dat het de argumenten als een enkele opdracht interpreteert.

## Veelvoorkomende voorbeelden

### Voorbeeld 1: Een eenvoudige variabele evalueren
```bash
command="ls -l"
eval $command
```
In dit voorbeeld wordt de variabele `command` geëvalueerd en uitgevoerd, wat resulteert in de uitvoer van `ls -l`.

### Voorbeeld 2: Dynamische variabelen gebruiken
```bash
var1="Hello"
var2="World"
eval echo \$var1, \$var2
```
Hier worden de variabelen `var1` en `var2` geëvalueerd en weergegeven als "Hello, World".

### Voorbeeld 3: Combineren van commando's
```bash
cmd1="echo 'Hello'"
cmd2="echo 'World'"
eval "$cmd1; $cmd2"
```
In dit geval worden beide commando's uitgevoerd, wat resulteert in de uitvoer van "Hello" en "World".

## Tips
- Wees voorzichtig met het gebruik van `eval`, vooral met invoer van gebruikers, omdat dit kan leiden tot beveiligingsrisico's zoals code-injectie.
- Gebruik `eval` alleen wanneer het absoluut noodzakelijk is, omdat het de leesbaarheid van je scripts kan verminderen.
- Test je commando's eerst zonder `eval` om te zien wat de uitvoer is voordat je het daadwerkelijk uitvoert.