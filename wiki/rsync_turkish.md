# [Linux] Bash rsync Kullanımı: Dosya senkronizasyonu ve aktarımı

## Genel Bakış
`rsync`, dosyaları ve dizinleri yerel veya uzak sistemler arasında senkronize etmek ve aktarmak için kullanılan güçlü bir komut satırı aracıdır. Hızlı ve verimli bir şekilde çalışır, çünkü yalnızca değişen dosya parçalarını aktarır.

## Kullanım
Temel kullanım şekli aşağıdaki gibidir:

```bash
rsync [seçenekler] [kaynak] [hedef]
```

## Yaygın Seçenekler
- `-a`: Arşiv modunu etkinleştirir; dosya izinlerini, zaman damgalarını ve sembolik bağlantıları korur.
- `-v`: Ayrıntılı çıktı sağlar; hangi dosyaların aktarıldığını gösterir.
- `-z`: Aktarım sırasında dosyaları sıkıştırır, bu da ağ üzerinden daha hızlı aktarım sağlar.
- `-r`: Alt dizinler dahil olmak üzere dizinleri kopyalar.
- `--delete`: Hedef dizindeki, kaynakta bulunmayan dosyaları siler.

## Yaygın Örnekler
1. **Yerel dosyaları senkronize etme:**
   ```bash
   rsync -av /kaynak/dizin/ /hedef/dizin/
   ```

2. **Uzak bir sunucuya dosya kopyalama:**
   ```bash
   rsync -av /yerel/dosya.txt kullanıcı@sunucu:/uzak/dizin/
   ```

3. **Uzak sunucudan yerel bir dizine dosya çekme:**
   ```bash
   rsync -av kullanıcı@sunucu:/uzak/dizin/ /yerel/dizin/
   ```

4. **Sıkıştırarak dosya aktarımı:**
   ```bash
   rsync -avz /kaynak/dizin/ kullanıcı@sunucu:/uzak/dizin/
   ```

5. **Hedefteki dosyaları silerek senkronize etme:**
   ```bash
   rsync -av --delete /kaynak/dizin/ /hedef/dizin/
   ```

## İpuçları
- **Yedekleme için kullanın:** `rsync`, dosyalarınızı yedeklemek için mükemmel bir araçtır. Değişiklikleri yalnızca bir kez aktararak zaman kazanabilirsiniz.
- **Test edin:** `--dry-run` seçeneği ile komutu test edebilir ve ne olacağını görebilirsiniz. Bu, yanlışlıkla dosya silme riskini azaltır.
- **SSH ile güvenli aktarım:** Uzak sunucularla güvenli bir bağlantı için `-e ssh` seçeneğini kullanabilirsiniz. Örneğin:
  ```bash
  rsync -av -e ssh /yerel/dosya.txt kullanıcı@sunucu:/uzak/dizin/
  ``` 

`rsync`, dosya aktarımında esneklik ve hız sunarak sıkça tercih edilen bir araçtır. Yukarıdaki örnekler ve ipuçları ile kullanımını kolaylaştırabilirsiniz.