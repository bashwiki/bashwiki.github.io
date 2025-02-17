# [Linux] Bash kullanıcıları kullanıcıları: Kullanıcı bilgilerini görüntüleme

## Genel Bakış
`users` komutu, sistemde oturum açmış olan kullanıcıların adlarını listelemek için kullanılır. Bu komut, birden fazla kullanıcının aynı anda oturum açtığı durumlarda oldukça faydalıdır.

## Kullanım
Temel sözdizimi şu şekildedir:
```bash
users [seçenekler] [argümanlar]
```

## Yaygın Seçenekler
- `-n`: Kullanıcı adlarını sadece bir kez gösterir, yani tekrar eden kullanıcı adlarını filtreler.
- `-r`: Sadece gerçek kullanıcıları gösterir, sistem kullanıcılarını hariç tutar.

## Yaygın Örnekler
Aşağıda `users` komutunun bazı pratik örnekleri bulunmaktadır:

1. **Tüm oturum açmış kullanıcıları listeleme:**
   ```bash
   users
   ```

2. **Tekrar eden kullanıcı adlarını filtreleme:**
   ```bash
   users -n
   ```

3. **Sadece gerçek kullanıcıları gösterme:**
   ```bash
   users -r
   ```

## İpuçları
- `users` komutunu sık sık kullanıyorsanız, çıktıyı bir dosyaya yönlendirmek için `>` operatörünü kullanabilirsiniz:
  ```bash
  users > kullanicilar.txt
  ```
- Oturum açmış kullanıcıların sayısını görmek için `wc -w` komutunu birleştirebilirsiniz:
  ```bash
  users | wc -w
  ```
- Kullanıcıların hangi terminalde oturum açtığını görmek için `who` komutunu kullanmayı düşünebilirsiniz.