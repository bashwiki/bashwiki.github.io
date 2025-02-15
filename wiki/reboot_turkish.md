# [리눅스] Bash reboot 사용법

## Overview
`reboot` komutu, bir Linux sistemini yeniden başlatmak için kullanılır. Bu komut, sistemin tüm çalışan süreçlerini durdurur ve ardından işletim sistemini yeniden yükler. Genellikle sistem güncellemeleri sonrası veya sistemin düzgün çalışmadığı durumlarda kullanılır.

## Usage
Temel `reboot` komutunun sözdizimi aşağıdaki gibidir:

```bash
reboot [seçenekler]
```

### Yaygın Seçenekler
- `-f` veya `--force`: Sistemi zorla yeniden başlatır. Bu seçenek, normal kapanma işlemlerini atlar ve tüm süreçleri hemen sonlandırır.
- `-p` veya `--poweroff`: Sistemi kapatır ve ardından güç kaynağını kapatır. Bu seçenek, `reboot` komutunun bir alternatifi olarak kullanılabilir.

## Examples
### Örnek 1: Basit Yeniden Başlatma
Aşağıdaki komut, sistemi normal bir şekilde yeniden başlatır:

```bash
sudo reboot
```

### Örnek 2: Zorla Yeniden Başlatma
Eğer sistem yanıt vermiyorsa ve normal yeniden başlatma işlemi çalışmıyorsa, aşağıdaki komut kullanılabilir:

```bash
sudo reboot -f
```

## Tips
- `reboot` komutunu kullanmadan önce, sistemdeki tüm önemli verilerin kaydedildiğinden emin olun. Yeniden başlatma işlemi sırasında açık olan dosyalar kaybolabilir.
- Sistem güncellemeleri sonrası yeniden başlatma yaparken, güncellemelerin tamamlandığından emin olun.
- Eğer sunucu ortamında çalışıyorsanız, yeniden başlatma işlemini planlı bir bakım süresi içinde gerçekleştirmek en iyi uygulamadır.