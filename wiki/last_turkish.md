# [Linux] Bash last komutu: Kullanıcı oturum geçmişini görüntüleme

## Genel Bakış
`last` komutu, sistemdeki kullanıcıların oturum açma ve kapama geçmişini görüntülemek için kullanılır. Bu komut, kullanıcıların ne zaman giriş yaptığını ve ne zaman sistemden çıktığını gösterir. Ayrıca, sistemin yeniden başlatıldığı zamanları da listeler.

## Kullanım
Temel sözdizimi şu şekildedir:
```
last [seçenekler] [argümanlar]
```

## Yaygın Seçenekler
- `-a`: Kullanıcıların bağlantı kurduğu uzak ana bilgisayar adını gösterir.
- `-n [sayı]`: Son [sayı] kadar oturumu gösterir.
- `-x`: Sistem yeniden başlatmalarını ve kapanmalarını da gösterir.
- `-R`: Uzak ana bilgisayar adını gizler.

## Yaygın Örnekler
1. Tüm kullanıcı oturum geçmişini görüntüleme:
   ```bash
   last
   ```

2. Son 5 oturumu görüntüleme:
   ```bash
   last -n 5
   ```

3. Kullanıcı adı "ali" olan kişinin oturum geçmişini görüntüleme:
   ```bash
   last ali
   ```

4. Sistem yeniden başlatmalarını ve kapanmalarını gösterme:
   ```bash
   last -x
   ```

5. Uzak ana bilgisayar adlarını gizleyerek oturum geçmişini görüntüleme:
   ```bash
   last -R
   ```

## İpuçları
- `last` komutunu düzenli olarak kullanarak sistemdeki kullanıcı etkinliklerini takip edebilir ve güvenlik denetimleri yapabilirsiniz.
- Eğer uzun bir oturum geçmişine sahipseniz, `-n` seçeneği ile belirli bir sayıda oturumu görüntülemek, çıktıyı daha yönetilebilir hale getirebilir.
- `last` çıktısını bir dosyaya yönlendirmek için `>` operatörünü kullanarak, geçmişi kaydedebilir ve daha sonra inceleyebilirsiniz. Örneğin:
  ```bash
  last > oturum_gecmisi.txt
  ```