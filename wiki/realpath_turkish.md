# [리눅스] Bash realpath 사용법

## Genel Bakış
`realpath` komutu, bir dosya veya dizinin gerçek yolunu (absolute path) belirlemek için kullanılır. Özellikle, sembolik bağlantılar (symlinks) içeren dosya yollarını çözümlemek ve mevcut çalışma dizinine göre tam yollar oluşturmak için yararlıdır. Bu komut, dosya sistemindeki dosyaların kesin konumlarını belirlemek isteyen geliştiriciler ve mühendisler için oldukça faydalıdır.

## Kullanım
`realpath` komutunun temel sözdizimi aşağıdaki gibidir:

```bash
realpath [seçenekler] dosya_yolu
```

### Yaygın Seçenekler
- `-m`, `--canonicalize-missing`: Dosya mevcut olmasa bile, belirtilen yolu çözümleyerek döndürür.
- `-q`, `--quiet`: Hata mesajlarını bastırır.
- `-s`, `--strip`: Yolu, yalnızca dosya adıyla döndürür, dizin bilgilerini içermez.

## Örnekler
### Örnek 1: Temel Kullanım
Aşağıdaki komut, `myfile.txt` adlı dosyanın gerçek yolunu döndürür:

```bash
realpath myfile.txt
```

Eğer `myfile.txt` dosyası mevcutsa, komut dosyanın tam yolunu (örneğin `/home/kullanici/myfile.txt`) gösterecektir.

### Örnek 2: Sembolik Bağlantıları Çözümleme
Eğer bir sembolik bağlantınız varsa, `realpath` komutu bu bağlantının gösterdiği gerçek dosya yolunu bulmanıza yardımcı olur:

```bash
realpath /path/to/symlink
```

Bu komut, `/path/to/symlink` bağlantısının gösterdiği gerçek dosyanın yolunu döndürecektir.

## İpuçları
- `realpath` komutunu kullanmadan önce dosyanın mevcut olup olmadığını kontrol etmek için `ls` veya `test` komutlarını kullanabilirsiniz.
- Sembolik bağlantılarla çalışırken, `realpath` komutunun çıktısını başka komutlarla birleştirerek daha karmaşık dosya işlemleri gerçekleştirebilirsiniz.
- Hata mesajlarını gizlemek için `-q` seçeneğini kullanarak daha temiz bir çıktı elde edebilirsiniz. 

`realpath`, dosya sistemindeki yolları yönetmek için güçlü bir araçtır ve doğru kullanıldığında, dosya ve dizinlerle çalışmayı büyük ölçüde kolaylaştırır.