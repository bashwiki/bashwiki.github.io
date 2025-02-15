# [리눅스] Bash return 사용법

## Overview
`return` komutu, bir fonksiyonun veya bir betiğin (script) çalışmasını sonlandırmak ve belirli bir çıkış kodu döndürmek için kullanılır. Bu komut, özellikle fonksiyonlar içinde kullanıldığında, fonksiyonun sonucunu çağıran yere iletmek için önemlidir. Çıkış kodları, bir işlemin başarılı olup olmadığını belirtmek için yaygın olarak kullanılır; genellikle 0 başarılı bir sonucu, 1 veya daha yüksek sayılar ise hataları temsil eder.

## Usage
`return` komutunun temel sözdizimi aşağıdaki gibidir:

```bash
return [çıkış_kodu]
```

- `çıkış_kodu`: (isteğe bağlı) Fonksiyonun veya betiğin döndüreceği çıkış kodudur. Belirtilmezse, son çalıştırılan komutun çıkış kodu kullanılır.

## Examples

### Örnek 1: Basit Bir Fonksiyon
Aşağıdaki örnekte, bir fonksiyon tanımlanmış ve bu fonksiyon bir çıkış kodu döndürmektedir:

```bash
my_function() {
    echo "Fonksiyon çalışıyor."
    return 0
}

my_function
echo "Çıkış kodu: $?"
```

Bu örnekte, `my_function` çağrıldığında "Fonksiyon çalışıyor." mesajı yazdırılır ve ardından çıkış kodu 0 olarak döner.

### Örnek 2: Hata Durumu
Aşağıdaki örnekte, bir hata durumu simüle edilmiştir:

```bash
check_file() {
    if [ ! -f "$1" ]; then
        echo "Dosya bulunamadı!"
        return 1
    fi
    echo "Dosya mevcut."
    return 0
}

check_file "olmayan_dosya.txt"
echo "Çıkış kodu: $?"
```

Bu örnekte, `check_file` fonksiyonu verilen dosyanın varlığını kontrol eder. Dosya mevcut değilse, hata mesajı yazdırılır ve çıkış kodu 1 olarak döner.

## Tips
- `return` komutunu yalnızca fonksiyonlar içinde kullanın; betiklerin ana akışında `exit` komutunu tercih edin.
- Çıkış kodlarını kullanarak hata ayıklama yaparken, her fonksiyonun sonunda uygun bir çıkış kodu döndürdüğünüzden emin olun.
- `return` komutunu kullanarak, fonksiyonlarınızın daha okunabilir ve yönetilebilir olmasını sağlayabilirsiniz.