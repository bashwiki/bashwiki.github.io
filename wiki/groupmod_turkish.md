# [리눅스] Bash groupmod 사용법

## Genel Bakış
`groupmod` komutu, Linux sistemlerinde mevcut bir grup üzerinde değişiklik yapmak için kullanılır. Bu komut, grup adını değiştirmek veya grup kimliğini (GID) güncellemek gibi işlemleri gerçekleştirmek için tasarlanmıştır. Sistem yöneticileri için, kullanıcı gruplarını yönetmek ve sistemdeki erişim kontrolünü düzenlemek açısından önemli bir araçtır.

## Kullanım
`groupmod` komutunun temel sözdizimi aşağıdaki gibidir:

```bash
groupmod [seçenekler] grup_adı
```

### Yaygın Seçenekler
- `-n, --new-name`: Grubun yeni adını belirtir.
- `-g, --gid`: Grubun yeni grup kimliğini (GID) belirtir. GID, grubun sistemdeki benzersiz tanımlayıcısıdır.

## Örnekler

### Örnek 1: Grup Adını Değiştirme
Aşağıdaki komut, mevcut "eski_grup" adındaki grubun adını "yeni_grup" olarak değiştirecektir:

```bash
sudo groupmod -n yeni_grup eski_grup
```

### Örnek 2: Grup GID'sini Değiştirme
Aşağıdaki komut, "ornek_grup" adlı grubun GID'sini 1001 olarak güncelleyecektir:

```bash
sudo groupmod -g 1001 ornek_grup
```

## İpuçları
- `groupmod` komutunu kullanmadan önce, grubun mevcut adını ve GID'sini kontrol etmek için `getent group` komutunu kullanabilirsiniz.
- Değişikliklerin etkili olabilmesi için, grup üzerinde işlem yapmadan önce ilgili kullanıcıların oturumlarını kapatmaları gerekebilir.
- Grubun adını veya GID'sini değiştirdikten sonra, bu gruba ait kullanıcıların izinlerini ve erişimlerini kontrol etmek önemlidir.