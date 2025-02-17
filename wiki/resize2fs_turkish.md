# [Linux] Bash resize2fs Kullanımı: Dosya sistemini yeniden boyutlandırma

## Genel Bakış
`resize2fs`, Linux işletim sistemlerinde kullanılan bir komuttur ve dosya sisteminin boyutunu değiştirmek için kullanılır. Bu komut, genellikle bir dosya sisteminin boyutunu artırmak veya azaltmak için kullanılır ve ext2, ext3 ve ext4 dosya sistemleri ile uyumludur.

## Kullanım
Temel sözdizimi aşağıdaki gibidir:

```
resize2fs [seçenekler] [argümanlar]
```

## Yaygın Seçenekler
- `-f`: Dosya sisteminin boyutunu zorla değiştirir.
- `-p`: İşlem sırasında ilerleme çubuğunu gösterir.
- `-s`: Dosya sisteminin boyutunu otomatik olarak ayarlar.
- `-M`: Dosya sistemini minimum boyuta küçültür.

## Yaygın Örnekler
Aşağıda `resize2fs` komutunun bazı pratik kullanım örnekleri bulunmaktadır:

### Dosya Sistemini Büyütme
Bir dosya sistemini büyütmek için aşağıdaki komutu kullanabilirsiniz:
```bash
resize2fs /dev/sda1
```

### Dosya Sistemini Küçültme
Bir dosya sistemini belirli bir boyuta küçültmek için:
```bash
resize2fs /dev/sda1 10G
```

### İlerleme Çubuğu ile Boyut Değiştirme
İlerleme çubuğunu göstererek dosya sistemini büyütmek için:
```bash
resize2fs -p /dev/sda1
```

### Minimum Boyuta Küçültme
Dosya sistemini minimum boyuta küçültmek için:
```bash
resize2fs -M /dev/sda1
```

## İpuçları
- `resize2fs` komutunu kullanmadan önce dosya sisteminin sağlıklı olduğundan emin olun. Bunu yapmak için `fsck` komutunu kullanabilirsiniz.
- Dosya sisteminin boyutunu değiştirmeden önce yedek almayı unutmayın.
- Boyut değişikliği işlemi sırasında sisteminize zarar vermemek için, mümkünse bu işlemleri bakım zamanlarında gerçekleştirin.