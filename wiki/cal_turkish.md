# [Linux] Bash cal Kullanımı: Takvim görüntüleme komutu

## Overview
`cal` komutu, belirli bir ay veya yıl için takvim görüntülemek amacıyla kullanılan bir Bash komutudur. Kullanıcılar, bu komut sayesinde geçmiş veya gelecek tarihlere ait takvimleri kolayca görüntüleyebilir.

## Usage
Temel sözdizimi aşağıdaki gibidir:

```bash
cal [seçenekler] [argümanlar]
```

## Common Options
- `-m`: Ayın ilk gününü haftanın ortasında gösterir.
- `-y`: Tüm yılı gösterir.
- `-3`: Mevcut ay, önceki ay ve sonraki ayı aynı anda gösterir.
- `-j`: Yılın gün numaralarını gösterir.
- `-A [n]`: Mevcut aydan sonra `n` ayı gösterir.
- `-B [n]`: Mevcut aydan önce `n` ayı gösterir.

## Common Examples
Aşağıda `cal` komutunun bazı yaygın kullanım örnekleri bulunmaktadır:

1. Mevcut ayın takvimini görüntülemek için:
   ```bash
   cal
   ```

2. Belirli bir ay ve yıl için takvim görüntülemek için (örneğin, Eylül 2023):
   ```bash
   cal 09 2023
   ```

3. Tüm yılı görüntülemek için:
   ```bash
   cal -y 2023
   ```

4. Mevcut ay ile birlikte önceki ve sonraki ayları görüntülemek için:
   ```bash
   cal -3
   ```

5. Yılın gün numaralarını gösteren takvim için:
   ```bash
   cal -j
   ```

## Tips
- `cal` komutunu sıkça kullanıyorsanız, belirli bir ay veya yıl için takvim görüntülemek için bir alias oluşturabilirsiniz.
- Takvimdeki günleri daha iyi anlamak için `-m` seçeneğini kullanarak haftanın ortasında başlayabilirsiniz.
- Eğer birden fazla ayı aynı anda görmek istiyorsanız, `-A` ve `-B` seçeneklerini kullanarak geçmiş ve gelecek ayları kolayca görüntüleyebilirsiniz.