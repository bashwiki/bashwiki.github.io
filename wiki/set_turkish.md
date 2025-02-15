# [리눅스] Bash set 사용법

## Overview
`set` komutu, Bash kabuğunda çeşitli ayarları yapılandırmak ve kontrol etmek için kullanılır. Bu komut, kabuk ortamının davranışını değiştirmek ve belirli özellikleri etkinleştirmek veya devre dışı bırakmak için kullanılır. Örneğin, hata ayıklama, fonksiyonların davranışları ve değişkenlerin özellikleri gibi çeşitli ayarları yönetmek için `set` komutunu kullanabilirsiniz.

## Usage
`set` komutunun temel sözdizimi şu şekildedir:

```bash
set [OPTION] [VALUE]
```

### Yaygın Seçenekler
- `-e`: Komutların hata durumunda durmasını sağlar. Bir komut hata verirse, sonraki komutlar çalıştırılmaz.
- `-u`: Tanımsız değişkenler kullanıldığında hata verir. Bu, kodun daha güvenli olmasını sağlar.
- `-x`: Komutları çalıştırmadan önce ekrana yazdırır. Hata ayıklama için faydalıdır.
- `-o`: Belirli bir seçenek etkinleştirmek veya devre dışı bırakmak için kullanılır. Örneğin, `set -o noclobber` mevcut dosyaların üzerine yazılmasını engeller.

## Examples
### Örnek 1: Hata Durumunda Durdurma
Aşağıdaki komut, bir hata oluştuğunda scriptin durmasını sağlar:

```bash
set -e
echo "Bu komut çalışacak."
false  # Bu komut hata verecek
echo "Bu komut çalışmayacak."  # Bu komut çalışmayacak
```

### Örnek 2: Tanımsız Değişken Hatası
Tanımsız bir değişken kullanıldığında hata vermesini sağlamak için:

```bash
set -u
echo "Değişkenin değeri: $MY_VAR"  # MY_VAR tanımsız olduğu için hata verecek
```

## Tips
- `set -e` ve `set -u` kullanarak scriptlerinizi daha güvenli hale getirebilirsiniz. Bu, beklenmeyen hataların önüne geçer.
- Hata ayıklama sırasında `set -x` kullanarak hangi komutların çalıştığını görmek, sorunları daha hızlı çözmenize yardımcı olabilir.
- `set` komutunu kullanmadan önce, hangi seçeneklerin etkin olduğunu kontrol etmek için `set` komutunu tek başına çalıştırabilirsiniz. Bu, mevcut ayarları görüntüler.