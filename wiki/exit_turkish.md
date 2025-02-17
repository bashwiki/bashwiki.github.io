# [Linux] Bash exit Kullanımı: Komut dosyasını sonlandırma

## Genel Bakış
`exit` komutu, bir Bash oturumunu veya komut dosyasını sonlandırmak için kullanılır. Bu komut, çalıştırılan süreçlerin durum kodunu belirlemek için de kullanılabilir. Durum kodu, genellikle bir işlemin başarılı olup olmadığını belirtir.

## Kullanım
Temel sözdizimi aşağıdaki gibidir:

```bash
exit [seçenekler] [argümanlar]
```

## Yaygın Seçenekler
- `n`: Çıkış durum kodunu belirtir. Varsayılan olarak 0 (başarı) kullanılır. Örneğin, `exit 1` komutu, bir hata durumunu belirtir.
- `-n`: Çıkış durum kodunu belirtmeden çıkış yapar.

## Yaygın Örnekler
1. **Basit çıkış:**
   ```bash
   exit
   ```
   Bu komut, mevcut oturumu veya komut dosyasını varsayılan durum kodu ile sonlandırır.

2. **Belirli bir durum kodu ile çıkış:**
   ```bash
   exit 0
   ```
   Bu komut, başarılı bir çıkış durumu ile oturumu sonlandırır.

3. **Hata durumu ile çıkış:**
   ```bash
   exit 1
   ```
   Bu komut, bir hata durumu ile çıkış yapar.

4. **Komut dosyası içinde çıkış:**
   ```bash
   #!/bin/bash
   echo "Bir hata oluştu!"
   exit 1
   ```
   Bu örnekte, bir hata mesajı gösterilir ve ardından durum kodu 1 ile çıkılır.

## İpuçları
- Komut dosyalarınızda, işlemlerin başarılı olup olmadığını kontrol etmek için `exit` komutunu kullanarak uygun durum kodları döndürün.
- `exit` komutunu kullanmadan önce, gerekli temizleme işlemlerini yapmayı unutmayın; bu, açık dosyaları kapatmayı veya kaynakları serbest bırakmayı içerebilir.
- Çıkış durum kodunu kontrol etmek için, komut dosyanızın sonunda `echo $?` komutunu kullanarak son çıkış durumunu görüntüleyebilirsiniz.