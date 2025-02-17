# [Linux] Bash wget Kullanımı: Dosya indirme aracı

## Genel Bakış
`wget`, web üzerinden dosya indirmek için kullanılan güçlü bir komut satırı aracıdır. HTTP, HTTPS ve FTP protokollerini destekler ve kullanıcıların dosyaları kolayca indirmesine olanak tanır.

## Kullanım
Temel sözdizimi şu şekildedir:

```bash
wget [seçenekler] [argümanlar]
```

## Yaygın Seçenekler
- `-O [dosya_adı]`: İndirilen dosyayı belirtilen adla kaydeder.
- `-c`: Kesilen indirmeleri devam ettirir.
- `-q`: Sessiz modda çalışır, yalnızca hata mesajlarını gösterir.
- `--limit-rate=[hız]`: İndirme hızını sınırlar.
- `-r`: Dizinleri ve alt dizinleri rekürsif olarak indirir.

## Yaygın Örnekler
1. Basit bir dosya indirme:
   ```bash
   wget https://example.com/dosya.zip
   ```

2. İndirilen dosyayı farklı bir adla kaydetme:
   ```bash
   wget -O yeni_dosya.zip https://example.com/dosya.zip
   ```

3. Kesilen bir indirmeyi devam ettirme:
   ```bash
   wget -c https://example.com/büyük_dosya.zip
   ```

4. İndirme hızını sınırlandırma:
   ```bash
   wget --limit-rate=200k https://example.com/dosya.zip
   ```

5. Bir web sitesinin tüm içeriğini indirme (rekürsif):
   ```bash
   wget -r https://example.com/
   ```

## İpuçları
- İndirme işlemlerini arka planda gerçekleştirmek için `-b` seçeneğini kullanabilirsiniz.
- İndirme işlemlerini zamanlamak için `cron` ile birlikte kullanabilirsiniz.
- `wget` ile indirdiğiniz dosyaların bütünlüğünü kontrol etmek için `--no-check-certificate` seçeneğini kullanabilirsiniz. Bu, SSL sertifikası hatalarını göz ardı eder.