# [리눅스] Bash rmdir 사용법

## Overview
`rmdir` komutu, boş dizinleri silmek için kullanılan bir Bash komutudur. Bu komut, yalnızca içinde dosya veya alt dizin bulunmayan dizinleri kaldırır. Eğer dizin içinde herhangi bir içerik varsa, `rmdir` komutu çalışmaz ve hata mesajı verir. Bu nedenle, dizinleri silmeden önce içeriğini kontrol etmek önemlidir.

## Usage
`rmdir` komutunun temel sözdizimi şu şekildedir:

```
rmdir [seçenekler] dizin_adı
```

### Yaygın Seçenekler
- `-p`, `--parents`: Belirtilen dizinin üst dizinlerini de siler, eğer bunlar da boşsa.
- `-v`, `--verbose`: Silme işlemi sırasında hangi dizinlerin silindiğini gösterir.

## Examples
### Örnek 1: Boş bir dizini silme
Aşağıdaki komut, `ornek_dizin` adındaki boş dizini siler:

```bash
rmdir ornek_dizin
```

### Örnek 2: Üst dizinleri silme
Eğer `alt_dizin` adında bir dizin var ve bu dizin `ust_dizin` içinde bulunuyorsa, aşağıdaki komut ile `alt_dizin` ve eğer boşsa `ust_dizin` de silinebilir:

```bash
rmdir -p ust_dizin/alt_dizin
```

## Tips
- `rmdir` komutunu kullanmadan önce silmek istediğiniz dizinlerin gerçekten boş olduğundan emin olun. İçinde dosya veya alt dizin bulunan bir dizini silmeye çalıştığınızda hata alırsınız.
- Dizinlerinizi silmeden önce bir yedekleme yapmayı düşünün, böylece yanlışlıkla silinen verileri geri alabilirsiniz.
- `-v` seçeneğini kullanarak hangi dizinlerin silindiğini görmek, işleminizi daha şeffaf hale getirebilir.