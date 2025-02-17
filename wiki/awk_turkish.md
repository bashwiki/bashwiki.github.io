# [Linux] Bash awk Kullanımı: Metin işleme aracı

## Genel Bakış
`awk`, metin dosyalarını işlemek ve analiz etmek için kullanılan güçlü bir programlama dilidir. Satır bazında işlem yaparak, belirli desenlere göre verileri filtreleyebilir, dönüştürebilir ve raporlayabilir.

## Kullanım
Temel sözdizimi şu şekildedir:

```bash
awk [seçenekler] [argümanlar]
```

## Yaygın Seçenekler
- `-F`: Alan ayırıcıyı belirtir. Varsayılan olarak boşluk kullanılır.
- `-v`: Değişken tanımlamak için kullanılır.
- `-f`: Bir dosyadan `awk` komutunu yükler.

## Yaygın Örnekler

### 1. Belirli bir alanı yazdırma
Bir dosyadaki ikinci alanı yazdırmak için:

```bash
awk '{print $2}' dosya.txt
```

### 2. Alan ayırıcıyı değiştirme
Virgülle ayrılmış bir dosyadaki ilk alanı yazdırmak için:

```bash
awk -F, '{print $1}' dosya.csv
```

### 3. Koşullu yazdırma
Sadece 50'den büyük sayıları yazdırmak için:

```bash
awk '$1 > 50' sayilar.txt
```

### 4. Değişken kullanma
Bir değişken tanımlayıp kullanmak için:

```bash
awk -v limit=100 '$1 > limit' sayilar.txt
```

### 5. Dosyadan komut yükleme
Bir `awk` komutunu bir dosyadan yüklemek için:

```bash
awk -f komutlar.awk dosya.txt
```

## İpuçları
- `awk` ile karmaşık işlemler yapmak için döngüler ve koşullu ifadeler kullanabilirsiniz.
- Verilerinizi daha iyi anlamak için `print` komutunu kullanarak ara sonuçları yazdırın.
- `awk` komutlarını birleştirerek daha karmaşık analizler yapabilirsiniz.