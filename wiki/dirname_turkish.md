# [Linux] Bash dirname Kullanımı: Dosya yolundan dizin adını almak

## Genel Bakış
`dirname` komutu, bir dosya yolundan dizin adını çıkarmak için kullanılır. Bu komut, dosya yolunun sonundaki dosya adını kaldırarak yalnızca dizin yolunu döndürür.

## Kullanım
Temel sözdizimi aşağıdaki gibidir:
```
dirname [seçenekler] [argümanlar]
```

## Yaygın Seçenekler
- `-z`: Boş dizin adlarını döndürür.
- `--help`: Komutun kullanımını gösterir.
- `--version`: Komutun sürüm bilgilerini gösterir.

## Yaygın Örnekler
Aşağıda `dirname` komutunun bazı pratik kullanımları bulunmaktadır:

1. Basit bir dosya yolu için dizin adını almak:
   ```bash
   dirname /home/kullanici/dosya.txt
   ```
   Çıktı:
   ```
   /home/kullanici
   ```

2. Bir başka dosya yolu için dizin adını almak:
   ```bash
   dirname /var/log/syslog
   ```
   Çıktı:
   ```
   /var/log
   ```

3. Birden fazla dosya yolu için dizin adlarını almak:
   ```bash
   dirname /usr/local/bin/script.sh /etc/hosts
   ```
   Çıktı:
   ```
   /usr/local/bin
   /etc
   ```

## İpuçları
- `dirname` komutunu, dosya yollarını işleyen betikler yazarken kullanmak, kodunuzu daha okunabilir hale getirebilir.
- Bir dosya yolunun dizinini almak için `basename` komutuyla birlikte kullanarak, dosya adını ve dizinini ayrı ayrı elde edebilirsiniz.
- Komutun çıktısını başka komutlarla birleştirerek daha karmaşık işlemler gerçekleştirebilirsiniz. Örneğin, dizin yolunu bir değişkene atayarak daha sonra kullanabilirsiniz.