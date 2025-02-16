# [Linux] Bash ss gebruik: Netwerkverbindingen bekijken

## Overzicht
De `ss` (socket statistics) command is een krachtige tool in Linux die wordt gebruikt om netwerkverbindingen en sockets te inspecteren. Het biedt gedetailleerde informatie over actieve verbindingen, inclusief TCP, UDP, en andere sockettypes.

## Gebruik
De basis syntaxis van de `ss` command is als volgt:

```bash
ss [opties] [argumenten]
```

## Veelvoorkomende Opties
- `-t`: Toont alleen TCP-verbindingen.
- `-u`: Toont alleen UDP-verbindingen.
- `-l`: Toont alleen luisterende sockets.
- `-p`: Toont het proces dat de socket gebruikt.
- `-n`: Toont numerieke adressen in plaats van hostnamen.

## Veelvoorkomende Voorbeelden

1. **Toon alle actieve verbindingen:**
   ```bash
   ss
   ```

2. **Toon alleen TCP-verbindingen:**
   ```bash
   ss -t
   ```

3. **Toon alleen luisterende sockets:**
   ```bash
   ss -l
   ```

4. **Toon UDP-verbindingen met procesinformatie:**
   ```bash
   ss -u -p
   ```

5. **Toon verbindingen met numerieke adressen:**
   ```bash
   ss -n
   ```

## Tips
- Gebruik de `-s` optie om een samenvatting van de socketstatistieken te krijgen.
- Combineer opties voor meer gerichte informatie, zoals `ss -tuln` om alle actieve TCP en UDP verbindingen te tonen met numerieke adressen.
- `ss` is vaak sneller en efficiënter dan het oudere `netstat` commando, dus het is een goede keuze voor netwerkdiagnose.