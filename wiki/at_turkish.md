# [리눅스] Bash at 사용법

## Genel Bakış
`at` komutu, belirli bir zamanda bir veya daha fazla komutun çalıştırılmasını sağlamak için kullanılan bir zamanlayıcıdır. Genellikle, belirli bir tarih ve saatte bir görev planlamak için kullanılır. Bu, sistem yöneticileri ve geliştiriciler için otomatik görevleri zamanlamak adına oldukça yararlıdır.

## Kullanım
`at` komutunun temel sözdizimi şu şekildedir:

```bash
at [seçenekler] [zaman]
```

### Yaygın Seçenekler
- `-f [dosya]`: Belirtilen dosyadaki komutları çalıştırır.
- `-m`: Görev tamamlandığında e-posta bildirimi gönderir.
- `-q [kuyruk]`: Görevin hangi kuyrukta çalışacağını belirtir.
- `-l`: Planlanmış görevlerin listesini gösterir.
- `-d`: Belirtilen görevi iptal eder.

## Örnekler

### Örnek 1: Basit Görev Planlama
Aşağıdaki komut, 5 dakika sonra `echo "Merhaba Dünya"` komutunu çalıştırır:

```bash
echo "echo Merhaba Dünya" | at now + 5 minutes
```

### Örnek 2: Belirli Bir Tarihte Görev Planlama
Aşağıdaki komut, 1 Ekim 2023 tarihinde saat 14:00'te `backup.sh` dosyasını çalıştırır:

```bash
at 14:00 10/01/2023 -f backup.sh
```

## İpuçları
- `at` komutunu kullanmadan önce, sisteminizde `atd` (at daemon) hizmetinin çalıştığından emin olun. Bu hizmet, planlanmış görevleri yürütmek için gereklidir.
- Görevlerinizi düzenli olarak kontrol etmek için `at -l` komutunu kullanarak planlanmış görevlerinizi listeleyebilirsiniz.
- Görevlerinizi iptal etmek için `at -d [görev numarası]` komutunu kullanabilirsiniz. Görev numarasını `at -l` komutuyla öğrenebilirsiniz.

Bu bilgilerle, `at` komutunu etkili bir şekilde kullanarak zamanlama işlemlerinizi kolaylaştırabilirsiniz.