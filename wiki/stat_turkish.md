# [Linux] Bash stat Kullanımı: Dosya ve dizin bilgilerini görüntüleme

## Genel Bakış
`stat` komutu, dosya ve dizinlerin ayrıntılı bilgilerini görüntülemek için kullanılır. Bu bilgiler arasında dosya boyutu, oluşturulma tarihi, son erişim tarihi ve izinler gibi özellikler yer alır.

## Kullanım
Temel sözdizimi aşağıdaki gibidir:

```bash
stat [seçenekler] [argümanlar]
```

## Yaygın Seçenekler
- `-c, --format=FORMAT`: Çıktıyı belirtilen FORMAT'a göre özelleştirir.
- `-f, --file-system`: Dosya sisteminin bilgilerini görüntüler.
- `--help`: Komut hakkında yardım bilgisi gösterir.
- `--version`: Komutun sürüm bilgisini gösterir.

## Yaygın Örnekler
Aşağıda `stat` komutunun bazı pratik örnekleri bulunmaktadır:

1. Bir dosyanın bilgilerini görüntülemek:
   ```bash
   stat dosya.txt
   ```

2. Bir dizinin bilgilerini görüntülemek:
   ```bash
   stat /home/kullanici/
   ```

3. Çıktıyı özel bir formatta görüntülemek:
   ```bash
   stat -c '%n: %s bytes' dosya.txt
   ```

4. Dosya sisteminin bilgilerini görüntülemek:
   ```bash
   stat -f /
   ```

## İpuçları
- `stat` komutunu sıkça kullanıyorsanız, belirli dosyaların bilgilerini hızlıca görüntülemek için alias tanımlayabilirsiniz.
- Çıktıyı daha okunabilir hale getirmek için `-c` seçeneği ile özelleştirilmiş formatlar kullanın.
- Dosya izinleri ve sahiplik bilgilerini kontrol etmek için `stat` komutunu kullanmak, güvenlik açısından önemlidir.