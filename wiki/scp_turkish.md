# [리눅스] Bash scp 사용법

## Overview
`scp` (Secure Copy Protocol), dosya transferi için kullanılan bir komuttur. SSH (Secure Shell) protokolünü temel alarak, ağ üzerinden güvenli bir şekilde dosya kopyalamak için kullanılır. `scp`, hem yerel hem de uzaktaki sistemler arasında dosya transferi yapma imkanı sunar ve bu transfer sırasında verilerin şifrelenmesini sağlar.

## Usage
`scp` komutunun temel sözdizimi aşağıdaki gibidir:

```bash
scp [seçenekler] kaynak hedef
```

### Yaygın Seçenekler
- `-r`: Klasörleri ve içindeki tüm dosyaları kopyalamak için kullanılır.
- `-P [port]`: Hedef sunucunun SSH portunu belirtmek için kullanılır (büyük "P" harfi ile).
- `-i [anahtar dosyası]`: Belirtilen özel anahtar dosyasını kullanarak kimlik doğrulaması yapmak için kullanılır.
- `-v`: Komutun çalıştırılması sırasında daha fazla bilgi vermek için "verbose" modunu etkinleştirir.

## Examples
### Örnek 1: Yerel bir dosyayı uzak bir sunucuya kopyalama
Aşağıdaki komut, `dosya.txt` adlı dosyayı `kullanici@sunucu_ip:/hedef/klasor/` adresine kopyalar:

```bash
scp dosya.txt kullanici@sunucu_ip:/hedef/klasor/
```

### Örnek 2: Uzak bir sunucudan yerel bir dizine dosya kopyalama
Aşağıdaki komut, `kullanici@sunucu_ip:/uzak_dosya.txt` dosyasını yerel makinedeki `./yerel_klasor/` dizinine kopyalar:

```bash
scp kullanici@sunucu_ip:/uzak_dosya.txt ./yerel_klasor/
```

## Tips
- **Anahtar Tabanlı Kimlik Doğrulama**: `scp` kullanırken, şifre yerine anahtar tabanlı kimlik doğrulama kullanmak, güvenliği artırır ve her seferinde şifre girme zorunluluğunu ortadan kaldırır.
- **Hızlı Transfer için `-C` Seçeneği**: Verilerin sıkıştırılmasını sağlamak için `-C` seçeneğini kullanabilirsiniz. Bu, büyük dosyaların transferinde hız kazandırabilir.
- **Kopyalama İşlemini Kontrol Etmek**: `-v` seçeneğini kullanarak, kopyalama işlemi sırasında daha fazla bilgi alabilir ve olası hataları daha kolay tespit edebilirsiniz.

Bu bilgilerle, `scp` komutunu etkili bir şekilde kullanarak dosya transferlerinizi güvenli bir şekilde gerçekleştirebilirsiniz.