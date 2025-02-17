# [Linux] Bash komutu cp: [dosya kopyalama]

## Genel Bakış
`cp` komutu, Linux ve diğer Unix benzeri işletim sistemlerinde dosyaları ve dizinleri kopyalamak için kullanılır. Bu komut, kaynak dosyaları hedef konuma kopyalayarak yeni dosyalar oluşturur.

## Kullanım
Temel sözdizimi şu şekildedir:

```
cp [seçenekler] [kaynak] [hedef]
```

## Yaygın Seçenekler
- `-r`: Dizinleri ve içindeki dosyaları kopyalamak için kullanılır. (recursive)
- `-i`: Hedef dosya mevcutsa, üzerine yazmadan önce kullanıcıdan onay ister. (interactive)
- `-u`: Sadece kaynak dosya hedef dosyadan daha yeni ise kopyalama yapar. (update)
- `-v`: Kopyalama işlemi sırasında hangi dosyaların kopyalandığını gösterir. (verbose)

## Yaygın Örnekler
1. Basit bir dosya kopyalama:
   ```bash
   cp dosya.txt yedek_dosya.txt
   ```

2. Bir dizini ve içindeki tüm dosyaları kopyalama:
   ```bash
   cp -r dizin_adi/ yedek_dizin/
   ```

3. Kullanıcıdan onay alarak dosya kopyalama:
   ```bash
   cp -i dosya.txt yedek_dosya.txt
   ```

4. Sadece daha yeni dosyaları kopyalama:
   ```bash
   cp -u dosya.txt yedek_dosya.txt
   ```

5. Kopyalama işlemi sırasında hangi dosyaların kopyalandığını gösterme:
   ```bash
   cp -v dosya.txt yedek_dosya.txt
   ```

## İpuçları
- Kopyalama işlemi sırasında dosya adlarını dikkatlice kontrol edin, yanlışlıkla mevcut dosyaların üzerine yazmamak için `-i` seçeneğini kullanın.
- Büyük dizinleri kopyalarken `-v` seçeneği ile hangi dosyaların kopyalandığını takip edebilirsiniz.
- Kopyalama işlemi sonrasında hedef dizinde dosyaların doğru bir şekilde kopyalandığını kontrol etmek için `ls` komutunu kullanabilirsiniz.