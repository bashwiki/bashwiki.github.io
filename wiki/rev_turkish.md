# [Linux] Bash rev: Ters çevirme işlemi

## Overview
`rev` komutu, bir dosyadaki veya standart girdideki her bir satırı ters çevirerek çıktı verir. Bu, metin dosyalarındaki kelimeleri veya karakterleri ters sırayla görmek için kullanışlıdır.

## Usage
Temel sözdizimi şu şekildedir:
```bash
rev [options] [arguments]
```

## Common Options
- `-o, --output=FILE`: Çıktıyı belirtilen dosyaya yazmak için kullanılır.
- `-h, --help`: Komut hakkında yardım bilgisi görüntüler.
- `-V, --version`: Komutun sürüm bilgilerini gösterir.

## Common Examples
Aşağıda `rev` komutunun bazı yaygın kullanım örnekleri bulunmaktadır:

### 1. Standart girdi ile ters çevirme
```bash
echo "merhaba dünya" | rev
```
Çıktı:
```
aynüd abahreM
```

### 2. Bir dosyadaki satırları ters çevirme
```bash
rev dosya.txt
```
Bu komut, `dosya.txt` dosyasındaki her bir satırı ters çevirir.

### 3. Çıktıyı yeni bir dosyaya yazma
```bash
rev dosya.txt -o ters_dosya.txt
```
Bu komut, `dosya.txt` dosyasındaki satırları ters çevirir ve sonucu `ters_dosya.txt` dosyasına yazar.

### 4. Birden fazla dosyayı ters çevirme
```bash
rev dosya1.txt dosya2.txt
```
Bu komut, `dosya1.txt` ve `dosya2.txt` dosyalarındaki satırları ters çevirir.

## Tips
- `rev` komutunu, metin dosyalarındaki verileri analiz etmek veya düzeltmek için kullanabilirsiniz.
- Uzun dosyalarla çalışırken, çıktıyı bir dosyaya yönlendirmek, çıktıyı daha sonra incelemek için faydalı olabilir.
- `rev` komutunu diğer komutlarla birleştirerek daha karmaşık işlemler gerçekleştirebilirsiniz; örneğin, `cat` komutuyla birleştirerek dosyaların içeriğini ters çevirebilirsiniz.