# [리눅스] Bash fg 사용법

## Overview
`fg` komutu, arka planda çalışan bir işlemi (job) ön plana almak için kullanılır. Bu komut, kullanıcıların terminalde arka planda çalışan işlemlerle etkileşimde bulunmalarını sağlar. Genellikle, bir işlemi durdurup (suspend) arka plana aldıktan sonra, bu işlemi tekrar ön plana almak için `fg` komutu kullanılır.

## Usage
Temel kullanım şekli aşağıdaki gibidir:

```bash
fg [job_spec]
```

- `job_spec`: Ön plana almak istediğiniz işlemin numarasını belirtir. Eğer bu parametre belirtilmezse, son durdurulan (suspend) iş ön plana alınır.

## Examples
### Örnek 1: Basit Kullanım
Bir işlemi başlatıp durdurduktan sonra onu ön plana almak için:

```bash
sleep 100 &
# İşlemi arka plana alır.
Ctrl + Z
# İşlemi durdurur ve arka plana alır.
fg
# Durdurulan işlemi ön plana alır.
```

### Örnek 2: Belirli Bir İşlemi Ön Plana Alma
Birden fazla arka planda çalışan işleminiz varsa, belirli bir işlemi ön plana almak için iş numarasını kullanabilirsiniz:

```bash
sleep 100 &
sleep 200 &
jobs
# Çıktı:
# [1]+  12345 Stopped                 sleep 100
# [2]-  12346 Stopped                 sleep 200
fg %1
# İlk işlemi ön plana alır.
```

## Tips
- `jobs` komutunu kullanarak arka planda çalışan işlemlerinizi görüntüleyebilirsiniz. Bu, hangi işlemi ön plana almak istediğinizi belirlemenize yardımcı olur.
- `fg` komutunu kullanmadan önce işleminizin durdurulmuş olduğundan emin olun. Durdurulmamış bir işlemi ön plana almaya çalışmak, hata mesajı almanıza neden olabilir.
- Bir işlemi arka plana alırken `&` karakterini kullanarak işlemi başlatmak, işlemi doğrudan arka planda çalıştırır ve terminali serbest bırakır.