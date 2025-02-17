# [Linux] Bash basename Kullanımı: Dosya adlarını almak için

## Overview
`basename` komutu, bir dosya yolunun yalnızca dosya adını almak için kullanılır. Yani, bir dosya yolunu verdiğinizde, bu komut size yalnızca dosyanın adını döndürür.

## Usage
Temel sözdizimi şu şekildedir:

```bash
basename [options] [arguments]
```

## Common Options
- `-a`, `--multiple`: Birden fazla dosya adı döndürür.
- `-s`, `--suffix`: Belirtilen bir son eki kaldırarak dosya adını döndürür.

## Common Examples
Aşağıda `basename` komutunun bazı yaygın kullanım örnekleri bulunmaktadır:

### Örnek 1: Basit kullanım
Bir dosya yolundan yalnızca dosya adını almak için:

```bash
basename /home/kullanici/dosya.txt
```
Çıktı:
```
dosya.txt
```

### Örnek 2: Son eki kaldırma
Bir dosya adından belirli bir son eki kaldırarak yalnızca temel adı almak için:

```bash
basename /home/kullanici/dosya.txt .txt
```
Çıktı:
```
dosya
```

### Örnek 3: Birden fazla dosya adı döndürme
Birden fazla dosya adını almak için:

```bash
basename -a /home/kullanici/dosya1.txt /home/kullanici/dosya2.txt
```
Çıktı:
```
dosya1.txt
dosya2.txt
```

## Tips
- `basename` komutunu, dosya adlarını işlemek istediğiniz betiklerde kullanarak daha okunabilir çıktılar elde edebilirsiniz.
- Dosya adlarını işlerken, son ekleri kaldırmak için `-s` seçeneğini kullanmak, dosya adlarını daha temiz hale getirebilir.
- Birden fazla dosya adı ile çalışıyorsanız, `-a` seçeneğini kullanarak hepsini aynı anda alabilirsiniz.