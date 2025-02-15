# [리눅스] Bash inotifywait 사용법

## Genel Bakış
`inotifywait`, Linux işletim sistemlerinde dosya sistemindeki değişiklikleri izlemek için kullanılan bir komuttur. Bu komut, belirli bir dosya veya dizindeki olayları (oluşturma, silme, değiştirme vb.) izleyerek, bu olaylar gerçekleştiğinde kullanıcıya bildirimde bulunur. Geliştiriciler ve sistem yöneticileri için, dosya değişikliklerini izlemek ve otomatik işlemler gerçekleştirmek için oldukça faydalıdır.

## Kullanım
Temel sözdizimi şu şekildedir:

```bash
inotifywait [seçenekler] [dosya veya dizin]
```

### Yaygın Seçenekler
- `-m`: Sürekli izleme modunu etkinleştirir. Bu seçenek ile komut, belirtilen dosya veya dizin üzerindeki değişiklikleri sürekli olarak izler.
- `-r`: Dizinleri ve alt dizinlerini rekürsif olarak izler.
- `-e`: İzlenecek olayları belirtir. Örneğin, `modify`, `create`, `delete` gibi olaylar seçilebilir.
- `--format`: Çıktının formatını belirler. Özel formatlar kullanarak çıktıyı özelleştirmek mümkündür.

## Örnekler
### Örnek 1: Bir Dizin Üzerinde Değişiklikleri İzleme
Aşağıdaki komut, `/path/to/directory` dizininde sürekli olarak dosya değişikliklerini izler ve her değişiklikte bir bildirim gösterir:

```bash
inotifywait -m /path/to/directory
```

### Örnek 2: Belirli Olayları İzleme
Aşağıdaki komut, `/path/to/file.txt` dosyasında sadece değişiklikler (modify) olduğunda bildirimde bulunur:

```bash
inotifywait -e modify /path/to/file.txt
```

## İpuçları
- `inotifywait` komutunu bir betik içinde kullanarak, dosya değişikliklerine otomatik yanıtlar verebilirsiniz. Örneğin, bir dosya güncellendiğinde otomatik olarak bir yedekleme işlemi başlatabilirsiniz.
- İzleme işlemi sırasında çok fazla olay meydana gelebileceğinden, `--format` seçeneğini kullanarak çıktıyı daha okunabilir hale getirebilirsiniz.
- Dizin izlerken, `-r` seçeneği ile alt dizinlerdeki değişiklikleri de izlemeyi unutmayın. Bu, daha kapsamlı bir izleme sağlar.

`inotifywait`, dosya sistemindeki değişiklikleri takip etmek için güçlü bir araçtır ve doğru kullanıldığında geliştiricilere ve sistem yöneticilerine büyük kolaylık sağlar.