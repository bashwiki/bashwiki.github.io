# [리눅스] Bash cd 사용법

## Genel Bakış
`cd` (change directory) komutu, Linux ve Unix tabanlı işletim sistemlerinde kullanılan bir komuttur. Bu komut, kullanıcıların dosya sisteminde dizinler arasında geçiş yapmalarını sağlar. `cd` komutunu kullanarak, terminalde bulunduğunuz dizini değiştirebilir ve dosya veya klasörlere erişim sağlayabilirsiniz.

## Kullanım
`cd` komutunun temel sözdizimi aşağıdaki gibidir:

```bash
cd [seçenekler] [hedef_dizin]
```

### Yaygın Seçenekler
- `..`: Bir üst dizine geçiş yapar.
- `~`: Kullanıcının ana dizinine geçiş yapar.
- `-`: Önceki dizine geri döner.

## Örnekler
### Örnek 1: Ana Dizin
Kullanıcının ana dizinine geçmek için:

```bash
cd ~
```

### Örnek 2: Üst Dizin
Bir üst dizine geçmek için:

```bash
cd ..
```

### Örnek 3: Belirli Bir Dizin
Belirli bir dizine geçmek için, dizinin tam yolunu belirtebilirsiniz:

```bash
cd /home/kullanici/dokumanlar
```

## İpuçları
- `cd` komutunu kullanırken, dizin adlarını tam olarak yazmak yerine otomatik tamamlama özelliğini kullanmak için `Tab` tuşuna basabilirsiniz.
- Dizin değiştirirken, dizin adlarının büyük/küçük harf duyarlı olduğunu unutmayın.
- Uzun dizin yollarını daha kolay yönetmek için, `~` karakterini kullanarak ana dizin yolunu kısaltabilirsiniz.
- Önceki dizine geri dönmek için `cd -` komutunu kullanarak hızlı bir geçiş yapabilirsiniz.