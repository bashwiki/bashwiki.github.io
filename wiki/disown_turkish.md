# [Linux] Bash disown Kullanımı: Arka planda çalışan işlemleri terminalden ayırma

## Genel Bakış
`disown` komutu, bir terminal oturumunda çalışan arka plan işlemlerini terminalden ayırarak, bu işlemlerin terminal kapandığında sonlanmasını engeller. Bu, kullanıcıların terminal oturumlarını kapatırken arka planda çalışan işlemlerinin devam etmesini sağlar.

## Kullanım
Temel sözdizimi aşağıdaki gibidir:

```bash
disown [seçenekler] [argümanlar]
```

## Yaygın Seçenekler
- `-h`: Belirtilen işlemi terminalden ayırır, ancak işlemi durdurmaz.
- `-a`: Tüm arka plan işlemlerini terminalden ayırır.
- `-r`: Sadece çalışmakta olan arka plan işlemlerini terminalden ayırır.

## Yaygın Örnekler
Aşağıda `disown` komutunun bazı pratik kullanımları yer almaktadır:

### Örnek 1: Bir işlemi arka planda çalıştırmak ve ayırmak
```bash
sleep 100 &
disown
```
Bu komut, `sleep 100` işlemini arka planda çalıştırır ve ardından terminalden ayırır.

### Örnek 2: Belirli bir işlemi ayırmak
```bash
sleep 200 &
disown %1
```
Bu komut, `sleep 200` işlemini arka planda çalıştırır ve `%1` ile belirtilen ilk arka plan işlemini terminalden ayırır.

### Örnek 3: Tüm arka plan işlemlerini ayırmak
```bash
sleep 300 &
sleep 400 &
disown -a
```
Bu komut, iki `sleep` işlemini arka planda çalıştırır ve ardından tüm arka plan işlemlerini terminalden ayırır.

## İpuçları
- `disown` komutunu kullanmadan önce işleminizin arka planda çalıştığından emin olun. Bunu `&` ile işlemi sonlandırarak yapabilirsiniz.
- `jobs` komutunu kullanarak arka planda çalışan işlemlerinizi kontrol edebilirsiniz.
- `disown` komutunu kullanmak, terminal oturumunuzu kapatırken önemli işlemlerinizin kaybolmamasını sağlar.