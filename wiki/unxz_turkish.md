# [리눅스] Bash unxz 사용법

## Genel Bakış
`unxz`, XZ sıkıştırma formatında olan dosyaları açmak için kullanılan bir Bash komutudur. Bu komut, XZ sıkıştırmasıyla oluşturulmuş dosyaları çözerek orijinal dosyaların geri kazanılmasını sağlar. `unxz`, genellikle büyük veri dosyalarının depolanması ve iletilmesi sırasında sıkıştırma işlemleri için kullanılır.

## Kullanım
Temel sözdizimi şu şekildedir:

```bash
unxz [seçenekler] [dosya_adı.xz]
```

### Yaygın Seçenekler
- `-k`, `--keep`: Orijinal sıkıştırılmış dosyayı silmeden açar. Varsayılan olarak, `unxz` dosyayı açtıktan sonra sıkıştırılmış dosyayı siler.
- `-f`, `--force`: Var olan dosyaların üzerine yazmak için zorlar. Eğer hedef dosya zaten mevcutsa, bu seçenek ile üzerine yazılmasını sağlayabilirsiniz.

## Örnekler

### Örnek 1: Basit Kullanım
Bir `data.xz` dosyasını açmak için aşağıdaki komutu kullanabilirsiniz:

```bash
unxz data.xz
```
Bu komut, `data.xz` dosyasını açacak ve orijinal dosyayı (örneğin `data`) oluşturacaktır.

### Örnek 2: Orijinal Dosyayı Koruma
Eğer `data.xz` dosyasını açarken orijinal sıkıştırılmış dosyayı korumak istiyorsanız, `-k` seçeneğini kullanabilirsiniz:

```bash
unxz -k data.xz
```
Bu komut, `data.xz` dosyasını açacak ve aynı zamanda orijinal dosyayı da saklayacaktır.

## İpuçları
- Sıkıştırılmış dosyalarınızı açmadan önce, dosyanın doğru bir şekilde sıkıştırıldığından emin olun. Hatalı veya bozuk dosyalar açılmayabilir.
- `unxz` komutunu kullanmadan önce, dosya sisteminizde yeterli boş alan olduğundan emin olun. Açılan dosya, sıkıştırılmış dosyadan daha büyük olabilir.
- Eğer sıkıştırılmış dosyalarınızı sık sık kullanıyorsanız, `-k` seçeneğini tercih ederek orijinal dosyaları kaybetmemek iyi bir uygulamadır.

Bu bilgilerle `unxz` komutunu etkili bir şekilde kullanabilirsiniz.