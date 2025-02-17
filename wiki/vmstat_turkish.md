# [Linux] Bash vmstat Kullanımı: Sistem kaynaklarını izleme aracı

## Overview
`vmstat` komutu, sistemin bellek, işlemci ve diğer kaynaklarının durumunu izlemek için kullanılır. Bu komut, sistem performansını değerlendirmek ve sorunları teşhis etmek için yararlı bilgiler sağlar.

## Usage
Temel kullanım sözdizimi aşağıdaki gibidir:

```bash
vmstat [options] [arguments]
```

## Common Options
- `-a`: Tüm bellek alanlarını gösterir.
- `-m`: Bellek sayfalarının istatistiklerini gösterir.
- `-s`: Bellek istatistiklerini detaylı bir şekilde listeler.
- `-t`: Zaman damgası ekler.
- `interval`: Verilerin güncellenme sıklığını belirler (saniye cinsinden).

## Common Examples
Aşağıda `vmstat` komutunun bazı yaygın kullanım örnekleri bulunmaktadır:

1. **Temel kullanım:**
   ```bash
   vmstat
   ```

2. **Her 2 saniyede bir güncellenen sistem durumu:**
   ```bash
   vmstat 2
   ```

3. **Bellek istatistiklerini detaylı olarak gösterme:**
   ```bash
   vmstat -s
   ```

4. **Zaman damgası ile birlikte sistem durumu:**
   ```bash
   vmstat -t
   ```

5. **Tüm bellek alanlarını gösterme:**
   ```bash
   vmstat -a
   ```

## Tips
- `vmstat` çıktısını daha iyi anlamak için, çıktıyı bir dosyaya yönlendirebilir ve inceleyebilirsiniz.
- Uzun süreli izleme için, `vmstat` komutunu bir döngü içinde kullanarak belirli aralıklarla verileri toplayabilirsiniz.
- Performans sorunlarını teşhis etmek için `vmstat` çıktısını diğer sistem izleme araçlarıyla birlikte kullanmak faydalı olabilir.