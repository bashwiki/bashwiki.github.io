# [리눅스] Bash git 사용법

## Genel Bakış
`git`, dağıtık bir versiyon kontrol sistemi olarak, yazılım geliştirme süreçlerinde kaynak kodunu yönetmek için kullanılır. Geliştiricilerin projeleri üzerinde işbirliği yapmalarını, değişiklikleri takip etmelerini ve geçmişe dönük sürümlere erişim sağlamalarını mümkün kılar. `git`, hem bireysel projelerde hem de ekip projelerinde etkin bir şekilde kullanılabilir.

## Kullanım
`git` komutunun temel sözdizimi aşağıdaki gibidir:

```
git [komut] [seçenekler]
```

### Yaygın Seçenekler
- `init`: Yeni bir git deposu oluşturur.
- `clone`: Var olan bir git deposunu kopyalar.
- `add`: Değişiklikleri sahneye ekler.
- `commit`: Sahneye alınan değişiklikleri kaydeder.
- `push`: Yerel değişiklikleri uzak bir depoya gönderir.
- `pull`: Uzak depodaki değişiklikleri yerel depoya alır.
- `status`: Depodaki dosyaların durumunu gösterir.

## Örnekler

### Örnek 1: Yeni Bir Git Deposu Oluşturma
Yeni bir proje için git deposu oluşturmak için aşağıdaki komutu kullanabilirsiniz:

```bash
git init my_project
```
Bu komut, `my_project` adında yeni bir klasör oluşturur ve içinde bir git deposu başlatır.

### Örnek 2: Değişiklikleri Kaydetme
Mevcut bir git deposunda dosyalar üzerinde değişiklik yaptıktan sonra bu değişiklikleri kaydetmek için:

```bash
git add .
git commit -m "İlk değişiklikler"
```
İlk komut, tüm değişiklikleri sahneye eklerken, ikinci komut bu değişiklikleri "İlk değişiklikler" mesajıyla kaydeder.

## İpuçları
- Değişikliklerinizi sık sık kaydedin ve anlamlı commit mesajları yazın. Bu, geçmişteki değişiklikleri anlamayı kolaylaştırır.
- `git status` komutunu düzenli olarak kullanarak dosyalarınızın durumunu kontrol edin.
- Uzak bir depoya gönderim yapmadan önce `git pull` komutunu kullanarak en son değişiklikleri yerel deponuza alın. Bu, çakışmaları önlemeye yardımcı olur.
- Branch (dal) kullanarak farklı özellikler üzerinde çalışın. Bu, projelerinizi daha düzenli ve yönetilebilir hale getirir.