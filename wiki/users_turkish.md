# [리눅스] Bash users 사용법

## Overview
`users` komutu, sistemde oturum açmış olan kullanıcıların kullanıcı adlarını listelemek için kullanılır. Bu komut, birden fazla kullanıcının aynı anda sisteme giriş yaptığı durumlarda, hangi kullanıcıların aktif olduğunu hızlı bir şekilde görmek için faydalıdır. Çıktı, kullanıcı adlarını boşluklarla ayrılmış bir şekilde gösterir.

## Usage
`users` komutunun temel sözdizimi oldukça basittir:

```bash
users [OPTIONS]
```

### Common Options
`users` komutunun kendine özgü seçenekleri yoktur; genellikle varsayılan olarak çalıştırılır ve yalnızca kullanıcı adlarını döndürür. Ancak, `users` komutunu diğer komutlarla birleştirerek daha fazla işlevsellik elde edebilirsiniz.

## Examples
### Örnek 1: Aktif Kullanıcıları Listeleme
Aşağıdaki komut, sistemde oturum açmış olan tüm kullanıcıların adlarını listeleyecektir:

```bash
users
```

Çıktı örneği:
```
user1 user2 user3
```

### Örnek 2: Kullanıcıları Başka Bir Komutla Birleştirme
`users` komutunu `wc` (word count) komutuyla birleştirerek, aktif kullanıcı sayısını öğrenebilirsiniz:

```bash
users | wc -w
```

Bu komut, oturum açmış kullanıcıların sayısını döndürür.

## Tips
- `users` komutunu, sistem izleme veya kullanıcı aktivitelerini kontrol etme gibi durumlarda kullanmak faydalıdır.
- Eğer daha fazla bilgiye ihtiyaç duyuyorsanız, `who` veya `w` komutlarını kullanarak kullanıcıların oturum bilgileri hakkında daha ayrıntılı bilgi alabilirsiniz.
- Komutun çıktısını bir dosyaya yönlendirmek isterseniz, aşağıdaki gibi kullanabilirsiniz:

```bash
users > aktif_kullanicilar.txt
```

Bu, aktif kullanıcıların listesini `aktif_kullanicilar.txt` dosyasına kaydeder.