# [리눅스] Bash sort 사용법

## Overview
`sort` komutu, bir dosyadaki veya standart girdi akışındaki verileri sıralamak için kullanılan bir Bash komutudur. Genellikle metin dosyalarındaki satırları alfabetik veya sayısal olarak sıralamak için kullanılır. `sort`, verileri belirli bir düzene göre düzenleyerek daha okunabilir hale getirir ve veri analizi için önemli bir araçtır.

## Usage
Temel `sort` komutunun sözdizimi şu şekildedir:

```bash
sort [seçenekler] [dosya_adı]
```

### Yaygın Seçenekler:
- `-r`: Sıralamayı tersine çevirir (büyükten küçüğe).
- `-n`: Sayısal sıralama yapar.
- `-k`: Belirli bir alanı (kolonu) sıralamak için kullanılır. Örneğin, `-k2` ikinci alanı kullanarak sıralama yapar.
- `-u`: Tekrar eden satırları kaldırarak yalnızca benzersiz satırları gösterir.
- `-o`: Sıralanmış çıktıyı belirtilen dosyaya kaydeder.

## Examples
### Örnek 1: Basit Sıralama
Aşağıdaki komut, `veriler.txt` dosyasındaki satırları alfabetik olarak sıralar ve çıktıyı ekrana yazdırır.

```bash
sort veriler.txt
```

### Örnek 2: Sayısal Sıralama
Aşağıdaki komut, `sayilar.txt` dosyasındaki sayıları sayısal olarak sıralar ve çıktıyı `sirali_sayilar.txt` dosyasına kaydeder.

```bash
sort -n sayilar.txt -o sirali_sayilar.txt
```

## Tips
- Sıralama işlemi büyük/küçük harf duyarlıdır. Eğer büyük harfleri küçük harflerle birleştirerek sıralama yapmak istiyorsanız, `-f` seçeneğini kullanabilirsiniz.
- Sıralama işlemi büyük dosyalar için zaman alabilir. Performansı artırmak için verilerinizi önceden filtrelemek veya düzenlemek iyi bir uygulamadır.
- `sort` komutunu diğer komutlarla birleştirerek daha karmaşık veri işleme görevleri gerçekleştirebilirsiniz. Örneğin, `grep` ile filtreleme yapıp ardından `sort` ile sıralama yapabilirsiniz.