# [Linux] Bash curl Kullanımı: HTTP istekleri yapmak için kullanılan bir araç

## Overview
`curl`, URL'ler üzerinden veri transferi yapmak için kullanılan bir komut satırı aracıdır. Genellikle HTTP, HTTPS, FTP gibi protokollerle çalışır ve web sunucularıyla etkileşimde bulunmak için yaygın olarak kullanılır.

## Usage
Temel kullanım şekli aşağıdaki gibidir:

```bash
curl [options] [arguments]
```

## Common Options
- `-X, --request <method>`: Belirtilen HTTP yöntemini kullanarak isteği gönderir (GET, POST, PUT, DELETE vb.).
- `-d, --data <data>`: İstekle birlikte gönderilecek veriyi belirtir. Genellikle POST istekleri için kullanılır.
- `-H, --header <header>`: İstekle birlikte gönderilecek özel başlıkları tanımlar.
- `-o, --output <file>`: İsteğin sonucunu belirtilen dosyaya kaydeder.
- `-I, --head`: Sadece HTTP başlıklarını almak için kullanılır.

## Common Examples
Aşağıda `curl` komutunun bazı yaygın kullanım örnekleri bulunmaktadır:

### Basit GET İsteği
Bir web sayfasını almak için:
```bash
curl https://www.example.com
```

### POST İsteği ile Veri Gönderme
Bir form verisi göndermek için:
```bash
curl -X POST -d "name=John&age=30" https://www.example.com/api
```

### Özel Başlık ile İstek Gönderme
Bir API'ye kimlik doğrulama başlığı ile istek göndermek için:
```bash
curl -H "Authorization: Bearer token" https://www.example.com/api/data
```

### Sonucu Dosyaya Kaydetme
Bir dosyayı indirmek için:
```bash
curl -o myfile.txt https://www.example.com/file.txt
```

### Sadece Başlıkları Alma
Bir URL'nin başlık bilgilerini almak için:
```bash
curl -I https://www.example.com
```

## Tips
- `curl` ile birlikte `-v` seçeneğini kullanarak isteğin ayrıntılı çıktısını görebilirsiniz. Bu, hata ayıklama için faydalıdır.
- HTTPS istekleri yaparken güvenlik sertifikalarını kontrol etmek için `-k` seçeneğini kullanabilirsiniz, ancak bu güvenlik riskleri taşıyabilir.
- İsteklerinizi kaydetmek ve tekrar kullanmak için bir komut dosyası oluşturmayı düşünebilirsiniz. Bu, işlemleri otomatikleştirmenize yardımcı olur.