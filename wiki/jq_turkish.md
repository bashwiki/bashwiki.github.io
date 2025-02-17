# [Linux] Bash jq Kullanımı: JSON verilerini işleme aracı

## Genel Bakış
`jq`, JSON verilerini işlemek ve analiz etmek için kullanılan güçlü bir komut satırı aracıdır. JSON formatındaki verileri kolayca filtreleme, dönüştürme ve biçimlendirme işlemleri yapmanıza olanak tanır.

## Kullanım
Temel sözdizimi şu şekildedir:
```bash
jq [seçenekler] [argümanlar]
```

## Yaygın Seçenekler
- `-c`: Çıktıyı sıkıştırılmış bir formatta gösterir.
- `-r`: Çıktıyı ham (raw) formatta verir, yani tırnak işaretleri olmadan.
- `-f`: Belirtilen bir dosyadaki jq ifadelerini kullanarak işlemi gerçekleştirir.
- `--arg`: Bir değişken tanımlamak için kullanılır.

## Yaygın Örnekler
Aşağıda `jq` komutunun bazı pratik kullanım örnekleri bulunmaktadır:

1. JSON dosyasındaki tüm verileri görüntüleme:
   ```bash
   jq . dosya.json
   ```

2. Belirli bir anahtara sahip verileri filtreleme:
   ```bash
   jq '.anahtar' dosya.json
   ```

3. Birden fazla anahtarı seçme:
   ```bash
   jq '{anahtar1, anahtar2}' dosya.json
   ```

4. JSON verisini sıkıştırılmış formatta yazdırma:
   ```bash
   jq -c . dosya.json
   ```

5. JSON verisinden belirli bir değeri ham formatta alma:
   ```bash
   jq -r '.anahtar.deger' dosya.json
   ```

## İpuçları
- JSON verilerinizi daha iyi anlamak için `jq` ile birlikte `less` veya `more` gibi sayfa kaydırma araçlarını kullanabilirsiniz.
- Karmaşık sorgular oluşturmak için `jq` ifadelerini bir dosyada saklayabilir ve `-f` seçeneği ile bu dosyayı kullanabilirsiniz.
- `jq` ile birlikte `curl` komutunu kullanarak API'den alınan JSON verilerini doğrudan işleyebilirsiniz. Örneğin:
  ```bash
  curl -s https://api.example.com/veri | jq '.'
  ```