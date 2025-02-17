# [Linux] Bash apt Kullanımı: Paket yönetimi aracı

## Genel Bakış
`apt` (Advanced Package Tool), Debian tabanlı Linux dağıtımlarında yazılım paketlerini yönetmek için kullanılan bir komut satırı aracıdır. Kullanıcıların yazılımları yüklemesine, güncellemesine ve kaldırmasına olanak tanır.

## Kullanım
`apt` komutunun temel sözdizimi aşağıdaki gibidir:

```bash
apt [seçenekler] [argümanlar]
```

## Yaygın Seçenekler
- `install`: Belirtilen paketi yükler.
- `remove`: Belirtilen paketi kaldırır.
- `update`: Paket listelerini günceller.
- `upgrade`: Yüklü paketleri günceller.
- `search`: Belirtilen terimi içeren paketleri arar.

## Yaygın Örnekler
Aşağıda `apt` komutunun bazı pratik örnekleri verilmiştir:

### 1. Paket Yükleme
Belirli bir paketi yüklemek için:

```bash
sudo apt install paket_adi
```

### 2. Paket Kaldırma
Yüklü bir paketi kaldırmak için:

```bash
sudo apt remove paket_adi
```

### 3. Paket Listelerini Güncelleme
Paket listelerini güncellemek için:

```bash
sudo apt update
```

### 4. Yüklü Paketleri Güncelleme
Tüm yüklü paketleri güncellemek için:

```bash
sudo apt upgrade
```

### 5. Paket Arama
Belirli bir terimi içeren paketleri aramak için:

```bash
apt search arama_terimi
```

## İpuçları
- `sudo` komutunu kullanarak yönetici hakları ile işlem yapmayı unutmayın.
- `apt` komutunu kullanmadan önce `update` komutunu çalıştırarak paket listelerinizi güncel tutun.
- Gereksiz dosyaları temizlemek için `sudo apt autoremove` komutunu kullanabilirsiniz.