# [Linux] Bash yes Kullanımı: Sürekli "evet" yanıtı verme

## Genel Bakış
`yes` komutu, belirli bir metni sürekli olarak ekrana yazdırmak için kullanılır. Genellikle, bir komutun otomatik olarak "evet" yanıtını alması gerektiğinde kullanılır. Bu, etkileşimli komutların otomatikleştirilmesine yardımcı olur.

## Kullanım
Temel sözdizimi şu şekildedir:

```bash
yes [seçenekler] [argümanlar]
```

## Yaygın Seçenekler
- `-n`: Belirtilen metni yazdırır. Varsayılan olarak "y" veya "evet" yazdırılır.
- `--help`: Komut hakkında yardım bilgisi gösterir.
- `--version`: Komutun sürüm bilgisini gösterir.

## Yaygın Örnekler
Aşağıda `yes` komutunun bazı pratik örnekleri bulunmaktadır:

1. Sürekli "evet" yazdırmak:
   ```bash
   yes
   ```

2. Sürekli "hayır" yazdırmak:
   ```bash
   yes no
   ```

3. Bir dosyaya sürekli "evet" yazdırmak:
   ```bash
   yes | head -n 10 > evet.txt
   ```

4. Bir komutun otomatik olarak "evet" yanıtı alması:
   ```bash
   yes | rm -i *.txt
   ```

## İpuçları
- `yes` komutunu kullanırken dikkatli olun, çünkü sonsuz döngü oluşturabilir.
- Çıktıyı sınırlamak için `head` veya `tail` komutları ile birleştirin.
- Otomatik yanıt vermek istediğiniz komutları dikkatlice seçin, aksi takdirde istenmeyen sonuçlar doğurabilir.