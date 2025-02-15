# [리눅스] Bash command 사용법

## Overview
`command` komutu, Bash kabuğunda belirli bir komutun çalıştırılmasını sağlamak için kullanılır. Bu komut, shell'in yerleşik fonksiyonları veya alias'ları atlayarak, doğrudan belirtilen komutu çalıştırmak için kullanılır. Genellikle, bir komutun yerleşik bir versiyonunu kullanmak istemediğinizde veya bir alias'ın etkisini geçersiz kılmak istediğinizde yararlıdır.

## Usage
Temel sözdizimi şu şekildedir:

```bash
command [options] [arguments]
```

Burada `options` komutun belirli davranışlarını değiştiren seçeneklerdir ve `arguments` ise komutun işlemesi gereken girdilerdir. `command` komutu genellikle herhangi bir özel seçenek içermez, ancak belirli bir komutun kendine özgü seçenekleri olabilir.

## Examples
### Örnek 1: Alias'ı Atlamak
Eğer `ls` komutunu bir alias ile değiştirdiyseniz ve gerçek `ls` komutunu çalıştırmak istiyorsanız:

```bash
command ls
```

Bu komut, `ls` alias'ını atlayarak doğrudan `ls` komutunu çalıştırır.

### Örnek 2: Yerleşik Fonksiyonu Atlamak
Eğer `echo` komutunu bir fonksiyon ile değiştirdiyseniz ve gerçek `echo` komutunu çalıştırmak istiyorsanız:

```bash
command echo "Hello, World!"
```

Bu komut, `echo` fonksiyonunu atlayarak doğrudan `echo` komutunu çalıştırır.

## Tips
- `command` komutunu kullanırken, hangi komutun çalıştırıldığını net bir şekilde bilmek önemlidir. Özellikle, alias veya fonksiyonlar ile çakışma durumlarında `command` komutunun sağladığı avantajı kullanabilirsiniz.
- `command` komutunu kullanmak, shell'de belirli bir komutun beklenen davranışını garanti eder, bu nedenle karmaşık scriptlerde kullanılması önerilir.
- Komutlarınızı test ederken `command` ile çalıştırarak, beklenmedik sonuçların önüne geçebilirsiniz.