# [리눅스] Bash lsusb 사용법

## Overview
`lsusb`, Linux işletim sistemlerinde USB aygıtlarının listesini görüntülemek için kullanılan bir komuttur. Bu komut, sistemde bağlı olan tüm USB aygıtlarını tanımlamak ve bu aygıtlar hakkında bilgi almak için kullanılır. Geliştiriciler ve mühendisler için, USB aygıtlarının durumunu kontrol etmek ve sorunları teşhis etmek açısından oldukça yararlıdır.

## Usage
`lsusb` komutunun temel sözdizimi aşağıdaki gibidir:

```bash
lsusb [options]
```

### Yaygın Seçenekler
- `-v`: Aygıtlar hakkında daha ayrıntılı bilgi görüntüler.
- `-t`: USB aygıtlarının ağaç yapısını gösterir.
- `-s [bus]:[device]`: Belirli bir USB aygıtını (bus ve device numarası ile) görüntüler.
- `-d [vendor]:[product]`: Belirli bir üretici ve ürün kimliğine sahip aygıtları listeler.

## Examples
### Örnek 1: Tüm USB Aygıtlarını Listeleme
Aşağıdaki komut, sistemde bağlı olan tüm USB aygıtlarını listeler:

```bash
lsusb
```

Çıktı, her bir USB aygıtının üretici ve ürün bilgilerini içerecektir.

### Örnek 2: Ayrıntılı Bilgi Alma
Aşağıdaki komut, sistemdeki USB aygıtları hakkında daha ayrıntılı bilgi sağlar:

```bash
lsusb -v
```

Bu komut, her bir aygıtın özellikleri, sınıfı, alt sınıfı ve daha fazlası hakkında detaylı bilgi sunar.

## Tips
- `lsusb` komutunu `grep` ile birleştirerek belirli bir aygıtı hızlıca bulabilirsiniz. Örneğin, bir USB belleği aramak için:

```bash
lsusb | grep 'USB Flash'
```

- Ayrıntılı bilgi almak için `-v` seçeneğini kullanırken, çıktının çok fazla bilgi içerebileceğini unutmayın. Bu nedenle, çıktıyı bir dosyaya yönlendirmek faydalı olabilir:

```bash
lsusb -v > usb_devices.txt
```

- `lsusb` komutunu sıkça kullanıyorsanız, kendi bash alias'ınızı oluşturmayı düşünebilirsiniz. Örneğin, `lsusb` komutunu daha kısa bir isimle çağırmak için `~/.bashrc` dosyanıza şu satırı ekleyebilirsiniz:

```bash
alias usb='lsusb'
```

Bu şekilde, `usb` yazarak hızlıca USB aygıtlarınızı listeleyebilirsiniz.