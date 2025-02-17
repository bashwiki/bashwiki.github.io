# [Linux] Bash fg Kullanımı: Arka planda çalışan bir işlemi ön plana çıkarma

## Overview
`fg` komutu, arka planda çalışan bir işlemi ön plana çıkararak kullanıcıya kontrol imkanı tanır. Bu, terminalde başlatılan bir işlemi durdurup, onu tekrar aktif hale getirerek etkileşimde bulunmayı sağlar.

## Usage
Temel sözdizimi aşağıdaki gibidir:

```bash
fg [işlem_numarası]
```

## Common Options
- `işlem_numarası`: Ön plana çıkarılacak işlemin numarasını belirtir. Eğer belirtilmezse, en son arka planda çalışan işlem ön plana çıkarılır.

## Common Examples
1. En son arka planda çalışan işlemi ön plana çıkarma:
   ```bash
   fg
   ```

2. Belirli bir işlem numarasını kullanarak ön plana çıkarma (örneğin, 1 numaralı işlem):
   ```bash
   fg %1
   ```

3. Arka planda çalışan işlemleri listeleme ve ardından birini ön plana çıkarma:
   ```bash
   jobs
   fg %2
   ```

## Tips
- `fg` komutunu kullanmadan önce `jobs` komutunu çalıştırarak hangi işlemlerin arka planda olduğunu kontrol etmek faydalı olabilir.
- İşlemi ön plana çıkardıktan sonra, işlemi durdurmak için `Ctrl + Z` tuş kombinasyonunu kullanabilirsiniz. Bu, işlemi arka plana alır.
- `bg` komutunu kullanarak bir işlemi arka planda çalışmaya devam ettirebilir ve ardından `fg` ile tekrar ön plana çıkarabilirsiniz.