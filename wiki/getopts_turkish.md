# [리눅스] Bash getopts 사용법

## Genel Bakış
`getopts`, Bash betiklerinde komut satırı argümanlarını işlemek için kullanılan bir yerleşik komuttur. Kullanıcıdan gelen argümanları analiz ederek, belirli seçenekleri ve bunların değerlerini almak için kullanılır. Bu, kullanıcıların betiklerinize daha esnek ve kullanıcı dostu bir şekilde girdi sağlamasına olanak tanır.

## Kullanım
`getopts` komutunun temel sözdizimi aşağıdaki gibidir:

```bash
getopts "seçenekler:" değişken
```

- `seçenekler`: İşlemek istediğiniz seçenekleri belirtir. Her bir seçenek bir harf ile temsil edilir. Eğer bir seçeneğin bir değeri varsa, bu durumda iki nokta üst üste (`:`) eklenir.
- `değişken`: `getopts` tarafından ayarlanan ve işlenen seçeneklerin saklanacağı değişken.

### Yaygın Seçenekler
- `:`: Eğer bir seçenek bir değer gerektiriyorsa, iki nokta üst üste (`:`) kullanılır.
- `?`: Geçersiz bir seçenek verildiğinde hata mesajı vermek için kullanılır.

## Örnekler

### Örnek 1: Basit Seçenek İşleme
Aşağıdaki örnek, `-a` ve `-b` seçeneklerini işleyen basit bir betik göstermektedir:

```bash
#!/bin/bash

while getopts "ab" opt; do
  case $opt in
    a)
      echo "Seçenek A seçildi."
      ;;
    b)
      echo "Seçenek B seçildi."
      ;;
    *)
      echo "Geçersiz seçenek."
      ;;
  esac
done
```

Bu betiği çalıştırdığınızda, örneğin `./script.sh -a` komutunu kullanarak "Seçenek A seçildi." mesajını alırsınız.

### Örnek 2: Değer Gerektiren Seçenekler
Aşağıdaki örnek, bir seçenek için değer gerektiren bir durumu göstermektedir:

```bash
#!/bin/bash

while getopts "u:p:" opt; do
  case $opt in
    u)
      echo "Kullanıcı: $OPTARG"
      ;;
    p)
      echo "Parola: $OPTARG"
      ;;
    *)
      echo "Geçersiz seçenek."
      ;;
  esac
done
```

Bu betiği `./script.sh -u kullanıcı_adı -p parola` şeklinde çalıştırdığınızda, "Kullanıcı: kullanıcı_adı" ve "Parola: parola" mesajlarını alırsınız.

## İpuçları
- `getopts` kullanırken, seçeneklerinizi ve değerlerinizi açık bir şekilde tanımlamak için yorum satırları eklemeyi unutmayın. Bu, kodunuzu daha okunabilir hale getirir.
- `getopts` ile birlikte `shift` komutunu kullanarak işlenmeyen argümanları yönetebilirsiniz. Bu, daha karmaşık betiklerde faydalı olabilir.
- Hatalı girişleri yönetmek için `?` seçeneğini kullanarak kullanıcıya anlamlı hata mesajları vermek iyi bir uygulamadır.

Bu bilgilerle, `getopts` komutunu etkili bir şekilde kullanarak Bash betiklerinizde komut satırı argümanlarını işleyebilirsiniz.