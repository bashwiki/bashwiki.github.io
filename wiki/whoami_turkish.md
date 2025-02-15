# [리눅스] Bash whoami 사용법

## Genel Bakış
`whoami` komutu, mevcut kullanıcı oturumunun adını gösteren basit bir Bash komutudur. Bu komut, hangi kullanıcı olarak oturum açtığınızı hızlı bir şekilde öğrenmenizi sağlar. Özellikle birden fazla kullanıcı hesabı olan sistemlerde veya kullanıcı izinlerini kontrol etmek için faydalıdır.

## Kullanım
`whoami` komutunun temel sözdizimi oldukça basittir:

```bash
whoami
```

Bu komut, ekrana mevcut kullanıcı adını yazdırır. `whoami` komutunun herhangi bir yerleşik seçeneği yoktur; bu nedenle, yalnızca bu şekilde kullanılmalıdır.

## Örnekler
1. Mevcut kullanıcı adınızı öğrenmek için `whoami` komutunu çalıştırabilirsiniz:

   ```bash
   whoami
   ```

   Çıktı olarak, örneğin `kullanici_adi` gibi bir kullanıcı adı göreceksiniz.

2. Eğer bir terminalde `su` komutuyla başka bir kullanıcıya geçiş yaptıysanız, `whoami` komutunu kullanarak hangi kullanıcı olarak oturum açtığınızı kontrol edebilirsiniz:

   ```bash
   su - yeni_kullanici
   whoami
   ```

   Bu durumda, `yeni_kullanici` adını göreceksiniz.

## İpuçları
- `whoami` komutunu kullanarak, bir script veya program içinde hangi kullanıcı ile çalıştığınızı kontrol edebilirsiniz. Bu, kullanıcı izinlerini yönetmek için yararlı olabilir.
- Eğer birden fazla terminal penceresi açtıysanız ve hangi kullanıcı ile oturum açtığınızı unuttuysanız, her terminalde `whoami` komutunu çalıştırarak hızlıca kontrol edebilirsiniz.
- `whoami` komutunu, kullanıcı kimlik bilgilerinizi doğrulamak için diğer komutlarla birlikte kullanmak, sistem güvenliğini artırabilir.