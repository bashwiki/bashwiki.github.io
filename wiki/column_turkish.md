# [Linux] Bash column Kullanımı: Verileri sütunlar halinde düzenleme

## Genel Bakış
`column` komutu, metin verilerini sütunlar halinde düzenlemek için kullanılır. Bu komut, özellikle verileri daha okunabilir hale getirmek için boşluk veya belirli bir ayırıcı ile ayrılmış verileri hizalamada oldukça faydalıdır.

## Kullanım
Temel sözdizimi aşağıdaki gibidir:
```bash
column [options] [arguments]
```

## Yaygın Seçenekler
- `-t`: Verileri tabular formatta hizalar.
- `-s`: Belirtilen ayırıcıyı kullanarak verileri ayırır. Varsayılan ayırıcı boşluktur.
- `-n`: Sütunları hizalarken, sayıları ve metinleri ayrı tutar.
- `-o`: Sütunlar arasında kullanılacak özel bir ayırıcı belirtir.

## Yaygın Örnekler
Aşağıda `column` komutunun bazı pratik örnekleri verilmiştir:

### Örnek 1: Basit Sütun Düzeni
Bir metin dosyasındaki verileri sütunlar halinde düzenlemek için:
```bash
cat dosya.txt | column
```

### Örnek 2: Belirli Bir Ayırıcı Kullanma
Virgülle ayrılmış verileri düzenlemek için:
```bash
cat veri.csv | column -s, -t
```

### Örnek 3: Özel Ayırıcı ile Çıktı
Sütunlar arasında bir tire (-) kullanarak düzenleme:
```bash
cat veri.txt | column -s" " -o "-"
```

### Örnek 4: Sayıları ve Metinleri Ayrı Tutma
Verileri hizalarken sayıları ve metinleri ayrı tutmak için:
```bash
cat dosya.txt | column -n
```

## İpuçları
- Verilerinizi daha iyi görüntülemek için `-t` seçeneğini kullanarak tabular formatta hizalayın.
- Ayırıcıları doğru ayarlamak, verilerin düzgün görünmesi için önemlidir; bu nedenle `-s` seçeneğini kullanarak uygun ayırıcıyı belirleyin.
- Büyük veri setleri ile çalışırken, çıktıyı bir dosyaya yönlendirmek için `>` operatörünü kullanabilirsiniz. Örneğin:
```bash
cat veri.txt | column -t > hizalanmis_veri.txt
```