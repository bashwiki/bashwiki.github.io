# [리눅스] Bash lsblk 사용법

## Genel Bakış
`lsblk` komutu, Linux işletim sistemlerinde blok aygıtlarının (diskler, bölümler, vb.) listesini görüntülemek için kullanılır. Bu komut, sistemdeki mevcut depolama aygıtlarını ve bunların hiyerarşik yapısını gösterir. Özellikle disk yönetimi ve sistem yapılandırması ile ilgilenen mühendisler ve geliştiriciler için faydalıdır.

## Kullanım
`lsblk` komutunun temel sözdizimi aşağıdaki gibidir:

```bash
lsblk [seçenekler]
```

### Yaygın Seçenekler
- `-a`, `--all`: Tüm aygıtları, boş olanlar dahil, listele.
- `-f`, `--fs`: Dosya sistemi bilgilerini göster.
- `-l`, `--list`: Liste formatında çıktı verir.
- `-o`, `--output`: Görüntülenecek sütunları belirtir.
- `-p`, `--paths`: Aygıt yollarını tam olarak gösterir.
- `-n`, `--noheadings`: Başlık satırını gizler.

## Örnekler

### Örnek 1: Temel Kullanım
Aşağıdaki komut, sistemdeki tüm blok aygıtlarını listeleyecektir:

```bash
lsblk
```

### Örnek 2: Dosya Sistemi Bilgileri ile Listeleme
Dosya sistemi bilgilerini de içeren bir liste görüntülemek için şu komutu kullanabilirsiniz:

```bash
lsblk -f
```

Bu komut, her bir aygıtın dosya sistemi türü ve etiket bilgilerini gösterir.

## İpuçları
- `lsblk` çıktısını daha okunabilir hale getirmek için `-o` seçeneği ile belirli sütunları seçebilirsiniz. Örneğin, sadece aygıt adı ve dosya sistemi türünü görüntülemek için:

  ```bash
  lsblk -o NAME,FSTYPE
  ```

- Çıktıyı bir dosyaya kaydetmek için `>` operatörünü kullanabilirsiniz:

  ```bash
  lsblk -f > lsblk_output.txt
  ```

Bu, `lsblk` komutunun çıktısını `lsblk_output.txt` dosyasına kaydedecektir. 

`lsblk` komutu, sistemdeki blok aygıtlarını anlamak ve yönetmek için güçlü bir araçtır. Doğru seçenekleri kullanarak, ihtiyacınıza uygun bilgileri kolayca elde edebilirsiniz.