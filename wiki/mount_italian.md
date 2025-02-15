# [리눅스] Bash mount 사용법

## Overview
Il comando `mount` in Bash è utilizzato per montare file system su directory specifiche nel sistema operativo Linux. La sua funzione principale è quella di rendere accessibili i file e le directory contenuti in un dispositivo di memorizzazione, come un disco rigido, una chiavetta USB o una partizione di rete, all'interno della struttura del file system del sistema operativo. Senza montare un dispositivo, il sistema non può accedere ai dati in esso contenuti.

## Usage
La sintassi di base del comando `mount` è la seguente:

```bash
mount [opzioni] <dispositivo> <punto_di_montaggio>
```

### Opzioni comuni:
- `-t <tipo>`: Specifica il tipo di file system (es. ext4, ntfs, vfat).
- `-o <opzioni>`: Permette di specificare opzioni aggiuntive come `ro` (read-only), `rw` (read-write), `noexec`, ecc.
- `-a`: Monta tutti i file system elencati nel file `/etc/fstab`.
- `-r`: Monta il file system in modalità di sola lettura.

## Examples
### Esempio 1: Montare una chiavetta USB
Supponiamo di voler montare una chiavetta USB che è stata riconosciuta come `/dev/sdb1` nella directory `/mnt/usb`.

```bash
sudo mount /dev/sdb1 /mnt/usb
```

### Esempio 2: Montare un file system NTFS
Se si desidera montare un disco NTFS presente in `/dev/sdc1` con opzioni di lettura e scrittura, si può utilizzare il seguente comando:

```bash
sudo mount -t ntfs -o rw /dev/sdc1 /mnt/ntfs
```

## Tips
- Assicurati di avere i permessi necessari per montare i dispositivi. Spesso è necessario utilizzare `sudo` per eseguire il comando come amministratore.
- Controlla sempre il file `/etc/fstab` per configurazioni di montaggio automatico all'avvio del sistema.
- Dopo aver finito di utilizzare un file system montato, è importante smontarlo utilizzando il comando `umount` per evitare la perdita di dati.
- Utilizza il comando `df -h` per verificare quali file system sono attualmente montati e per ottenere informazioni sul loro utilizzo.