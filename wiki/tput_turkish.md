# [리눅스] Bash tput 사용법

## Genel Bakış
`tput`, terminal üzerinde çeşitli özellikleri kontrol etmek ve ayarlamak için kullanılan bir Bash komutudur. Bu komut, terminalin görünümünü ve davranışını değiştirmek için ANSI kaçış dizilerini kullanarak, metin biçimlendirme, renk ayarlama ve ekran kontrolü gibi işlemleri gerçekleştirmeye olanak tanır. `tput`, özellikle terminal tabanlı uygulamalar geliştiren mühendisler ve geliştiriciler için yararlıdır.

## Kullanım
`tput` komutunun temel sözdizimi şu şekildedir:

```bash
tput [seçenekler]
```

### Yaygın Seçenekler
- `setaf [numara]`: Metin rengini ayarlamak için kullanılır. Renk numarası 0-7 arasında bir değer alır.
- `setab [numara]`: Arka plan rengini ayarlamak için kullanılır. Renk numarası 0-7 arasında bir değer alır.
- `bold`: Metni kalın yapmak için kullanılır.
- `clear`: Terminal ekranını temizler.
- `cup [satır] [sütun]`: İmleci belirtilen satır ve sütuna taşır.

## Örnekler

### Örnek 1: Metin Rengini Değiştirme
Aşağıdaki komut, metin rengini yeşil yapmak için kullanılabilir:

```bash
tput setaf 2; echo "Bu yeşil bir metin."; tput sgr0
```
Bu komut, metni yeşil renkte yazdırır ve ardından varsayılan ayarlara geri döner.

### Örnek 2: Ekranı Temizleme
Terminal ekranını temizlemek için şu komutu kullanabilirsiniz:

```bash
tput clear
```
Bu komut, terminal ekranını temizler ve imleci en üst satıra taşır.

## İpuçları
- `tput` komutunu kullanmadan önce terminalinizin desteklediği renk ve özellikleri kontrol edin. Bazı terminal emülatörleri tüm renkleri desteklemeyebilir.
- `tput` ile birden fazla özellik ayarlamak için komutları birleştirebilirsiniz. Örneğin, metni kalın ve kırmızı yapmak için:

```bash
tput bold; tput setaf 1; echo "Bu kalın ve kırmızı bir metin."; tput sgr0
```
- Terminal uygulamalarınızda kullanıcı deneyimini geliştirmek için `tput` komutunu kullanarak görsel geri bildirimler sağlayabilirsiniz.