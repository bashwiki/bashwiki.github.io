# [Linux] Bash mknod Kullanımı: Özel dosya sistemleri oluşturma

## Genel Bakış
`mknod` komutu, özel dosya sistemleri oluşturmak için kullanılır. Bu komut, karakter ve blok aygıt dosyaları oluşturmanıza olanak tanır ve genellikle sistem yöneticileri tarafından donanım aygıtlarını temsil eden dosyalar oluşturmak için kullanılır.

## Kullanım
Temel sözdizimi aşağıdaki gibidir:

```bash
mknod [seçenekler] [argümanlar]
```

## Yaygın Seçenekler
- `-m, --mode`: Oluşturulan dosyanın izinlerini belirler.
- `-b, --block`: Blok aygıt dosyası oluşturur.
- `-c, --character`: Karakter aygıt dosyası oluşturur.

## Yaygın Örnekler
Aşağıda `mknod` komutunun bazı pratik örnekleri verilmiştir:

1. **Karakter aygıt dosyası oluşturma:**
   ```bash
   mknod /dev/mychar c 100 0
   ```
   Bu komut, `mychar` adında bir karakter aygıt dosyası oluşturur. `100` ana numara ve `0` alt numaradır.

2. **Blok aygıt dosyası oluşturma:**
   ```bash
   mknod /dev/myblock b 200 0
   ```
   Bu komut, `myblock` adında bir blok aygıt dosyası oluşturur. `200` ana numara ve `0` alt numaradır.

3. **Özel izinlerle dosya oluşturma:**
   ```bash
   mknod -m 660 /dev/mydevice c 300 0
   ```
   Bu komut, `mydevice` adında bir karakter aygıt dosyası oluşturur ve dosya izinlerini `660` olarak ayarlar.

## İpuçları
- `mknod` komutunu kullanmadan önce, hangi aygıt dosyasını oluşturmak istediğinizi ve gerekli ana ve alt numaraları belirlediğinizden emin olun.
- Özel dosya sistemleri genellikle kök (root) yetkileri gerektirir, bu nedenle komutu çalıştırırken `sudo` kullanmayı unutmayın.
- Yanlış aygıt dosyası oluşturmak sisteminize zarar verebilir, bu nedenle dikkatli olun ve yalnızca gerekli durumlarda kullanın.