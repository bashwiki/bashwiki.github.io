# [리눅스] Bash basename 사용법

## Genel Bakış
`basename` komutu, bir dosya yolunun son kısmını (dosya adını) almak için kullanılır. Bu komut, genellikle bir dosya yolunun tam adresinden yalnızca dosya adını çıkarmak için kullanılır. Özellikle script yazarken veya dosya işlemleri gerçekleştirirken, dosya adını izole etmek için oldukça yararlıdır.

## Kullanım
`basename` komutunun temel sözdizimi şu şekildedir:

```bash
basename [YOL] [UZANTI]
```

- **YOL**: İşlem yapmak istediğiniz dosya veya dizin yolunu belirtir.
- **UZANTI**: (isteğe bağlı) Dosya adından kaldırılacak uzantıyı belirtir. Eğer bu argüman verilirse, belirtilen uzantı dosya adından çıkarılır.

### Yaygın Seçenekler
`basename` komutunun kendine özgü seçenekleri yoktur, ancak yukarıda belirtilen argümanlar ile birlikte kullanılabilir.

## Örnekler

### Örnek 1: Basit Kullanım
Bir dosya yolundan yalnızca dosya adını almak için:

```bash
basename /home/kullanici/dosya.txt
```
Bu komutun çıktısı:
```
dosya.txt
```

### Örnek 2: Uzantı Kaldırma
Bir dosya adından belirli bir uzantıyı kaldırmak için:

```bash
basename /home/kullanici/dosya.txt .txt
```
Bu komutun çıktısı:
```
dosya
```

## İpuçları
- `basename` komutunu, dosya adlarını işlerken ve dosya yollarını yönetirken kullanmak, kodunuzu daha okunabilir hale getirebilir.
- Uzantıyı kaldırmak için doğru uzantıyı belirttiğinizden emin olun; aksi takdirde beklenmedik sonuçlar alabilirsiniz.
- `basename` komutunu bir script içinde kullanarak, dinamik dosya adları oluşturabilir veya dosya işlemlerini otomatikleştirebilirsiniz.