# [리눅스] Bash readarray 사용법

## Genel Bakış
`readarray`, Bash'de bir diziye (array) satır satır veri okuma işlemi için kullanılan bir komuttur. Bu komut, genellikle bir dosyadan veya standart girdi (stdin) üzerinden gelen verileri dizi elemanlarına atamak için kullanılır. `readarray`, özellikle büyük veri setleriyle çalışırken veya bir dosyadaki verileri dizi olarak işlemek gerektiğinde oldukça faydalıdır.

## Kullanım
Temel sözdizimi şu şekildedir:

```bash
readarray [seçenekler] dizi_adı
```

### Yaygın Seçenekler
- `-t`: Satır sonu karakterlerini (newline) kaldırır. Bu, dizinin elemanlarının sonundaki gereksiz boşlukları önlemek için kullanışlıdır.
- `-n`: Okunacak satır sayısını belirtir. Bu seçenek ile yalnızca belirtilen sayıda satır okunur.
- `-s`: Okunacak satırların başlangıç indeksini belirtir. Bu, dizinin hangi satırdan itibaren doldurulacağını belirlemek için kullanılır.

## Örnekler

### Örnek 1: Bir Dosyadan Veri Okuma
Aşağıdaki örnekte, bir dosyadaki verileri bir diziye okuma işlemi gösterilmektedir:

```bash
# data.txt dosyasının içeriği:
# satır1
# satır2
# satır3

readarray -t my_array < data.txt

# Dizi elemanlarını yazdırma
printf '%s\n' "${my_array[@]}"
```

Bu örnekte, `data.txt` dosyasındaki her bir satır `my_array` dizisine atanır ve `-t` seçeneği sayesinde satır sonu karakterleri kaldırılır.

### Örnek 2: Standart Girdiden Veri Okuma
Aşağıdaki örnekte, kullanıcıdan alınan veriler bir diziye kaydedilmektedir:

```bash
echo "Birden fazla satır girin (çıkmak için Ctrl+D basın):"
readarray -t user_input

# Kullanıcının girdiği verileri yazdırma
printf '%s\n' "${user_input[@]}"
```

Bu örnekte, kullanıcıdan alınan veriler `user_input` dizisine kaydedilir ve kullanıcı Ctrl+D tuşuna basarak girişi sonlandırır.

## İpuçları
- `readarray` komutunu kullanırken, dizinin elemanlarını kontrol etmek için `printf` veya `echo` gibi komutları kullanabilirsiniz.
- Eğer bir dosyadan okuma yapıyorsanız, dosyanın doğru bir şekilde mevcut olduğundan emin olun. Aksi takdirde, `readarray` komutu hata verebilir.
- Dizi elemanlarını işlemek için döngüler kullanarak daha karmaşık işlemler gerçekleştirebilirsiniz.

`readarray`, Bash'de dizilerle çalışmayı kolaylaştıran güçlü bir araçtır ve yukarıdaki bilgilerle etkili bir şekilde kullanılabilir.