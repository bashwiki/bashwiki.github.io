# [Linux] Bash route gebruik: Beheer netwerkroutes

## Overzicht
De `route` opdracht in Bash wordt gebruikt om de routingstabel van een Linux-systeem te beheren. Hiermee kun je routes toevoegen, verwijderen of weergeven, wat essentieel is voor netwerkconfiguratie en -beheer.

## Gebruik
De basis syntaxis van de `route` opdracht is als volgt:

```bash
route [opties] [argumenten]
```

## Veelvoorkomende opties
- `-n`: Toon de routingstabel zonder naamresolutie, wat de uitvoer versnelt.
- `add`: Voeg een nieuwe route toe.
- `del`: Verwijder een bestaande route.
- `-net`: Specificeer dat je een netwerkroute wilt beheren.
- `-host`: Specificeer dat je een hostroute wilt beheren.

## Veelvoorkomende voorbeelden

### 1. Weergeven van de huidige routingstabel
```bash
route -n
```

### 2. Een nieuwe route toevoegen
Voeg een route toe naar het netwerk 192.168.1.0 met een subnetmasker van 255.255.255.0 via de gateway 192.168.1.1:
```bash
route add -net 192.168.1.0 netmask 255.255.255.0 gw 192.168.1.1
```

### 3. Een route verwijderen
Verwijder de eerder toegevoegde route:
```bash
route del -net 192.168.1.0 netmask 255.255.255.0
```

### 4. Een specifieke hostroute toevoegen
Voeg een route toe voor een specifieke host, bijvoorbeeld 192.168.1.10, via de gateway 192.168.1.1:
```bash
route add -host 192.168.1.10 gw 192.168.1.1
```

## Tips
- Gebruik de `-n` optie om de uitvoer sneller te maken, vooral op systemen met veel routes.
- Controleer altijd de routingstabel na het toevoegen of verwijderen van routes om er zeker van te zijn dat de wijzigingen correct zijn doorgevoerd.
- Wees voorzichtig bij het verwijderen van routes, omdat dit de netwerkverbindingen kan beïnvloeden.