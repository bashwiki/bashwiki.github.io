# [Linux] Bash inotifywait Kullanımı: Dosya sistemindeki değişiklikleri izleme

## Genel Bakış
`inotifywait`, Linux işletim sistemlerinde dosya sistemindeki değişiklikleri izlemek için kullanılan bir komut satırı aracıdır. Bu komut, belirli bir dosya veya dizin üzerinde meydana gelen olayları takip eder ve bu olaylar gerçekleştiğinde kullanıcıya bildirimde bulunur.

## Kullanım
Temel sözdizimi şu şekildedir:

```bash
inotifywait [seçenekler] [argümanlar]
```

## Yaygın Seçenekler
- `-m`: İzlemeyi sürekli hale getirir; olaylar meydana geldikçe bildirim yapar.
- `-r`: Alt dizinleri de dahil ederek rekürsif olarak izler.
- `-e`: İzlemek istediğiniz olayları belirtir (örneğin, `modify`, `create`, `delete`).
- `--format`: Çıktının formatını özelleştirmenizi sağlar.

## Yaygın Örnekler
Aşağıda `inotifywait` komutunun bazı pratik kullanım örnekleri verilmiştir:

### 1. Belirli bir dosyayı izleme
```bash
inotifywait /path/to/file.txt
```
Bu komut, `file.txt` dosyasında meydana gelen değişiklikleri izler.

### 2. Bir dizini izleme
```bash
inotifywait -m /path/to/directory
```
Bu komut, belirtilen dizindeki tüm değişiklikleri sürekli olarak izler.

### 3. Belirli olayları izleme
```bash
inotifywait -e modify,create,delete /path/to/directory
```
Bu komut, belirtilen dizinde dosya değiştirme, oluşturma ve silme olaylarını izler.

### 4. Rekürsif izleme
```bash
inotifywait -mr /path/to/directory
```
Bu komut, belirtilen dizin ve alt dizinlerdeki tüm değişiklikleri izler.

## İpuçları
- `inotifywait` komutunu bir betik içinde kullanarak otomatik bildirimler oluşturabilirsiniz.
- İzleme işlemini daha verimli hale getirmek için yalnızca gerekli olayları belirtin.
- Çıktıyı bir dosyaya yönlendirmek için `>` operatörünü kullanarak log dosyası oluşturabilirsiniz. Örneğin:
  ```bash
  inotifywait -m /path/to/directory > changes.log
  ```