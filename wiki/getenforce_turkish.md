# [리눅스] Bash getenforce 사용법

## Overview
`getenforce` komutu, Linux işletim sistemlerinde SELinux (Security-Enhanced Linux) güvenlik modunun mevcut durumunu kontrol etmek için kullanılır. SELinux, sistemin güvenliğini artırmak amacıyla uygulamalara ve kullanıcıların erişim haklarına kısıtlamalar getiren bir güvenlik mimarisidir. `getenforce` komutu, SELinux'un aktif olup olmadığını ve hangi modda çalıştığını gösterir.

## Usage
Temel kullanım şekli oldukça basittir. Komutun genel sözdizimi aşağıdaki gibidir:

```bash
getenforce
```

Bu komut, SELinux'un mevcut durumunu döndürür. `getenforce` komutunun döndürebileceği üç ana sonuç vardır:

- **Enforcing**: SELinux kuralları aktif ve uygulanıyor.
- **Permissive**: SELinux kuralları aktif ancak uygulanmıyor; ihlaller kaydediliyor.
- **Disabled**: SELinux devre dışı.

## Examples
Aşağıda `getenforce` komutunun nasıl kullanılacağına dair birkaç örnek bulunmaktadır:

1. **SELinux Durumunu Kontrol Etme**:
   ```bash
   getenforce
   ```
   Bu komut, SELinux'un mevcut durumunu (Enforcing, Permissive veya Disabled) ekrana yazdırır.

2. **Durumu Script İçinde Kullanma**:
   ```bash
   if [ "$(getenforce)" == "Enforcing" ]; then
       echo "SELinux aktif ve kurallar uygulanıyor."
   else
       echo "SELinux ya devre dışı ya da izin verici modda."
   fi
   ```
   Bu örnek, `getenforce` komutunu bir koşul ifadesi içinde kullanarak SELinux durumuna göre farklı mesajlar yazdırır.

## Tips
- `getenforce` komutunu sık sık kullanarak SELinux'un durumunu kontrol etmek, sistem güvenliğini sağlamak için iyi bir uygulamadır.
- Eğer SELinux'un durumunu değiştirmek istiyorsanız, `setenforce` komutunu kullanabilirsiniz. Ancak, bu komutun etkili olabilmesi için yeterli izinlere sahip olmalısınız.
- SELinux ile ilgili daha fazla bilgi almak ve yapılandırma seçeneklerini öğrenmek için `man selinux` veya `man setenforce` komutlarını kullanabilirsiniz.