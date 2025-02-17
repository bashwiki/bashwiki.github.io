# [Linux] Bash alias Kullanımı: Komut kısayolları oluşturma

## Genel Bakış
`alias` komutu, Bash kabuğunda sık kullanılan komutlar için kısayollar oluşturmanıza olanak tanır. Bu, uzun ve karmaşık komutları daha kısa ve hatırlanması kolay hale getirir.

## Kullanım
Temel sözdizimi aşağıdaki gibidir:

```bash
alias [seçenekler] [kısayol]='[komut]'
```

## Yaygın Seçenekler
- `-p`: Mevcut tüm alias'ları listelemek için kullanılır.
- `-d`: Belirtilen alias'ı silmek için kullanılır.

## Yaygın Örnekler
Aşağıda `alias` komutunun bazı pratik örnekleri bulunmaktadır:

1. **Basit bir alias oluşturma**:
   ```bash
   alias ll='ls -la'
   ```
   Bu komut, `ll` yazdığınızda `ls -la` komutunu çalıştırır.

2. **Bir alias silme**:
   ```bash
   unalias ll
   ```
   Bu komut, daha önce oluşturduğunuz `ll` alias'ını siler.

3. **Birden fazla alias oluşturma**:
   ```bash
   alias gs='git status'
   alias gc='git commit'
   ```
   Bu komutlar, `gs` ve `gc` yazarak git durumunu kontrol etmenizi ve commit yapmanızı sağlar.

4. **Alias'ları listeleme**:
   ```bash
   alias -p
   ```
   Bu komut, mevcut tüm alias'ları gösterir.

## İpuçları
- Alias'larınızı genellikle `~/.bashrc` veya `~/.bash_profile` dosyasına ekleyerek her oturumda kullanılabilir hale getirin.
- Kısa ve anlamlı isimler seçin, böylece hangi komutun ne işe yaradığını hatırlamak kolay olur.
- Alias'larınızı düzenli olarak gözden geçirin ve kullanmadıklarınızı kaldırın.