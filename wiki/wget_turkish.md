# [리눅스] Bash wget 사용법

## Overview
`wget`, web üzerinden dosya indirmek için kullanılan bir komut satırı aracıdır. HTTP, HTTPS ve FTP protokollerini destekleyerek, kullanıcıların internetten dosya indirmesine olanak tanır. `wget`, özellikle büyük dosyaların veya birden fazla dosyanın indirilmesi gerektiğinde kullanışlıdır. Ayrıca, bağlantı kesildiğinde indirme işlemini devam ettirme yeteneği ile dikkat çeker.

## Usage
`wget` komutunun temel sözdizimi aşağıdaki gibidir:

```bash
wget [seçenekler] [URL]
```

### Yaygın Seçenekler
- `-O [dosya_adı]`: İndirilen dosyayı belirtilen isimle kaydeder.
- `-c`: Kesilen bir indirmeyi devam ettirir.
- `-r`: Belirtilen URL'den kaynakları (örneğin, HTML sayfaları ve bağlantılı dosyalar) rekürsif olarak indirir.
- `-q`: Sessiz modda çalışır, yalnızca hata mesajlarını gösterir.
- `--limit-rate=[hız]`: İndirme hızını sınırlamak için kullanılır (örneğin, `--limit-rate=200k`).

## Examples
### Örnek 1: Basit Dosya İndirme
Aşağıdaki komut, belirtilen URL'den bir dosya indirir:

```bash
wget https://example.com/dosya.zip
```

### Örnek 2: İndirmeyi Devam Ettirme
Eğer indirme işlemi kesildiyse, aşağıdaki komut ile kaldığı yerden devam edebilirsiniz:

```bash
wget -c https://example.com/buyuk_dosya.iso
```

## Tips
- İndirme işlemlerini daha verimli hale getirmek için `-q` seçeneğini kullanarak gereksiz çıktıları gizleyebilirsiniz.
- Birden fazla dosyayı indirmek için bir metin dosyası oluşturup, her bir URL'yi bu dosyaya yazdıktan sonra `-i [dosya_adı]` seçeneği ile bu dosyayı kullanabilirsiniz.
- İndirme hızını sınırlamak, ağ trafiğinizi yönetmek için faydalı olabilir, bu nedenle `--limit-rate` seçeneğini kullanmayı düşünün.