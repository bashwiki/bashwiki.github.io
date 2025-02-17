# [Linux] Bash tar Kullanımı: Arşiv dosyası oluşturma ve çıkarma

## Genel Bakış
`tar` komutu, dosyaları bir arşiv dosyasında toplamak ve bu arşiv dosyalarını çıkarmak için kullanılan bir araçtır. Genellikle yedekleme ve dosya transferi işlemlerinde kullanılır. `tar`, "tape archive" kelimelerinin kısaltmasıdır ve başlangıçta manyetik bantlarda veri saklamak için geliştirilmiştir.

## Kullanım
Temel sözdizimi aşağıdaki gibidir:

```bash
tar [seçenekler] [argümanlar]
```

## Yaygın Seçenekler
- `-c`: Yeni bir arşiv oluşturur.
- `-x`: Var olan bir arşivi çıkarır.
- `-f`: Arşiv dosyasının adını belirtir.
- `-v`: İşlem sırasında ayrıntılı çıktı verir (verbose).
- `-z`: Arşivi gzip ile sıkıştırır veya çıkarır.
- `-j`: Arşivi bzip2 ile sıkıştırır veya çıkarır.

## Yaygın Örnekler
1. **Yeni bir arşiv oluşturma:**
   ```bash
   tar -cvf arşiv.tar dosya1.txt dosya2.txt
   ```
   Bu komut, `dosya1.txt` ve `dosya2.txt` dosyalarını `arşiv.tar` adlı bir arşiv dosyasında toplar.

2. **Arşivi gzip ile sıkıştırma:**
   ```bash
   tar -czvf arşiv.tar.gz dosya1.txt dosya2.txt
   ```
   Bu komut, belirtilen dosyaları gzip ile sıkıştırarak `arşiv.tar.gz` oluşturur.

3. **Arşivi çıkarma:**
   ```bash
   tar -xvf arşiv.tar
   ```
   Bu komut, `arşiv.tar` dosyasını çıkartır ve içindeki dosyaları mevcut dizine yerleştirir.

4. **Sıkıştırılmış arşivi çıkarma:**
   ```bash
   tar -xzvf arşiv.tar.gz
   ```
   Bu komut, gzip ile sıkıştırılmış `arşiv.tar.gz` dosyasını çıkarır.

## İpuçları
- Arşiv dosyalarını oluştururken, dosya isimlerini tam yol ile belirtmek, karışıklığı önleyebilir.
- `-v` seçeneğini kullanarak, hangi dosyaların işlendiğini görebilirsiniz; bu, büyük arşivlerde faydalı olabilir.
- Arşiv dosyalarını sıkıştırmak, disk alanından tasarruf sağlar, ancak sıkıştırma işlemi zaman alabilir. Bu nedenle, sıkıştırma ihtiyacını değerlendirin.