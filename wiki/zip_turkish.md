# [리눅스] Bash zip 사용법

## Overview
`zip` komutu, dosyaları ve dizinleri sıkıştırmak için kullanılan bir araçtır. Bu komut, dosyaları bir araya getirerek tek bir sıkıştırılmış dosya oluşturur. Genellikle dosya boyutunu azaltmak ve dosyaları daha kolay taşımak veya paylaşmak amacıyla kullanılır. `zip`, ZIP formatında sıkıştırma yapar ve birçok platformda yaygın olarak desteklenir.

## Usage
Temel `zip` komutunun sözdizimi şu şekildedir:

```bash
zip [seçenekler] sıkıştırılmış_dosya.zip dosya1 dosya2 ...
```

### Yaygın Seçenekler
- `-r`: Dizini ve alt dizinleri sıkıştırmak için kullanılır.
- `-e`: Sıkıştırılmış dosyayı şifrelemek için kullanılır.
- `-u`: Mevcut bir zip dosyasını güncellemek için kullanılır.
- `-d`: Zip dosyasından dosyaları silmek için kullanılır.

## Examples
### Örnek 1: Basit bir dosya sıkıştırma
Aşağıdaki komut, `belge.txt` dosyasını `arşiv.zip` adlı bir sıkıştırılmış dosya haline getirir:

```bash
zip arşiv.zip belge.txt
```

### Örnek 2: Bir dizini sıkıştırma
Aşağıdaki komut, `proje` adlı dizini ve içindeki tüm dosyaları sıkıştırarak `proje.zip` dosyasını oluşturur:

```bash
zip -r proje.zip proje/
```

## Tips
- Sıkıştırma işlemi sırasında, sıkıştırılacak dosyaların ve dizinlerin tam yollarını belirtmek, dosyaların doğru bir şekilde bulunmasını sağlar.
- Şifreleme seçeneğini kullanarak hassas verileri korumak için `-e` seçeneğini eklemeyi unutmayın.
- Sıkıştırılmış dosyaları güncellerken `-u` seçeneğini kullanarak mevcut dosyaları güncelleyebilir ve yeni dosyalar ekleyebilirsiniz.
- Büyük dosyalarla çalışırken, sıkıştırma süresinin uzayabileceğini göz önünde bulundurun ve işlemi arka planda çalıştırmak için `&` kullanabilirsiniz.