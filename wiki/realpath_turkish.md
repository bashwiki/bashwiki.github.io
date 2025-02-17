# [Linux] Bash realpath Kullanımı: Dosya yollarını normalize etme

## Overview
`realpath` komutu, verilen bir dosya veya dizin yolunu normalize ederek, mutlak yolunu döndürür. Bu, sembolik bağlantıları takip eder ve yolun en güncel halini sağlar.

## Usage
Temel sözdizimi aşağıdaki gibidir:

```bash
realpath [options] [arguments]
```

## Common Options
- `-m`, `--canonicalize-missing`: Eksik dosya veya dizin yollarını da normalize eder.
- `-q`, `--quiet`: Hata mesajlarını bastırır.
- `-s`, `--strip`: Yolda bulunan sembolik bağlantıları kaldırır.

## Common Examples

### 1. Basit bir dosya yolunu normalize etme
```bash
realpath myfile.txt
```
Bu komut, `myfile.txt` dosyasının mutlak yolunu döndürür.

### 2. Sembolik bağlantıları takip etme
```bash
realpath /path/to/symlink
```
Bu komut, `/path/to/symlink` sembolik bağlantısının gösterdiği gerçek dosyanın yolunu verir.

### 3. Eksik dosya yollarını normalize etme
```bash
realpath -m /path/to/missing/file
```
Bu komut, belirtilen eksik dosya yolunu normalize eder ve mevcut dizin yapısına göre bir yol döndürür.

### 4. Hata mesajlarını bastırma
```bash
realpath -q /path/to/nonexistent/file
```
Bu komut, mevcut olmayan bir dosya için hata mesajı vermeden çalışır.

## Tips
- `realpath` komutunu, dosya yollarını kontrol etmek ve doğrulamak için sıkça kullanabilirsiniz.
- Sembolik bağlantılarla çalışıyorsanız, `realpath` komutunu kullanarak gerçek dosya yollarını kolayca bulabilirsiniz.
- Hata mesajlarını bastırmak için `-q` seçeneğini kullanarak daha temiz bir çıktı elde edebilirsiniz.