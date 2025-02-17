# [Linux] Bash finger Kullanımı: Kullanıcı bilgilerini görüntüleme

## Overview
`finger` komutu, sistemdeki kullanıcılar hakkında bilgi almak için kullanılır. Bu komut, kullanıcıların oturum durumu, gerçek adı, ev dizini gibi bilgileri görüntülemenizi sağlar.

## Usage
Temel sözdizimi aşağıdaki gibidir:

```bash
finger [options] [arguments]
```

## Common Options
- `-l`: Kullanıcı bilgilerini daha ayrıntılı bir şekilde gösterir.
- `-m`: Kullanıcı adını tam olarak eşleştirir.
- `-s`: Kullanıcı bilgilerini daha kısa bir formatta gösterir.

## Common Examples
Aşağıda `finger` komutunun bazı yaygın kullanım örnekleri bulunmaktadır:

1. Tüm kullanıcıları listeleme:
   ```bash
   finger
   ```

2. Belirli bir kullanıcı hakkında bilgi alma:
   ```bash
   finger kullanıcı_adı
   ```

3. Kullanıcı bilgilerini daha ayrıntılı gösterme:
   ```bash
   finger -l kullanıcı_adı
   ```

4. Kullanıcı adını tam olarak eşleştirerek arama:
   ```bash
   finger -m kullanıcı_adı
   ```

5. Kısa formatta kullanıcı bilgilerini görüntüleme:
   ```bash
   finger -s
   ```

## Tips
- `finger` komutunu kullanmadan önce, sistemde bu komutun yüklü olduğundan emin olun.
- Kullanıcı adlarını yazarken büyük/küçük harf duyarlılığına dikkat edin.
- `finger` komutunu sıkça kullanıyorsanız, alias oluşturarak daha hızlı erişim sağlayabilirsiniz. Örneğin:
  ```bash
  alias f='finger'
  ```