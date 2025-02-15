# [리눅스] Bash fgrep 사용법

## Genel Bakış
`fgrep`, belirli bir metin parçasını bir dosya içinde aramak için kullanılan bir komuttur. `fgrep`, "fixed grep" anlamına gelir ve arama işlemini sabit bir dize ile gerçekleştirir. Bu, arama sırasında özel karakterlerin yorumlanmadığı anlamına gelir; dolayısıyla, aradığınız metin tam olarak belirtilen biçimde bulunur. `fgrep`, genellikle büyük metin dosyalarında belirli bir kelime veya ifadeyi hızlı bir şekilde bulmak için kullanılır.

## Kullanım
Temel sözdizimi şu şekildedir:

```bash
fgrep [seçenekler] "arama_dizesi" dosya_adı
```

### Yaygın Seçenekler
- `-i`: Büyük/küçük harf duyarsız arama yapar.
- `-v`: Belirtilen dizeyi içermeyen satırları gösterir.
- `-c`: Eşleşen satırların sayısını gösterir.
- `-n`: Eşleşen satırların numaralarını gösterir.
- `-r`: Alt dizinlerdeki dosyalar dahil olmak üzere, belirtilen dizindeki tüm dosyalarda arama yapar.

## Örnekler
### Örnek 1: Basit Arama
Aşağıdaki komut, `metin.txt` dosyasında "örnek" kelimesini arar:

```bash
fgrep "örnek" metin.txt
```

### Örnek 2: Büyük/Küçük Harf Duyarsız Arama
Aşağıdaki komut, "örnek" kelimesini büyük/küçük harf duyarsız olarak arar:

```bash
fgrep -i "örnek" metin.txt
```

## İpuçları
- `fgrep` kullanırken, aradığınız dizeyi tırnak içinde belirtmek, boşluk veya özel karakter içeren dizelerin doğru bir şekilde işlenmesini sağlar.
- Büyük metin dosyalarında arama yaparken, `-c` seçeneğini kullanarak eşleşen satır sayısını hızlıca öğrenebilirsiniz.
- Eğer birden fazla dosyada arama yapıyorsanız, dosya adlarını boşlukla ayırarak belirtebilirsiniz:

```bash
fgrep "örnek" dosya1.txt dosya2.txt
```

Bu bilgilerle `fgrep` komutunu etkili bir şekilde kullanabilir ve metin dosyalarınızda arama işlemlerinizi hızlandırabilirsiniz.