# [Linux] Bash yerel komut: Yerel değişkenler tanımlama

## Genel Bakış
`local` komutu, bir fonksiyon içinde yerel değişkenler tanımlamak için kullanılır. Bu değişkenler, yalnızca tanımlandıkları fonksiyonun kapsamı içinde geçerlidir ve fonksiyon dışında erişilemezler. Bu, değişkenlerin çakışmasını önler ve kodun daha düzenli olmasına yardımcı olur.

## Kullanım
Temel sözdizimi aşağıdaki gibidir:

```bash
local [seçenekler] [argümanlar]
```

## Yaygın Seçenekler
- `-n`: Değişkenin değerini okur, ancak değişkeni tanımlamaz.
- `-p`: Mevcut yerel değişkenlerin listesini yazdırır.

## Yaygın Örnekler

### Örnek 1: Basit Yerel Değişken Tanımlama
```bash
my_function() {
    local my_var="Hello, World!"
    echo $my_var
}

my_function
# Çıktı: Hello, World!
```

### Örnek 2: Yerel Değişkenin Kapsamı
```bash
my_function() {
    local my_var="Inside Function"
    echo $my_var
}

my_function
echo $my_var  # Bu satır hata verecektir çünkü my_var yerel bir değişkendir.
```

### Örnek 3: Yerel Değişken ile Hesaplama
```bash
calculate() {
    local result=$(( $1 + $2 ))
    echo $result
}

calculate 5 10
# Çıktı: 15
```

## İpuçları
- `local` komutunu kullanarak, fonksiyonlarınızda değişkenlerin çakışmasını önleyebilirsiniz.
- Fonksiyonlarınızda kullandığınız değişkenlerin kapsamını sınırlamak, kodunuzu daha okunabilir ve yönetilebilir hale getirir.
- Yerel değişkenlerinizi tanımlarken anlamlı isimler kullanmaya özen gösterin, bu sayede kodunuzu okuyanlar için daha anlaşılır olur.