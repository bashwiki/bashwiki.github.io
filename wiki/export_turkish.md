# [Linux] Bash export Kullanımı: Ortam değişkenlerini ayarlamak

## Genel Bakış
`export` komutu, bir ortam değişkenini tanımlamak ve bu değişkenin alt süreçlerde kullanılabilmesini sağlamak için kullanılır. Bu, özellikle bir shell oturumu boyunca değişkenlerin değerlerini korumak ve paylaşmak için önemlidir.

## Kullanım
Temel sözdizimi şu şekildedir:

```bash
export [seçenekler] [argümanlar]
```

## Yaygın Seçenekler
- `-n`: Belirtilen değişkeni export listesinden kaldırır.
- `-p`: Mevcut export edilmiş değişkenlerin listesini gösterir.

## Yaygın Örnekler

1. **Basit bir ortam değişkeni oluşturma:**
   ```bash
   export MY_VAR="Merhaba Dünya"
   ```

2. **Bir ortam değişkenini görüntüleme:**
   ```bash
   echo $MY_VAR
   ```

3. **Birden fazla değişkeni aynı anda export etme:**
   ```bash
   export VAR1="Değer1" VAR2="Değer2"
   ```

4. **Export edilmiş değişkenleri listeleme:**
   ```bash
   export -p
   ```

5. **Export edilmiş bir değişkeni kaldırma:**
   ```bash
   export -n MY_VAR
   ```

## İpuçları
- Ortam değişkenlerini ayarlarken, değişken adlarının büyük harfle başlamasına dikkat edin; bu, genellikle standart uygulama olarak kabul edilir.
- Değişkenlerinizi export ettikten sonra, alt süreçlerde kullanılabilir olduklarından emin olun.
- Değişkenlerinizi kontrol etmek için `env` veya `printenv` komutlarını kullanabilirsiniz.