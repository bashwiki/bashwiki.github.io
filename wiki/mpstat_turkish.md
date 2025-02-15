# [리눅스] Bash mpstat 사용법

## Genel Bakış
`mpstat`, çoklu işlemci sistemlerinde CPU kullanım istatistiklerini görüntülemek için kullanılan bir komuttur. Bu komut, her bir işlemcinin veya çekirdeğin yükünü izlemek ve analiz etmek için yararlıdır. Sistem yöneticileri ve geliştiriciler, sistem performansını değerlendirmek ve darboğazları tespit etmek amacıyla bu komutu kullanabilirler.

## Kullanım
`mpstat` komutunun temel sözdizimi aşağıdaki gibidir:

```bash
mpstat [seçenekler] [interval] [count]
```

### Yaygın Seçenekler
- `-P ALL`: Tüm işlemcilerin istatistiklerini gösterir.
- `-u`: CPU kullanım yüzdelerini gösterir (varsayılan olarak gösterilir).
- `-h`: Çıktıyı daha okunabilir hale getirir (kısa biçim).
- `interval`: İstatistiklerin gösterileceği süre (saniye cinsinden).
- `count`: İstatistiklerin kaç kez gösterileceği.

## Örnekler
### Örnek 1: Tüm İşlemcilerin İstatistiklerini Görüntüleme
Aşağıdaki komut, her 2 saniyede bir tüm işlemcilerin istatistiklerini gösterir:

```bash
mpstat -P ALL 2
```

### Örnek 2: Belirli Bir İşlemcinin Kullanımını İzleme
Sadece 0 numaralı işlemcinin kullanım istatistiklerini görüntülemek için şu komutu kullanabilirsiniz:

```bash
mpstat -P 0 1 5
```
Bu komut, 1 saniye aralıklarla 5 kez 0 numaralı işlemcinin istatistiklerini gösterir.

## İpuçları
- `mpstat` çıktısını daha iyi analiz edebilmek için, verileri bir dosyaya yönlendirebilir ve daha sonra bu dosyayı inceleyebilirsiniz. Örneğin:

```bash
mpstat -P ALL 2 > cpu_usage.txt
```

- Uzun süreli izleme yapıyorsanız, `interval` ve `count` değerlerini dikkatlice seçin. Çok sık aralıklarla veri toplamak, sistem kaynaklarını tüketebilir.
- `mpstat` çıktısında yer alan "idle" yüzdesi, işlemcinin ne kadar süreyle boşta kaldığını gösterir. Bu değer, sistemin genel performansı hakkında önemli bilgiler sunar.