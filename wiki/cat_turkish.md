# [Linux] Bash cat Kullanımı: Dosya içeriğini görüntüleme

## Genel Bakış
`cat` komutu, bir veya daha fazla dosyanın içeriğini terminalde görüntülemek için kullanılan bir Bash komutudur. Ayrıca dosyaları birleştirmek ve yeni dosyalar oluşturmak için de kullanılabilir.

## Kullanım
Temel sözdizimi aşağıdaki gibidir:

```bash
cat [seçenekler] [argümanlar]
```

## Yaygın Seçenekler
- `-n`: Satır numaralarını gösterir.
- `-b`: Boş olmayan satırları numaralandırır.
- `-E`: Her satırın sonuna `$` işareti ekler.
- `-s`: Ardışık boş satırları birleştirir.

## Yaygın Örnekler
1. **Bir dosyanın içeriğini görüntüleme:**
   ```bash
   cat dosya.txt
   ```

2. **Birden fazla dosyanın içeriğini birleştirip görüntüleme:**
   ```bash
   cat dosya1.txt dosya2.txt
   ```

3. **Bir dosyanın içeriğini başka bir dosyaya kopyalama:**
   ```bash
   cat dosya.txt > yeni_dosya.txt
   ```

4. **Satır numaraları ile dosya içeriğini görüntüleme:**
   ```bash
   cat -n dosya.txt
   ```

5. **Boş satırları birleştirerek görüntüleme:**
   ```bash
   cat -s dosya.txt
   ```

## İpuçları
- `cat` komutunu kullanırken, büyük dosyalar için `less` veya `more` komutlarını tercih etmek daha iyi olabilir; çünkü bu komutlar sayfalandırma yaparak daha kolay okunmasını sağlar.
- Dosya içeriğini birleştirirken, çıktı dosyasının üzerine yazılmasını istemiyorsanız, `>>` operatörünü kullanarak ekleme yapabilirsiniz.
- `cat` komutunu, dosya oluşturma işlemleri için de kullanabilirsiniz. Örneğin, `cat > yeni_dosya.txt` komutunu kullanarak yeni bir dosya oluşturabilir ve içerik girebilirsiniz. Çıkmak için `CTRL+D` tuşlarına basmayı unutmayın.