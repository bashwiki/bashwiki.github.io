# [리눅스] Bash last 사용법

## Overview
`last` komutu, sistemdeki kullanıcıların oturum açma ve kapama bilgilerini görüntülemek için kullanılır. Bu komut, sistem günlüklerinden (log) yararlanarak, kullanıcıların ne zaman giriş yaptığını, ne kadar süreyle oturum açtığını ve hangi terminal üzerinden bağlandığını gösterir. Genellikle sistem yöneticileri tarafından, kullanıcı aktivitelerini izlemek ve güvenlik denetimleri yapmak amacıyla kullanılır.

## Usage
Temel `last` komutunun sözdizimi şu şekildedir:

```bash
last [options] [username]
```

### Yaygın Seçenekler
- `-a`: Kullanıcıların bağlandığı uzak ana bilgisayar adını gösterir.
- `-n [number]`: Belirtilen sayıda giriş kaydını gösterir. Örneğin, `-n 5` son 5 oturumu gösterir.
- `-x`: Sistem kapanma ve yeniden başlatma bilgilerini de dahil eder.
- `-R`: Uzak ana bilgisayar adını göstermez.

## Examples
### Örnek 1: Tüm kullanıcı oturumlarını görüntüleme
Aşağıdaki komut, sistemdeki tüm kullanıcıların oturum açma ve kapama bilgilerini gösterir:

```bash
last
```

### Örnek 2: Son 3 oturumu görüntüleme
Aşağıdaki komut, yalnızca son 3 oturumu görüntüler:

```bash
last -n 3
```

## Tips
- `last` komutunu kullanırken, çıktının daha okunabilir olması için `less` komutuyla birleştirebilirsiniz. Örneğin:

```bash
last | less
```

- Kullanıcı aktivitelerini izlemek için düzenli olarak `last` komutunu çalıştırmak, sistem güvenliğini artırabilir.
- Eğer belirli bir kullanıcıya ait oturum bilgilerini görmek istiyorsanız, kullanıcı adını komutun sonuna ekleyebilirsiniz. Örneğin:

```bash
last username
```

Bu şekilde, belirli bir kullanıcının oturum geçmişini inceleyebilirsiniz.