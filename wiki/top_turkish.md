# [Linux] Bash top Kullanımı: Sistem kaynaklarını izleme aracı

## Genel Bakış
`top` komutu, sistemdeki işlemleri ve kaynak kullanımını gerçek zamanlı olarak izlemek için kullanılan bir araçtır. Bu komut, CPU ve bellek kullanımını gösterir ve sistemdeki en yoğun kaynak tüketen işlemleri hızlıca belirlemenizi sağlar.

## Kullanım
`top` komutunun temel sözdizimi aşağıdaki gibidir:

```bash
top [seçenekler] [argümanlar]
```

## Yaygın Seçenekler
- `-d [saniye]`: Güncellemelerin ne sıklıkla yapılacağını belirler. Varsayılan değer 3 saniyedir.
- `-p [PID]`: Belirli bir işlem kimliğini (PID) izlemek için kullanılır.
- `-u [kullanıcı]`: Belirli bir kullanıcıya ait işlemleri görüntüler.
- `-n [sayı]`: Belirtilen sayıda güncelleme sonrası çıkış yapar.

## Yaygın Örnekler
Aşağıda `top` komutunun bazı pratik kullanım örnekleri verilmiştir:

1. **Temel Kullanım**: Sistemdeki tüm işlemleri izlemek için sadece `top` yazmanız yeterlidir.
   ```bash
   top
   ```

2. **Güncelleme Süresini Değiştirme**: Güncellemelerin her 5 saniyede bir yapılmasını sağlamak için:
   ```bash
   top -d 5
   ```

3. **Belirli Bir PID'yi İzleme**: PID'si 1234 olan işlemi izlemek için:
   ```bash
   top -p 1234
   ```

4. **Belirli Bir Kullanıcıya Ait İşlemleri Görüntüleme**: "kullanici1" adlı kullanıcının işlemlerini görüntülemek için:
   ```bash
   top -u kullanici1
   ```

5. **Sadece 10 Güncelleme Sonrası Çıkış Yapma**: 10 güncelleme sonrası otomatik olarak çıkmak için:
   ```bash
   top -n 10
   ```

## İpuçları
- `top` ekranında `h` tuşuna basarak yardım alabilirsiniz.
- `k` tuşuna basarak bir işlemi sonlandırabilirsiniz; ardından işlem kimliğini (PID) girmeniz gerekecek.
- `M` tuşuna basarak işlemleri bellek kullanımına göre sıralayabilirsiniz.
- `P` tuşuna basarak işlemleri CPU kullanımına göre sıralamak mümkündür.

Bu bilgilerle `top` komutunu etkili bir şekilde kullanarak sistem kaynaklarınızı izleyebilir ve yönetebilirsiniz.