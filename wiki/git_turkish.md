# [Linux] Bash git Kullanımı: Versiyon kontrol sistemi

## Genel Bakış
Git, yazılım geliştirme süreçlerinde kaynak kodunu yönetmek için kullanılan bir versiyon kontrol sistemidir. Geliştiricilerin projelerini takip etmelerine, değişiklikleri kaydetmelerine ve ekip içinde işbirliği yapmalarına olanak tanır.

## Kullanım
Git komutunun temel sözdizimi aşağıdaki gibidir:

```bash
git [seçenekler] [argümanlar]
```

## Yaygın Seçenekler
- `clone`: Uzak bir depoyu yerel bir kopyasını oluşturur.
- `commit`: Değişiklikleri kaydeder.
- `push`: Yerel değişiklikleri uzak depoya gönderir.
- `pull`: Uzak depodaki değişiklikleri yerel depoya alır.
- `status`: Depodaki dosyaların durumunu gösterir.

## Yaygın Örnekler
Aşağıda git komutunun bazı yaygın kullanım örnekleri bulunmaktadır:

### Depo Klonlama
Uzak bir depoyu yerel bilgisayarınıza klonlamak için:

```bash
git clone https://github.com/kullanici/depoadi.git
```

### Değişiklikleri Kaydetme
Yapılan değişiklikleri kaydetmek için:

```bash
git add .
git commit -m "Değişiklik mesajı"
```

### Değişiklikleri Gönderme
Yerel değişikliklerinizi uzak depoya göndermek için:

```bash
git push origin ana
```

### Uzak Depodan Güncelleme Alma
Uzak depodaki değişiklikleri yerel deponuza almak için:

```bash
git pull origin ana
```

### Depo Durumunu Kontrol Etme
Depodaki dosyaların durumunu kontrol etmek için:

```bash
git status
```

## İpuçları
- Değişikliklerinizi sık sık kaydedin ve anlamlı commit mesajları yazın.
- Uzak depoya gönderim yapmadan önce `git pull` komutunu kullanarak güncel olduğunuzdan emin olun.
- Branch (dal) kullanarak farklı özellikler üzerinde çalışın ve ana dalı koruyun.