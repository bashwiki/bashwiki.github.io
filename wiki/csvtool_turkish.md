# [Linux] Bash csvtool Kullanımı: CSV dosyalarını işlemek için bir araç

## Genel Bakış
csvtool, CSV (Virgülle Ayrılmış Değerler) dosyalarını işlemek için kullanılan bir komut satırı aracıdır. Bu araç, CSV dosyalarındaki verileri düzenlemek, filtrelemek ve analiz etmek için çeşitli işlevler sunar.

## Kullanım
Temel sözdizimi aşağıdaki gibidir:
```bash
csvtool [seçenekler] [argümanlar]
```

## Yaygın Seçenekler
- `-c`: Belirtilen sütunu seçer.
- `-r`: Belirtilen satırı seçer.
- `-t`: Sütun ayırıcıyı belirtir (varsayılan olarak virgül).
- `-h`: Başlık satırını gösterir veya gizler.

## Yaygın Örnekler
Aşağıda, csvtool komutunun bazı pratik kullanım örnekleri bulunmaktadır:

### 1. Sadece Belirli Sütunları Görüntüleme
Sadece 1. ve 3. sütunları görüntülemek için:
```bash
csvtool -c 1,3 dosya.csv
```

### 2. Belirli Bir Satırı Görüntüleme
5. satırı görüntülemek için:
```bash
csvtool -r 5 dosya.csv
```

### 3. Farklı Sütun Ayırıcı Kullanma
Tab ile ayrılmış bir dosyayı işlemek için:
```bash
csvtool -t $'\t' -c 1,2 dosya.tsv
```

### 4. Başlık Satırını Gizleme
Başlık satırını gizleyerek verileri görüntülemek için:
```bash
csvtool -h -c 1 dosya.csv
```

## İpuçları
- CSV dosyalarınızda boşluk veya özel karakterler varsa, sütun ayırıcıyı doğru bir şekilde ayarladığınızdan emin olun.
- Verilerinizi filtrelemek için birden fazla seçenek kullanabilirsiniz; bu, daha karmaşık sorgular oluşturmanıza yardımcı olur.
- csvtool ile birlikte diğer komutları (örneğin, `grep` veya `sort`) kullanarak daha güçlü veri işleme senaryoları oluşturabilirsiniz.