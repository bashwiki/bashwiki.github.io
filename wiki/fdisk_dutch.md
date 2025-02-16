# [Linux] Bash fdisk gebruik: Schijfpartitiebeheer

## Overzicht
De `fdisk`-opdracht is een krachtige tool voor het beheren van schijfpartities op Linux-systemen. Het stelt gebruikers in staat om partities te maken, te verwijderen en te wijzigen op harde schijven en andere opslagapparaten.

## Gebruik
De basis syntaxis van de `fdisk`-opdracht is als volgt:

```bash
fdisk [opties] [apparaat]
```

Hierbij is `[apparaat]` meestal iets als `/dev/sda` of `/dev/nvme0n1`, afhankelijk van je systeem.

## Veelvoorkomende opties
- `-l`: Lijst alle beschikbare schijven en hun partities.
- `-u`: Gebruik sectoren in plaats van cilinders voor de weergave van partitie-informatie.
- `-n`: Maak een nieuwe partitie aan.
- `-d`: Verwijder een bestaande partitie.
- `-t`: Wijzig het type van een partitie.

## Veelvoorkomende voorbeelden

### Lijst beschikbare schijven
Om een lijst van alle beschikbare schijven en hun partities te tonen, gebruik je:

```bash
fdisk -l
```

### Nieuwe partitie aanmaken
Om een nieuwe partitie aan te maken op `/dev/sda`, start je `fdisk` met het apparaat:

```bash
fdisk /dev/sda
```
Volg de prompts om een nieuwe partitie te maken.

### Een partitie verwijderen
Om een bestaande partitie te verwijderen, start je `fdisk` en kies je de optie om een partitie te verwijderen:

```bash
fdisk /dev/sda
```
Kies vervolgens de optie `d` en geef het partitie nummer op dat je wilt verwijderen.

### Partitietype wijzigen
Om het type van een partitie te wijzigen, start je `fdisk` en gebruik je de `t` optie:

```bash
fdisk /dev/sda
```
Kies de optie `t`, geef het partitie nummer op en selecteer het nieuwe type.

## Tips
- Maak altijd een back-up van belangrijke gegevens voordat je wijzigingen aanbrengt in partities.
- Gebruik `parted` of `gparted` voor een grafische interface als je niet vertrouwd bent met de commandoregel.
- Wees voorzichtig met het verwijderen van partities, omdat dit kan leiden tot gegevensverlies.