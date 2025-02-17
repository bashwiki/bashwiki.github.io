# [Linux] Bash umask Kullanımı: Dosya izinlerini kontrol etme

## Overview
`umask` komutu, yeni oluşturulan dosya ve dizinlerin varsayılan izinlerini belirlemek için kullanılır. Bu komut, kullanıcıların dosya ve dizinlere erişim izinlerini yönetmesine olanak tanır.

## Usage
Temel sözdizimi şu şekildedir:
```bash
umask [seçenekler] [argümanlar]
```

## Common Options
- `-S`: Umask değerini sembolik olarak gösterir.
- `-p`: Mevcut umask değerini gösterir.
- `-h`: Yardım bilgilerini gösterir.

## Common Examples
Aşağıda `umask` komutunun bazı yaygın kullanım örnekleri bulunmaktadır:

1. **Mevcut umask değerini görüntüleme:**
   ```bash
   umask
   ```

2. **Umask değerini ayarlama:**
   ```bash
   umask 027
   ```
   Bu komut, yeni dosyaların varsayılan izinlerini `rw-r-----` olarak ayarlayacaktır.

3. **Sembolik umask değerini görüntüleme:**
   ```bash
   umask -S
   ```

4. **Umask değerini geçici olarak değiştirme:**
   ```bash
   umask 002
   touch yeni_dosya.txt
   ```
   Bu komut, `yeni_dosya.txt` dosyasını `rw-rw-r--` izinleriyle oluşturur.

## Tips
- Umask değerini ayarlarken, güvenlik gereksinimlerinizi göz önünde bulundurun; çok geniş izinler vermekten kaçının.
- Umask ayarlarını `.bashrc` veya `.bash_profile` dosyanıza ekleyerek, her oturum açtığınızda otomatik olarak ayarlanmasını sağlayabilirsiniz.
- Umask değerlerini kontrol etmek ve gerektiğinde güncellemek, sistem güvenliğini artırmak için önemlidir.