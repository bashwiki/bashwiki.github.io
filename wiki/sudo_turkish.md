# [리눅스] Bash sudo 사용법

## Overview
`sudo`, "superuser do" ifadesinin kısaltmasıdır ve bir kullanıcıya, sistemdeki diğer kullanıcıların (genellikle root kullanıcısı) yetkilerine sahip olarak komutlar çalıştırma yetkisi verir. Bu komut, özellikle sistem yönetimi ve bakım işlemleri için gereklidir. Kullanıcıların, belirli komutları çalıştırırken daha yüksek yetkilere ihtiyaç duyması durumunda kullanılır.

## Usage
Temel `sudo` komutunun sözdizimi şu şekildedir:

```bash
sudo [seçenekler] [komut]
```

### Yaygın Seçenekler
- `-u [kullanıcı]`: Komutu belirtilen kullanıcı olarak çalıştırır. Varsayılan olarak root kullanıcısıdır.
- `-k`: Kullanıcının sudo yetkisini geçersiz kılar, böylece bir sonraki sudo komutunda şifre istenir.
- `-l`: Kullanıcının hangi komutları çalıştırabileceğini listeler.

## Examples
### Örnek 1: Paket Yükleme
Bir yazılım paketini yüklemek için `apt` komutunu kullanabilirsiniz:

```bash
sudo apt install paket_adi
```
Bu komut, belirtilen `paket_adi` adlı yazılım paketini yüklemek için root yetkileri ile çalıştırılır.

### Örnek 2: Dosya İzinlerini Değiştirme
Bir dosyanın sahipliğini değiştirmek için `chown` komutunu kullanabilirsiniz:

```bash
sudo chown yeni_kullanici dosya_adi
```
Bu komut, `dosya_adi` adlı dosyanın sahipliğini `yeni_kullanici` olarak değiştirmek için gerekli yetkileri sağlar.

## Tips
- `sudo` komutunu kullanırken dikkatli olun; çünkü yanlış bir komut çalıştırmak sistemde ciddi sorunlara yol açabilir.
- `sudo` kullanırken, komutun doğru olduğundan emin olun. Yanlış bir komut, sistem dosyalarını değiştirebilir veya silinebilir.
- Sık kullanılan komutlar için `sudo` ile birlikte `-l` seçeneğini kullanarak hangi yetkilere sahip olduğunuzu kontrol edebilirsiniz.
- `sudo` ile çalışırken, şifre girmeniz istenecektir. Bu şifre, kullanıcının kendi şifresidir ve root şifresi değildir.