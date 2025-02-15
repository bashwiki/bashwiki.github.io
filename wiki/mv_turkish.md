# [리눅스] Bash mv 사용법

## Genel Bakış
`mv` komutu, Linux ve Unix tabanlı sistemlerde dosya ve dizinleri taşımak veya yeniden adlandırmak için kullanılan bir komuttur. Bu komut, bir dosyanın veya dizinin yerini değiştirmek veya mevcut bir dosyayı yeni bir isimle yeniden adlandırmak için kullanılır. `mv` komutu, dosya yönetimi işlemlerinde sıkça kullanılan temel bir araçtır.

## Kullanım
Temel sözdizimi şu şekildedir:

```bash
mv [seçenekler] kaynak hedef
```

- **kaynak**: Taşınacak veya yeniden adlandırılacak dosya veya dizin.
- **hedef**: Dosyanın taşınacağı veya yeni adının verileceği yer.

### Yaygın Seçenekler
- `-i`: Hedef dosya zaten mevcutsa, kullanıcıdan onay ister.
- `-u`: Sadece kaynak dosya, hedef dosyadan daha yeni ise taşır.
- `-v`: Taşıma işlemi sırasında hangi dosyaların taşındığını gösterir.

## Örnekler

### Örnek 1: Dosya Taşıma
Bir dosyayı bir dizine taşımak için aşağıdaki komutu kullanabilirsiniz:

```bash
mv dosya.txt /hedef/dizin/
```
Bu komut, `dosya.txt` dosyasını `/hedef/dizin/` dizinine taşır.

### Örnek 2: Dosya Yeniden Adlandırma
Bir dosyanın adını değiştirmek için şu komutu kullanabilirsiniz:

```bash
mv eski_ad.txt yeni_ad.txt
```
Bu komut, `eski_ad.txt` dosyasını `yeni_ad.txt` olarak yeniden adlandırır.

## İpuçları
- Dosyaları taşırken veya yeniden adlandırırken, hedef dosyanın mevcut olup olmadığını kontrol edin. Eğer mevcutsa, `-i` seçeneğini kullanarak yanlışlıkla üzerine yazmaktan kaçınabilirsiniz.
- Büyük dosyalar veya dizinler taşınırken, işlemin tamamlanmasını bekleyin. `-v` seçeneği ile hangi dosyaların taşındığını takip edebilirsiniz.
- Taşıma işlemi sırasında dosya izinlerini kontrol etmek önemlidir. Hedef dizinde yazma izniniz yoksa, taşıma işlemi başarısız olacaktır.

Bu bilgilerle `mv` komutunu etkili bir şekilde kullanabilir ve dosya yönetimi işlemlerinizi kolaylaştırabilirsiniz.