# [Linux] Bash sort Kullanımı: Dosya içeriğini sıralama

## Genel Bakış
`sort` komutu, bir dosya veya standart girdi içindeki satırları sıralamak için kullanılır. Bu komut, verileri alfabetik veya sayısal olarak düzenleyerek daha okunabilir hale getirir.

## Kullanım
Temel sözdizimi şu şekildedir:
```bash
sort [seçenekler] [argümanlar]
```

## Yaygın Seçenekler
- `-r`: Sıralamayı tersine çevirir (azalan sırada).
- `-n`: Sayısal sıralama yapar.
- `-k`: Belirli bir alanı (kolonu) kullanarak sıralama yapar.
- `-u`: Tekrar eden satırları kaldırarak yalnızca benzersiz satırları gösterir.
- `-o`: Sonuçları belirtilen dosyaya yazmak için kullanılır.

## Yaygın Örnekler
1. **Basit Sıralama:**
   Bir dosyadaki satırları alfabetik olarak sıralamak için:
   ```bash
   sort dosya.txt
   ```

2. **Ters Sıralama:**
   Satırları tersine sıralamak için:
   ```bash
   sort -r dosya.txt
   ```

3. **Sayısal Sıralama:**
   Sayıları içeren bir dosyayı sayısal olarak sıralamak için:
   ```bash
   sort -n sayilar.txt
   ```

4. **Belirli Bir Alan Üzerinden Sıralama:**
   İkinci alana göre sıralamak için:
   ```bash
   sort -k2 dosya.txt
   ```

5. **Benzersiz Satırları Gösterme:**
   Tekrar eden satırları kaldırarak sıralamak için:
   ```bash
   sort -u dosya.txt
   ```

6. **Sonuçları Başka Bir Dosyaya Yazma:**
   Sıralanmış çıktıyı yeni bir dosyaya kaydetmek için:
   ```bash
   sort dosya.txt -o sirali_dosya.txt
   ```

## İpuçları
- Sıralama işlemlerini hızlandırmak için büyük dosyalarla çalışırken `-S` seçeneği ile bellek kullanımını ayarlayabilirsiniz.
- Sıralama işlemlerinin sonuçlarını görmek için `-n` ve `-k` seçeneklerini birleştirerek karmaşık sıralamalar yapabilirsiniz.
- `sort` komutunu diğer komutlarla birleştirerek daha karmaşık veri işleme işlemleri gerçekleştirebilirsiniz, örneğin `cat dosya.txt | sort | uniq`.