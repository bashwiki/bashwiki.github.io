# [Linux] Bash tput Kullanımı: Terminalde metin biçimlendirme ve renk ayarlama

## Genel Bakış
`tput` komutu, terminalde metin biçimlendirme ve renk ayarlama işlemleri için kullanılan bir araçtır. Bu komut, terminalin özelliklerini kontrol etmeye ve terminaldeki metinlerin görünümünü değiştirmeye olanak tanır.

## Kullanım
Temel sözdizimi aşağıdaki gibidir:

```bash
tput [seçenekler] [argümanlar]
```

## Yaygın Seçenekler
- `setaf [numara]`: Metin rengini ayarlar. Renk numarası 0-7 arasında olmalıdır.
- `setab [numara]`: Arka plan rengini ayarlar. Renk numarası 0-7 arasında olmalıdır.
- `bold`: Metni kalın yapar.
- `underline`: Metni altı çizili yapar.
- `clear`: Terminal ekranını temizler.
- `cup [satır] [sütun]`: İmleci belirtilen satır ve sütuna taşır.

## Yaygın Örnekler
Aşağıda `tput` komutunun bazı pratik kullanım örnekleri bulunmaktadır:

1. **Metin Rengini Ayarlamak:**
   ```bash
   tput setaf 1; echo "Bu kırmızı bir metin."
   ```

2. **Arka Plan Rengini Ayarlamak:**
   ```bash
   tput setab 4; echo "Bu mavi arka plana sahip bir metin."
   ```

3. **Kalın Metin:**
   ```bash
   tput bold; echo "Bu kalın bir metin."
   ```

4. **Altı Çizili Metin:**
   ```bash
   tput underline; echo "Bu altı çizili bir metin."
   ```

5. **Ekranı Temizlemek:**
   ```bash
   tput clear
   ```

6. **İmleci Belirli Bir Konuma Taşımak:**
   ```bash
   tput cup 5 10; echo "İmleç buraya taşındı."
   ```

## İpuçları
- `tput` komutunu bir script içinde kullanarak, terminal çıktılarınızı daha okunabilir hale getirebilirsiniz.
- Renk kodlarını öğrenmek için `tput colors` komutunu kullanarak terminalinizin desteklediği renk sayısını kontrol edebilirsiniz.
- Terminaldeki değişikliklerin kalıcı olması için `tput` komutlarını bir profil dosyasına ekleyebilirsiniz.