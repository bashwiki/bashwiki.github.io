# [리눅스] Bash su 사용법

## Genel Bakış
`su` (substitute user) komutu, bir kullanıcıdan diğerine geçiş yapmayı sağlayan bir Bash komutudur. Genellikle, bir kullanıcının başka bir kullanıcı olarak oturum açmasını sağlamak için kullanılır. En yaygın kullanım durumu, sistem yöneticilerinin veya geliştiricilerin root (yönetici) kullanıcı olarak oturum açmalarıdır. Bu komut, kullanıcıların yetkilerini artırarak sistem üzerinde daha fazla kontrol sahibi olmalarına olanak tanır.

## Kullanım
Temel `su` komutunun sözdizimi şu şekildedir:

```bash
su [seçenekler] [kullanıcı]
```

### Yaygın Seçenekler
- `-`: Kullanıcı geçişi sırasında yeni bir oturum başlatır ve kullanıcının ortam değişkenlerini yükler.
- `-c`: Belirtilen komutu belirtilen kullanıcı olarak çalıştırır.
- `-l` veya `--login`: Kullanıcı oturumunu başlatır ve kullanıcının ortam değişkenlerini yükler.

## Örnekler
### Örnek 1: Root Kullanıcısına Geçiş
Aşağıdaki komut, root kullanıcısına geçiş yapar:

```bash
su -
```

Bu komut, root kullanıcısının şifresini girmenizi isteyecektir. Başarılı bir şekilde giriş yaptıktan sonra, root yetkilerine sahip olursunuz.

### Örnek 2: Belirli Bir Komutu Farklı Bir Kullanıcı Olarak Çalıştırma
Aşağıdaki komut, `kullanici_adi` adlı kullanıcı olarak `ls` komutunu çalıştırır:

```bash
su -c "ls" kullanici_adi
```

Bu komut, `kullanici_adi` kullanıcısının şifresini girmenizi isteyecektir ve ardından belirtilen komutu çalıştıracaktır.

## İpuçları
- `su` komutunu kullanırken, güvenlik açısından dikkatli olun. Özellikle root kullanıcısına geçiş yaparken, sistemdeki kritik dosyaları değiştirmemeye özen gösterin.
- `su` komutunu sık kullanıyorsanız, `sudo` komutunu da göz önünde bulundurabilirsiniz. `sudo`, belirli komutları belirli kullanıcılar olarak çalıştırmanıza olanak tanır ve daha güvenli bir alternatif olabilir.
- Kullanıcı geçişleri sırasında, ortam değişkenlerini yüklemek için `su -` veya `su --login` seçeneklerini kullanmayı unutmayın. Bu, kullanıcıya ait ayarların doğru bir şekilde yüklenmesini sağlar.