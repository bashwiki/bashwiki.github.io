# [리눅스] Bash nohup 사용법

## Genel Bakış
`nohup` (no hang up) komutu, bir komutun veya programın terminalden bağımsız olarak çalışmasını sağlar. Terminal oturumu kapatılsa bile, `nohup` ile başlatılan süreçler arka planda çalışmaya devam eder. Bu, özellikle uzun süren işlemleri başlatırken ve terminal oturumunu kapatmayı planlarken faydalıdır.

## Kullanım
Temel `nohup` komutunun sözdizimi şu şekildedir:

```bash
nohup [komut] [argümanlar] &
```

- `komut`: Çalıştırmak istediğiniz komut veya program.
- `argümanlar`: Komutun alacağı opsiyonel argümanlar.
- `&`: Komutun arka planda çalışmasını sağlar.

### Yaygın Seçenekler
- `-o [dosya]`: Çıktının yönlendirileceği dosya. Varsayılan olarak `nohup.out` dosyasına yönlendirilir.
- `-h`: Yardım bilgilerini gösterir.

## Örnekler

### Örnek 1: Basit bir komut çalıştırma
Aşağıdaki komut, `my_script.sh` adlı bir betiği arka planda çalıştırır ve çıktısını `nohup.out` dosyasına kaydeder:

```bash
nohup bash my_script.sh &
```

### Örnek 2: Çıktıyı özel bir dosyaya yönlendirme
Aşağıdaki komut, `long_running_process` adlı bir programı çalıştırır ve çıktısını `output.log` dosyasına yönlendirir:

```bash
nohup long_running_process > output.log 2>&1 &
```
Burada `2>&1`, hata çıktısını da aynı dosyaya yönlendirmek için kullanılır.

## İpuçları
- `nohup` kullanırken, çıktıyı yönlendirmek için `>` operatörünü kullanmayı unutmayın. Aksi takdirde, varsayılan olarak `nohup.out` dosyasına yazılır.
- Uzun süren işlemler için `nohup` kullanmak, terminal oturumunu kapatmanıza olanak tanır. Ancak, işlemin durumunu kontrol etmek için arka planda çalışan süreçlerinizi takip etmeyi unutmayın.
- `jobs` komutu ile arka planda çalışan işlemlerinizi listeleyebilir ve `fg` komutu ile bunları ön plana alabilirsiniz.