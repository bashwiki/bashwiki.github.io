# [Linux] Bash groupmod Kullanımı: Grupları yönetmek için

## Genel Bakış
`groupmod` komutu, Linux sistemlerinde mevcut bir grubun özelliklerini değiştirmek için kullanılır. Bu komut, grubun adını veya GID'sini güncelleyerek grup yönetimini kolaylaştırır.

## Kullanım
Temel sözdizimi şu şekildedir:
```bash
groupmod [seçenekler] [argümanlar]
```

## Yaygın Seçenekler
- `-n, --new-name`: Grubun yeni adını belirtir.
- `-g, --gid`: Grubun yeni GID'sini (grup kimliği) ayarlar.
- `-h, --help`: Kullanım bilgilerini gösterir.
- `-o, --non-unique`: GID'nin benzersiz olmamasına izin verir.

## Yaygın Örnekler
Grup adını değiştirmek için:
```bash
groupmod -n yeni_grup_adi eski_grup_adi
```

Grup GID'sini değiştirmek için:
```bash
groupmod -g 1001 grup_adi
```

Grup adını ve GID'sini aynı anda değiştirmek için:
```bash
groupmod -n yeni_grup_adi -g 1001 eski_grup_adi
```

## İpuçları
- Değişiklik yapmadan önce mevcut grup bilgilerini kontrol etmek için `getent group grup_adi` komutunu kullanın.
- Grubun adını veya GID'sini değiştirdikten sonra, bu gruba ait kullanıcıların ayarlarını kontrol edin; bazı durumlarda, kullanıcı ayarlarının güncellenmesi gerekebilir.
- `groupmod` komutunu kullanmadan önce root veya sudo yetkilerine sahip olduğunuzdan emin olun.