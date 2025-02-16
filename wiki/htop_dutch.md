# [Linux] Bash htop gebruik: Systeemmonitor in real-time

## Overzicht
De `htop`-opdracht is een interactieve procesviewer voor Unix-systemen. Het biedt een overzicht van de systeemprocessen en hun gebruik van systeembronnen zoals CPU, geheugen en swapgeheugen. In tegenstelling tot de traditionele `top`-opdracht biedt `htop` een gebruiksvriendelijke interface met kleuraanpassingen en de mogelijkheid om processen eenvoudig te beheren.

## Gebruik
De basis syntaxis van de `htop`-opdracht is als volgt:

```bash
htop [opties] [argumenten]
```

## Veelvoorkomende opties
- `-h`, `--help`: Toont de helpinformatie voor htop.
- `-s`, `--sort`: Sorteert de processen op basis van een opgegeven criterium (bijvoorbeeld CPU of geheugen).
- `-p`, `--pid`: Start htop met een specifieke proces-ID.
- `-u`, `--user`: Toont alleen de processen van een specifieke gebruiker.

## Veelvoorkomende voorbeelden
Hier zijn enkele praktische voorbeelden van het gebruik van `htop`:

- Start htop zonder extra opties:
  ```bash
  htop
  ```

- Start htop en sorteer processen op CPU-gebruik:
  ```bash
  htop -s PERCENT_CPU
  ```

- Start htop en toon alleen processen van de gebruiker "jan":
  ```bash
  htop -u jan
  ```

- Start htop met een specifieke proces-ID (bijvoorbeeld 1234):
  ```bash
  htop -p 1234
  ```

## Tips
- Gebruik de pijltjestoetsen om door de processen te navigeren en druk op `F9` om een proces te beëindigen.
- Druk op `F2` om het configuratiemenu te openen en pas de weergave aan naar jouw voorkeuren.
- Maak gebruik van de zoekfunctie door op `/` te drukken om snel een specifiek proces te vinden.
- Vergeet niet dat je `htop` moet installeren op sommige systemen, omdat het mogelijk niet standaard is geïnstalleerd. Gebruik hiervoor de pakketbeheerder van jouw distributie.