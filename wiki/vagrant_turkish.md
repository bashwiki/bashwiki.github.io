# [Linux] Bash vagrant Kullanımı: Sanal Ortam Yönetimi

## Genel Bakış
Vagrant, yazılım geliştirme süreçlerinde sanal ortamlar oluşturmak ve yönetmek için kullanılan bir araçtır. Geliştiricilerin projeleri için tutarlı ve taşınabilir geliştirme ortamları oluşturmasına olanak tanır.

## Kullanım
Vagrant komutunun temel sözdizimi aşağıdaki gibidir:

```bash
vagrant [seçenekler] [argümanlar]
```

## Yaygın Seçenekler
- `init`: Yeni bir Vagrant projesi başlatmak için kullanılır.
- `up`: Vagrant ortamını başlatır ve yapılandırır.
- `halt`: Çalışan Vagrant ortamını durdurur.
- `destroy`: Vagrant ortamını tamamen siler.
- `ssh`: Vagrant makinesine SSH ile bağlanır.

## Yaygın Örnekler
Aşağıda Vagrant komutunun bazı pratik örnekleri verilmiştir:

### Yeni Bir Vagrant Projesi Başlatma
```bash
vagrant init ubuntu/bionic64
```

### Vagrant Ortamını Başlatma
```bash
vagrant up
```

### Vagrant Ortamını Durdurma
```bash
vagrant halt
```

### Vagrant Ortamını Silme
```bash
vagrant destroy
```

### Vagrant Makinesine SSH ile Bağlanma
```bash
vagrant ssh
```

## İpuçları
- Vagrantfile'ınızı versiyon kontrol sistemine ekleyin, böylece ekip arkadaşlarınızla paylaşabilirsiniz.
- Ortamınızı güncel tutmak için `vagrant box update` komutunu düzenli olarak kullanın.
- Vagrant ile çalışırken, her zaman `vagrant status` komutunu kullanarak ortamınızın durumunu kontrol edin.