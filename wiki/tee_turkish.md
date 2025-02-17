# [Linux] Bash tee Kullanımı: Çıktıyı dosyaya yönlendirme

## Genel Bakış
`tee` komutu, standart çıktıyı hem ekrana yazdırmak hem de bir dosyaya kaydetmek için kullanılır. Bu, bir komutun çıktısını hem görüntülemek hem de daha sonra kullanılmak üzere saklamak için oldukça faydalıdır.

## Kullanım
Temel sözdizimi şu şekildedir:
```bash
tee [seçenekler] [argümanlar]
```

## Yaygın Seçenekler
- `-a`, `--append`: Çıktıyı dosyaya ekler, dosyayı silmeden.
- `-i`, `--ignore-interrupts`: Kesme sinyallerini yok sayar.
- `--help`: Kullanım hakkında yardım bilgisi gösterir.
- `--version`: `tee` komutunun sürüm bilgilerini gösterir.

## Yaygın Örnekler
1. **Temel Kullanım**: Bir komutun çıktısını dosyaya kaydetme.
   ```bash
   echo "Merhaba Dünya" | tee dosya.txt
   ```

2. **Çıktıyı Ekleme**: Var olan bir dosyaya çıktı ekleme.
   ```bash
   echo "Yeni Satır" | tee -a dosya.txt
   ```

3. **Birden Fazla Dosyaya Yazma**: Çıktıyı birden fazla dosyaya yönlendirme.
   ```bash
   echo "Bu bir deneme" | tee dosya1.txt dosya2.txt
   ```

4. **Hata Çıktısını Yönlendirme**: Hata çıktısını da dosyaya yazma.
   ```bash
   komut 2>&1 | tee hata.txt
   ```

## İpuçları
- `tee` komutunu, uzun komutların çıktısını kaydetmek için kullanarak, çıktıyı daha sonra incelemek üzere saklayabilirsiniz.
- `-a` seçeneği ile mevcut dosyaya ekleme yaparak, dosyanın içeriğini kaybetmeden yeni veriler ekleyebilirsiniz.
- Çıktıyı bir dosyaya kaydederken, aynı zamanda terminalde de görmek istiyorsanız `tee` komutunu kullanmayı unutmayın.