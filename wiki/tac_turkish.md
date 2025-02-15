# [리눅스] Bash tac 사용법

## Genel Bakış
`tac` komutu, bir dosyanın içeriğini ters sırada görüntülemek için kullanılan bir Bash komutudur. "cat" komutunun tersine çalışarak, dosyadaki satırları alt alta değil, en son satırdan başlayarak yukarı doğru sıralar. Bu, özellikle dosya içeriğini ters sırada incelemek isteyen mühendisler ve geliştiriciler için faydalıdır.

## Kullanım
Temel `tac` komutunun sözdizimi aşağıdaki gibidir:

```bash
tac [seçenekler] [dosya_adı]
```

### Yaygın Seçenekler
- `-r`, `--regex`: Girdi dosyasındaki satırları bir düzenli ifade ile eşleştirerek ters sırada görüntüler.
- `-s`, `--separator`: Satırları ayırmak için özel bir ayırıcı belirlemenizi sağlar. Varsayılan ayırıcı yeni satırdır.

## Örnekler
### Örnek 1: Basit Kullanım
Bir dosyanın içeriğini ters sırada görüntülemek için `tac` komutunu kullanabilirsiniz:

```bash
tac dosya.txt
```
Bu komut, `dosya.txt` dosyasındaki satırları ters sırada gösterir.

### Örnek 2: Özel Ayırıcı ile Kullanım
Bir dosyadaki satırları özel bir ayırıcı ile ters sırada görüntülemek için `-s` seçeneğini kullanabilirsiniz:

```bash
tac -s ',' dosya.csv
```
Bu komut, `dosya.csv` dosyasındaki satırları virgül ile ayırarak ters sırada gösterir.

## İpuçları
- `tac` komutunu büyük dosyalarla kullanırken, çıktıyı bir dosyaya yönlendirmek performansı artırabilir. Örneğin:

```bash
tac büyük_dosya.txt > ters_büyük_dosya.txt
```
Bu komut, `büyük_dosya.txt` dosyasının ters sıralanmış içeriğini `ters_büyük_dosya.txt` dosyasına kaydeder.

- `tac` komutunu diğer komutlarla birleştirerek daha karmaşık işlemler gerçekleştirebilirsiniz. Örneğin, `grep` ile belirli bir deseni arayıp ardından ters sırada görüntülemek:

```bash
grep 'desen' dosya.txt | tac
```

Bu komut, `dosya.txt` dosyasında 'desen' kelimesini içeren satırları bulur ve bunları ters sırada gösterir.