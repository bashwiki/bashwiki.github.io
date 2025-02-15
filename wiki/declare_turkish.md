# [리눅스] Bash declare 사용법

## Overview
`declare` komutu, Bash kabuğunda değişkenlerin özelliklerini tanımlamak ve yönetmek için kullanılır. Bu komut, değişkenlerin türünü ve özelliklerini belirleyerek, programlama sırasında daha fazla kontrol ve esneklik sağlar. Özellikle, değişkenlerin dizi veya okunan değişkenler gibi belirli türlerde tanımlanmasına olanak tanır.

## Usage
`declare` komutunun temel sözdizimi şu şekildedir:

```bash
declare [options] [name[=value]]
```

### Yaygın Seçenekler
- `-a`: Dizi değişkeni olarak tanımlar.
- `-A`: İlişkisel dizi (associative array) olarak tanımlar.
- `-i`: Tam sayı olarak tanımlar; bu, değişkenin aritmetik işlemlerle otomatik olarak işlenmesini sağlar.
- `-r`: Değişkeni salt okunur (readonly) olarak tanımlar; bu, değişkenin değerinin daha sonra değiştirilmesini engeller.
- `-x`: Değişkeni ortam değişkeni (environment variable) olarak tanımlar; bu, değişkenin alt süreçlere geçmesini sağlar.

## Examples
### Örnek 1: Dizi Değişkeni Tanımlama
```bash
declare -a my_array
my_array=(1 2 3 4 5)
echo "${my_array[2]}"  # Çıktı: 3
```
Bu örnekte, `my_array` adında bir dizi değişkeni tanımlanmış ve içine bazı değerler atanmıştır. Daha sonra, dizinin üçüncü elemanı ekrana yazdırılmıştır.

### Örnek 2: Salt Okunur Değişken
```bash
declare -r my_const="Bu bir sabittir"
echo "$my_const"  # Çıktı: Bu bir sabittir
# my_const="Yeni değer"  # Bu satır hata verecektir.
```
Bu örnekte, `my_const` adında bir salt okunur değişken tanımlanmıştır. Değişkenin değeri daha sonra değiştirilmeye çalışıldığında hata verecektir.

## Tips
- `declare` komutunu kullanarak değişkenlerinizi tanımlarken, türlerini belirlemek, kodunuzun okunabilirliğini artırır ve hata yapma olasılığını azaltır.
- Değişkenlerinizi salt okunur olarak tanımlamak, beklenmedik değişikliklerden kaçınmanıza yardımcı olur.
- Dizi değişkenleri ile çalışırken, dizinin boyutunu ve elemanlarını kontrol etmek için `declare -p` komutunu kullanabilirsiniz. Bu, mevcut değişkenlerin durumunu gösterir.

Bu bilgilerle, `declare` komutunu etkili bir şekilde kullanarak Bash betiklerinizi daha yönetilebilir ve hatasız hale getirebilirsiniz.