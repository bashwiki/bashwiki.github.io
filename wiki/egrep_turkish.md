# [Linux] Bash egrep Kullanımı: Metin içinde düzenli ifadelerle arama yapma

## Overview
`egrep`, metin dosyalarında düzenli ifadeler kullanarak arama yapmayı sağlayan bir komut satırı aracıdır. `egrep`, `grep -E` ile eşdeğerdir ve genişletilmiş düzenli ifadeleri destekler. Bu, daha karmaşık arama desenleri oluşturmanıza olanak tanır.

## Usage
Temel kullanım şekli aşağıdaki gibidir:

```bash
egrep [options] [arguments]
```

## Common Options
- `-i`: Büyük/küçük harf duyarsız arama yapar.
- `-v`: Eşleşmeyen satırları gösterir.
- `-c`: Eşleşen satırların sayısını gösterir.
- `-n`: Eşleşen satırların numaralarını gösterir.
- `-r`: Alt dizinlerde de arama yapar.

## Common Examples
Aşağıda `egrep` komutunun bazı pratik kullanım örnekleri bulunmaktadır:

### Örnek 1: Basit bir arama
Belirli bir kelimeyi içeren satırları bulmak için:

```bash
egrep "kelime" dosya.txt
```

### Örnek 2: Büyük/küçük harf duyarsız arama
Büyük/küçük harf farkı gözetmeden arama yapmak için:

```bash
egrep -i "kelime" dosya.txt
```

### Örnek 3: Eşleşmeyen satırları gösterme
Belirli bir kelimeyi içermeyen satırları bulmak için:

```bash
egrep -v "kelime" dosya.txt
```

### Örnek 4: Eşleşen satır sayısını gösterme
Eşleşen satırların sayısını öğrenmek için:

```bash
egrep -c "kelime" dosya.txt
```

### Örnek 5: Alt dizinlerde arama
Belirli bir kelimeyi alt dizinlerde de aramak için:

```bash
egrep -r "kelime" dizin/
```

## Tips
- Düzenli ifadeleri kullanarak daha karmaşık arama desenleri oluşturabilirsiniz. Örneğin, `egrep "kelime1|kelime2"` ile birden fazla kelimeyi arayabilirsiniz.
- Arama sonuçlarını daha iyi analiz etmek için `-n` seçeneğini kullanarak satır numaralarını görebilirsiniz.
- Uzun dosya adları veya karmaşık dizin yapılarıyla çalışırken, `--color` seçeneğini ekleyerek eşleşen kelimeleri renklendirebilirsiniz.