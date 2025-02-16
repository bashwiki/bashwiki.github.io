# [Linux] Bash virsh gebruik: Beheer virtuele machines

## Overzicht
De `virsh`-opdracht is een commandoregelinterface voor het beheren van virtuele machines die draaien op hypervisors zoals KVM, QEMU en Xen. Met `virsh` kunt u virtuele machines aanmaken, starten, stoppen en configureren, evenals andere beheerfuncties uitvoeren.

## Gebruik
De basis syntaxis van de `virsh`-opdracht is als volgt:

```bash
virsh [opties] [argumenten]
```

## Veelvoorkomende opties
- `--help`: Toont de helpinformatie voor de opdracht.
- `list`: Lijst alle actieve virtuele machines.
- `start`: Start een opgegeven virtuele machine.
- `shutdown`: Stopt een opgegeven virtuele machine.
- `define`: Definieert een nieuwe virtuele machine op basis van een XML-bestand.

## Veelvoorkomende voorbeelden
Hier zijn enkele praktische voorbeelden van het gebruik van `virsh`:

1. **Lijst actieve virtuele machines**:
   ```bash
   virsh list
   ```

2. **Start een virtuele machine**:
   ```bash
   virsh start naam_van_vm
   ```

3. **Stop een virtuele machine**:
   ```bash
   virsh shutdown naam_van_vm
   ```

4. **Definieer een nieuwe virtuele machine**:
   ```bash
   virsh define /pad/naar/virtuele_machine.xml
   ```

5. **Verwijder een virtuele machine**:
   ```bash
   virsh undefine naam_van_vm
   ```

## Tips
- Zorg ervoor dat u de juiste machtigingen heeft om `virsh`-opdrachten uit te voeren, vooral als u virtuele machines wilt starten of stoppen.
- Gebruik `virsh --help` om een lijst van beschikbare commando's en opties te bekijken.
- Maak regelmatig back-ups van uw virtuele machineconfiguraties om gegevensverlies te voorkomen.