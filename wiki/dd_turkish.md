# [리눅스] Bash dd 사용법

## Genel Bakış
`dd` komutu, Unix ve Unix benzeri işletim sistemlerinde kullanılan bir komuttur. Temel amacı, dosyaları ve disk bölümlerini düşük seviyede kopyalamak ve dönüştürmektir. `dd`, genellikle disk imajları oluşturmak, verileri yedeklemek veya taşımak ve veri dönüşümleri yapmak için kullanılır. Bu komut, özellikle sistem yöneticileri ve geliştiriciler için güçlü bir araçtır.

## Kullanım
`dd` komutunun temel sözdizimi aşağıdaki gibidir:

```bash
dd if=<girdi_dosyası> of=<çıktı_dosyası> [opsiyonlar]
```

Burada:
- `if` (input file): Kopyalanacak giriş dosyasını belirtir.
- `of` (output file): Kopyalanacak çıkış dosyasını belirtir.

### Yaygın Seçenekler
- `bs=<boyut>`: Blok boyutunu belirtir. Varsayılan blok boyutu 512 bayttır.
- `count=<adet>`: Kopyalanacak blok sayısını belirtir.
- `skip=<adet>`: Giriş dosyasından atlanacak blok sayısını belirtir.
- `seek=<adet>`: Çıkış dosyasına atlanacak blok sayısını belirtir.

## Örnekler

### Örnek 1: Disk İmajı Oluşturma
Bir disk bölümünün imajını oluşturmak için aşağıdaki komutu kullanabilirsiniz:

```bash
dd if=/dev/sda of=/path/to/disk_image.img bs=4M
```
Bu komut, `/dev/sda` disk bölümünün imajını `disk_image.img` dosyasına 4 MB'lık bloklarla kopyalar.

### Örnek 2: Disk İmajını Geri Yükleme
Daha önce oluşturduğunuz bir disk imajını geri yüklemek için şu komutu kullanabilirsiniz:

```bash
dd if=/path/to/disk_image.img of=/dev/sda bs=4M
```
Bu komut, `disk_image.img` dosyasını `/dev/sda` diskine geri yükler.

## İpuçları
- `dd` komutunu kullanmadan önce, özellikle disk işlemleri yaparken dikkatli olun. Yanlış bir `of` parametresi, verilerinizi kaybetmenize neden olabilir.
- İşlemin ilerlemesini görmek için `status=progress` seçeneğini ekleyebilirsiniz. Örneğin:

```bash
dd if=/dev/sda of=/path/to/disk_image.img bs=4M status=progress
```
- Büyük dosyalarla çalışırken, `conv=sync` seçeneğini kullanarak, eksik blokları sıfırlarla doldurabilirsiniz.

`dd` komutu, güçlü ve esnek bir araçtır, ancak dikkatli kullanılmalıdır. Doğru seçenekleri ve parametreleri kullanarak, veri yönetimini etkili bir şekilde gerçekleştirebilirsiniz.