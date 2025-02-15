# [리눅스] Bash umount 사용법

## Overview
`umount` komutu, Linux ve Unix benzeri işletim sistemlerinde dosya sistemlerini ayırmak için kullanılır. Bu komut, bir dosya sisteminin veya aygıtın sistemden çıkarılmasını sağlar, böylece dosya sistemine erişim sona erer. `umount`, genellikle bir depolama aygıtının güvenli bir şekilde çıkarılması için gereklidir ve veri kaybını önlemek için dosya sisteminin düzgün bir şekilde kapatılmasını sağlar.

## Usage
`umount` komutunun temel sözdizimi şu şekildedir:

```bash
umount [seçenekler] <dosya_sistemi>
```

### Yaygın Seçenekler
- `-a`: Tüm dosya sistemlerini ayırır.
- `-f`: Zorla ayırma işlemi yapar. Dosya sistemi hala kullanılıyorsa bile ayırmayı dener.
- `-l`: Geçici olarak ayırma işlemi yapar. Dosya sistemi, hala kullanılıyorsa bile hemen ayırılır, ancak işlemler tamamlandığında gerçek ayırma işlemi yapılır.
- `-r`: Ayırma işlemi sırasında hata oluşursa, dosya sistemini otomatik olarak yeniden bağlamaya çalışır.

## Examples
### Örnek 1: Bir dosya sistemini ayırma
Aşağıdaki komut, `/dev/sdb1` aygıtını ayırır:

```bash
umount /dev/sdb1
```

### Örnek 2: Bir dizini ayırma
Eğer bir dosya sistemi bir dizine bağlanmışsa, o dizini ayırmak için de `umount` komutunu kullanabilirsiniz:

```bash
umount /mnt/mydrive
```

## Tips
- Dosya sistemini ayırmadan önce, o dosya sisteminde açık dosya veya işlem olmadığından emin olun. Aksi takdirde, `umount` komutu başarısız olabilir.
- Zorla ayırma (`-f`) seçeneğini kullanırken dikkatli olun; bu, veri kaybına yol açabilir.
- Ayırma işlemi sırasında hata alıyorsanız, `l` seçeneği ile geçici ayırma yapmayı deneyebilirsiniz.
- Dosya sisteminin düzgün bir şekilde ayırıldığını kontrol etmek için `mount` komutunu kullanarak bağlı dosya sistemlerini listeleyebilirsiniz.