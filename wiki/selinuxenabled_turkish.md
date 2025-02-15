# [리눅스] Bash selinuxenabled 사용법

## Overview
`selinuxenabled` komutu, sistemde SELinux (Security-Enhanced Linux) güvenlik modülünün etkin olup olmadığını kontrol etmek için kullanılır. SELinux, Linux çekirdeği üzerinde çalışan bir güvenlik mimarisidir ve sistemin güvenliğini artırmak için erişim kontrol politikaları uygular. Bu komut, SELinux'un etkin olup olmadığını belirlemek için basit bir yol sunar ve genellikle sistem yöneticileri ve geliştiriciler tarafından kullanılır.

## Usage
`selinuxenabled` komutunun temel sözdizimi oldukça basittir:

```bash
selinuxenabled
```

Bu komut, SELinux etkinse 0 (başarılı) döner, değilse 1 (başarısız) döner. Komutun herhangi bir ek seçeneği yoktur; yalnızca SELinux'un durumunu kontrol etmek için kullanılır.

## Examples
Aşağıda `selinuxenabled` komutunun nasıl kullanılacağına dair iki örnek verilmiştir:

### Örnek 1: SELinux Durumunu Kontrol Etme
Aşağıdaki komut, SELinux'un etkin olup olmadığını kontrol eder:

```bash
if selinuxenabled; then
    echo "SELinux etkin."
else
    echo "SELinux etkin değil."
fi
```

Bu komut, SELinux etkinse "SELinux etkin." mesajını, değilse "SELinux etkin değil." mesajını yazdırır.

### Örnek 2: Script İçinde Kullanma
`selinuxenabled` komutunu bir bash script içinde kullanarak SELinux durumuna göre farklı işlemler gerçekleştirebilirsiniz:

```bash
#!/bin/bash

if selinuxenabled; then
    echo "SELinux aktif, güvenlik politikaları uygulanıyor."
    # Güvenlik ile ilgili başka işlemler burada yapılabilir
else
    echo "SELinux pasif, dikkatli olun."
    # Alternatif güvenlik önlemleri burada yapılabilir
fi
```

Bu script, SELinux'un durumuna göre farklı mesajlar ve işlemler gerçekleştirecektir.

## Tips
- `selinuxenabled` komutunu, sisteminizin güvenlik durumunu kontrol etmek için düzenli olarak kullanmanız önerilir.
- SELinux'un etkin olup olmadığını kontrol etmek, sisteminizin güvenliğini artırmak için önemli bir adımdır; bu nedenle, bu komutu otomasyon scriptlerinizde kullanmayı düşünün.
- SELinux'un etkin olduğu durumlarda, uygulamalarınızın doğru çalışabilmesi için uygun güvenlik politikalarının yapılandırıldığından emin olun.