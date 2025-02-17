# [Linux] Bash firewalld Kullanımı: Güvenlik duvarı yönetimi

## Genel Bakış
firewalld, Linux sistemlerinde güvenlik duvarı yapılandırmasını yönetmek için kullanılan bir komut satırı aracıdır. Dinamik bir güvenlik duvarı yönetimi sağlar ve ağ trafiğini kontrol etmek için bölge tabanlı bir yaklaşım kullanır.

## Kullanım
firewalld komutunun temel sözdizimi aşağıdaki gibidir:

```bash
firewalld [seçenekler] [argümanlar]
```

## Yaygın Seçenekler
- `--zone`: Belirli bir bölgeyi tanımlar.
- `--add-service`: Belirli bir hizmeti güvenlik duvarına ekler.
- `--remove-service`: Belirli bir hizmeti güvenlik duvarından kaldırır.
- `--list-all`: Mevcut bölgenin tüm ayarlarını listeler.
- `--permanent`: Değişikliklerin kalıcı olmasını sağlar.

## Yaygın Örnekler
Aşağıda firewalld komutunun bazı pratik örnekleri bulunmaktadır:

### 1. Belirli Bir Hizmeti Ekleme
HTTP hizmetini güvenlik duvarına eklemek için:

```bash
firewalld --add-service=http
```

### 2. Belirli Bir Hizmeti Kaldırma
SSH hizmetini güvenlik duvarından kaldırmak için:

```bash
firewalld --remove-service=ssh
```

### 3. Mevcut Bölge Ayarlarını Görüntüleme
Aktif bölgenin tüm ayarlarını listelemek için:

```bash
firewalld --list-all
```

### 4. Kalıcı Değişiklik Yapma
HTTP hizmetini kalıcı olarak eklemek için:

```bash
firewalld --permanent --add-service=http
```

## İpuçları
- Değişiklik yapmadan önce mevcut ayarların bir yedeğini almak iyi bir uygulamadır.
- Güvenlik duvarı kurallarını test etmek için `--dry-run` seçeneğini kullanarak etkilerini önceden görebilirsiniz.
- Belirli bir bölgeyi yönetmek için `--zone` seçeneğini kullanarak daha hassas kontrol sağlayabilirsiniz.