# [Linux] Bash g++ Kullanımı: C++ programlarını derlemek için kullanılan bir araç

## Genel Bakış
g++ komutu, C++ programlarını derlemek için kullanılan bir derleyicidir. GNU Compiler Collection (GCC) içinde yer alır ve C++ kodunu makine diline çevirerek çalıştırılabilir dosyalar oluşturur.

## Kullanım
g++ komutunun temel sözdizimi aşağıdaki gibidir:

```bash
g++ [seçenekler] [argümanlar]
```

## Yaygın Seçenekler
- `-o <dosya_adı>`: Oluşturulan çıktının adını belirler.
- `-Wall`: Tüm uyarıları etkinleştirir.
- `-g`: Hata ayıklama bilgilerini ekler.
- `-std=<standart>`: Kullanılacak C++ standartını belirtir (örneğin, `-std=c++11`).
- `-I<klasör>`: Ek başlık dosyalarının bulunduğu dizini belirtir.

## Yaygın Örnekler
Aşağıda g++ komutunun bazı pratik kullanımları verilmiştir:

1. Basit bir C++ dosyasını derlemek:
   ```bash
   g++ program.cpp
   ```

2. Çıktı dosyasının adını belirlemek:
   ```bash
   g++ program.cpp -o program
   ```

3. Hata ayıklama bilgileri ile derlemek:
   ```bash
   g++ -g program.cpp -o program
   ```

4. Belirli bir C++ standardı kullanarak derlemek:
   ```bash
   g++ -std=c++11 program.cpp -o program
   ```

5. Birden fazla dosyayı derlemek:
   ```bash
   g++ dosya1.cpp dosya2.cpp -o program
   ```

## İpuçları
- Derleme sırasında uyarıları görmek için `-Wall` seçeneğini kullanmayı unutmayın.
- Hata ayıklama yapacaksanız `-g` seçeneğini ekleyin.
- Projelerinizde başlık dosyalarını düzenli tutmak için `-I` seçeneği ile dizinleri belirtin.
- Derleme işlemi sırasında performansı artırmak için optimizasyon seçeneklerini kullanabilirsiniz, örneğin `-O2`.