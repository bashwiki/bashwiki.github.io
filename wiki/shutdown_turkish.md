# [Linux] Bash shutdown Kullanımı: Sistemi kapatma komutu

## Genel Bakış
`shutdown` komutu, bir Linux veya Unix tabanlı sistemde sistemi kapatmak veya yeniden başlatmak için kullanılır. Bu komut, sistem yöneticilerine belirli bir süre içinde veya hemen kapatma işlemi gerçekleştirme imkanı sunar.

## Kullanım
Temel sözdizimi aşağıdaki gibidir:

```bash
shutdown [seçenekler] [argümanlar]
```

## Yaygın Seçenekler
- `-h`: Sistemi kapatır.
- `-r`: Sistemi yeniden başlatır.
- `now`: Hemen kapatma veya yeniden başlatma işlemi yapar.
- `+m`: Belirtilen dakika sayısı kadar bekledikten sonra kapatma veya yeniden başlatma işlemi yapar.
- `hh:mm`: Belirtilen saat ve dakikada kapatma veya yeniden başlatma işlemi yapar.

## Yaygın Örnekler
Aşağıda `shutdown` komutunun bazı pratik kullanım örnekleri bulunmaktadır:

1. Sistemi hemen kapatmak için:
   ```bash
   shutdown -h now
   ```

2. Sistemi 5 dakika sonra kapatmak için:
   ```bash
   shutdown -h +5
   ```

3. Sistemi hemen yeniden başlatmak için:
   ```bash
   shutdown -r now
   ```

4. Sistemi belirli bir saatte kapatmak için (örneğin, 22:30):
   ```bash
   shutdown -h 22:30
   ```

## İpuçları
- Kapatma işlemi gerçekleştirmeden önce açık olan kullanıcı oturumlarını kontrol edin ve gerekli verilerin kaydedildiğinden emin olun.
- Kapatma işlemini iptal etmek için `shutdown -c` komutunu kullanabilirsiniz.
- Sistem kapatma işlemi için bir zamanlayıcı ayarlamak, sistemin düzgün bir şekilde kapanmasını sağlamak için iyi bir uygulamadır.