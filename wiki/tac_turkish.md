# [Linux] Bash tac Kullanımı: Dosyaları Tersine Görüntüleme

## Genel Bakış
`tac` komutu, bir dosyanın içeriğini ters sırayla görüntülemek için kullanılır. Bu komut, "cat" komutunun tersidir; yani, dosya içeriğini son satırdan ilk satıra doğru okur ve çıktısını verir.

## Kullanım
Temel sözdizimi aşağıdaki gibidir:

```bash
tac [seçenekler] [argümanlar]
```

## Yaygın Seçenekler
- `-b`: Boş satırları korur.
- `-s`: Satırları ayırmak için özel bir ayırıcı belirtir.
- `-r`: Satırları ters sırada okur ve çıktıyı verir.

## Yaygın Örnekler
Aşağıda `tac` komutunun bazı pratik örnekleri bulunmaktadır:

1. **Bir dosyanın içeriğini ters sırayla görüntüleme:**
   ```bash
   tac dosya.txt
   ```

2. **Birden fazla dosyanın içeriğini ters sırayla görüntüleme:**
   ```bash
   tac dosya1.txt dosya2.txt
   ```

3. **Boş satırları koruyarak bir dosyanın içeriğini ters sırayla görüntüleme:**
   ```bash
   tac -b dosya.txt
   ```

4. **Özel bir ayırıcı kullanarak ters sırayla görüntüleme:**
   ```bash
   tac -s ',' dosya.csv
   ```

## İpuçları
- `tac` komutunu `grep` veya `sort` gibi diğer komutlarla birleştirerek daha karmaşık işlemler gerçekleştirebilirsiniz.
- Çıktıyı bir dosyaya yönlendirmek için `>` operatörünü kullanabilirsiniz:
  ```bash
  tac dosya.txt > ters_dosya.txt
  ```
- Büyük dosyalarla çalışırken, `tac` komutunun performansını göz önünde bulundurun; gerektiğinde daha küçük parçalara bölmek faydalı olabilir.