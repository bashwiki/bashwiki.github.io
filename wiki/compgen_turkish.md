# [리눅스] Bash compgen 사용법

## Genel Bakış
`compgen`, Bash kabuğunda kullanılan bir komuttur ve tamamlama (completion) işlemleri için kullanılır. Bu komut, belirli bir kelimenin veya komutun tamamlanması için olası seçenekleri oluşturur. Genellikle, kullanıcıların komutları daha hızlı ve hatasız bir şekilde yazmalarını sağlamak amacıyla kullanılır. Özellikle, kullanıcıların mevcut komutları, dosya adlarını veya değişkenleri hızlı bir şekilde görüntülemelerine olanak tanır.

## Kullanım
`compgen` komutunun temel sözdizimi şu şekildedir:

```bash
compgen [seçenekler] [şartlar]
```

### Yaygın Seçenekler
- `-c`: Mevcut komutları listeler.
- `-d`: Mevcut dizinleri listeler.
- `-e`: Mevcut çevresel değişkenleri listeler.
- `-f`: Mevcut dosya ve dizin adlarını listeler.
- `-A`: Belirli bir türdeki tamamlamaları oluşturur (örneğin, `alias`, `function`, `command` gibi).

## Örnekler
### Örnek 1: Mevcut Komutları Listeleme
Aşağıdaki komut, mevcut komutları listelemek için `compgen` kullanır:

```bash
compgen -c
```

Bu komut, terminalde kullanılabilir tüm komutların bir listesini döndürür.

### Örnek 2: Mevcut Dizinleri Listeleme
Aşağıdaki komut, mevcut dizinleri listelemek için `compgen` kullanır:

```bash
compgen -d
```

Bu komut, geçerli dizindeki tüm alt dizinlerin isimlerini gösterir.

## İpuçları
- `compgen` komutunu, kullanıcı tanımlı komutlar veya alias'lar için de kullanarak, kendi oluşturduğunuz komutları hızlıca görüntüleyebilirsiniz.
- `compgen` ile birlikte `grep` kullanarak belirli bir kelime ile başlayan komutları filtreleyebilirsiniz. Örneğin:

```bash
compgen -c | grep 'git'
```

Bu komut, yalnızca 'git' ile başlayan mevcut komutları listeleyecektir.
- Tamamlamaları daha etkin kullanmak için, `compgen` komutunu bir fonksiyon içinde kullanarak özelleştirilmiş tamamlamalar oluşturabilirsiniz.