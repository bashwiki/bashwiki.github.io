# [리눅스] Bash source 사용법

## Genel Bakış
`source` komutu, bir Bash betiğini veya bir dosyayı geçerli kabuk ortamında çalıştırmak için kullanılır. Bu komut, belirtilen dosyadaki tüm komutları yürütür ve bu komutların etkileri, çağrıldığı kabukta kalır. `source` komutu, genellikle ortam değişkenlerini ayarlamak veya kabuk ayar dosyalarını yüklemek için kullanılır.

## Kullanım
Temel sözdizimi şu şekildedir:

```bash
source [dosya_adı]
```

Alternatif olarak, `.` (nokta) ile de kullanılabilir:

```bash
. [dosya_adı]
```

### Yaygın Seçenekler
`source` komutunun kendine özgü seçenekleri yoktur; ancak, dosya adını belirtirken, dosyanın tam yolunu kullanmak veya mevcut dizinde olup olmadığını kontrol etmek önemlidir.

## Örnekler

### Örnek 1: Ortam Değişkenlerini Yüklemek
Bir dosyada tanımlı ortam değişkenlerini yüklemek için `source` komutunu kullanabilirsiniz. Örneğin, `env.sh` adında bir dosyanız varsa:

```bash
source env.sh
```

Bu komut, `env.sh` dosyasındaki tüm değişkenleri geçerli kabuk ortamınıza yükleyecektir.

### Örnek 2: Kabuk Ayar Dosyalarını Yüklemek
Kendi kabuk ayar dosyanızı yüklemek için de `source` komutunu kullanabilirsiniz. Örneğin, `.bashrc` dosyanızı güncelledikten sonra değişikliklerin hemen etkili olmasını sağlamak için:

```bash
source ~/.bashrc
```

Bu komut, `.bashrc` dosyasındaki tüm ayarları geçerli oturumda uygulayacaktır.

## İpuçları
- `source` komutunu kullanarak dosyaları yüklerken, dosyanın doğru bir şekilde yazıldığından ve gerekli izinlere sahip olduğundan emin olun.
- Sıklıkla kullandığınız ortam değişkenlerini ve fonksiyonları içeren bir dosya oluşturmak, çalışma ortamınızı daha verimli hale getirebilir.
- `.bash_profile` veya `.bashrc` gibi dosyalarınızı güncelledikten sonra değişikliklerinizi görmek için `source` komutunu kullanmayı unutmayın.