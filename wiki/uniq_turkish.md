# [Linux] Bash uniq Kullanımı: Tekil satırları listeleme

## Overview
`uniq` komutu, bir dosyadaki veya standart girdideki ardışık tekrar eden satırları kaldırarak yalnızca benzersiz satırları listelemek için kullanılır. Genellikle, sıralı verilerle birlikte kullanıldığında en etkili sonucu verir.

## Usage
Temel sözdizimi aşağıdaki gibidir:
```
uniq [options] [arguments]
```

## Common Options
- `-c`: Her benzersiz satırın önüne, o satırın kaç kez tekrar ettiğini yazar.
- `-d`: Sadece tekrar eden satırları gösterir.
- `-u`: Sadece benzersiz (tekrar etmeyen) satırları gösterir.
- `-i`: Büyük/küçük harf duyarsız olarak karşılaştırma yapar.

## Common Examples
Aşağıda `uniq` komutunun bazı yaygın kullanım örnekleri bulunmaktadır:

### 1. Temel Kullanım
Bir dosyadaki benzersiz satırları listelemek için:
```bash
uniq dosya.txt
```

### 2. Tekrar Sayısını Gösterme
Her benzersiz satırın tekrar sayısını görmek için:
```bash
uniq -c dosya.txt
```

### 3. Sadece Tekrar Eden Satırları Gösterme
Sadece tekrar eden satırları listelemek için:
```bash
uniq -d dosya.txt
```

### 4. Büyük/Küçük Harf Duyarsız Kullanım
Büyük/küçük harf duyarsız olarak benzersiz satırları listelemek için:
```bash
uniq -i dosya.txt
```

## Tips
- `uniq` komutunu kullanmadan önce verilerinizi sıralamak, daha doğru sonuçlar elde etmenizi sağlar. Bunu `sort` komutuyla yapabilirsiniz:
  ```bash
  sort dosya.txt | uniq
  ```
- `uniq` komutunu bir boru (pipe) ile başka komutlarla birleştirerek daha karmaşık işlemler gerçekleştirebilirsiniz.
- Dosya içeriğini doğrudan bir komutla oluşturup `uniq` ile işlemek için `echo` veya `cat` gibi komutları kullanabilirsiniz.