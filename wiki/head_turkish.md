# [리눅스] Bash head 사용법

## Genel Bakış
`head` komutu, bir dosyanın en üst kısmındaki belirli sayıda satırı görüntülemek için kullanılır. Genellikle büyük dosyaların içeriğini hızlıca gözden geçirmek veya dosyanın başındaki önemli bilgileri kontrol etmek için tercih edilir. Varsayılan olarak, `head` komutu bir dosyanın ilk 10 satırını gösterir.

## Kullanım
`head` komutunun temel sözdizimi şu şekildedir:

```bash
head [seçenekler] [dosya_adı]
```

### Yaygın Seçenekler
- `-n [sayı]`: Görüntülenecek satır sayısını belirtir. Örneğin, `-n 5` ifadesi, dosyanın ilk 5 satırını gösterir.
- `-c [bayt]`: Görüntülenecek bayt sayısını belirtir. Örneğin, `-c 100` ifadesi, dosyanın ilk 100 baytını gösterir.
- `-q`: Birden fazla dosya belirtilmişse, dosya adlarını yazdırmadan sadece içeriklerini gösterir.

## Örnekler
### Örnek 1: Bir dosyanın ilk 10 satırını görüntüleme
```bash
head dosya.txt
```
Bu komut, `dosya.txt` dosyasının ilk 10 satırını gösterir.

### Örnek 2: Bir dosyanın ilk 5 satırını görüntüleme
```bash
head -n 5 dosya.txt
```
Bu komut, `dosya.txt` dosyasının ilk 5 satırını gösterir.

### Örnek 3: Bir dosyanın ilk 100 baytını görüntüleme
```bash
head -c 100 dosya.txt
```
Bu komut, `dosya.txt` dosyasının ilk 100 baytını gösterir.

## İpuçları
- `head` komutunu, büyük log dosyalarını veya metin dosyalarını hızlıca incelemek için kullanabilirsiniz. Bu sayede dosyanın başındaki önemli bilgileri kolayca görebilirsiniz.
- `head` komutunu `tail` komutuyla birlikte kullanarak dosyanın hem başını hem de sonunu inceleyebilirsiniz. Örneğin, `head -n 10 dosya.txt | tail -n 5` komutu, dosyanın ilk 10 satırından son 5 satırı gösterir.
- Birden fazla dosya belirtirseniz, her dosyanın içeriği arasında bir ayırıcı olarak dosya adları gösterilecektir. Bu, birden fazla dosyanın içeriğini karşılaştırmak için yararlıdır.