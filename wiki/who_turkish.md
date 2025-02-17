# [Linux] Bash who Kullanımı: Kullanıcı bilgilerini görüntüleme

## Genel Bakış
`who` komutu, sistemde oturum açmış olan kullanıcıların bilgilerini görüntülemek için kullanılır. Bu komut, kullanıcı adı, oturum açma zamanı ve terminal bilgileri gibi detayları sağlar.

## Kullanım
Temel sözdizimi aşağıdaki gibidir:
```
who [seçenekler] [argümanlar]
```

## Yaygın Seçenekler
- `-b`: Sistemin en son ne zaman başlatıldığını gösterir.
- `-q`: Sadece kullanıcı adlarını ve toplam kullanıcı sayısını gösterir.
- `-H`: Başlık satırını gösterir, yani sütun adlarını ekler.

## Yaygın Örnekler
Aşağıda `who` komutunun bazı pratik örnekleri bulunmaktadır:

### Örnek 1: Tüm oturum açmış kullanıcıları görüntüleme
```bash
who
```

### Örnek 2: Sistemin en son ne zaman başlatıldığını gösterme
```bash
who -b
```

### Örnek 3: Sadece kullanıcı adlarını ve toplam kullanıcı sayısını görüntüleme
```bash
who -q
```

### Örnek 4: Başlık satırını göstererek kullanıcı bilgilerini görüntüleme
```bash
who -H
```

## İpuçları
- `who` komutunu sık sık kullanarak sistemdeki aktif kullanıcıları takip edebilirsiniz.
- `-H` seçeneği ile çıktıyı daha okunabilir hale getirebilirsiniz.
- Eğer belirli bir kullanıcı hakkında bilgi almak istiyorsanız, `who | grep kullanıcı_adı` komutunu kullanabilirsiniz.