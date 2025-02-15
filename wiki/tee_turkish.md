# [리눅스] Bash tee 사용법

## Genel Bakış
`tee` komutu, standart girdi akışını (stdin) hem ekrana (standart çıktı) hem de bir veya daha fazla dosyaya yönlendirmek için kullanılır. Bu komut, bir komutun çıktısını hem görüntülemek hem de kaydetmek isteyen mühendisler ve geliştiriciler için oldukça faydalıdır. `tee`, genellikle bir komutun çıktısını bir dosyaya kaydederken aynı zamanda bu çıktıyı terminalde görüntülemek için kullanılır.

## Kullanım
Temel `tee` komutunun sözdizimi şu şekildedir:

```bash
tee [seçenekler] [dosya...]
```

### Yaygın Seçenekler
- `-a`, `--append`: Çıktıyı belirtilen dosyaya ekler. Varsayılan olarak, `tee` dosyayı her çalıştırıldığında üzerine yazar.
- `-i`, `--ignore-interrupts`: Kesme sinyallerini yok sayar. Bu, komutun kesintisiz çalışmasını sağlar.

## Örnekler

### Örnek 1: Basit Kullanım
Aşağıdaki komut, `echo` komutunun çıktısını hem ekrana yazdırır hem de `output.txt` dosyasına kaydeder:

```bash
echo "Merhaba, Dünya!" | tee output.txt
```

Bu komut çalıştırıldığında, "Merhaba, Dünya!" ifadesi terminalde görüntülenir ve aynı zamanda `output.txt` dosyasına kaydedilir.

### Örnek 2: Dosyaya Ekleme
Aşağıdaki komut, `output.txt` dosyasına yeni bir satır ekler:

```bash
echo "Yeni bir satır" | tee -a output.txt
```

Bu komut, `output.txt` dosyasının sonuna "Yeni bir satır" ifadesini eklerken, aynı zamanda bu ifadeyi terminalde de görüntüler.

## İpuçları
- `tee` komutunu kullanırken, dosya adlarını belirtirken tam yol kullanmak, dosyanın doğru yerde oluşturulmasını sağlar.
- Birden fazla dosyaya yazmak için dosya adlarını boşlukla ayırarak belirtebilirsiniz. Örneğin: `tee dosya1.txt dosya2.txt`.
- Çıktıyı bir dosyaya kaydetmeden önce, `cat` veya `less` gibi komutlarla çıktıyı inceleyerek doğru veriyi kaydettiğinizden emin olun.

`tee` komutu, çıktıyı hem görüntülemek hem de kaydetmek isteyenler için oldukça kullanışlı bir araçtır. Bu komut sayesinde, komut satırında çalışırken verilerinizi kolayca yönetebilirsiniz.