# [리눅스] Bash sleep 사용법

## Overview
`sleep` komutu, belirli bir süre boyunca işlemciyi duraklatmak için kullanılır. Bu komut, genellikle bir betik içinde belirli bir süre beklemek gerektiğinde, zamanlama yapmak için veya bir işlemin tamamlanmasını beklemek için kullanılır. `sleep`, genellikle diğer komutlarla birlikte kullanılarak, belirli bir süre sonra bir işlemi başlatmak için faydalıdır.

## Usage
`sleep` komutunun temel sözdizimi şu şekildedir:

```bash
sleep [süre]
```

### Süre
Süre, beklemek istediğiniz zamanı belirtir. Bu süre, aşağıdaki birimlerle ifade edilebilir:

- `s`: Saniye (varsayılan birim)
- `m`: Dakika
- `h`: Saat
- `d`: Gün

Örneğin, `5m` ifadesi 5 dakika beklemek anlamına gelir.

## Examples
### Örnek 1: 10 Saniye Bekleme
Aşağıdaki komut, 10 saniye bekledikten sonra bir mesaj yazdırır:

```bash
echo "10 saniye bekliyorum..."
sleep 10
echo "Bekleme süresi sona erdi."
```

### Örnek 2: 2 Dakika Bekleme
Bu örnekte, 2 dakika bekledikten sonra bir dosya oluşturulmaktadır:

```bash
echo "2 dakika bekliyorum..."
sleep 2m
touch yeni_dosya.txt
echo "Yeni dosya oluşturuldu: yeni_dosya.txt"
```

## Tips
- `sleep` komutunu, uzun süreli işlemler arasında bekleme süresi eklemek için kullanarak sistem kaynaklarını daha verimli kullanabilirsiniz.
- Betiklerinizi daha okunabilir hale getirmek için, bekleme sürelerini açıklayıcı yorumlarla destekleyin.
- Çok kısa bekleme süreleri (örneğin, milisaniyeler) için `sleep` yerine `usleep` komutunu kullanmayı düşünebilirsiniz. Ancak, `usleep` komutu genellikle daha az yaygındır ve her sistemde mevcut olmayabilir.