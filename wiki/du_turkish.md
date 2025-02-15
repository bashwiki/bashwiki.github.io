# [리눅스] Bash du 사용법

## Genel Bakış
`du` (disk usage) komutu, bir dosya veya dizinin disk alanını ne kadar kullandığını gösteren bir araçtır. Bu komut, sistem yöneticileri ve geliştiriciler için disk alanı yönetimi ve analizinde önemli bir rol oynar. `du`, belirli bir dizin altındaki dosyaların ve alt dizinlerin boyutlarını hesaplayarak, kullanıcıların disk alanını daha verimli bir şekilde yönetmelerine yardımcı olur.

## Kullanım
`du` komutunun temel sözdizimi şu şekildedir:

```bash
du [seçenekler] [dosya/dizin]
```

### Yaygın Seçenekler
- `-h`: Boyutları insan tarafından okunabilir formatta gösterir (örneğin, KB, MB, GB).
- `-s`: Sadece toplam boyutu gösterir, alt dizinleri listelemez.
- `-a`: Tüm dosyaların boyutlarını gösterir, yalnızca dizinleri değil.
- `-c`: Toplam boyutu da dahil ederek, tüm dosya ve dizinlerin toplamını gösterir.

## Örnekler
### Örnek 1: Dizin Boyutunu Görüntüleme
Aşağıdaki komut, mevcut dizinin altındaki tüm dosya ve dizinlerin boyutlarını insan tarafından okunabilir formatta gösterir:

```bash
du -h
```

### Örnek 2: Belirli Bir Dizin İçin Toplam Boyutu Görüntüleme
Aşağıdaki komut, `/var/log` dizininin toplam boyutunu gösterir:

```bash
du -sh /var/log
```

## İpuçları
- `du` komutunu kullanarak hangi dosyaların veya dizinlerin en fazla disk alanını kullandığını belirlemek için `du -h --max-depth=1` komutunu kullanabilirsiniz. Bu, yalnızca birinci seviye alt dizinlerin boyutlarını gösterir.
- Disk alanı kullanımını izlemek için `du` komutunu düzenli olarak çalıştırmak, gereksiz dosyaları temizlemenize ve disk alanınızı optimize etmenize yardımcı olabilir.
- `du` komutunu `sort` ile birleştirerek, en fazla alan kullanan dosya ve dizinleri sıralayabilirsiniz. Örneğin:

```bash
du -h | sort -hr
```

Bu komut, disk kullanımını en yüksekten en düşüğe doğru sıralar.