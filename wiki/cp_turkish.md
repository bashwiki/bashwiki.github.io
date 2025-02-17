# [Linux] Bash cp Kullanımı: Dosya kopyalama komutu

## Genel Bakış
`cp` komutu, Linux ve diğer Unix benzeri işletim sistemlerinde dosya ve dizinleri kopyalamak için kullanılır. Bu komut, kaynak dosyayı veya dizini belirtilen hedef konuma kopyalar.

## Kullanım
Temel sözdizimi şu şekildedir:
```bash
cp [seçenekler] [argümanlar]
```

## Yaygın Seçenekler
- `-r`: Dizinleri ve içindeki dosyaları kopyalamak için kullanılır (rekürsif).
- `-i`: Hedef dosya mevcutsa, üzerine yazmadan önce onay ister.
- `-u`: Sadece kaynak dosya, hedef dosyadan daha yeni ise kopyalar.
- `-v`: Kopyalama işlemi sırasında hangi dosyaların kopyalandığını gösterir (ayrıntılı).
- `-a`: Dosyaları ve dizinleri, tüm özellikleriyle birlikte kopyalar (arka plan ve izinler dahil).

## Yaygın Örnekler
Aşağıda `cp` komutunun bazı pratik örnekleri bulunmaktadır:

1. Basit bir dosya kopyalama:
   ```bash
   cp dosya.txt yedek_dosya.txt
   ```

2. Bir dizini ve içindeki tüm dosyaları kopyalama:
   ```bash
   cp -r dizin_adi/ yedek_dizin/
   ```

3. Hedef dosya mevcutsa onay isteme:
   ```bash
   cp -i dosya.txt yedek_dosya.txt
   ```

4. Sadece daha yeni dosyaları kopyalama:
   ```bash
   cp -u dosya.txt yedek_dosya.txt
   ```

5. Kopyalama işlemini ayrıntılı olarak gösterme:
   ```bash
   cp -v dosya.txt yedek_dosya.txt
   ```

## İpuçları
- Kopyalama işlemi sırasında dosya izinlerini korumak için `-a` seçeneğini kullanın.
- Dizin kopyalarken `-r` seçeneğini unutmayın; aksi takdirde yalnızca dosyalar kopyalanır.
- Kopyalama işlemi yapmadan önce, hedef dosyanın üzerine yazılmasını istemiyorsanız `-i` seçeneğini kullanarak güvenliğinizi artırabilirsiniz.