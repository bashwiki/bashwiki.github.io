# [리눅스] Bash paste 사용법

## Overview
`paste` komutu, bir veya daha fazla dosyadaki satırları yan yana birleştirerek bir çıktı oluşturur. Genellikle metin dosyalarını birleştirmek ve verileri düzenlemek için kullanılır. Her bir dosyanın satırları, varsayılan olarak tab ile ayrılarak birleştirilir. Bu, özellikle verileri sütunlar halinde düzenlemek isteyen mühendisler ve geliştiriciler için faydalıdır.

## Usage
Temel `paste` komutunun sözdizimi şu şekildedir:

```bash
paste [seçenekler] [dosya1] [dosya2] ...
```

### Yaygın Seçenekler
- `-d, --delimiters=SEPERATOR`: Satırları birleştirirken kullanılacak ayırıcıyı belirtir. Varsayılan ayırıcı tab karakteridir.
- `-s, --serial`: Girdi dosyalarındaki satırları ardışık olarak birleştirir. Yani, her dosyanın tüm satırları birleştirilir ve ardından bir sonraki dosyaya geçilir.
- `-z, --zero-terminated`: Girdi satırlarının sonunu null karakter (`\0`) ile belirler.

## Examples
### Örnek 1: Temel Kullanım
İki dosyadaki satırları yan yana birleştirmek için aşağıdaki komutu kullanabilirsiniz:

```bash
paste dosya1.txt dosya2.txt
```

Bu komut, `dosya1.txt` ve `dosya2.txt` dosyalarındaki satırları tab ile ayırarak birleştirir.

### Örnek 2: Özel Ayırıcı Kullanma
Eğer farklı bir ayırıcı kullanmak isterseniz, `-d` seçeneğini kullanabilirsiniz:

```bash
paste -d ',' dosya1.txt dosya2.txt
```

Bu komut, `dosya1.txt` ve `dosya2.txt` dosyalarındaki satırları virgül ile ayırarak birleştirir.

## Tips
- `paste` komutunu kullanmadan önce dosyalarınızın satır sayılarının eşit olduğundan emin olun. Farklı satır sayıları, beklenmedik sonuçlara yol açabilir.
- `-s` seçeneği ile dosyaları ardışık olarak birleştirirken, her dosyanın tüm satırlarını birleştirdiğinizden emin olun. Bu, verilerinizi daha düzenli hale getirebilir.
- Büyük veri setleri ile çalışıyorsanız, `paste` komutunu bir boru (pipe) ile diğer komutlarla birleştirerek daha karmaşık veri işleme işlemleri gerçekleştirebilirsiniz.