# [리눅스] Bash printf 사용법

## Genel Bakış
`printf` komutu, formatlanmış çıktı üretmek için kullanılan bir Bash komutudur. C dilindeki `printf` fonksiyonuna benzer şekilde çalışır ve kullanıcıların belirli bir formatta metin, sayılar veya diğer verileri ekrana yazdırmasına olanak tanır. `printf`, özellikle karmaşık çıktılar oluşturmak için oldukça kullanışlıdır ve daha fazla kontrol sağlar.

## Kullanım
Temel sözdizimi şu şekildedir:

```bash
printf "format" [arguments...]
```

- **format**: Çıktının nasıl görüneceğini belirten format dizgisi. `%` ile başlayan format belirteçleri kullanılır.
- **arguments**: Format dizgisinde belirtilen yer tutucular için sağlanan değerler.

### Yaygın Seçenekler
- `%s`: String (metin) formatı.
- `%d`: Tam sayı formatı.
- `%f`: Ondalık sayı formatı.
- `\n`: Yeni satır karakteri.
- `\t`: Sekme karakteri.

## Örnekler

### Örnek 1: Basit Metin Yazdırma
Aşağıdaki komut, "Merhaba, Dünya!" ifadesini ekrana yazdırır:

```bash
printf "Merhaba, Dünya!\n"
```

### Örnek 2: Formatlı Sayı Yazdırma
Aşağıdaki komut, bir tam sayıyı ve bir ondalık sayıyı formatlı bir şekilde yazdırır:

```bash
printf "Tam Sayı: %d, Ondalık: %.2f\n" 42 3.14159
```
Bu komut, "Tam Sayı: 42, Ondalık: 3.14" çıktısını verir.

## İpuçları
- `printf`, `echo` komutuna göre daha fazla formatlama seçeneği sunar. Özellikle karmaşık çıktılar için tercih edilmelidir.
- Format dizgisinde yer tutucuların sırasına dikkat edin; her bir yer tutucu, sağlanan argümanlarla eşleşmelidir.
- Çıktıyı daha okunabilir hale getirmek için `\n` ve `\t` gibi özel karakterleri kullanmayı unutmayın.
- Hatalı formatlama veya eksik argümanlar, beklenmeyen çıktılara neden olabilir; bu nedenle dikkatli olun.