# [Linux] Bash lsusb Kullanımı: USB aygıtlarını listeleme

## Overview
`lsusb` komutu, sistemdeki USB aygıtlarını listelemek için kullanılır. Bu komut, bağlı olan USB cihazlarının bilgilerini gösterir ve kullanıcıların bu cihazlar hakkında bilgi edinmesine yardımcı olur.

## Usage
Temel sözdizimi aşağıdaki gibidir:
```bash
lsusb [options] [arguments]
```

## Common Options
- `-v`: Ayrıntılı bilgi gösterir. Her bir USB aygıtı hakkında daha fazla detay sağlar.
- `-t`: Aygıtların ağaç yapısını gösterir. USB aygıtlarının hiyerarşik yapısını görmenizi sağlar.
- `-s [bus]:[device]`: Belirli bir USB aygıtını hedeflemek için kullanılır. `[bus]` ve `[device]` numaralarını belirtmelisiniz.
- `-d [vendor]:[product]`: Belirli bir üretici ve ürün kimliğine sahip aygıtları listelemek için kullanılır.

## Common Examples
Aşağıda `lsusb` komutunun bazı yaygın kullanım örnekleri bulunmaktadır:

1. Tüm USB aygıtlarını listeleme:
   ```bash
   lsusb
   ```

2. Ayrıntılı bilgi ile listeleme:
   ```bash
   lsusb -v
   ```

3. Belirli bir USB aygıtını listeleme (örneğin, bus 001 ve device 002):
   ```bash
   lsusb -s 001:002
   ```

4. Belirli bir üretici ve ürün kimliğine sahip aygıtları listeleme (örneğin, 1234:5678):
   ```bash
   lsusb -d 1234:5678
   ```

5. Aygıtların ağaç yapısını gösterme:
   ```bash
   lsusb -t
   ```

## Tips
- `lsusb` komutunu `sudo` ile kullanarak daha fazla ayrıntı elde edebilirsiniz.
- USB aygıtlarının doğru çalışıp çalışmadığını kontrol etmek için `lsusb` komutunu düzenli olarak kullanın.
- Aygıtların bağlantı noktalarını ve durumlarını takip etmek için `lsusb` çıktısını bir dosyaya yönlendirebilirsiniz:
  ```bash
  lsusb > usb_devices.txt
  ```