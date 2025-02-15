# [리눅스] Bash times 사용법

## Overview
`times` komutu, bir shell oturumunda geçen zaman bilgilerini gösterir. Bu komut, kullanıcıya CPU zamanını ve sistemin ne kadar süre çalıştığını göstererek, performans analizi yapmasına yardımcı olur. Özellikle, bir shell oturumu içinde çalıştırılan komutların toplam CPU zamanını ve kullanıcı ile sistem zamanını izlemek için kullanılır.

## Usage
`times` komutunun temel kullanımı oldukça basittir. Aşağıdaki gibi yazılır:

```bash
times
```

Bu komut, mevcut shell oturumunda daha önce çalıştırılan komutlar için toplam CPU zamanını gösterir. `times` komutunun herhangi bir özel seçeneği yoktur; sadece çağrıldığında mevcut zaman bilgilerini döndürür.

## Examples
### Örnek 1: Basit Kullanım
Aşağıdaki komut, `times` komutunun nasıl kullanılacağını gösterir. Öncelikle birkaç basit komut çalıştırdıktan sonra `times` komutunu çağırarak zaman bilgilerini görebiliriz.

```bash
# Bazı komutları çalıştır
sleep 2
ls -l
echo "Merhaba Dünya"

# Zaman bilgilerini göster
times
```

Bu örnekte, `sleep`, `ls` ve `echo` komutları çalıştırıldıktan sonra `times` komutu çağrıldığında, bu komutların toplam CPU zamanını göreceksiniz.

### Örnek 2: Zaman Bilgilerini İnceleme
Aşağıdaki komut dizisi, `times` komutunun çıktısını incelemek için kullanılabilir:

```bash
# Daha fazla komut çalıştır
find / -name "*.txt" > /dev/null 2>&1
grep "test" somefile.txt > /dev/null 2>&1

# Zaman bilgilerini göster
times
```

Bu örnekte, `find` ve `grep` komutları çalıştırıldıktan sonra `times` komutunu çağırarak bu komutların CPU zamanını görebilirsiniz.

## Tips
- `times` komutunu, uzun süre çalışan veya kaynak tüketen komutlardan sonra kullanmak, hangi komutların ne kadar süre çalıştığını anlamanıza yardımcı olabilir.
- Shell oturumunuzda `times` komutunu çağırmadan önce birkaç komut çalıştırarak, zaman bilgilerini daha anlamlı hale getirebilirsiniz.
- `times` çıktısı, kullanıcı ve sistem zamanını ayrı olarak gösterir; bu nedenle, hangi tür işlemlerin daha fazla zaman aldığını analiz etmek için bu bilgileri kullanabilirsiniz.