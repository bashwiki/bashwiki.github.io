# [Linux] Bash svn Kullanımı: Versiyon kontrolü için bir araç

## Genel Bakış
`svn` (Subversion), dosya ve dizinlerin versiyon kontrolünü sağlamak için kullanılan bir komut satırı aracıdır. Geliştiricilerin ve ekiplerin projelerini yönetmelerine, değişiklikleri takip etmelerine ve işbirliği yapmalarına olanak tanır.

## Kullanım
Temel sözdizimi şu şekildedir:

```bash
svn [seçenekler] [argümanlar]
```

## Yaygın Seçenekler
- `checkout`: Bir depo kopyasını yerel makineye indirmek için kullanılır.
- `commit`: Yerel değişiklikleri depoya göndermek için kullanılır.
- `update`: Yerel kopyayı depodaki en son değişikliklerle güncellemek için kullanılır.
- `status`: Yerel çalışma kopyasındaki değişikliklerin durumunu gösterir.
- `log`: Depodaki geçmiş değişiklikleri görüntülemek için kullanılır.

## Yaygın Örnekler
1. **Depo Kopyalama**
   ```bash
   svn checkout https://example.com/svn/myproject
   ```

2. **Değişiklikleri Gönderme**
   ```bash
   svn commit -m "Yenilikler eklendi"
   ```

3. **Güncelleme Yapma**
   ```bash
   svn update
   ```

4. **Değişiklik Durumunu Görüntüleme**
   ```bash
   svn status
   ```

5. **Geçmiş Değişiklikleri Görüntüleme**
   ```bash
   svn log
   ```

## İpuçları
- Değişikliklerinizi sık sık `commit` edin, böylece kaybolma riski azalır.
- `svn status` komutunu kullanarak, hangi dosyaların değiştiğini kontrol edin.
- Her `commit` işlemine açıklayıcı bir mesaj ekleyin, böylece geçmişteki değişiklikleri anlamak daha kolay olur.