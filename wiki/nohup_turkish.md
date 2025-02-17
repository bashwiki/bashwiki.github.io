# [Linux] Bash nohup Kullanımı: Arka planda komut çalıştırma

## Overview
`nohup` komutu, bir komutun terminal oturumu kapatılsa bile çalışmaya devam etmesini sağlar. Bu, özellikle uzun süren işlemleri başlatırken kullanışlıdır; böylece oturum kapandığında işlem sonlanmaz.

## Usage
Temel sözdizimi aşağıdaki gibidir:

```bash
nohup [options] [arguments]
```

## Common Options
- `&`: Komutu arka planda çalıştırır.
- `-h`: Yardım bilgilerini gösterir.
- `-n`: Çıktıyı `nohup.out` dosyasına yönlendirmeden çalıştırır.

## Common Examples
1. Basit bir komut çalıştırma:
   ```bash
   nohup sleep 60 &
   ```
   Bu komut, 60 saniye boyunca uykuya dalan bir işlemi arka planda başlatır.

2. Bir Python betiğini çalıştırma:
   ```bash
   nohup python my_script.py &
   ```
   Bu komut, `my_script.py` adlı Python betiğini arka planda çalıştırır.

3. Çıktıyı özel bir dosyaya yönlendirme:
   ```bash
   nohup my_command > output.log &
   ```
   Bu komut, `my_command` çalıştırıldığında çıktıyı `output.log` dosyasına yönlendirir.

## Tips
- `nohup` komutunu kullanırken, çıktıyı yönlendirmek için `>` operatörünü kullanmayı unutmayın, aksi takdirde varsayılan olarak `nohup.out` dosyasına yazılır.
- Uzun süren işlemler için `nohup` kullanmak, terminal oturumunu kapatmanıza rağmen işlemin devam etmesini sağlar.
- İşleminizin durumu hakkında bilgi almak için `jobs` komutunu kullanabilirsiniz.