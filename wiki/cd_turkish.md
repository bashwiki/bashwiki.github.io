# [Linux] Bash cd Kullanımı: Dizinler arasında geçiş yapma

## Genel Bakış
`cd` (change directory) komutu, kullanıcıların dosya sisteminde dizinler arasında geçiş yapmalarını sağlar. Bu komut, terminalde çalışırken belirli bir dizine gitmek için kullanılır.

## Kullanım
Temel sözdizimi şu şekildedir:

```bash
cd [seçenekler] [argümanlar]
```

## Yaygın Seçenekler
- `..`: Bir üst dizine geçiş yapar.
- `-`: Önceki dizine geri döner.
- `~`: Kullanıcının ana dizinine geçiş yapar.

## Yaygın Örnekler
Aşağıda `cd` komutunun bazı pratik kullanım örnekleri bulunmaktadır:

1. Bir üst dizine geçiş yapmak:
   ```bash
   cd ..
   ```

2. Önceki dizine geri dönmek:
   ```bash
   cd -
   ```

3. Kullanıcının ana dizinine geçiş yapmak:
   ```bash
   cd ~
   ```

4. Belirli bir dizine geçiş yapmak (örneğin, `Belgeler` dizinine):
   ```bash
   cd Belgeler
   ```

5. Tam yol kullanarak bir dizine geçiş yapmak:
   ```bash
   cd /home/kullanici/Belgeler
   ```

## İpuçları
- `cd` komutunu kullanırken dizin adlarını tam olarak yazmak yerine, dizin adının ilk birkaç harfini yazıp `Tab` tuşuna basarak otomatik tamamlama yapabilirsiniz.
- Dizinler arasında hızlı geçiş yapmak için `cd -` komutunu kullanarak önceki dizine kolayca dönebilirsiniz.
- Sık kullandığınız dizinler için bir alias tanımlayarak daha hızlı erişim sağlayabilirsiniz. Örneğin:
  ```bash
  alias projeler='cd /home/kullanici/projeler'
  ```