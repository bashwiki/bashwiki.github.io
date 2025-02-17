# [Linux] Bash bg Kullanımı: Arka planda çalışan işlemleri devam ettirir

## Overview
`bg` komutu, terminalde duraklatılmış bir işlemi arka planda çalıştırmak için kullanılır. Bu, kullanıcıların terminali kullanmaya devam ederken işlemlerin arka planda sürdürülmesine olanak tanır.

## Usage
Temel sözdizimi şu şekildedir:
```bash
bg [options] [job_spec]
```

## Common Options
- `job_spec`: Arka planda çalıştırılacak işlemi belirtir. Bu, iş numarası veya iş adı olabilir.
- `-n`: İşin arka planda çalıştırılmasını sağlarken, çıktısını terminale yönlendirmeden yapar.

## Common Examples
1. Duraklatılmış bir işlemi arka planda çalıştırmak:
   ```bash
   bg %1
   ```
   Bu komut, iş numarası 1 olan duraklatılmış işlemi arka planda devam ettirir.

2. Tüm duraklatılmış işlemleri arka planda çalıştırmak:
   ```bash
   bg
   ```
   Bu komut, mevcut tüm duraklatılmış işlemleri arka planda çalıştırır.

3. Belirli bir işlemi arka planda çalıştırırken çıktı yönlendirmesi yapmak:
   ```bash
   bg -n %2
   ```
   Bu komut, iş numarası 2 olan duraklatılmış işlemi arka planda çalıştırır ve çıktısını terminale yönlendirmez.

## Tips
- İşlerinizi yönetmek için `jobs` komutunu kullanarak hangi işlemlerin duraklatıldığını görebilirsiniz.
- `fg` komutunu kullanarak arka planda çalışan bir işlemi tekrar ön plana alabilirsiniz.
- İş numaralarını kullanarak belirli bir işlemi hedeflemek, yönetimi kolaylaştırır.