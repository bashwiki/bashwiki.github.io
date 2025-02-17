# [Linux] Bash reboot Kullanımı: Sistemi yeniden başlatma

## Genel Bakış
`reboot` komutu, bir Linux sistemini güvenli bir şekilde yeniden başlatmak için kullanılır. Bu komut, sistemin tüm işlemlerini durdurur ve ardından işletim sistemini yeniden başlatır.

## Kullanım
Temel sözdizimi şu şekildedir:
```
reboot [seçenekler] [argümanlar]
```

## Yaygın Seçenekler
- `-f`: Sistemi zorla yeniden başlatır, bu seçenek ile tüm işlemler kapatılmadan yeniden başlatma yapılır.
- `-h`: Sistemi kapatır, ancak yeniden başlatmaz.
- `now`: Anında yeniden başlatma işlemi yapar.

## Yaygın Örnekler
Aşağıda `reboot` komutunun bazı pratik örnekleri verilmiştir:

### 1. Sistemi hemen yeniden başlatma
```bash
reboot
```

### 2. Sistemi zorla yeniden başlatma
```bash
reboot -f
```

### 3. Sistemi belirli bir süre sonra yeniden başlatma
```bash
shutdown -r +5
```
Bu komut, 5 dakika sonra sistemi yeniden başlatır.

### 4. Sistemi kapatıp yeniden başlatma
```bash
reboot -h
```
Bu komut, sistemi kapatır ve ardından yeniden başlatır.

## İpuçları
- `reboot` komutunu kullanmadan önce, açık olan dosyalarınızı kaydetmeyi unutmayın.
- Sistemi yeniden başlatmadan önce, kritik işlemlerin tamamlandığından emin olun.
- Zorla yeniden başlatma (`-f`) seçeneğini kullanırken dikkatli olun, çünkü bu açık olan işlemleri kaybetmenize neden olabilir.