# [Linux] Bash hash gebruik: Beheer van de opdrachtcache

## Overzicht
De `hash` opdracht in Bash wordt gebruikt om de cache van de locaties van uitvoerbare bestanden te beheren. Wanneer je een commando uitvoert, slaat Bash de locatie op in een interne cache, zodat het de volgende keer sneller kan worden gevonden. Dit is vooral nuttig voor het optimaliseren van de prestaties bij het uitvoeren van veelgebruikte commando's.

## Gebruik
De basis syntaxis van de `hash` opdracht is als volgt:

```bash
hash [opties] [argumenten]
```

## Veelvoorkomende Opties
- `-r`: Vernietig de huidige cache en reset deze.
- `-p`: Geef een specifieke pad op voor het commando dat je wilt cachen.
- `-l`: Toon de huidige hash cache.

## Veelvoorkomende Voorbeelden

### 1. Toon de huidige hash cache
Om de huidige cache van uitvoerbare bestanden te bekijken, gebruik je:

```bash
hash
```

### 2. Reset de hash cache
Als je de cache wilt wissen en opnieuw wilt beginnen, gebruik je:

```bash
hash -r
```

### 3. Voeg een specifiek pad toe aan de hash cache
Als je een specifiek pad wilt cachen voor een commando, gebruik je:

```bash
hash -p /pad/naar/commando commando
```

### 4. Toon de hash van een specifiek commando
Om de locatie van een specifiek commando in de cache te bekijken, gebruik je:

```bash
hash commando
```

## Tips
- Gebruik `hash -r` na het installeren van nieuwe software om ervoor te zorgen dat Bash de nieuwste versies van de commando's gebruikt.
- Controleer regelmatig je hash cache met `hash` om te zien welke commando's zijn gecached en hun locaties.
- Het gebruik van `hash -p` kan handig zijn als je meerdere versies van een commando hebt en je wilt specificeren welke versie je wilt gebruiken.