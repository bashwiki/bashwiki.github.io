# [Linux] Bash shopt Kullanımı: Bash ortamını yapılandırma

## Genel Bakış
`shopt` komutu, Bash kabuğunun davranışını ve özelliklerini yapılandırmak için kullanılır. Bu komut, belirli özellikleri etkinleştirmek veya devre dışı bırakmak için seçenekler sunar. Kullanıcıların Bash ortamlarını özelleştirmelerine olanak tanır.

## Kullanım
`shopt` komutunun temel sözdizimi aşağıdaki gibidir:

```bash
shopt [seçenekler] [argümanlar]
```

## Yaygın Seçenekler
- `-s`: Belirtilen özelliği etkinleştirir.
- `-u`: Belirtilen özelliği devre dışı bırakır.
- `-p`: Mevcut tüm özelliklerin durumunu listelemek için kullanılır.

## Yaygın Örnekler

### 1. Özellikleri Listeleme
Tüm mevcut özelliklerin durumunu görmek için:

```bash
shopt -p
```

### 2. Genişletilmiş Dosya Adı Tamamlama
Genişletilmiş dosya adı tamamlama özelliğini etkinleştirmek için:

```bash
shopt -s extglob
```

### 3. Geri Dönüşüm Özelliğini Devre Dışı Bırakma
Geri dönüşüm özelliğini devre dışı bırakmak için:

```bash
shopt -u histappend
```

### 4. Küçük/Büyük Harf Duyarsız Arama
Küçük/büyük harf duyarsız arama özelliğini etkinleştirmek için:

```bash
shopt -s nocaseglob
```

## İpuçları
- `shopt -p` komutunu kullanarak mevcut ayarları kontrol etmek, hangi özelliklerin etkin olduğunu anlamanıza yardımcı olabilir.
- Özellikleri etkinleştirirken veya devre dışı bırakırken dikkatli olun; bazı özellikler, komutlarınızın davranışını önemli ölçüde etkileyebilir.
- Özelleştirilmiş ayarlarınızı kalıcı hale getirmek için `.bashrc` dosyanıza `shopt` komutlarını ekleyebilirsiniz.