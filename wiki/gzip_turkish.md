# [Linux] Bash gzip Kullanımı: Dosyaları sıkıştırma aracı

## Genel Bakış
`gzip`, dosyaları sıkıştırmak için kullanılan bir komut satırı aracıdır. Genellikle dosya boyutunu küçültmek ve depolama alanından tasarruf etmek amacıyla kullanılır. `gzip`, genellikle metin dosyaları gibi belirli dosya türlerinde daha etkili sonuçlar verir.

## Kullanım
Temel sözdizimi şu şekildedir:

```bash
gzip [seçenekler] [argümanlar]
```

## Yaygın Seçenekler
- `-d` veya `--decompress`: Sıkıştırılmış dosyayı açar.
- `-k` veya `--keep`: Sıkıştırma işlemi sırasında orijinal dosyayı korur.
- `-v` veya `--verbose`: İşlem hakkında daha fazla bilgi verir.
- `-r` veya `--recursive`: Alt dizinlerdeki dosyaları da sıkıştırır.

## Yaygın Örnekler
Aşağıda `gzip` komutunun bazı pratik kullanım örnekleri bulunmaktadır:

### 1. Bir dosyayı sıkıştırma
```bash
gzip dosya.txt
```
Bu komut, `dosya.txt` dosyasını sıkıştırarak `dosya.txt.gz` adında yeni bir dosya oluşturur.

### 2. Sıkıştırılmış bir dosyayı açma
```bash
gzip -d dosya.txt.gz
```
Bu komut, `dosya.txt.gz` dosyasını açarak orijinal `dosya.txt` dosyasını geri getirir.

### 3. Orijinal dosyayı koruyarak sıkıştırma
```bash
gzip -k dosya.txt
```
Bu komut, `dosya.txt` dosyasını sıkıştırırken orijinal dosyayı da korur.

### 4. Bir dizindeki tüm dosyaları sıkıştırma
```bash
gzip -r dizin_adi/
```
Bu komut, belirtilen dizindeki tüm dosyaları sıkıştırır.

## İpuçları
- Sıkıştırılmış dosyaların boyutunu kontrol etmek için `ls -lh` komutunu kullanabilirsiniz.
- Sıkıştırma işlemi sırasında dosya kaybı olmaması için `-k` seçeneğini kullanarak orijinal dosyayı saklayın.
- Büyük dosyalarla çalışırken, sıkıştırma işleminin zaman alabileceğini unutmayın; bu nedenle işlemi arka planda çalıştırmak için `&` sembolünü kullanabilirsiniz.