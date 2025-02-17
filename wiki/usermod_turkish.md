# [Linux] Bash usermod Kullanımı: Kullanıcı bilgilerini değiştirme

## Overview
`usermod` komutu, Linux sistemlerinde mevcut kullanıcı hesaplarının özelliklerini değiştirmek için kullanılır. Bu komut sayesinde kullanıcı adı, grup üyelikleri, ev dizini gibi bilgileri güncelleyebilirsiniz.

## Usage
Temel sözdizimi aşağıdaki gibidir:

```bash
usermod [options] [arguments]
```

## Common Options
- `-a`: Kullanıcıyı mevcut grup üyeliklerine ekler (append).
- `-G`: Kullanıcının eklenmesini istediğiniz grup isimlerini belirtir.
- `-d`: Kullanıcının ev dizinini değiştirir.
- `-l`: Kullanıcının adını değiştirir.
- `-s`: Kullanıcının varsayılan kabuk ayarını değiştirir.

## Common Examples
Aşağıda `usermod` komutunun bazı yaygın kullanım örnekleri verilmiştir:

1. Kullanıcının ev dizinini değiştirmek:
   ```bash
   usermod -d /yeni/ev/dizini kullanıcı_adı
   ```

2. Kullanıcıyı bir gruba eklemek:
   ```bash
   usermod -a -G grup_adı kullanıcı_adı
   ```

3. Kullanıcı adını değiştirmek:
   ```bash
   usermod -l yeni_kullanici_adı eski_kullanici_adı
   ```

4. Kullanıcının varsayılan kabuğunu değiştirmek:
   ```bash
   usermod -s /bin/zsh kullanıcı_adı
   ```

## Tips
- `usermod` komutunu kullanmadan önce, değişiklik yapacağınız kullanıcının oturumunun kapalı olduğundan emin olun.
- Değişikliklerin etkili olabilmesi için sistemdeki oturum açma işlemlerini yeniden başlatmanız gerekebilir.
- Kullanıcı bilgilerini değiştirmeden önce mevcut ayarları yedeklemek iyi bir uygulamadır.