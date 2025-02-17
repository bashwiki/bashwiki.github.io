# [Linux] Bash rar Kullanımı: Dosyaları sıkıştırma ve arşivleme

## Genel Bakış
`rar` komutu, dosyaları sıkıştırmak ve arşivlemek için kullanılan bir araçtır. RAR formatında dosyalar oluşturmanıza ve mevcut RAR dosyalarını açmanıza olanak tanır. Bu komut, dosya boyutunu azaltmak ve dosyaları düzenli bir şekilde saklamak için sıklıkla tercih edilir.

## Kullanım
Temel sözdizimi aşağıdaki gibidir:

```bash
rar [seçenekler] [argümanlar]
```

## Yaygın Seçenekler
- `a`: Yeni bir RAR arşivi oluşturur.
- `x`: RAR arşivinden dosyaları çıkarır.
- `t`: RAR arşivinin içeriğini test eder.
- `v`: Arşiv hakkında ayrıntılı bilgi verir.
- `m`: Sıkıştırma seviyesini ayarlar (0-5 arasında).

## Yaygın Örnekler
1. **Yeni bir RAR arşivi oluşturma:**
   ```bash
   rar a arşivim.rar dosya1.txt dosya2.txt
   ```
   Bu komut, `dosya1.txt` ve `dosya2.txt` dosyalarını `arşivim.rar` adında bir RAR arşivine ekler.

2. **RAR arşivinden dosyaları çıkarma:**
   ```bash
   rar x arşivim.rar
   ```
   Bu komut, `arşivim.rar` içindeki tüm dosyaları mevcut dizine çıkarır.

3. **RAR arşivini test etme:**
   ```bash
   rar t arşivim.rar
   ```
   Bu komut, `arşivim.rar` dosyasının bozulup bozulmadığını kontrol eder.

4. **Sıkıştırma seviyesini ayarlama:**
   ```bash
   rar a -m5 arşivim.rar dosya1.txt
   ```
   Bu komut, `dosya1.txt` dosyasını en yüksek sıkıştırma seviyesi ile `arşivim.rar` arşivine ekler.

## İpuçları
- RAR arşivlerinizi düzenli olarak yedekleyin, böylece veri kaybını önleyebilirsiniz.
- Sıkıştırma seviyesini ayarlarken, dosya boyutu ile sıkıştırma süresi arasında bir denge kurmaya çalışın.
- Büyük dosyalarla çalışıyorsanız, arşivleme işlemini arka planda gerçekleştirmek için `&` operatörünü kullanabilirsiniz. Örneğin:
  ```bash
  rar a arşivim.rar büyükdosya.txt &
  ```