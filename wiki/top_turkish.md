# [리눅스] Bash top 사용법

## Overview
`top` komutu, Linux ve Unix benzeri işletim sistemlerinde çalışan bir komuttur. Bu komut, sistemdeki işlemci ve bellek kullanımını gerçek zamanlı olarak izlemek için kullanılır. Kullanıcıya, sistemdeki en aktif süreçlerin ve kaynak kullanımının anlık bir görünümünü sunarak, sistem performansını değerlendirmeye yardımcı olur. `top`, sistem yöneticileri ve geliştiriciler için kritik bir araçtır, çünkü sistemdeki darboğazları ve performans sorunlarını hızlı bir şekilde tespit etmeye olanak tanır.

## Usage
`top` komutunun temel sözdizimi oldukça basittir:

```bash
top [options]
```

### Yaygın Seçenekler
- `-d <saniye>`: Güncelleme aralığını saniye cinsinden ayarlamak için kullanılır. Örneğin, `-d 2` ile her 2 saniyede bir güncelleme yapılır.
- `-u <kullanıcı>`: Belirli bir kullanıcıya ait süreçleri görüntülemek için kullanılır. Örneğin, `-u john` ile sadece "john" kullanıcısına ait süreçler gösterilir.
- `-p <PID>`: Belirli bir işlem kimliğine (PID) sahip süreçleri izlemek için kullanılır. Örneğin, `-p 1234` ile PID'si 1234 olan süreç izlenir.

## Examples
### Örnek 1: Temel Kullanım
Aşağıdaki komut, `top` aracını varsayılan ayarlarla başlatır ve sistemdeki tüm süreçleri gerçek zamanlı olarak gösterir:

```bash
top
```

### Örnek 2: Güncelleme Aralığını Ayarlama
Aşağıdaki komut, güncelleme aralığını 3 saniye olarak ayarlayarak `top` komutunu çalıştırır:

```bash
top -d 3
```

### Örnek 3: Belirli Bir Kullanıcının Süreçlerini Görüntüleme
Aşağıdaki komut, sadece "alice" kullanıcısına ait süreçleri görüntüler:

```bash
top -u alice
```

## Tips
- `top` arayüzünde, süreçleri sıralamak için `Shift + M` (bellek kullanımına göre) veya `Shift + P` (CPU kullanımına göre) tuşlarına basabilirsiniz.
- `top` komutunu durdurmak için `q` tuşuna basmanız yeterlidir.
- Daha fazla bilgi ve yardım için `man top` komutunu kullanarak `top` komutunun kılavuz sayfasını görüntüleyebilirsiniz.
- `top` çıktısını bir dosyaya kaydetmek için `top -b -n 1 > output.txt` komutunu kullanabilirsiniz. Bu, `top` çıktısını bir kez alır ve "output.txt" dosyasına yazar.