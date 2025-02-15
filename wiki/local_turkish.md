# [리눅스] Bash local 사용법

## Overview
`local` komutu, Bash betiklerinde yerel değişkenler tanımlamak için kullanılır. Bu değişkenler, yalnızca tanımlandıkları fonksiyonun kapsamı içinde geçerlidir ve fonksiyon dışında erişilemezler. Bu özellik, değişken adlarının çakışmasını önlemeye yardımcı olur ve kodun daha okunabilir olmasını sağlar.

## Usage
`local` komutunun temel sözdizimi aşağıdaki gibidir:

```bash
local VARIABLE_NAME=VALUE
```

Burada `VARIABLE_NAME`, tanımlamak istediğiniz yerel değişkenin adıdır ve `VALUE`, bu değişkene atamak istediğiniz değerdir. `local` komutu, yalnızca bir fonksiyon içinde kullanılmalıdır.

### Örnek Seçenekler
- `local VAR`: Sadece bir değişken tanımlamak için.
- `local VAR=VALUE`: Değişkeni bir değerle başlatmak için.

## Examples

### Örnek 1: Basit Yerel Değişken Tanımlama
Aşağıdaki örnekte, bir fonksiyon içinde yerel bir değişken tanımlanmıştır:

```bash
my_function() {
    local my_var="Hello, World!"
    echo $my_var
}

my_function  # Çıktı: Hello, World!
echo $my_var # Çıktı: (boş, çünkü my_var yerel bir değişkendir)
```

### Örnek 2: Yerel Değişkenlerle Hesaplama
Bu örnekte, yerel değişkenler kullanılarak basit bir hesaplama yapılmaktadır:

```bash
calculate() {
    local a=5
    local b=10
    local sum=$((a + b))
    echo "Sum: $sum"
}

calculate  # Çıktı: Sum: 15
```

## Tips
- `local` komutunu yalnızca fonksiyonlar içinde kullanın; aksi takdirde hata alırsınız.
- Yerel değişkenlerin adlarını, global değişkenlerle çakışmaması için dikkatlice seçin.
- Fonksiyonlarınızda `local` kullanmak, kodunuzu daha modüler ve hatasız hale getirir.