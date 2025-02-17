# [Linux] Bash whoami Kullanımı: Kullanıcı adını gösterir

## Genel Bakış
`whoami` komutu, terminalde oturum açmış olan kullanıcının adını gösterir. Bu komut, kullanıcı kimliğini doğrulamak veya sistemde hangi kullanıcı olarak çalıştığınızı öğrenmek için oldukça yararlıdır.

## Kullanım
Temel sözdizimi aşağıdaki gibidir:

```
whoami [seçenekler] [argümanlar]
```

## Yaygın Seçenekler
`whoami` komutunun genellikle kullanılan seçenekleri şunlardır:

- `--help`: Komut hakkında yardım bilgisi gösterir.
- `--version`: Komutun sürüm bilgilerini gösterir.

## Yaygın Örnekler
Aşağıda `whoami` komutunun bazı pratik örnekleri bulunmaktadır:

1. **Basit Kullanım**
   ```bash
   whoami
   ```
   Bu komut, oturum açmış olan kullanıcı adını döndürür.

2. **Yardım Bilgisi Alma**
   ```bash
   whoami --help
   ```
   Bu komut, `whoami` komutunun nasıl kullanılacağına dair yardım bilgilerini gösterir.

3. **Sürüm Bilgisi Alma**
   ```bash
   whoami --version
   ```
   Bu komut, `whoami` komutunun sürüm bilgilerini gösterir.

## İpuçları
- `whoami` komutunu, birden fazla kullanıcı hesabı arasında geçiş yaptığınızda hangi kullanıcıda olduğunuzu kontrol etmek için kullanabilirsiniz.
- Komutu, betiklerinizde kullanıcı doğrulama amacıyla entegre edebilirsiniz.
- Eğer sistemdeki diğer kullanıcıların bilgilerini görmek istiyorsanız, `who` veya `users` komutlarını kullanmayı düşünebilirsiniz.