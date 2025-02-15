# [리눅스] Bash sed 사용법

## Genel Bakış
`sed`, "stream editor" (akış düzenleyici) olarak bilinen bir komuttur ve metin dosyalarını düzenlemek için kullanılır. Genellikle metin akışları üzerinde arama, değiştirme, silme ve biçimlendirme işlemleri yapmak için kullanılır. `sed`, özellikle büyük dosyalarla çalışırken veya dosya içeriğini otomatik olarak düzenlemek gerektiğinde oldukça kullanışlıdır.

## Kullanım
Temel `sed` sözdizimi şu şekildedir:

```bash
sed [seçenekler] 'komutlar' dosya_adı
```

### Yaygın Seçenekler
- `-e`: Birden fazla `sed` komutu belirtmek için kullanılır.
- `-i`: Dosyayı yerinde (in-place) düzenler, yani değişiklikleri dosyaya kaydeder.
- `-n`: Varsayılan olarak çıktı vermemek için kullanılır; yalnızca belirtilen komutlarla eşleşen satırları gösterir.

## Örnekler

### Örnek 1: Metin Değiştirme
Aşağıdaki komut, `metin.txt` dosyasında "eski" kelimesini "yeni" ile değiştirir ve sonucu ekrana yazdırır.

```bash
sed 's/eski/yeni/g' metin.txt
```

### Örnek 2: Satır Silme
Aşağıdaki komut, `metin.txt` dosyasının 2. satırını siler ve sonucu dosyaya kaydeder.

```bash
sed -i '2d' metin.txt
```

## İpuçları
- `sed` ile çalışırken, dosyanızın bir yedeğini almak iyi bir uygulamadır; özellikle `-i` seçeneğini kullanıyorsanız.
- Düzenlemeleri test etmek için `-n` seçeneğini kullanarak yalnızca belirli satırları görüntüleyebilirsiniz.
- Karmaşık düzenlemeler için birden fazla `sed` komutunu `-e` seçeneğiyle birleştirebilirsiniz.

Bu bilgiler, `sed` komutunu etkili bir şekilde kullanmanıza yardımcı olacaktır.