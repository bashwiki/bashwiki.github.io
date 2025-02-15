# [리눅스] Bash gcc 사용법

## Genel Bakış
`gcc` (GNU Compiler Collection), C ve C++ gibi dillerde yazılmış kaynak kodlarını derlemek için kullanılan bir derleyicidir. `gcc`, yazılımcıların yazdığı kodları makine diline çevirerek çalıştırılabilir dosyalar oluşturur. Bu, yazılım geliştirme sürecinin temel bir parçasıdır ve sistem programlama, uygulama geliştirme ve daha fazlası için yaygın olarak kullanılır.

## Kullanım
`gcc` komutunun temel sözdizimi şu şekildedir:

```bash
gcc [seçenekler] [kaynak dosyaları] [-o çıkış dosyası]
```

### Yaygın Seçenekler
- `-o [çıkış dosyası]`: Derleme sonucunda oluşturulacak dosyanın adını belirtir. Varsayılan olarak, derleme sonucu `a.out` adıyla bir dosya oluşturulur.
- `-Wall`: Tüm uyarıları etkinleştirir. Bu, kodunuzdaki potansiyel sorunları tespit etmenize yardımcı olur.
- `-g`: Hata ayıklama bilgilerini ekler. Bu, `gdb` gibi hata ayıklayıcılarla daha iyi bir deneyim sağlar.
- `-O`: Kod optimizasyonu yapar. `-O1`, `-O2`, `-O3` gibi seviyelerle optimizasyon derecesi artırılabilir.

## Örnekler
### Basit Derleme
Aşağıdaki komut, `hello.c` adlı bir kaynak dosyasını derleyerek `hello` adlı çalıştırılabilir bir dosya oluşturur:

```bash
gcc hello.c -o hello
```

### Hata Ayıklama Bilgisi ile Derleme
Aşağıdaki komut, `program.c` adlı dosyayı hata ayıklama bilgileri ile derleyerek `program` adlı bir dosya oluşturur:

```bash
gcc -g program.c -o program
```

## İpuçları
- Derleme sırasında `-Wall` seçeneğini kullanarak tüm uyarıları görmek, kodunuzun kalitesini artırmanıza yardımcı olur.
- Hata ayıklama yaparken `-g` seçeneğini kullanmayı unutmayın, bu sayede hata ayıklayıcılar ile daha etkili bir şekilde çalışabilirsiniz.
- Kodunuzu optimize etmek için `-O` seçeneklerini deneyin, ancak optimizasyonun derleme süresini artırabileceğini unutmayın.
- Birden fazla kaynak dosyasını derlemek için dosya adlarını boşlukla ayırarak listeleyebilirsiniz:

```bash
gcc file1.c file2.c -o output
```

Bu makale, `gcc` komutunun temel kullanımını ve en iyi uygulamalarını anlamanıza yardımcı olmayı amaçlamaktadır.