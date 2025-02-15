# [리눅스] Bash jobs 사용법

## Overview
`jobs` komutu, mevcut terminal oturumunda çalışan arka plan işlemlerini listelemek için kullanılır. Bu komut, kullanıcıların hangi işlemlerin arka planda çalıştığını görmesine ve bu işlemler üzerinde işlem yapmasına olanak tanır. Genellikle, bir terminal oturumunda birden fazla işlem çalıştırıldığında, bu işlemleri yönetmek için kullanılır.

## Usage
`jobs` komutunun temel sözdizimi şu şekildedir:

```bash
jobs [options]
```

### Yaygın Seçenekler
- `-l`: Her bir işlemin PID'sini (Process ID) gösterir.
- `-n`: Sadece durum değişikliği olan işleri listeler.
- `-p`: Sadece işlemlerin PID'lerini gösterir.

## Examples
### Örnek 1: Temel Kullanım
Terminalde birkaç işlem çalıştırdıktan sonra, arka planda hangi işlemlerin çalıştığını görmek için `jobs` komutunu kullanabilirsiniz:

```bash
$ sleep 100 &
[1] 12345
$ sleep 200 &
[2] 12346
$ jobs
[1]+  Running                 sleep 100 &
[2]-  Running                 sleep 200 &
```

Bu örnekte, iki `sleep` işlemi arka planda çalışmaktadır.

### Örnek 2: PID ile Listeleme
Eğer işlemlerin PID'lerini görmek istiyorsanız, `-l` seçeneğini kullanabilirsiniz:

```bash
$ jobs -l
[1]+  12345 Running                 sleep 100 &
[2]-  12346 Running                 sleep 200 &
```

Bu komut, her bir işlemin PID'si ile birlikte durumunu gösterir.

## Tips
- Arka planda çalışan işlemleri yönetmek için `fg` ve `bg` komutları ile birlikte `jobs` komutunu kullanabilirsiniz. Örneğin, bir işlemi ön plana almak için `fg %1` komutunu kullanabilirsiniz.
- İşlemleri takip etmek için `jobs` komutunu düzenli olarak kullanmak, hangi işlemlerin aktif olduğunu anlamanızı kolaylaştırır.
- Eğer bir işlemi durdurmak isterseniz, `Ctrl + Z` tuş kombinasyonunu kullanarak işlemi durdurabilir ve ardından `bg` komutuyla arka plana alabilirsiniz.