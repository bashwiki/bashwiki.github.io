# [Linux] Bash su Kullanımı: Kullanıcı Değiştirme Komutu

## Genel Bakış
`su` komutu, Linux ve Unix benzeri işletim sistemlerinde kullanıcı değiştirmek için kullanılır. Bu komut, mevcut oturumdan farklı bir kullanıcı olarak oturum açmanıza olanak tanır. Genellikle, yönetici (root) yetkilerine sahip olmak için kullanılır.

## Kullanım
Temel sözdizimi aşağıdaki gibidir:

```bash
su [seçenekler] [kullanıcı]
```

## Yaygın Seçenekler
- `-l` veya `--login`: Hedef kullanıcının oturumunu başlatır ve kullanıcının ortam değişkenlerini yükler.
- `-c` : Belirtilen komutu hedef kullanıcı olarak çalıştırır.
- `-s` : Hedef kullanıcı için belirli bir kabuk belirtir.

## Yaygın Örnekler
Aşağıda `su` komutunun bazı yaygın kullanım örnekleri verilmiştir:

1. **Root Kullanıcısına Geçiş:**
   ```bash
   su
   ```
   Bu komut, root kullanıcısına geçiş yapmanızı sağlar. Şifre girmeniz istenecektir.

2. **Belirli Bir Kullanıcıya Geçiş:**
   ```bash
   su kullanıcı_adı
   ```
   Bu komut, belirtilen kullanıcıya geçiş yapmanızı sağlar.

3. **Belirli Bir Komutu Başka Bir Kullanıcı Olarak Çalıştırma:**
   ```bash
   su -c "komut" kullanıcı_adı
   ```
   Bu komut, belirtilen komutu hedef kullanıcı olarak çalıştırır.

4. **Login Shell ile Geçiş:**
   ```bash
   su -l kullanıcı_adı
   ```
   Bu komut, belirtilen kullanıcı için tam bir oturum başlatır.

## İpuçları
- `su` komutunu kullanırken, hedef kullanıcının şifresini bilmeniz gerektiğini unutmayın.
- Root kullanıcısı olarak çalışırken dikkatli olun; yanlış bir komut sisteminize zarar verebilir.
- `sudo` komutunu kullanmayı düşünün; bu, belirli komutları çalıştırmak için root yetkisi almanın daha güvenli bir yoludur.