# [리눅스] Bash ls 사용법

## Genel Bakış
`ls` komutu, Unix ve Linux tabanlı işletim sistemlerinde dizin içeriğini listelemek için kullanılan bir komuttur. Kullanıcıların dosya ve dizinleri hızlı bir şekilde görüntülemesine olanak tanır. `ls`, genellikle terminalde çalıştırılarak, belirli bir dizindeki dosyaların ve alt dizinlerin adlarını gösterir.

## Kullanım
Temel `ls` komutunun sözdizimi aşağıdaki gibidir:

```bash
ls [seçenekler] [dizin]
```

### Yaygın Seçenekler
- `-l`: Uzun formatta listeleme yapar; dosya izinleri, sahip, boyut ve tarih gibi bilgileri gösterir.
- `-a`: Gizli dosyaları (nokta ile başlayan dosyalar) da dahil ederek tüm dosyaları listeler.
- `-h`: Boyutları insan tarafından okunabilir formatta gösterir (örneğin, KB, MB).
- `-R`: Dizinleri ve alt dizinleri rekürsif olarak listeler.
- `-t`: Dosyaları son değiştirilme tarihine göre sıralar.

## Örnekler
1. Temel kullanım:
   ```bash
   ls
   ```
   Bu komut, mevcut dizindeki dosya ve dizinlerin adlarını listeler.

2. Uzun formatta listeleme:
   ```bash
   ls -l
   ```
   Bu komut, mevcut dizindeki dosyaların detaylı bilgilerini gösterir.

3. Gizli dosyaları da listeleme:
   ```bash
   ls -a
   ```
   Bu komut, gizli dosyalar dahil olmak üzere mevcut dizindeki tüm dosyaları listeler.

## İpuçları
- `ls` komutunu daha okunabilir hale getirmek için `-lh` seçeneklerini birleştirerek kullanabilirsiniz:
  ```bash
  ls -lh
  ```
  Bu, dosya boyutlarını insan tarafından okunabilir formatta gösterir.
  
- Dizin içindeki dosyaları tarih sırasına göre görüntülemek için `-lt` seçeneğini kullanabilirsiniz:
  ```bash
  ls -lt
  ```
  
- `ls` komutunu sıkça kullandığınız dizinler için bir alias tanımlayarak zaman kazanabilirsiniz. Örneğin:
  ```bash
  alias ll='ls -l'
  ```
  Bu komut, `ll` yazarak uzun formatta listeleme yapmanızı sağlar.