# [리눅스] Bash htop 사용법

## Genel Bakış
`htop`, Linux sistemlerinde çalışan bir etkileşimli süreç görüntüleyicisidir. `top` komutunun daha gelişmiş bir versiyonu olarak düşünülebilir. Kullanıcıların sistemdeki işlemleri, bellek ve CPU kullanımını gerçek zamanlı olarak izlemesine olanak tanır. `htop`, kullanıcı dostu bir arayüze sahip olup, süreçleri kolayca yönetme ve sıralama imkanı sunar.

## Kullanım
Temel `htop` komutunun sözdizimi oldukça basittir:

```bash
htop [seçenekler]
```

### Yaygın Seçenekler
- `-d, --delay`: Güncelleme aralığını (saniye cinsinden) ayarlamak için kullanılır.
- `-u, --user`: Belirli bir kullanıcıya ait süreçleri görüntülemek için kullanılır.
- `-p, --pid`: Belirli bir süreç kimliğine (PID) ait bilgileri görüntülemek için kullanılır.
- `--sort-key`: Görüntüleme sırasını belirlemek için kullanılır (örneğin, CPU veya bellek kullanımı).

## Örnekler
### Örnek 1: Temel Kullanım
`htop` komutunu terminalde çalıştırarak sistemdeki tüm süreçleri görüntüleyebilirsiniz:

```bash
htop
```

### Örnek 2: Belirli Bir Kullanıcıya Ait Süreçleri Görüntüleme
Belirli bir kullanıcıya ait süreçleri görüntülemek için `-u` seçeneğini kullanabilirsiniz. Örneğin, "kullaniciadi" adlı kullanıcının süreçlerini görmek için:

```bash
htop -u kullaniciadi
```

## İpuçları
- `htop` arayüzünde, süreçleri seçip `F9` tuşuna basarak sonlandırabilirsiniz.
- Arama yapmak için `F3` tuşunu kullanarak belirli bir süreci hızlıca bulabilirsiniz.
- `htop`'u daha verimli kullanmak için, sıralama seçeneklerini değiştirerek (örneğin, CPU veya bellek kullanımına göre) süreçleri analiz edebilirsiniz.
- Renkli arayüzü sayesinde, kaynak kullanımını hızlı bir şekilde değerlendirebilirsiniz.