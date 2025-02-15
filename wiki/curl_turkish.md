# [리눅스] Bash curl 사용법

## Genel Bakış
`curl`, URL'ler üzerinden veri transferi yapmak için kullanılan bir komut satırı aracıdır. HTTP, HTTPS, FTP ve daha birçok protokolü destekler. Geliştiriciler ve mühendisler için, API'lerle etkileşimde bulunmak, dosya indirmek veya yüklemek gibi işlemleri kolaylaştırır. `curl`, ağ üzerinde veri alışverişi yaparken esneklik ve kontrol sağlar.

## Kullanım
Temel `curl` komutunun sözdizimi aşağıdaki gibidir:

```bash
curl [seçenekler] [URL]
```

### Yaygın Seçenekler
- `-X, --request`: Belirli bir HTTP isteği türünü belirtir (GET, POST, PUT, DELETE vb.).
- `-d, --data`: İstekle birlikte gönderilecek veriyi belirtir. Genellikle POST istekleri için kullanılır.
- `-H, --header`: İsteğe özel başlıklar eklemek için kullanılır.
- `-o, --output`: İndirilen verinin kaydedileceği dosya adını belirtir.
- `-I, --head`: Sadece HTTP başlıklarını almak için kullanılır.
- `-L, --location`: Yönlendirmeleri takip eder.

## Örnekler

### Örnek 1: Basit GET İsteği
Aşağıdaki komut, belirtilen URL'den veri almak için bir GET isteği gönderir:

```bash
curl https://api.example.com/data
```

### Örnek 2: POST İsteği ile Veri Gönderme
Aşağıdaki komut, bir API'ye JSON formatında veri göndermek için POST isteği yapar:

```bash
curl -X POST -H "Content-Type: application/json" -d '{"key":"value"}' https://api.example.com/submit
```

## İpuçları
- `curl` komutunu kullanırken, `-v` seçeneğini ekleyerek isteğin detaylı bir çıktısını alabilirsiniz. Bu, hata ayıklama için faydalıdır.
- API anahtarları veya hassas bilgileri komut satırında doğrudan yazmak yerine, çevresel değişkenler kullanarak güvenliğinizi artırabilirsiniz.
- İndirilen dosyaların kaydedilmesi için `-o` seçeneğini kullanarak dosya adını belirlemek, dosyaların karışmasını önler.
- `curl` ile birlikte `jq` gibi araçlar kullanarak JSON verilerini işlemek, çıktıyı daha okunabilir hale getirebilir.