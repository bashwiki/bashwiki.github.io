# [리눅스] Bash disown 사용법

## Genel Bakış
`disown` komutu, bir arka plan işlemini (background job) terminalden ayırmak için kullanılır. Bu, kullanıcı terminalden çıkarken veya oturumu kapatırken arka planda çalışan işlemlerin sonlanmamasını sağlar. `disown` komutu, özellikle uzun süren işlemleri terminalden bağımsız hale getirmek isteyen geliştiriciler ve mühendisler için yararlıdır.

## Kullanım
Temel sözdizimi şu şekildedir:

```bash
disown [işlem_numarası]
```

- `işlem_numarası`: (isteğe bağlı) Terminaldeki arka plan işleminin numarasıdır. Eğer belirtilmezse, en son arka plan işlemi disown edilir.

### Yaygın Seçenekler
- `-h`: Bu seçenek, belirtilen işlemi yalnızca terminalden ayırır, ancak işlemin durumu üzerinde herhangi bir değişiklik yapmaz. Yani, işlem hala terminal tarafından izlenir.

## Örnekler

### Örnek 1: Arka Planda Bir İşlem Başlatma ve Disown Etme
```bash
sleep 300 &
disown %1
```
Bu örnekte, `sleep 300` komutu arka planda başlatılır ve ardından `disown` komutu ile terminalden ayrılır. Böylece, terminal kapatılsa bile `sleep` işlemi devam eder.

### Örnek 2: Tüm Arka Plan İşlemlerini Disown Etme
```bash
disown
```
Bu komut, terminaldeki en son arka plan işlemini disown eder. Eğer birden fazla arka plan işlemi varsa, en son başlatılan işlem disown edilir.

## İpuçları
- `jobs` komutunu kullanarak mevcut arka plan işlemlerinin listesini görebilirsiniz. Bu, hangi işlemleri disown etmek istediğinizi belirlemenize yardımcı olur.
- `disown` komutunu kullanmadan önce işleminizin arka planda çalıştığından emin olun. Aksi takdirde, disown işlemi bir etkisi olmayacaktır.
- Eğer bir işlemi disown ettikten sonra tekrar terminalden izlemek isterseniz, bu mümkün değildir. Bu nedenle, disown işlemini dikkatli bir şekilde yapmanız önemlidir.

`disown` komutu, terminalden bağımsız olarak uzun süre çalışan işlemlerle çalışırken oldukça kullanışlıdır. Bu komut sayesinde, terminal oturumunuz kapansa bile işlemlerinizin devam etmesini sağlayabilirsiniz.