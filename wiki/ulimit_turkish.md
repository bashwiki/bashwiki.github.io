# [Linux] Bash ulimit Kullanımı: Sistem kaynaklarını yönetme

## Genel Bakış
`ulimit` komutu, bir shell oturumu için sistem kaynaklarını sınırlandırmak amacıyla kullanılır. Bu komut, kullanıcıların belirli kaynakların (örneğin, açık dosya sayısı, bellek kullanımı) kullanımını kontrol etmelerine olanak tanır.

## Kullanım
Temel sözdizimi aşağıdaki gibidir:

```bash
ulimit [seçenekler] [argümanlar]
```

## Yaygın Seçenekler
- `-a`: Tüm mevcut sınırlamaları gösterir.
- `-c`: Çekirdek dosyası boyutunu ayarlar.
- `-d`: Veri segmenti boyutunu ayarlar.
- `-f`: Dosya boyutu sınırını ayarlar.
- `-l`: Kilitlenmiş bellek boyutunu ayarlar.
- `-n`: Açık dosya sayısı sınırını ayarlar.
- `-s`: Yığın boyutunu ayarlar.
- `-t`: CPU zamanını ayarlar.
- `-v`: Sanal bellek boyutunu ayarlar.

## Yaygın Örnekler
Aşağıda `ulimit` komutunun bazı pratik kullanımları verilmiştir:

1. **Tüm sınırlamaları görüntüleme:**
   ```bash
   ulimit -a
   ```

2. **Açık dosya sayısını 1024 olarak ayarlama:**
   ```bash
   ulimit -n 1024
   ```

3. **Çekirdek dosyası boyutunu sınırsız yapma:**
   ```bash
   ulimit -c unlimited
   ```

4. **Veri segmenti boyutunu 512 MB olarak ayarlama:**
   ```bash
   ulimit -d 524288
   ```

5. **CPU zamanını 60 saniye ile sınırlama:**
   ```bash
   ulimit -t 60
   ```

## İpuçları
- `ulimit` ayarlarını kalıcı hale getirmek için, genellikle `~/.bashrc` veya `~/.bash_profile` dosyasına ekleyebilirsiniz.
- Sınırlamaları ayarlarken dikkatli olun; yanlış ayarlar, uygulamalarınızın düzgün çalışmamasına neden olabilir.
- `ulimit` komutunu kullanmadan önce mevcut sınırlamaları kontrol etmek iyi bir uygulamadır, böylece gereksiz kısıtlamalar getirmemiş olursunuz.