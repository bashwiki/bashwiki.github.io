# [Linux] Bash hostname Kullanımı: Bilgisayarın ağ adını görüntüleme ve ayarlama

## Overview
`hostname` komutu, bir bilgisayarın ağ üzerindeki adını görüntülemek veya değiştirmek için kullanılır. Bu ad, ağda diğer cihazlar tarafından tanınmasını sağlar.

## Usage
Temel sözdizimi aşağıdaki gibidir:

```bash
hostname [options] [arguments]
```

## Common Options
- `-a`, `--alias`: Bilgisayarın takma adını görüntüler.
- `-d`, `--domain`: Bilgisayarın alan adını görüntüler.
- `-f`, `--fqdn`: Tam nitelikli alan adını (FQDN) görüntüler.
- `-i`, `--ip-address`: Bilgisayarın IP adresini görüntüler.
- `-s`, `--short`: Bilgisayarın kısa adını görüntüler.
- `--help`: Kullanım hakkında yardım bilgisi gösterir.
- `--version`: Komutun sürüm bilgilerini gösterir.

## Common Examples

### 1. Bilgisayarın adını görüntüleme
```bash
hostname
```
Bu komut, mevcut bilgisayarın ağ adını gösterir.

### 2. Tam nitelikli alan adını görüntüleme
```bash
hostname -f
```
Bu komut, bilgisayarın tam nitelikli alan adını görüntüler.

### 3. Bilgisayarın IP adresini görüntüleme
```bash
hostname -i
```
Bu komut, bilgisayarın IP adresini gösterir.

### 4. Bilgisayar adını değiştirme
```bash
sudo hostname yeni-ad
```
Bu komut, bilgisayarın ağ adını "yeni-ad" olarak değiştirir. Değişikliğin kalıcı olması için `/etc/hostname` dosyasını da güncellemek gerekebilir.

## Tips
- Bilgisayar adını değiştirdikten sonra, değişikliğin etkili olması için bilgisayarı yeniden başlatmak iyi bir uygulamadır.
- `hostname` komutunu sık sık kullanıyorsanız, çıktıyı daha okunabilir hale getirmek için `-s` veya `-f` seçeneklerini kullanabilirsiniz.
- Ağda birden fazla cihaz varsa, her cihazın benzersiz bir adı olduğundan emin olun; bu, ağ yönetimini kolaylaştırır.