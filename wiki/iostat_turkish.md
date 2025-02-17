# [Linux] Bash iostat Kullanımı: Sistem Giriş/Çıkış İstatistiklerini Görüntüleme

## Genel Bakış
`iostat` komutu, sistemin giriş/çıkış (I/O) istatistiklerini görüntülemek için kullanılır. Bu komut, disklerin ve diğer I/O aygıtlarının performansını izlemek ve analiz etmek için faydalıdır. Ayrıca, CPU kullanımını da raporlayarak sistemin genel durumunu değerlendirmeye yardımcı olur.

## Kullanım
Temel sözdizimi şu şekildedir:
```
iostat [seçenekler] [argümanlar]
```

## Yaygın Seçenekler
- `-c`: Sadece CPU istatistiklerini gösterir.
- `-d`: Sadece disk istatistiklerini gösterir.
- `-x`: Genişletilmiş disk istatistiklerini gösterir.
- `-h`: İnsan tarafından okunabilir formatta çıktı verir.
- `interval`: İstatistiklerin güncellenme süresini belirler (saniye cinsinden).
- `count`: Belirtilen sayıda güncelleme yapar.

## Yaygın Örnekler
1. **Temel İstatistikleri Görüntüleme**
   ```bash
   iostat
   ```

2. **CPU İstatistiklerini Gösterme**
   ```bash
   iostat -c
   ```

3. **Disk İstatistiklerini Görüntüleme**
   ```bash
   iostat -d
   ```

4. **Genişletilmiş Disk İstatistikleri ile Birlikte Görüntüleme**
   ```bash
   iostat -x
   ```

5. **Her 5 Saniyede Bir Güncellenen İstatistikler**
   ```bash
   iostat 5
   ```

6. **10 Saniyede Bir 3 Kez Güncellenen Disk İstatistikleri**
   ```bash
   iostat -d 10 3
   ```

## İpuçları
- `iostat` çıktısını analiz ederken, yüksek `await` ve `svctm` değerlerinin disk performans sorunlarına işaret edebileceğini unutmayın.
- Uzun süreli izleme için `iostat` komutunu bir betik içinde kullanarak belirli aralıklarla verileri kaydedebilirsiniz.
- Çıktıyı daha iyi anlamak için `-h` seçeneğini kullanarak insan tarafından okunabilir formatta görüntüleyin.