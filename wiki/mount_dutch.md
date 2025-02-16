# [Linux] Bash mount gebruik: Koppel bestandssystemen

## Overzicht
De `mount`-opdracht in Bash wordt gebruikt om bestandssystemen aan te sluiten op een bepaald punt in de bestandshierarchie. Dit stelt gebruikers in staat om toegang te krijgen tot bestanden op verschillende schijven of partities alsof ze deel uitmaken van het hoofdbestandssysteem.

## Gebruik
De basis syntaxis van de `mount`-opdracht is als volgt:

```bash
mount [opties] [argumenten]
```

## Veelvoorkomende Opties
- `-t type`: Specificeert het type bestandssysteem (bijv. ext4, ntfs).
- `-o opties`: Geeft extra opties op, zoals `ro` voor alleen-lezen of `rw` voor lezen en schrijven.
- `-a`: Mount alle bestandssystemen die zijn vermeld in `/etc/fstab`.
- `-r`: Mount het bestandssysteem als alleen-lezen.

## Veelvoorkomende Voorbeelden
Hier zijn enkele praktische voorbeelden van het gebruik van de `mount`-opdracht:

1. **Een ext4-bestandssysteem mounten:**
   ```bash
   mount -t ext4 /dev/sdb1 /mnt/mijnschijf
   ```

2. **Een NTFS-bestandssysteem mounten met alleen-lezen toegang:**
   ```bash
   mount -t ntfs -o ro /dev/sdc1 /mnt/usb
   ```

3. **Alle bestandssystemen in `/etc/fstab` mounten:**
   ```bash
   mount -a
   ```

4. **Een bestandssysteem mounten met extra opties:**
   ```bash
   mount -t ext4 -o rw,noatime /dev/sda1 /mnt/data
   ```

## Tips
- Zorg ervoor dat je de juiste machtigingen hebt om een bestandssysteem te mounten; vaak zijn root-rechten vereist.
- Controleer altijd of het bestandssysteem correct is ontkoppeld met de `umount`-opdracht voordat je het fysiek verwijdert.
- Gebruik de `df -h`-opdracht om een overzicht te krijgen van alle gemounte bestandssystemen en hun gebruik.