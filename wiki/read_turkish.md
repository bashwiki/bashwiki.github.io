# [리눅스] Bash read 사용법

## Overview
`read` komutu, Bash betiklerinde kullanıcıdan girdi almak için kullanılır. Bu komut, kullanıcıdan bir veya daha fazla değer alarak, bu değerleri değişkenlere atar. Genellikle etkileşimli betiklerde, kullanıcıdan bilgi toplamak için kullanılır.

## Usage
Temel sözdizimi şu şekildedir:

```bash
read [OPTIONS] VARIABLE_NAME
```

### Yaygın Seçenekler:
- `-p PROMPT`: Kullanıcıdan girdi almadan önce bir istem (prompt) görüntüler.
- `-a ARRAY`: Kullanıcının girdiği değerleri bir diziye atar.
- `-d DELIMITER`: Girdi sonunu belirlemek için bir ayırıcı tanımlar. Varsayılan olarak, girdi yeni bir satır ile sonlanır.
- `-s`: Girdi alırken ekranda göstermez (örneğin, şifre girişi için kullanışlıdır).
- `-t TIMEOUT`: Belirtilen süre içinde kullanıcıdan girdi alınmazsa komutun zaman aşımına uğramasını sağlar.

## Examples

### Örnek 1: Basit Kullanım
Kullanıcıdan bir isim almak ve bunu ekrana yazdırmak için:

```bash
#!/bin/bash
read -p "Adınızı girin: " name
echo "Merhaba, $name!"
```

Bu betik, kullanıcıdan bir isim girmesini ister ve ardından "Merhaba, [isim]!" mesajını gösterir.

### Örnek 2: Dizi Kullanımı
Kullanıcıdan birden fazla girdi almak için:

```bash
#!/bin/bash
read -p "Favori meyvelerinizi girin (boşlukla ayırarak): " -a fruits
echo "Seçtiğiniz meyveler: ${fruits[@]}"
```

Bu betik, kullanıcıdan birden fazla meyve adı alır ve bunları bir diziye atar. Ardından, seçilen meyveleri ekrana yazdırır.

## Tips
- Kullanıcıdan alınan girdilerin doğruluğunu kontrol etmek için `if` koşulları kullanabilirsiniz.
- Girdi alırken kullanıcıya net bir istem sağlamak, kullanıcı deneyimini artırır.
- `-s` seçeneğini kullanarak şifre gibi hassas bilgileri gizli tutabilirsiniz.
- Dizi kullanımı ile birden fazla girdi almak, kullanıcıdan daha fazla bilgi toplamak için etkili bir yöntemdir.