# [Linux] Bash iptables Kullanımı: Ağ trafiğini kontrol etme

## Genel Bakış
iptables, Linux işletim sistemlerinde ağ trafiğini kontrol etmek için kullanılan bir komuttur. Bu komut, gelen ve giden verileri filtrelemek, yönlendirmek ve belirli kurallar oluşturmak için kullanılır. Güvenlik duvarı işlevi görerek, sisteminize gelen tehditleri azaltmanıza yardımcı olur.

## Kullanım
iptables komutunun temel sözdizimi aşağıdaki gibidir:

```bash
iptables [seçenekler] [argümanlar]
```

## Yaygın Seçenekler
- `-A`: Bir kuralı zincire ekler.
- `-D`: Bir kuralı zincirden siler.
- `-I`: Bir kuralı zincirin başına ekler.
- `-L`: Mevcut kuralları listeler.
- `-F`: Tüm kuralları temizler.
- `-P`: Varsayılan politika ayarlar.

## Yaygın Örnekler
Aşağıda iptables komutunun bazı yaygın kullanım örnekleri verilmiştir:

### 1. Tüm mevcut kuralları listeleme
```bash
iptables -L
```

### 2. Belirli bir IP adresinden gelen trafiği engelleme
```bash
iptables -A INPUT -s 192.168.1.100 -j DROP
```

### 3. Tüm gelen bağlantılara izin verme
```bash
iptables -P INPUT ACCEPT
```

### 4. Tüm kuralları temizleme
```bash
iptables -F
```

### 5. Belirli bir portu açma (örneğin, 80 numaralı port)
```bash
iptables -A INPUT -p tcp --dport 80 -j ACCEPT
```

## İpuçları
- Kurallarınızı düzenli olarak yedekleyin, böylece yanlışlıkla silinen veya değiştirilen kuralları geri yükleyebilirsiniz.
- Değişiklik yapmadan önce mevcut kurallarınızı kontrol edin ve not alın.
- Test ortamında kuralları denemek, canlı sistemde sorun yaşamamanız için iyi bir uygulamadır.
- iptables kurallarını uyguladıktan sonra, etkilerini görmek için ağ trafiğinizi izlemeyi unutmayın.