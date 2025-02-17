# [Linux] Bash du Kullanımı: Disk kullanımını gösterir

## Genel Bakış
`du` (disk usage) komutu, bir dosya veya dizinin disk alanını ne kadar kullandığını gösterir. Bu komut, sistem yöneticileri ve kullanıcılar için disk alanı yönetimi açısından oldukça faydalıdır.

## Kullanım
Temel sözdizimi şu şekildedir:
```bash
du [seçenekler] [argümanlar]
```

## Yaygın Seçenekler
- `-h`: İnsan tarafından okunabilir formatta çıktı verir (örneğin, KB, MB).
- `-s`: Sadece toplam boyutu gösterir, alt dizinleri listelemez.
- `-a`: Tüm dosyaların ve dizinlerin boyutlarını gösterir.
- `-c`: Toplam boyutu da içeren bir özet verir.

## Yaygın Örnekler
1. Belirli bir dizinin disk kullanımını gösterme:
   ```bash
   du /home/kullanici
   ```

2. İnsan tarafından okunabilir formatta çıktı almak:
   ```bash
   du -h /home/kullanici
   ```

3. Sadece toplam boyutu gösterme:
   ```bash
   du -sh /home/kullanici
   ```

4. Tüm dosyaların boyutlarını gösterme:
   ```bash
   du -ah /home/kullanici
   ```

5. Bir dizindeki tüm alt dizinlerin boyutlarını listeleme:
   ```bash
   du -h --max-depth=1 /home/kullanici
   ```

## İpuçları
- `du` komutunu `sort` ile birleştirerek en fazla yer kaplayan dosyaları bulabilirsiniz:
  ```bash
  du -ah /home/kullanici | sort -hr | head -n 10
  ```
- Disk kullanımını düzenli olarak kontrol etmek, gereksiz dosyaları temizlemek için faydalıdır.
- `du` komutunu kullanırken, büyük dizinlerde işlem süresinin uzayabileceğini unutmayın; bu nedenle belirli bir derinlikte sınırlama yapmayı düşünebilirsiniz.