# [리눅스] Bash journalctl 사용법

## Overview
`journalctl`, sistem günlüklerini görüntülemek için kullanılan bir komuttur. Systemd tabanlı sistemlerde, sistemin ve uygulamaların günlük kayıtlarını merkezi bir yerde toplar. Bu komut, günlükleri sorgulamak, filtrelemek ve analiz etmek için güçlü bir araçtır. Geliştiriciler ve sistem yöneticileri için, sistemin durumu hakkında bilgi edinmek ve hataları teşhis etmek için kritik öneme sahiptir.

## Usage
Temel `journalctl` komutunun sözdizimi aşağıdaki gibidir:

```bash
journalctl [SEÇENEKLER]
```

### Yaygın Seçenekler:
- `-b`: Son sistem başlangıcından itibaren günlükleri gösterir.
- `-f`: Gerçek zamanlı olarak günlükleri takip eder (son eklenen kayıtları gösterir).
- `--since "tarih"`: Belirtilen tarihten itibaren günlükleri gösterir.
- `--until "tarih"`: Belirtilen tarihe kadar günlükleri gösterir.
- `-u, --unit=UNIT`: Belirtilen sistem birimi için günlükleri gösterir.

## Examples
### Örnek 1: Son sistem başlangıcından itibaren günlükleri görüntüleme
```bash
journalctl -b
```
Bu komut, sistemin en son başlangıcından itibaren tüm günlük kayıtlarını gösterir.

### Örnek 2: Gerçek zamanlı günlük takibi
```bash
journalctl -f
```
Bu komut, günlükleri gerçek zamanlı olarak takip eder ve yeni eklenen kayıtları anlık olarak görüntüler.

## Tips
- Günlükleri filtrelemek için `--since` ve `--until` seçeneklerini kullanarak belirli bir zaman aralığında sorgulama yapabilirsiniz.
- `-u` seçeneği ile belirli bir hizmetin günlüklerini görüntülemek, sorunları daha hızlı teşhis etmenizi sağlar.
- Günlüklerin daha okunabilir olması için `--no-pager` seçeneğini kullanarak çıktıyı doğrudan terminale yazdırabilirsiniz.
- `journalctl` komutunu sık sık kullanıyorsanız, sık kullandığınız seçenekleri bir alias ile kısayol haline getirmek işinizi kolaylaştırabilir.