# [리눅스] Bash renice 사용법

## Overview
`renice` komutu, çalışan bir işlemin önceliğini değiştirmek için kullanılır. İşletim sistemi, işlem önceliğine göre kaynakları tahsis eder; bu nedenle, bir işlemin önceliğini artırmak veya azaltmak, sistem performansını etkileyebilir. `renice`, özellikle yüksek öncelikli işlemlerin daha fazla CPU zamanı almasını sağlamak veya düşük öncelikli işlemleri yavaşlatmak için yararlıdır.

## Usage
`renice` komutunun temel sözdizimi aşağıdaki gibidir:

```bash
renice [yeni öncelik] -p [işlem ID'si]
```

### Yaygın Seçenekler:
- `-p`: Belirtilen işlem ID'sine (PID) sahip işlemin önceliğini değiştirir.
- `-g`: Belirtilen grup ID'sine (GID) sahip işlemlerin önceliğini değiştirir.
- `-u`: Belirtilen kullanıcıya ait işlemlerin önceliğini değiştirir.

Öncelik değeri, -20 (en yüksek öncelik) ile 19 (en düşük öncelik) arasında bir tam sayı olmalıdır.

## Examples
### Örnek 1: Bir İşlemin Önceliğini Artırma
Aşağıdaki komut, PID'si 1234 olan işlemin önceliğini 10 olarak ayarlayacaktır:

```bash
renice 10 -p 1234
```

### Örnek 2: Belirli Bir Kullanıcıya Ait Tüm İşlemlerin Önceliğini Düşürme
Aşağıdaki komut, "kullanici_adi" adlı kullanıcının tüm işlemlerinin önceliğini 5 olarak ayarlayacaktır:

```bash
renice 5 -u kullanici_adi
```

## Tips
- İşlem önceliğini değiştirirken dikkatli olun; yüksek öncelikli işlemler, sistemin diğer işlemler için yeterli kaynak bulmasını zorlaştırabilir.
- `renice` komutunu çalıştırmak için genellikle root yetkilerine ihtiyaç duyulur, bu nedenle `sudo` kullanmayı unutmayın.
- İşlem önceliğini değiştirmeden önce, mevcut öncelikleri görmek için `ps` veya `top` komutlarını kullanabilirsiniz. Bu, hangi işlemlerin önceliğini değiştireceğinizi belirlemenize yardımcı olur.