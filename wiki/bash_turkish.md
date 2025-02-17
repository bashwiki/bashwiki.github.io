# [Linux] Bash komutu kullanımı: Komut satırında işlemler yapmak

## Overview
Bash, Unix benzeri işletim sistemlerinde kullanılan bir komut yorumlayıcısıdır. Kullanıcıların komutları yazıp çalıştırmasına, betikler oluşturmasına ve sistemle etkileşimde bulunmasına olanak tanır.

## Usage
Bash komutunun temel sözdizimi aşağıdaki gibidir:

```bash
bash [seçenekler] [argümanlar]
```

## Common Options
- `-c`: Komutları bir dize olarak çalıştırır.
- `-i`: Etkileşimli bir kabuk başlatır.
- `-l`: Giriş kabuğu başlatır.
- `-s`: Standart girdi üzerinden komutları okur.

## Common Examples
1. Basit bir komut çalıştırma:
   ```bash
   bash -c "echo Merhaba Dünya"
   ```

2. Etkileşimli bir kabuk başlatma:
   ```bash
   bash -i
   ```

3. Bir betik dosyasını çalıştırma:
   ```bash
   bash script.sh
   ```

4. Standart girdi üzerinden komut okuma:
   ```bash
   echo "echo Merhaba" | bash -s
   ```

## Tips
- Betik yazarken, dosya izinlerini kontrol edin ve çalıştırılabilir hale getirin (`chmod +x script.sh`).
- Betiklerinizi düzenli tutmak için açıklamalar ekleyin.
- Hataları daha iyi anlamak için `set -x` komutunu kullanarak hata ayıklama modunu etkinleştirin.