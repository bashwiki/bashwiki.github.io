# [Linux] Bash traceroute Kullanımı: Ağ yolunu izleme aracı

## Overview
`traceroute` komutu, bir ağ üzerindeki veri paketlerinin bir hedefe ulaşana kadar geçtiği yolları izlemek için kullanılır. Bu komut, ağ bağlantı sorunlarını teşhis etmek ve ağın performansını değerlendirmek için oldukça faydalıdır.

## Usage
Temel sözdizimi aşağıdaki gibidir:
```bash
traceroute [seçenekler] [hedef]
```

## Common Options
- `-m <sayı>`: Maksimum sıçrama sayısını belirler.
- `-n`: IP adreslerini çözümlemeden doğrudan gösterir.
- `-p <port>`: Hedefe gönderilecek UDP paketinin portunu belirtir.
- `-w <süre>`: Her bir yanıt için bekleme süresini ayarlar.

## Common Examples
Aşağıda `traceroute` komutunun bazı pratik örnekleri verilmiştir:

1. Basit bir traceroute:
   ```bash
   traceroute example.com
   ```

2. Maksimum 15 sıçrama ile traceroute:
   ```bash
   traceroute -m 15 example.com
   ```

3. IP adreslerini çözümlemeden gösterme:
   ```bash
   traceroute -n example.com
   ```

4. Belirli bir port üzerinden traceroute:
   ```bash
   traceroute -p 80 example.com
   ```

5. Yanıt süresi için 2 saniye bekleme:
   ```bash
   traceroute -w 2 example.com
   ```

## Tips
- `traceroute` komutunu çalıştırmadan önce, ağ bağlantınızın aktif olduğundan emin olun.
- Hedefin IP adresini kullanarak daha hızlı sonuçlar alabilirsiniz.
- Ağ sorunlarını teşhis etmek için, `traceroute` çıktısını dikkatlice inceleyin; kaybolan paketler veya yüksek gecikme süreleri sorunları gösterebilir.