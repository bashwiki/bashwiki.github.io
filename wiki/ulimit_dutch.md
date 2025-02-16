# [Linux] Bash ulimit gebruik: Beperk systeembronnen voor processen

## Overzicht
De `ulimit`-opdracht in Bash wordt gebruikt om de systeembronnen te beperken die beschikbaar zijn voor de shell en de processen die daaruit voortkomen. Dit is nuttig voor het beheren van systeembronnen en het voorkomen van overbelasting van het systeem door processen die te veel geheugen of andere bronnen gebruiken.

## Gebruik
De basis syntaxis van de `ulimit`-opdracht is als volgt:

```bash
ulimit [opties] [argumenten]
```

## Veelvoorkomende Opties
Hier zijn enkele veelvoorkomende opties die je kunt gebruiken met `ulimit`:

- `-a`: Toont alle huidige limieten.
- `-c`: Stelt de maximale grootte van core-bestanden in.
- `-d`: Stelt de maximale grootte van het datasegment in.
- `-f`: Stelt de maximale grootte van bestanden in die kunnen worden aangemaakt.
- `-l`: Stelt de maximale grootte van gelockt geheugen in.
- `-m`: Stelt de maximale grootte van resident geheugen in.
- `-n`: Stelt het maximale aantal open bestanden in.
- `-s`: Stelt de maximale grootte van de stack in.
- `-t`: Stelt de maximale tijd in seconden in dat een proces mag draaien.
- `-v`: Stelt de maximale virtuele geheugen grootte in.

## Veelvoorkomende Voorbeelden
Hier zijn enkele praktische voorbeelden van het gebruik van `ulimit`:

1. **Toon alle huidige limieten:**
   ```bash
   ulimit -a
   ```

2. **Stel de maximale grootte van een core-bestand in op 0 (geen core-bestanden):**
   ```bash
   ulimit -c 0
   ```

3. **Stel de maximale grootte van bestanden in op 100 MB:**
   ```bash
   ulimit -f 102400
   ```

4. **Stel het maximale aantal open bestanden in op 200:**
   ```bash
   ulimit -n 200
   ```

5. **Stel de maximale tijd voor een proces in op 60 seconden:**
   ```bash
   ulimit -t 60
   ```

## Tips
- Controleer altijd de huidige limieten met `ulimit -a` voordat je wijzigingen aanbrengt.
- Gebruik `ulimit` in scripts om ervoor te zorgen dat processen niet meer bronnen gebruiken dan toegestaan.
- Wees voorzichtig bij het verhogen van limieten, omdat dit kan leiden tot systeeminstabiliteit.
- Vergeet niet dat limieten per shell-sessie zijn ingesteld; je moet ze mogelijk opnieuw instellen in nieuwe sessies.