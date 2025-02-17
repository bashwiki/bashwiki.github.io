# [Linux] Bash halt Kullanımı: Sistemi durdurma komutu

## Overview
`halt` komutu, bir Linux sistemini durdurmak için kullanılır. Bu komut, sistemin hemen kapanmasını sağlar ve genellikle sistem yöneticileri tarafından kullanılır.

## Usage
Temel sözdizimi aşağıdaki gibidir:

```bash
halt [options] [arguments]
```

## Common Options
- `-h`: Sistemi durdurur ve kapatır.
- `-p`: Sistemi kapatır ve güç kaynağını kapatır.
- `-f`: Sistemi hemen durdurur, herhangi bir kapanma işlemi olmadan.

## Common Examples
1. Sistemi durdurmak için:
   ```bash
   halt
   ```

2. Sistemi kapatıp güç kaynağını kapatmak için:
   ```bash
   halt -p
   ```

3. Hızlı bir şekilde durdurmak için:
   ```bash
   halt -f
   ```

## Tips
- `halt` komutunu kullanmadan önce, sistemdeki açık dosyaları ve işlemleri kontrol edin. Açık işlemler kaybolabilir.
- Bu komutu yalnızca yönetici (root) yetkileri ile çalıştırın.
- Eğer sistemin düzgün bir şekilde kapanmasını istiyorsanız, `shutdown` komutunu tercih edebilirsiniz.