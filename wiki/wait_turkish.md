# [리눅스] Bash wait 사용법

## Overview
`wait` komutu, bir veya daha fazla arka plan işleminin tamamlanmasını beklemek için kullanılır. Bu komut, özellikle birden fazla işlemi aynı anda çalıştırdığınızda ve bu işlemlerin sonuçlarını almak istediğinizde faydalıdır. `wait`, belirtilen bir işlem kimliğini (PID) veya hiçbir argüman verilmediğinde mevcut shell'deki tüm arka plan işlemlerini bekler.

## Usage
Temel kullanım şekli aşağıdaki gibidir:

```bash
wait [PID...]
```

- **PID**: Beklemek istediğiniz arka plan işleminin işlem kimliğidir. Birden fazla PID belirtebilirsiniz. Eğer hiçbir PID verilmezse, `wait` mevcut shell'deki tüm arka plan işlemlerini bekler.

## Examples
### Örnek 1: Tek bir arka plan işlemini beklemek
Aşağıdaki örnekte, bir arka plan işlemi başlatılır ve ardından `wait` komutu ile bu işlemin tamamlanması beklenir.

```bash
sleep 5 &  # 5 saniye bekleyen bir arka plan işlemi başlat
PID=$!     # Arka plan işleminin PID'sini al
echo "Arka plan işlemi başlatıldı, PID: $PID"
wait $PID  # Belirtilen PID'yi bekle
echo "Arka plan işlemi tamamlandı."
```

### Örnek 2: Birden fazla arka plan işlemini beklemek
Aşağıdaki örnekte, iki arka plan işlemi başlatılır ve her ikisinin de tamamlanması beklenir.

```bash
sleep 3 &  # İlk arka plan işlemi
PID1=$!    # İlk işlemin PID'sini al
sleep 4 &  # İkinci arka plan işlemi
PID2=$!    # İkinci işlemin PID'sini al

echo "İki arka plan işlemi başlatıldı, PID1: $PID1, PID2: $PID2"
wait $PID1 $PID2  # Her iki PID'yi bekle
echo "Her iki arka plan işlemi tamamlandı."
```

## Tips
- `wait` komutunu kullanırken, arka plan işlemlerinin PID'lerini kaydetmek için `$!` değişkenini kullanmayı unutmayın.
- Birden fazla işlemi beklerken, işlemlerin tamamlanma sürelerini göz önünde bulundurarak hangi işlemin daha önce tamamlanacağını tahmin edebilirsiniz.
- `wait` komutu, bir hata oluşursa hata kodunu döndürür. Bu nedenle, `wait` komutunu kullandıktan sonra `$?` değişkenini kontrol ederek işlemin başarılı bir şekilde tamamlanıp tamamlanmadığını kontrol edebilirsiniz.