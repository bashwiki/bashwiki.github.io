# [Linux] Bash wait gebruik: Wacht op processen

## Overzicht
De `wait` opdracht in Bash wordt gebruikt om te wachten op de voltooiing van achtergrondprocessen. Het is een handige manier om ervoor te zorgen dat een script pas verder gaat als bepaalde taken zijn afgerond.

## Gebruik
De basis syntaxis van de `wait` opdracht is als volgt:

```bash
wait [options] [arguments]
```

## Veelvoorkomende Opties
- `-n`: Wacht op de voltooiing van de eerstvolgende achtergrondtaak.
- `PID`: Wacht op de voltooiing van het proces met het opgegeven proces-ID.

## Veelvoorkomende Voorbeelden

### Voorbeeld 1: Wachten op een specifiek proces
Als je een proces op de achtergrond start en wilt wachten tot het is voltooid, kun je het PID gebruiken:

```bash
sleep 5 &
wait $!
echo "Het proces is voltooid."
```

### Voorbeeld 2: Wachten op meerdere processen
Je kunt ook wachten op meerdere achtergrondprocessen tegelijk:

```bash
sleep 3 &
sleep 5 &
wait
echo "Alle processen zijn voltooid."
```

### Voorbeeld 3: Wachten op de eerstvolgende achtergrondtaak
Met de `-n` optie kun je wachten op de eerstvolgende taak die is voltooid:

```bash
sleep 2 &
sleep 4 &
wait -n
echo "Een achtergrondtaak is voltooid."
```

## Tips
- Gebruik `wait` aan het einde van je script om ervoor te zorgen dat alle achtergrondprocessen zijn voltooid voordat het script eindigt.
- Controleer altijd de exitstatus van het proces met `$?` na het gebruik van `wait` om te zien of het succesvol is uitgevoerd.
- Combineer `wait` met andere commando's in een script om complexe taken te automatiseren zonder dat je handmatig hoeft te wachten.