# [Linux] Bash chattr Kullanımı: Dosya özelliklerini değiştirme

## Overview
`chattr` komutu, Linux dosya sistemlerinde dosya ve dizinlerin özelliklerini değiştirmek için kullanılır. Bu komut, dosyaların belirli özelliklerini ayarlayarak, onları koruma veya erişim kontrolü sağlama imkanı tanır.

## Usage
Temel sözdizimi aşağıdaki gibidir:

```bash
chattr [options] [arguments]
```

## Common Options
- `+`: Belirtilen özelliği ekler.
- `-`: Belirtilen özelliği kaldırır.
- `=`: Belirtilen özelliği ayarlar ve diğer tüm özellikleri kaldırır.
- `i`: Dosyayı değiştirilmez hale getirir (immutable).
- `a`: Dosyaya sadece ekleme yapılmasını sağlar (append only).
- `e`: Dosyanın verilerini sıkıştırır (extent format).

## Common Examples
Aşağıda `chattr` komutunun bazı yaygın kullanım örnekleri bulunmaktadır:

### 1. Bir dosyayı değiştirilemez hale getirme
```bash
chattr +i dosya.txt
```

### 2. Bir dosyaya sadece ekleme izni verme
```bash
chattr +a dosya.txt
```

### 3. Bir dosyanın özelliklerini görüntüleme
```bash
lsattr dosya.txt
```

### 4. Değiştirilemez özelliği kaldırma
```bash
chattr -i dosya.txt
```

## Tips
- `chattr` komutunu kullanmadan önce, dosya sisteminin bu komutu desteklediğinden emin olun.
- Özellikleri değiştirmeden önce dosyanın yedeğini almak iyi bir uygulamadır.
- Özelliklerin etkilerini anlamak için `lsattr` komutunu kullanarak dosya özelliklerini kontrol edin.