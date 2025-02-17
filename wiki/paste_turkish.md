# [Linux] Bash paste Kullanımı: Dosyaları yan yana birleştirme

## Genel Bakış
`paste` komutu, birden fazla dosyadaki satırları yan yana birleştirerek yeni bir çıktı oluşturur. Bu komut, özellikle metin dosyalarını birleştirirken veya verileri düzenlerken kullanışlıdır.

## Kullanım
Temel sözdizimi aşağıdaki gibidir:

```bash
paste [seçenekler] [argümanlar]
```

## Yaygın Seçenekler
- `-d`: Birleştirme sırasında kullanılacak ayırıcıyı belirtir. Varsayılan ayırıcı, tab karakteridir.
- `-s`: Her dosyadaki satırları ardışık olarak birleştirir, yani her dosyanın satırları tek bir satırda yer alır.
- `-z`: Null karakterini ayırıcı olarak kullanır.

## Yaygın Örnekler

1. İki dosyayı yan yana birleştirme:
   ```bash
   paste dosya1.txt dosya2.txt
   ```

2. Belirli bir ayırıcı ile birleştirme (örneğin, virgül):
   ```bash
   paste -d ',' dosya1.txt dosya2.txt
   ```

3. Her dosyanın satırlarını ardışık olarak birleştirme:
   ```bash
   paste -s dosya1.txt
   ```

4. Birden fazla dosyayı birleştirip çıktıyı bir dosyaya yönlendirme:
   ```bash
   paste dosya1.txt dosya2.txt > birlesik_dosya.txt
   ```

## İpuçları
- `paste` komutunu kullanmadan önce dosyaların doğru formatta olduğundan emin olun.
- Farklı ayırıcılar kullanarak çıktıyı daha okunabilir hale getirebilirsiniz.
- `man paste` komutunu kullanarak daha fazla bilgi ve seçenekler hakkında detaylı bilgi alabilirsiniz.