# [리눅스] Bash netstat 사용법

## Genel Bakış
`netstat`, ağ bağlantılarını, yönlendirme tablolarını, arayüz istatistiklerini ve daha fazlasını görüntülemek için kullanılan bir komut satırı aracıdır. Sistem yöneticileri ve geliştiriciler, ağ durumu hakkında bilgi edinmek ve sorunları teşhis etmek için bu komutu sıklıkla kullanır. `netstat`, aktif bağlantılar, dinleme portları ve ağ istatistikleri hakkında kapsamlı bilgiler sunar.

## Kullanım
`netstat` komutunun temel sözdizimi şu şekildedir:

```bash
netstat [seçenekler]
```

### Yaygın Seçenekler
- `-a`: Tüm bağlantıları ve dinleme portlarını gösterir.
- `-t`: TCP bağlantılarını gösterir.
- `-u`: UDP bağlantılarını gösterir.
- `-n`: Adresleri ve port numaralarını sayısal olarak gösterir.
- `-l`: Sadece dinleyen portları gösterir.
- `-p`: Hangi programın hangi bağlantıyı kullandığını gösterir.

## Örnekler
### Örnek 1: Tüm Aktif Bağlantıları Görüntüleme
Aşağıdaki komut, sistemdeki tüm aktif bağlantıları ve dinleme portlarını listeleyecektir:

```bash
netstat -a
```

### Örnek 2: TCP Bağlantılarını Görüntüleme
Sadece TCP bağlantılarını görmek için şu komutu kullanabilirsiniz:

```bash
netstat -t
```

## İpuçları
- `netstat` çıktısını daha okunabilir hale getirmek için `grep` komutunu kullanabilirsiniz. Örneğin, belirli bir portu kontrol etmek için:

```bash
netstat -tuln | grep ':80'
```

- Ağ sorunlarını teşhis ederken, `netstat` çıktısını düzenli olarak kontrol etmek, bağlantı sorunlarını hızlı bir şekilde tespit etmenize yardımcı olabilir.
- `-p` seçeneği ile hangi uygulamanın hangi bağlantıyı kullandığını görmek, güvenlik ve performans sorunlarını analiz etmek için faydalıdır.

`netstat`, ağ durumu hakkında derinlemesine bilgi sağladığı için sistem yöneticileri ve geliştiriciler için vazgeçilmez bir araçtır.