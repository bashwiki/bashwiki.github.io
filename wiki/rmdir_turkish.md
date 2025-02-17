# [Linux] Bash rmdir Kullanımı: Boş dizinleri silme komutu

## Overview
`rmdir` komutu, boş dizinleri silmek için kullanılan bir Bash komutudur. Eğer dizin içinde dosya veya alt dizin varsa, bu komut çalışmaz.

## Usage
Temel sözdizimi aşağıdaki gibidir:

```bash
rmdir [options] [arguments]
```

## Common Options
- `-p`: Üst dizinleri de siler, eğer dizinler boşsa.
- `--ignore-fail-on-non-empty`: Boş olmayan dizinleri silmeye çalışırken hata mesajı vermez.

## Common Examples
Aşağıda `rmdir` komutunun bazı yaygın kullanım örnekleri bulunmaktadır:

1. Boş bir dizini silmek:
   ```bash
   rmdir /path/to/empty-directory
   ```

2. Birden fazla boş dizini silmek:
   ```bash
   rmdir /path/to/empty-directory1 /path/to/empty-directory2
   ```

3. Üst dizinleri de silmek (boş oldukları sürece):
   ```bash
   rmdir -p /path/to/empty-directory/parent-directory
   ```

4. Hata mesajı almadan boş olmayan dizinleri denemek:
   ```bash
   rmdir --ignore-fail-on-non-empty /path/to/non-empty-directory
   ```

## Tips
- `rmdir` komutunu kullanmadan önce dizinin gerçekten boş olduğundan emin olun. Aksi takdirde, komut çalışmayacak ve hata mesajı alacaksınız.
- Dizinleri silmeden önce `ls` komutunu kullanarak içeriğini kontrol etmek iyi bir uygulamadır.
- Eğer dizin içinde dosya veya alt dizin varsa, `rm -r` komutunu kullanarak dizini ve içeriğini silmeyi düşünebilirsiniz. Ancak dikkatli olun, çünkü bu komut geri alınamaz.