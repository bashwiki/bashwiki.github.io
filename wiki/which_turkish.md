# [Linux] Bash which komutu: İlgili dosya yollarını bulma

## Overview
`which` komutu, belirtilen bir komutun veya programın sistemdeki dosya yolunu bulmak için kullanılır. Bu, bir komutun hangi dosya tarafından yürütüleceğini belirlemek için oldukça faydalıdır.

## Usage
Temel sözdizimi aşağıdaki gibidir:

```bash
which [options] [arguments]
```

## Common Options
- `-a`: Belirtilen komutun tüm yollarını listelemek için kullanılır.
- `-s`: Çıktıyı bastırır; sadece çıkış durumu döner.
- `--help`: Yardım bilgilerini gösterir.

## Common Examples
Aşağıda `which` komutunun bazı yaygın kullanım örnekleri bulunmaktadır:

1. Belirli bir komutun yolunu bulmak:
   ```bash
   which python
   ```

2. Birden fazla komutun yollarını listelemek:
   ```bash
   which git node npm
   ```

3. Tüm yolları listelemek için `-a` seçeneği ile kullanmak:
   ```bash
   which -a python
   ```

4. Çıktıyı bastırmadan sadece çıkış durumu almak:
   ```bash
   which -s python
   ```

## Tips
- `which` komutunu sıkça kullandığınız komutların hangi dosyalardan geldiğini öğrenmek için kullanın.
- Eğer bir komutun yüklü olup olmadığını kontrol etmek istiyorsanız, `which` komutu hızlı bir çözüm sunar.
- `which` komutunun çıktısını başka komutlarla birleştirerek daha karmaşık işlemler gerçekleştirebilirsiniz.