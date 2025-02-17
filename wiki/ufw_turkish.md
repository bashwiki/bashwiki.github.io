# [Linux] Bash ufw Kullanımı: Güvenlik Duvarı Yönetimi

## Genel Bakış
`ufw` (Uncomplicated Firewall), Linux sistemlerinde güvenlik duvarı yapılandırmasını kolaylaştırmak için kullanılan bir komut satırı aracıdır. Kullanıcı dostu bir arayüze sahip olan `ufw`, ağ trafiğini kontrol etmek ve güvenlik politikalarını uygulamak için basit bir yol sunar.

## Kullanım
Temel sözdizimi aşağıdaki gibidir:
```bash
ufw [seçenekler] [argümanlar]
```

## Yaygın Seçenekler
- `enable`: Güvenlik duvarını etkinleştirir.
- `disable`: Güvenlik duvarını devre dışı bırakır.
- `allow [port]`: Belirtilen port üzerinden gelen trafiğe izin verir.
- `deny [port]`: Belirtilen port üzerinden gelen trafiği reddeder.
- `status`: Güvenlik duvarının mevcut durumunu gösterir.
- `reset`: Tüm kuralları sıfırlar.

## Yaygın Örnekler
Aşağıda `ufw` komutunun bazı pratik örnekleri bulunmaktadır:

1. **Güvenlik duvarını etkinleştirme:**
   ```bash
   sudo ufw enable
   ```

2. **Güvenlik duvarını devre dışı bırakma:**
   ```bash
   sudo ufw disable
   ```

3. **Belirli bir portu açma (örneğin, 22 numaralı port için SSH):**
   ```bash
   sudo ufw allow 22
   ```

4. **Belirli bir portu kapatma (örneğin, 80 numaralı port için HTTP):**
   ```bash
   sudo ufw deny 80
   ```

5. **Güvenlik duvarı durumunu kontrol etme:**
   ```bash
   sudo ufw status
   ```

6. **Tüm kuralları sıfırlama:**
   ```bash
   sudo ufw reset
   ```

## İpuçları
- `ufw` kullanmadan önce, mevcut ağ yapılandırmanızı ve hangi hizmetlerin çalıştığını kontrol edin.
- Belirli bir IP adresine izin vermek için `allow from [IP]` komutunu kullanabilirsiniz.
- Güvenlik duvarı kurallarını düzenli olarak gözden geçirerek gereksiz kuralları kaldırın.
- `ufw` ile çalışırken dikkatli olun; yanlış yapılandırmalar ağ bağlantınızı etkileyebilir.