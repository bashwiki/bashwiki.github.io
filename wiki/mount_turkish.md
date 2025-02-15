# [리눅스] Bash mount 사용법

## Overview
`mount` komutu, bir dosya sistemini belirli bir dizine bağlamak için kullanılır. Bu işlem, işletim sisteminin dosya sistemine erişimini sağlar. Genellikle, harici depolama aygıtları (USB bellekler, sabit diskler vb.) veya ağ dosya sistemleri gibi kaynakları sisteme entegre etmek için kullanılır. `mount` komutu, bağlama işlemi sırasında dosya sisteminin hangi aygıta ait olduğunu ve hangi dizine bağlanacağını belirler.

## Usage
`mount` komutunun temel sözdizimi aşağıdaki gibidir:

```bash
mount [seçenekler] <cihaz> <bağlama_noktası>
```

### Yaygın Seçenekler
- `-t <dosya_sistemi>`: Bağlanacak dosya sisteminin türünü belirtir (örneğin, ext4, ntfs, vfat).
- `-o <seçenekler>`: Bağlama işlemi sırasında kullanılacak özel seçenekleri belirtir (örneğin, `ro` sadece okunur, `rw` okuma/yazma).
- `-a`: `/etc/fstab` dosyasındaki tüm dosya sistemlerini bağlar.
- `-r`: Dosya sistemini sadece okunur modda bağlar.

## Examples
### Örnek 1: USB Belleği Bağlama
Bir USB bellek cihazını `/mnt/usb` dizinine bağlamak için aşağıdaki komutu kullanabilirsiniz:

```bash
sudo mount /dev/sdb1 /mnt/usb
```

Burada `/dev/sdb1`, bağlanacak USB bellek aygıtının cihaz dosyasıdır ve `/mnt/usb` ise bağlama noktasını temsil eder.

### Örnek 2: Ağ Dosya Sistemini Bağlama
Bir ağ dosya sistemini bağlamak için aşağıdaki komutu kullanabilirsiniz:

```bash
sudo mount -t nfs 192.168.1.100:/paylasim /mnt/nfs
```

Bu komut, `192.168.1.100` IP adresindeki bir NFS paylaşımını `/mnt/nfs` dizinine bağlar.

## Tips
- Bağlama işlemi yapmadan önce, bağlama noktasının (örneğin, `/mnt/usb`) mevcut olduğundan emin olun. Eğer yoksa, `mkdir` komutuyla oluşturabilirsiniz.
- Bağlı dosya sistemini çıkarmak için `umount <bağlama_noktası>` komutunu kullanmayı unutmayın.
- `mount` komutunu kullanırken root yetkilerine ihtiyaç duyabilirsiniz, bu nedenle `sudo` ile çalıştırmak yaygın bir uygulamadır.
- `/etc/fstab` dosyasını düzenleyerek, sistem açıldığında otomatik olarak bağlanacak dosya sistemlerini tanımlayabilirsiniz.