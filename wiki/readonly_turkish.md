# [리눅스] Bash readonly 사용법

## Genel Bakış
`readonly` komutu, Bash kabuğunda değişkenlerin değerlerini değiştirilmez hale getirmek için kullanılır. Bir değişken `readonly` olarak tanımlandığında, bu değişkenin değeri daha sonra değiştirilemez. Bu, özellikle değişkenlerin sabit kalmasını istediğiniz durumlarda faydalıdır ve kodun daha güvenilir ve hatasız olmasına yardımcı olur.

## Kullanım
`readonly` komutunun temel sözdizimi şu şekildedir:

```bash
readonly [değişken_adı[=değer]]
```

- `değişken_adı`: Değişkenin adı. Bu değişken, `readonly` olarak tanımlanacaktır.
- `değer`: (isteğe bağlı) Değişkene atanacak değer. Eğer değer verilmezse, sadece değişkenin `readonly` olarak tanımlanması sağlanır.

### Yaygın Seçenekler
`readonly` komutu için özel bir seçenek bulunmamaktadır. Ancak, birden fazla değişkeni aynı anda `readonly` yapmak için birden fazla değişken adı verebilirsiniz.

## Örnekler

### Örnek 1: Basit Kullanım
Aşağıdaki örnekte, bir değişken `readonly` olarak tanımlanmıştır ve daha sonra değeri değiştirilmek istendiğinde hata alınacaktır.

```bash
# readonly ile değişken tanımlama
readonly MY_VAR="Sabit Değer"

# Değişkenin değerini değiştirmeye çalışmak
MY_VAR="Yeni Değer"  # Bu satır hata verecektir.
```

### Örnek 2: Birden Fazla Değişkeni readonly Yapma
Birden fazla değişkeni aynı anda `readonly` olarak tanımlamak mümkündür.

```bash
# Birden fazla değişkeni readonly olarak tanımlama
readonly VAR1="Değer 1" VAR2="Değer 2"

# Değişkenlerden birinin değerini değiştirmeye çalışmak
VAR1="Yeni Değer"  # Bu satır hata verecektir.
```

## İpuçları
- `readonly` kullanırken, değişkenlerinizi dikkatlice seçin. Değişkenlerinizi `readonly` olarak tanımlamak, kodunuzun belirli bölümlerinde beklenmedik değişiklikleri önleyebilir.
- `readonly` ile tanımlanan değişkenlerin değerlerini kontrol etmek için `declare -p` komutunu kullanabilirsiniz. Bu, hangi değişkenlerin `readonly` olduğunu görmenizi sağlar.
- `readonly` değişkenlerinizi, kodunuzu daha okunabilir hale getirmek için anlamlı isimlerle tanımlayın. Bu, diğer geliştiricilerin kodunuzu anlamasını kolaylaştırır.