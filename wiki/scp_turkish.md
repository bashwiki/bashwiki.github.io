# [Linux] Bash scp Kullanımı: Dosya transferi için güvenli bir yöntem

## Genel Bakış
`scp` (Secure Copy Protocol), dosyaları bir ağ üzerinden güvenli bir şekilde kopyalamak için kullanılan bir komut satırı aracıdır. SSH (Secure Shell) protokolünü kullanarak, yerel ve uzak sistemler arasında dosya transferi gerçekleştirir.

## Kullanım
Temel sözdizimi şu şekildedir:

```bash
scp [seçenekler] [kaynak] [hedef]
```

## Yaygın Seçenekler
- `-r`: Dizini ve içindeki tüm dosyaları kopyalamak için kullanılır.
- `-P`: Uzak sunucunun SSH bağlantı portunu belirtir (büyük "P" ile).
- `-i`: Belirtilen özel anahtar dosyasını kullanarak kimlik doğrulaması yapar.
- `-v`: Ayrıntılı çıktı almak için kullanılır, hata ayıklama için faydalıdır.

## Yaygın Örnekler
1. **Yerel bir dosyayı uzak bir sunucuya kopyalama:**
   ```bash
   scp dosya.txt kullanıcı@sunucu:/hedef/klasör/
   ```

2. **Uzak bir dosyayı yerel bir makineye kopyalama:**
   ```bash
   scp kullanıcı@sunucu:/uzak/dosya.txt /yerel/klasör/
   ```

3. **Bir dizini ve içindeki tüm dosyaları kopyalama:**
   ```bash
   scp -r /yerel/dizin/ kullanıcı@sunucu:/hedef/dizin/
   ```

4. **Belirli bir port ile kopyalama:**
   ```bash
   scp -P 2222 dosya.txt kullanıcı@sunucu:/hedef/klasör/
   ```

## İpuçları
- `-v` seçeneğini kullanarak, bağlantı sırasında oluşabilecek sorunları daha iyi anlayabilirsiniz.
- Kopyalama işlemi sırasında dosya boyutunu kontrol etmek için `-C` seçeneğini ekleyerek sıkıştırma yapabilirsiniz.
- Eğer sık sık aynı sunucuya bağlanıyorsanız, SSH anahtarları kullanarak şifre girmeden bağlanmayı kolaylaştırabilirsiniz.