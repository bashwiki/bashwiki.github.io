# [리눅스] Bash timeout 사용법

## Genel Bakış
`timeout` komutu, belirli bir süre boyunca bir komutun çalışmasına izin veren ve bu süre dolduğunda komutu otomatik olarak sonlandıran bir araçtır. Bu, uzun süren işlemleri kontrol altında tutmak ve sistem kaynaklarını verimli bir şekilde yönetmek için kullanışlıdır. Özellikle, bir komutun beklenmedik şekilde sonsuza kadar çalışmasını önlemek için idealdir.

## Kullanım
`timeout` komutunun temel sözdizimi şu şekildedir:

```bash
timeout [SEÇENEKLER] SÜRE KOMUT [ARGÜMANLAR]
```

### Yaygın Seçenekler
- `SÜRE`: Komutun çalışmasına izin verilen süreyi belirtir. Bu süre, `s` (saniye), `m` (dakika), `h` (saat) veya `d` (gün) ile birim olarak ifade edilebilir. Örneğin, `30s` 30 saniye, `1m` 1 dakika anlamına gelir.
- `-k SÜRE`: Komut zaman aşımına uğradıktan sonra, belirtilen süre boyunca (bu süre içinde) komutun sonlandırılmadan önce bir sinyal almasını sağlar.
- `-s SİNYAL`: Komuta gönderilecek sinyali belirtir. Varsayılan olarak `TERM` sinyali gönderilir.

## Örnekler
### Örnek 1: Basit Kullanım
Aşağıdaki komut, `sleep` komutunu 5 saniye boyunca çalıştırır. Eğer 5 saniye içinde bitmezse, komut otomatik olarak sonlandırılır.

```bash
timeout 5s sleep 10
```
Bu durumda, `sleep` komutu 10 saniye sürecek olsa da, `timeout` onu 5 saniye sonra sonlandıracaktır.

### Örnek 2: Sinyal Gönderme
Aşağıdaki komut, `sleep` komutunu 5 saniye boyunca çalıştırır ve zaman aşımına uğradığında `KILL` sinyali gönderir.

```bash
timeout -s KILL 5s sleep 10
```
Bu durumda, `sleep` komutu 5 saniye sonra `KILL` sinyali ile sonlandırılacaktır.

## İpuçları
- Zaman aşımını ayarlarken, komutun beklenen çalışma süresini göz önünde bulundurun. Çok kısa bir süre belirlemek, komutun beklenmedik bir şekilde sonlanmasına neden olabilir.
- `-k` seçeneğini kullanarak, komutun sonlanmadan önce belirli bir süre daha çalışmasına izin verebilirsiniz. Bu, bazı durumlarda önemli olabilir.
- Uzun süren işlemler için `timeout` kullanarak sistem kaynaklarınızı koruyabilir ve beklenmedik durumlarla başa çıkabilirsiniz.