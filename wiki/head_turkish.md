# [Linux] Bash head Kullanımı: Dosyanın Başındaki Satırları Görüntüleme

## Genel Bakış
`head` komutu, bir dosyanın en üst kısmındaki belirli sayıda satırı görüntülemek için kullanılır. Genellikle büyük dosyaların içeriğini hızlı bir şekilde gözden geçirmek için faydalıdır.

## Kullanım
Temel sözdizimi şu şekildedir:

```bash
head [seçenekler] [argümanlar]
```

## Yaygın Seçenekler
- `-n [sayı]`: Görüntülenecek satır sayısını belirtir. Varsayılan olarak 10 satır gösterir.
- `-c [bayt]`: Görüntülenecek bayt sayısını belirtir.
- `-q`: Birden fazla dosya belirtildiğinde, dosya adlarını göstermeden çıktı verir.
- `-v`: Her dosya için başlık bilgilerini gösterir.

## Yaygın Örnekler
Aşağıda `head` komutunun bazı pratik kullanım örnekleri bulunmaktadır:

### 1. Varsayılan 10 Satırı Görüntüleme
```bash
head dosya.txt
```

### 2. İlk 5 Satırı Görüntüleme
```bash
head -n 5 dosya.txt
```

### 3. İlk 20 Baytı Görüntüleme
```bash
head -c 20 dosya.txt
```

### 4. Birden Fazla Dosya ile Kullanma
```bash
head dosya1.txt dosya2.txt
```

### 5. Başlık Bilgisi ile Görüntüleme
```bash
head -v dosya1.txt dosya2.txt
```

## İpuçları
- Büyük dosyalarla çalışırken, `head` komutunu kullanarak dosyanın içeriğini hızlıca gözden geçirebilirsiniz.
- `head` komutunu bir boru (pipe) ile diğer komutlarla birleştirerek daha karmaşık işlemler gerçekleştirebilirsiniz. Örneğin, `grep` ile birlikte kullanarak belirli bir terimi içeren dosyanın başındaki satırları bulabilirsiniz.
- Dosya içeriğini incelemek için `tail` komutuyla birlikte kullanarak hem baştan hem de sondan satırları görüntülemek faydalı olabilir.