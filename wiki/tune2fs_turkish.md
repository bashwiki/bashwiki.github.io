# [리눅스] Bash tune2fs 사용법

## Genel Bakış
`tune2fs`, Linux işletim sistemlerinde kullanılan bir komuttur ve ext2, ext3 ve ext4 dosya sistemlerinin ayarlarını değiştirmek için kullanılır. Bu komut, dosya sisteminin performansını ve güvenliğini artırmak için çeşitli parametreleri ayarlamanıza olanak tanır. Örneğin, dosya sistemi etiketini değiştirebilir, günlükleme seçeneklerini ayarlayabilir veya dosya sistemi için maksimum dosya sayısını belirleyebilirsiniz.

## Kullanım
`tune2fs` komutunun temel sözdizimi aşağıdaki gibidir:

```bash
tune2fs [seçenekler] <dosya_sistemi>
```

### Yaygın Seçenekler
- `-L <etiket>`: Dosya sisteminin etiketini ayarlamak için kullanılır.
- `-O <özellik>`: Dosya sistemine yeni özellikler eklemek için kullanılır.
- `-c <maks_dosya_sayısı>`: Dosya sisteminin maksimum dosya sayısını ayarlamak için kullanılır.
- `-i <gün>`: Dosya sisteminin kontrol edilme sıklığını ayarlamak için kullanılır.
- `-f`: Komutun zorla çalıştırılmasını sağlar.

## Örnekler
### Örnek 1: Dosya Sistemi Etiketini Değiştirme
Aşağıdaki komut, `/dev/sda1` dosya sisteminin etiketini "YeniEtiket" olarak değiştirir:

```bash
sudo tune2fs -L YeniEtiket /dev/sda1
```

### Örnek 2: Maksimum Dosya Sayısını Ayarlama
Aşağıdaki komut, `/dev/sda1` dosya sisteminin maksimum dosya sayısını 100000 olarak ayarlar:

```bash
sudo tune2fs -c 100000 /dev/sda1
```

## İpuçları
- `tune2fs` komutunu kullanmadan önce dosya sisteminin yedeklemesini almanız önerilir. Yanlış ayarlar, veri kaybına yol açabilir.
- Komutu çalıştırmadan önce dosya sisteminin bağlı olmadığından emin olun. Aksi takdirde, dosya sistemi üzerinde beklenmedik sonuçlar doğurabilir.
- `tune2fs` ile yapılan değişikliklerin etkili olabilmesi için dosya sisteminin yeniden bağlanması veya sistemin yeniden başlatılması gerekebilir.