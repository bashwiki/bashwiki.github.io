# [Linux] Bash id Kullanımı: Kullanıcı kimliğini gösterir

## Genel Bakış
`id` komutu, Linux ve Unix tabanlı sistemlerde mevcut kullanıcının veya belirtilen bir kullanıcının kimlik bilgilerini gösterir. Bu bilgiler arasında kullanıcı kimliği (UID), grup kimliği (GID) ve kullanıcının ait olduğu gruplar yer alır.

## Kullanım
Temel sözdizimi aşağıdaki gibidir:

```bash
id [seçenekler] [argümanlar]
```

## Yaygın Seçenekler
- `-u`: Sadece kullanıcı kimliğini (UID) gösterir.
- `-g`: Sadece grup kimliğini (GID) gösterir.
- `-G`: Kullanıcının ait olduğu tüm grup kimliklerini gösterir.
- `-n`: Kullanıcı veya grup adını gösterir.
- `-r`: Gerçek GID veya UID'yi gösterir (eğer bir geçici GID veya UID varsa).

## Yaygın Örnekler
Aşağıda `id` komutunun bazı pratik örnekleri bulunmaktadır:

1. Mevcut kullanıcının kimlik bilgilerini görüntülemek için:
   ```bash
   id
   ```

2. Belirli bir kullanıcının kimlik bilgilerini görüntülemek için (örneğin, "ali" kullanıcısı):
   ```bash
   id ali
   ```

3. Sadece mevcut kullanıcının UID'sini görüntülemek için:
   ```bash
   id -u
   ```

4. Mevcut kullanıcının GID'sini görüntülemek için:
   ```bash
   id -g
   ```

5. Mevcut kullanıcının ait olduğu grup kimliklerini görüntülemek için:
   ```bash
   id -G
   ```

## İpuçları
- `id` komutunu kullanarak bir kullanıcının hangi gruplara ait olduğunu hızlıca öğrenebilirsiniz.
- Eğer bir kullanıcı adı yerine UID kullanıyorsanız, `id` komutunu UID ile birlikte kullanarak o kullanıcıya ait bilgileri alabilirsiniz.
- `id` komutunu sık sık kullanıyorsanız, çıktıyı daha okunabilir hale getirmek için `grep` veya `awk` gibi diğer komutlarla birleştirebilirsiniz.