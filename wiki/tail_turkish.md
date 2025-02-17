# [Linux] Bash tail Kullanımı: Dosyanın son satırlarını görüntüleme

## Genel Bakış
`tail` komutu, bir dosyanın son kısımlarını görüntülemek için kullanılır. Genellikle log dosyalarını izlemek veya büyük dosyaların sonundaki verileri hızlıca kontrol etmek için tercih edilir.

## Kullanım
Temel sözdizimi aşağıdaki gibidir:
```bash
tail [seçenekler] [argümanlar]
```

## Yaygın Seçenekler
- `-n [sayı]`: Görüntülenecek satır sayısını belirtir. Örneğin, `-n 10` son 10 satırı gösterir.
- `-f`: Dosya sonuna eklenen yeni satırları sürekli izler. Log dosyalarını takip etmek için kullanışlıdır.
- `-c [sayı]`: Görüntülenecek bayt sayısını belirtir. Örneğin, `-c 100` son 100 baytı gösterir.

## Yaygın Örnekler
Aşağıda `tail` komutunun bazı pratik kullanım örnekleri bulunmaktadır:

1. Son 10 satırı görüntüleme:
   ```bash
   tail -n 10 dosya.txt
   ```

2. Bir log dosyasını sürekli izleme:
   ```bash
   tail -f log.txt
   ```

3. Son 50 baytı görüntüleme:
   ```bash
   tail -c 50 dosya.txt
   ```

4. Belirli bir dosyanın son 20 satırını görüntüleme:
   ```bash
   tail -n 20 başka_dosya.log
   ```

## İpuçları
- Log dosyalarını izlerken `-f` seçeneğini kullanarak gerçek zamanlı güncellemeleri takip edebilirsiniz.
- `tail` komutunu diğer komutlarla birleştirerek daha karmaşık işlemler gerçekleştirebilirsiniz. Örneğin, `grep` ile belirli bir kelimeyi aramak için:
  ```bash
  tail -f log.txt | grep "hata"
  ```
- Büyük dosyalarla çalışırken, `-n` seçeneği ile sadece ihtiyaç duyduğunuz kadar satırı görüntüleyerek zaman kazanabilirsiniz.