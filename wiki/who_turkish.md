# [리눅스] Bash who 사용법

## Overview
`who` komutu, Linux ve Unix tabanlı işletim sistemlerinde, sistemde oturum açmış olan kullanıcıların listesini gösterir. Bu komut, kullanıcıların hangi terminalde oturum açtığını, oturum açma zamanını ve diğer bazı bilgileri görüntüleyerek sistem yöneticilerine ve kullanıcılarına oturum açma durumunu takip etme imkanı sunar.

## Usage
`who` komutunun temel sözdizimi aşağıdaki gibidir:

```
who [seçenekler]
```

### Yaygın Seçenekler
- `-a`: Tüm bilgileri gösterir, kullanıcıların oturum açma durumları, terminal bilgileri ve daha fazlasını içerir.
- `-b`: Sistemin en son yeniden başlatıldığı zamanı gösterir.
- `-q`: Sadece kullanıcıların isimlerini ve toplam kullanıcı sayısını gösterir.

## Examples
1. Temel kullanım:
   ```
   who
   ```
   Bu komut, sistemde oturum açmış olan tüm kullanıcıların listesini gösterir.

2. Tüm bilgileri görüntüleme:
   ```
   who -a
   ```
   Bu komut, kullanıcıların oturum açma bilgileri ile birlikte daha fazla detay sunar.

## Tips
- `who` komutunu sık sık kullanarak sistemdeki aktif kullanıcıları takip edebilir, bu sayede sistem güvenliğini artırabilirsiniz.
- `who` komutunu `grep` ile birleştirerek belirli bir kullanıcıyı aramak için kullanabilirsiniz. Örneğin:
  ```
  who | grep kullanıcı_adı
  ```
  Bu komut, belirli bir kullanıcının oturum açıp açmadığını kontrol etmenize yardımcı olur.