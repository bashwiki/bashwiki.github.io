# [Linux] Bash lsof Kullanımı: Açık dosyaları listeleme

## Genel Bakış
`lsof` (List Open Files), sistemde açık olan dosyaları ve bu dosyaları kullanan süreçleri listelemek için kullanılan bir komuttur. Bu komut, dosya tanımlayıcıları, ağ bağlantıları ve daha fazlası hakkında bilgi sağlar.

## Kullanım
Temel sözdizimi aşağıdaki gibidir:
```bash
lsof [seçenekler] [argümanlar]
```

## Yaygın Seçenekler
- `-i`: Ağ bağlantılarını listelemek için kullanılır.
- `-u [kullanıcı]`: Belirtilen kullanıcıya ait açık dosyaları gösterir.
- `-p [pid]`: Belirtilen süreç kimliğine (PID) ait açık dosyaları listeler.
- `+D [dizin]`: Belirtilen dizindeki tüm dosyaları ve alt dizinlerdeki dosyaları gösterir.

## Yaygın Örnekler
Aşağıda `lsof` komutunun bazı pratik kullanımları verilmiştir:

1. Tüm açık dosyaları listelemek için:
   ```bash
   lsof
   ```

2. Belirli bir kullanıcıya ait açık dosyaları görüntülemek için:
   ```bash
   lsof -u kullanıcı_adı
   ```

3. Belirli bir süreç kimliğine ait dosyaları listelemek için:
   ```bash
   lsof -p 1234
   ```

4. Belirli bir ağ bağlantısını kontrol etmek için:
   ```bash
   lsof -i :80
   ```

5. Belirli bir dizindeki açık dosyaları listelemek için:
   ```bash
   lsof +D /path/to/directory
   ```

## İpuçları
- `lsof` komutunu çalıştırmak için genellikle yönetici (root) yetkilerine ihtiyaç duyulabilir, bu nedenle `sudo` ile kullanmak faydalı olabilir.
- Açık dosyaları izlemek için `lsof` çıktısını `grep` ile filtreleyerek belirli dosyaları veya süreçleri bulabilirsiniz.
- `lsof` çıktısını bir dosyaya yönlendirmek için `>` operatörünü kullanarak sonuçları kaydedebilirsiniz. Örneğin:
  ```bash
  lsof > lsof_output.txt
  ```