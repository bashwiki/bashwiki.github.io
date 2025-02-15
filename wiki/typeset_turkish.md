# [리눅스] Bash typeset 사용법

## Genel Bakış
`typeset` komutu, Bash kabuğunda değişkenlerin özelliklerini tanımlamak ve yönetmek için kullanılır. Bu komut, değişkenlerin türünü belirlemeye, değişkenleri yerel hale getirmeye ve değişkenlerin değerlerini kontrol etmeye olanak tanır. Özellikle fonksiyonlar içinde değişkenlerin kapsamını sınırlamak için faydalıdır.

## Kullanım
Temel sözdizimi şu şekildedir:

```bash
typeset [seçenekler] [değişken_adı]=[değer]
```

### Yaygın Seçenekler
- `-i`: Değişkeni tam sayı olarak tanımlar. Bu, değişkenin aritmetik işlemlerde kullanılmasını sağlar.
- `-r`: Değişkenin okunabilirliğini artırır ve değişkenin değerinin değiştirilmesini engeller.
- `-x`: Değişkeni ortam değişkeni olarak işaretler, böylece alt süreçlerde de erişilebilir hale gelir.
- `-l`: Değişkenin değerini küçük harflerle saklar.
- `-u`: Değişkenin değerini büyük harflerle saklar.

## Örnekler

### Örnek 1: Tam Sayı Değişkeni Tanımlama
Aşağıdaki komut, `num` adında bir tam sayı değişkeni tanımlar ve ona 10 değerini atar:

```bash
typeset -i num=10
echo $num
```

Bu komutun çıktısı `10` olacaktır. `num` değişkeni artık aritmetik işlemlerde kullanılabilir.

### Örnek 2: Okunamaz Değişken Tanımlama
Aşağıdaki örnekte, `readonly_var` adında bir değişken tanımlanır ve bu değişkenin değeri değiştirilemez:

```bash
typeset -r readonly_var="Değiştirilemez"
echo $readonly_var
# readonly_var="Yeni Değer"  # Bu satır hata verecektir.
```

## İpuçları
- `typeset` komutunu kullanırken, değişkenlerin kapsamını iyi yönetmek için fonksiyonlar içinde yerel değişkenler tanımlamak önemlidir.
- Değişkenlerinizi tanımlarken, hangi türde olduklarını belirtmek, kodun okunabilirliğini artırır ve hata yapma olasılığını azaltır.
- `typeset` komutunu kullanarak değişkenlerinizi daha güvenli hale getirebilir ve beklenmedik değişikliklerden koruyabilirsiniz.