# [리눅스] Bash crontab 사용법

## Overview
`crontab`, Unix benzeri işletim sistemlerinde zamanlanmış görevleri yönetmek için kullanılan bir komuttur. Kullanıcıların belirli zaman dilimlerinde otomatik olarak çalıştırılacak komutları veya scriptleri tanımlamalarına olanak tanır. Bu, sistem bakım görevleri, veri yedekleme, rapor oluşturma gibi işlemleri otomatikleştirmek için oldukça yararlıdır.

## Usage
`crontab` komutunun temel sözdizimi şu şekildedir:

```
crontab [seçenekler]
```

### Yaygın Seçenekler:
- `-e`: Kullanıcının crontab dosyasını düzenlemesini sağlar.
- `-l`: Kullanıcının mevcut crontab görevlerini listelemesini sağlar.
- `-r`: Kullanıcının mevcut crontab dosyasını siler.

## Examples
### Örnek 1: Crontab Dosyasını Düzenleme
Aşağıdaki komut, kullanıcının crontab dosyasını düzenlemesine olanak tanır:

```bash
crontab -e
```

Bu komut çalıştırıldığında, varsayılan metin düzenleyici açılır ve kullanıcı, zamanlanmış görevleri ekleyebilir veya mevcut görevleri düzenleyebilir.

### Örnek 2: Her Gün Belirli Bir Saate Komut Çalıştırma
Aşağıdaki örnek, her gün saat 2:30'da bir yedekleme scriptinin çalıştırılmasını sağlar:

```bash
30 2 * * * /path/to/backup_script.sh
```

Bu satır, `backup_script.sh` dosyasını her gün saat 02:30'da çalıştırır.

## Tips
- Zamanlama ifadelerini doğru bir şekilde yazmak için, her bir alanın ne anlama geldiğini iyi anlamak önemlidir. Zamanlama ifadeleri şu şekildedir: `dakika saat gün ay hafta günü`.
- Crontab dosyasını düzenlerken, her satırın sonunda bir yeni satır karakteri olduğundan emin olun. Aksi takdirde, son satır çalışmayabilir.
- Komutların çıktısını bir dosyaya yönlendirmek için, komutun sonuna `>> /path/to/logfile.log 2>&1` ekleyerek hata ve çıktı mesajlarını kaydedebilirsiniz.
- Crontab dosyasını düzenledikten sonra, değişikliklerin etkili olması için dosyayı kaydetmeyi unutmayın.