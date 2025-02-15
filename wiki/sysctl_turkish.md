# [리눅스] Bash sysctl 사용법

## Genel Bakış
`sysctl`, Linux ve diğer Unix benzeri işletim sistemlerinde çekirdek parametrelerini ve ayarlarını yönetmek için kullanılan bir komuttur. Bu komut, sistem yöneticilerinin ve geliştiricilerin çekirdek yapılandırmalarını dinamik olarak değiştirmelerine olanak tanır. `sysctl`, sistemin çalışma zamanında performansını ve davranışını optimize etmek için kritik öneme sahiptir.

## Kullanım
`sysctl` komutunun temel sözdizimi aşağıdaki gibidir:

```bash
sysctl [seçenekler] [parametre]
```

### Yaygın Seçenekler
- `-a` veya `--all`: Tüm çekirdek parametrelerini ve mevcut değerlerini listelemek için kullanılır.
- `-n`: Parametre değerlerini yalnızca değerleriyle birlikte gösterir, anahtarları göstermez.
- `-w`: Çekirdek parametrelerini değiştirmek için kullanılır. Örneğin, `sysctl -w parametre=değer`.

## Örnekler
### Örnek 1: Tüm Çekirdek Parametrelerini Listeleme
Aşağıdaki komut, sistemdeki tüm çekirdek parametrelerini ve mevcut değerlerini listeleyecektir:

```bash
sysctl -a
```

### Örnek 2: Çekirdek Parametresini Değiştirme
Aşağıdaki komut, `vm.swappiness` parametresini 10 olarak ayarlayacaktır. Bu parametre, sistemin bellek yönetimi davranışını etkiler.

```bash
sysctl -w vm.swappiness=10
```

## İpuçları
- Çekirdek parametrelerini değiştirmeden önce mevcut değerleri not almak iyi bir uygulamadır. Bu, gerektiğinde geri dönmenizi kolaylaştırır.
- Değişikliklerin kalıcı olmasını istiyorsanız, `/etc/sysctl.conf` dosyasına parametreleri eklemeyi unutmayın. Bu dosya, sistem her başlatıldığında `sysctl` tarafından okunur.
- `sysctl` komutunu kullanırken dikkatli olun; bazı parametrelerin yanlış ayarlanması sistemin kararlılığını etkileyebilir.