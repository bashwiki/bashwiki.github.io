# [Linux] Bash grep Kullanımı: Metin içinde desen arama

## Genel Bakış
`grep` komutu, metin dosyalarında belirli bir deseni aramak için kullanılan güçlü bir araçtır. Kullanıcıların dosyalar içinde kelimeleri, ifadeleri veya düzenli ifadeleri hızlı bir şekilde bulmalarını sağlar.

## Kullanım
Temel sözdizimi şu şekildedir:

```bash
grep [seçenekler] [argümanlar]
```

## Yaygın Seçenekler
- `-i`: Büyük/küçük harf duyarsız arama yapar.
- `-v`: Belirtilen deseni içermeyen satırları gösterir.
- `-r`: Alt dizinler dahil olmak üzere dizin içinde arama yapar.
- `-n`: Eşleşen satırların numaralarını gösterir.
- `-l`: Eşleşen dosya adlarını listeler.

## Yaygın Örnekler
Aşağıda `grep` komutunun bazı pratik kullanım örnekleri bulunmaktadır:

### 1. Basit Arama
Bir dosyada belirli bir kelimeyi aramak için:
```bash
grep "kelime" dosya.txt
```

### 2. Büyük/Küçük Harf Duyarsız Arama
Büyük/küçük harf fark etmeksizin arama yapmak için:
```bash
grep -i "kelime" dosya.txt
```

### 3. Eşleşmeyen Satırları Gösterme
Belirli bir kelimeyi içermeyen satırları görüntülemek için:
```bash
grep -v "kelime" dosya.txt
```

### 4. Dizin İçinde Arama
Bir dizin ve alt dizinlerinde arama yapmak için:
```bash
grep -r "kelime" /path/to/dizin
```

### 5. Satır Numaraları ile Gösterme
Eşleşen satırların numaralarını görmek için:
```bash
grep -n "kelime" dosya.txt
```

## İpuçları
- `grep` komutunu diğer komutlarla birleştirerek daha karmaşık aramalar yapabilirsiniz. Örneğin, `cat` komutuyla birlikte kullanarak dosyanın içeriğini görüntüleyebilir ve belirli bir deseni arayabilirsiniz.
- Arama işlemlerini hızlandırmak için dosyaların boyutuna dikkat edin. Büyük dosyalarda arama yaparken, arama kriterlerinizi daraltmak faydalı olabilir.
- Düzenli ifadeleri kullanarak daha esnek ve güçlü aramalar gerçekleştirebilirsiniz.