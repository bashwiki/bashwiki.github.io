# [Linux] Bash mount Kullanımı: Dosya sistemlerini bağlama

## Genel Bakış
`mount` komutu, bir dosya sistemini belirli bir dizine bağlamak için kullanılır. Bu işlem, dosya sisteminin içeriğine erişim sağlamanın yanı sıra, sistemin dosya yapısını yönetmeyi de kolaylaştırır.

## Kullanım
Temel sözdizimi şu şekildedir:

```bash
mount [seçenekler] [argümanlar]
```

## Yaygın Seçenekler
- `-t`: Bağlanacak dosya sisteminin türünü belirtir.
- `-o`: Bağlama işlemi için özel seçenekler tanımlar.
- `-a`: `/etc/fstab` dosyasında tanımlı olan tüm dosya sistemlerini bağlar.
- `-r`: Dosya sistemini yalnızca okunur modda bağlar.

## Yaygın Örnekler
Aşağıda `mount` komutunun bazı pratik örnekleri verilmiştir:

1. **Bir USB sürücüsünü bağlama:**
   ```bash
   mount /dev/sdb1 /mnt/usb
   ```

2. **Bir NFS dosya sistemini bağlama:**
   ```bash
   mount -t nfs 192.168.1.100:/paylasim /mnt/nfs
   ```

3. **Tüm dosya sistemlerini bağlama:**
   ```bash
   mount -a
   ```

4. **Bir dosya sistemini yalnızca okunur modda bağlama:**
   ```bash
   mount -o ro /dev/sdc1 /mnt/read_only
   ```

## İpuçları
- Bağlama işlemi için yeterli izinlere sahip olduğunuzdan emin olun; genellikle `root` kullanıcısı olmanız gerekir.
- Bağladığınız dosya sistemini çıkarmadan önce, dosya sisteminin kullanılmadığından emin olun. Bunu sağlamak için `umount` komutunu kullanabilirsiniz.
- `fstab` dosyasını düzenleyerek, sistem açıldığında otomatik olarak bağlanacak dosya sistemlerini tanımlayabilirsiniz.