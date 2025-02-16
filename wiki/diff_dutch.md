# [Linux] Bash diff gebruik: Vergelijk bestanden en mappen

## Overzicht
Het `diff`-commando in Bash wordt gebruikt om de verschillen tussen twee bestanden of mappen te vergelijken. Het toont de regels die verschillen, zodat gebruikers eenvoudig kunnen zien wat er is gewijzigd.

## Gebruik
De basis syntaxis van het `diff`-commando is als volgt:

```bash
diff [opties] [argumenten]
```

## Veelvoorkomende opties
- `-u`: Toon de verschillen in een "unified" formaat, wat het gemakkelijker maakt om wijzigingen te begrijpen.
- `-c`: Toon de verschillen in een "context" formaat, dat meer context geeft rond de wijzigingen.
- `-i`: Negeer hoofdlettergevoeligheid bij het vergelijken van tekst.
- `-w`: Negeer spaties en tabs bij het vergelijken van regels.
- `-r`: Vergelijk ook alle bestanden in submappen.

## Veelvoorkomende voorbeelden

### Basis vergelijking van twee bestanden
Om de verschillen tussen twee tekstbestanden te zien, gebruik je:

```bash
diff bestand1.txt bestand2.txt
```

### Gebruik van de unified optie
Om de verschillen in een unified formaat te tonen:

```bash
diff -u bestand1.txt bestand2.txt
```

### Vergelijken van twee mappen
Om de inhoud van twee mappen te vergelijken, inclusief submappen:

```bash
diff -r map1/ map2/
```

### Negeer spaties en tabs
Als je wilt dat spaties en tabs worden genegeerd tijdens de vergelijking:

```bash
diff -w bestand1.txt bestand2.txt
```

## Tips
- Gebruik de `-u` optie voor een duidelijker overzicht van de wijzigingen, vooral bij het delen van patches.
- Combineer `diff` met `patch` om wijzigingen eenvoudig toe te passen op bestanden.
- Controleer altijd de verschillen voordat je bestanden samenvoegt of overschrijft om gegevensverlies te voorkomen.