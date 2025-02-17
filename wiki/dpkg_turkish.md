# [Linux] Bash dpkg Kullanımı: Paket yönetimi aracı

## Overview
`dpkg`, Debian tabanlı sistemlerde kullanılan bir paket yönetim aracıdır. Bu komut, yazılım paketlerini kurmak, kaldırmak ve yönetmek için kullanılır. `dpkg`, sistemde yüklü olan paketlerin durumunu kontrol etme ve paketlerle ilgili bilgi alma gibi işlevler de sunar.

## Usage
Temel sözdizimi aşağıdaki gibidir:

```bash
dpkg [options] [arguments]
```

## Common Options
- `-i`, `--install`: Belirtilen .deb dosyasını kurar.
- `-r`, `--remove`: Belirtilen paketi kaldırır.
- `-l`, `--list`: Yüklü olan paketlerin listesini gösterir.
- `-s`, `--status`: Belirtilen paketin durumunu gösterir.
- `-S`, `--search`: Belirtilen dosyanın hangi pakete ait olduğunu bulur.

## Common Examples
Aşağıda `dpkg` komutunun bazı yaygın kullanım örnekleri bulunmaktadır:

### 1. Paket Kurma
Bir `.deb` dosyasını kurmak için:

```bash
sudo dpkg -i paket_adi.deb
```

### 2. Paket Kaldırma
Bir paketi kaldırmak için:

```bash
sudo dpkg -r paket_adi
```

### 3. Yüklü Paketlerin Listesini Görüntüleme
Sistemde yüklü olan tüm paketleri listelemek için:

```bash
dpkg -l
```

### 4. Paket Durumunu Kontrol Etme
Belirli bir paketin durumunu kontrol etmek için:

```bash
dpkg -s paket_adi
```

### 5. Dosya Arama
Bir dosyanın hangi pakete ait olduğunu bulmak için:

```bash
dpkg -S dosya_adi
```

## Tips
- `dpkg` komutunu kullanırken, genellikle `sudo` ile çalıştırmak gerekir, çünkü paket yönetimi sistem düzeyinde değişiklikler yapar.
- Kurulum sırasında bağımlılık sorunlarıyla karşılaşabilirsiniz; bu durumda `apt-get` veya `apt` komutlarını kullanarak bağımlılıkları çözebilirsiniz.
- Yükleme veya kaldırma işlemlerinden sonra sistemin güncel kalmasını sağlamak için `sudo apt-get update` ve `sudo apt-get upgrade` komutlarını kullanmayı unutmayın.