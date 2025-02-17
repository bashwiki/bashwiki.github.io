# [Linux] Bash dd Kullanımı: Verileri kopyalamak ve dönüştürmek

## Overview
`dd` komutu, Unix benzeri işletim sistemlerinde verileri kopyalamak ve dönüştürmek için kullanılan güçlü bir araçtır. Genellikle disk imajları oluşturmak, verileri yedeklemek veya belirli bir biçimde dönüştürmek için kullanılır.

## Usage
Temel sözdizimi aşağıdaki gibidir:
```bash
dd [options] [arguments]
```

## Common Options
- `if=`: Giriş dosyasını belirtir. (Input file)
- `of=`: Çıkış dosyasını belirtir. (Output file)
- `bs=`: Blok boyutunu belirtir. (Block size)
- `count=`: Kopyalanacak blok sayısını belirtir.
- `skip=`: Giriş dosyasından atlanacak blok sayısını belirtir.
- `seek=`: Çıkış dosyasına atlanacak blok sayısını belirtir.

## Common Examples
- Bir dosyayı başka bir dosyaya kopyalamak:
```bash
dd if=source.txt of=destination.txt
```

- Bir disk imajı oluşturmak:
```bash
dd if=/dev/sda of=/path/to/disk.img bs=4M
```

- Disk imajını geri yüklemek:
```bash
dd if=/path/to/disk.img of=/dev/sda bs=4M
```

- Belirli bir boyutta veri kopyalamak (örneğin, ilk 100 blok):
```bash
dd if=source.txt of=destination.txt count=100
```

## Tips
- `dd` komutunu kullanmadan önce, özellikle disklerle çalışırken dikkatli olun; yanlış bir hedef belirlemek veri kaybına neden olabilir.
- İşlemin ilerlemesini görmek için `status=progress` seçeneğini ekleyebilirsiniz:
```bash
dd if=/dev/sda of=/path/to/disk.img bs=4M status=progress
```
- Blok boyutunu ayarlamak, performansı artırabilir; genellikle 4M veya 1M gibi daha büyük değerler kullanmak daha hızlı sonuçlar verebilir.