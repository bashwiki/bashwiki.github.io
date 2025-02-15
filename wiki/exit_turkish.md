# [리눅스] Bash exit 사용법

## Overview
`exit` komutu, bir Bash shell oturumunu veya bir shell script'ini sonlandırmak için kullanılır. Bu komut, shell'den çıkarken bir çıkış durumu (exit status) belirlemenizi sağlar. Çıkış durumu, bir programın veya script'in başarılı bir şekilde çalışıp çalışmadığını belirtmek için kullanılır; genellikle 0, başarılı bir çıkışı, 1 veya daha yüksek değerler ise hataları temsil eder.

## Usage
`exit` komutunun temel sözdizimi şu şekildedir:

```bash
exit [n]
```

Burada `n`, çıkış durumunu temsil eden bir tamsayıdır. Eğer `n` belirtilmezse, shell, en son çalıştırılan komutun çıkış durumunu kullanır.

### Ortak Seçenekler
- `n`: Çıkış durumunu belirtir. 0, başarılı bir çıkışı; 1-255 arası değerler ise hata durumlarını temsil eder.

## Examples
### Örnek 1: Basit Çıkış
Aşağıdaki komut, mevcut shell oturumunu 0 çıkış durumu ile sonlandırır:

```bash
exit
```

### Örnek 2: Hata Durumu ile Çıkış
Aşağıdaki komut, mevcut shell oturumunu 1 çıkış durumu ile sonlandırır:

```bash
exit 1
```

Bu durumda, çıkış durumu 1 olarak ayarlanır ve bu, bir hata olduğunu belirtir.

## Tips
- Script yazarken, `exit` komutunu kullanarak script'inizin başarılı bir şekilde tamamlandığından emin olun. Örneğin, kritik bir hata durumunda `exit 1` kullanarak script'inizi sonlandırabilirsiniz.
- Çıkış durumlarını kontrol etmek için, script'lerinizi çalıştırdıktan sonra `$?` değişkenini kullanabilirsiniz. Bu değişken, en son çalıştırılan komutun çıkış durumunu tutar.
- `exit` komutunu kullanmadan önce, script'inizdeki tüm işlemlerin tamamlandığından emin olun; aksi takdirde, beklenmeyen sonuçlar elde edebilirsiniz.