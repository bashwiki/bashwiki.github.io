# [Linux] Bash ip gebruik: Netwerkconfiguratie en -beheer

## Overzicht
De `ip`-opdracht is een krachtig hulpmiddel voor het beheren van netwerkinstellingen op Linux-systemen. Het stelt gebruikers in staat om netwerkinterfaces te configureren, routes te beheren en informatie over netwerken op te vragen.

## Gebruik
De basis syntaxis van de `ip`-opdracht is als volgt:

```bash
ip [opties] [argumenten]
```

## Veelvoorkomende opties
- `link`: Beheer netwerkinterfaces.
- `addr`: Toon of configureer IP-adressen.
- `route`: Beheer de routingstabel.
- `neigh`: Beheer de ARP-tabel (adres-resolutieprotocol).

## Veelvoorkomende voorbeelden

### 1. Toon netwerkinterfaces
Om een lijst van alle netwerkinterfaces en hun status te bekijken, gebruik je:

```bash
ip link show
```

### 2. Voeg een IP-adres toe aan een interface
Om een IP-adres toe te voegen aan een specifieke interface, gebruik je:

```bash
ip addr add 192.168.1.10/24 dev eth0
```

### 3. Verwijder een IP-adres van een interface
Om een IP-adres van een interface te verwijderen, gebruik je:

```bash
ip addr del 192.168.1.10/24 dev eth0
```

### 4. Toon de routingstabel
Om de huidige routingstabel weer te geven, gebruik je:

```bash
ip route show
```

### 5. Voeg een route toe
Om een nieuwe route toe te voegen, gebruik je:

```bash
ip route add 10.0.0.0/24 via 192.168.1.1
```

## Tips
- Gebruik `ip -h` voor een lijst van beschikbare opties en hun beschrijvingen.
- Wees voorzichtig bij het wijzigen van netwerkconfiguraties, vooral op een remote server, om te voorkomen dat je jezelf verliest.
- Combineer `ip` met andere commando's zoals `grep` om specifieke informatie te filteren, bijvoorbeeld: 

```bash
ip addr show | grep inet
```