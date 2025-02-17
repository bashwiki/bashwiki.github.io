# [Linux] Bash unxz Kullanımı: Sıkıştırılmış dosyaları açma

## Genel Bakış
`unxz` komutu, XZ formatında sıkıştırılmış dosyaları açmak için kullanılır. Bu komut, sıkıştırılmış dosyaları orijinal hallerine geri döndürerek, kullanıcıların verilerine erişimini sağlar.

## Kullanım
Temel sözdizimi şu şekildedir:

```bash
unxz [seçenekler] [argümanlar]
```

## Yaygın Seçenekler
- `-k`, `--keep`: Sıkıştırılmış dosyayı açtıktan sonra orijinal dosyayı korur.
- `-f`, `--force`: Zaten var olan dosyaların üzerine yazmak için zorlar.
- `-v`, `--verbose`: İşlem sırasında ayrıntılı bilgi verir.

## Yaygın Örnekler
Aşağıda `unxz` komutunun bazı pratik örnekleri bulunmaktadır:

1. Basit bir dosyayı açma:
   ```bash
   unxz dosya.xz
   ```

2. Orijinal dosyayı koruyarak açma:
   ```bash
   unxz -k dosya.xz
   ```

3. Zaten var olan bir dosyanın üzerine yazmak için zorlayarak açma:
   ```bash
   unxz -f dosya.xz
   ```

4. Ayrıntılı bilgi ile açma:
   ```bash
   unxz -v dosya.xz
   ```

## İpuçları
- `unxz` komutunu kullanmadan önce dosyanızın yedeğini almak iyi bir uygulamadır.
- Sıkıştırılmış dosyaların bulunduğu dizinde çalıştığınızdan emin olun.
- Eğer birden fazla dosyayı açmak istiyorsanız, dosya isimlerini boşlukla ayırarak birden fazla dosyayı aynı anda belirtebilirsiniz:
  ```bash
  unxz dosya1.xz dosya2.xz
  ```