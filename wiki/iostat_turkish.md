# [리눅스] Bash iostat 사용법

## Genel Bakış
`iostat`, sistemin giriş/çıkış (I/O) istatistiklerini izlemek için kullanılan bir komuttur. Bu komut, CPU kullanımını ve disk I/O istatistiklerini göstererek, sistem performansını analiz etmeye yardımcı olur. Özellikle, sistem yöneticileri ve geliştiriciler için, uygulamaların ve disklerin performansını değerlendirmek amacıyla kritik bir araçtır.

## Kullanım
`iostat` komutunun temel sözdizimi aşağıdaki gibidir:

```bash
iostat [seçenekler] [interval] [count]
```

### Yaygın Seçenekler
- `-c`: Sadece CPU istatistiklerini gösterir.
- `-d`: Sadece disk istatistiklerini gösterir.
- `-x`: Genişletilmiş disk istatistiklerini gösterir.
- `-m`: Çıktıyı megabayt cinsinden gösterir.
- `interval`: İstatistiklerin ne sıklıkla güncelleneceğini belirten süre (saniye cinsinden).
- `count`: İstatistiklerin kaç kez gösterileceğini belirtir.

## Örnekler

### Örnek 1: Temel Kullanım
Aşağıdaki komut, her 2 saniyede bir CPU ve disk istatistiklerini gösterir:

```bash
iostat 2
```

### Örnek 2: Genişletilmiş Disk İstatistikleri
Aşağıdaki komut, her 5 saniyede bir genişletilmiş disk istatistiklerini gösterir:

```bash
iostat -x 5
```

## İpuçları
- `iostat` çıktısını analiz ederken, yüksek `iowait` değerlerinin sistem performansında dar boğazlara işaret edebileceğini unutmayın.
- Disklerin performansını izlemek için `-x` seçeneğini kullanarak daha ayrıntılı bilgi alabilirsiniz.
- Uzun süreli izleme için, `iostat` çıktısını bir dosyaya yönlendirebilir ve daha sonra analiz edebilirsiniz:

```bash
iostat -x 5 > iostat_output.txt
```

Bu komut, her 5 saniyede bir genişletilmiş disk istatistiklerini `iostat_output.txt` dosyasına kaydeder.