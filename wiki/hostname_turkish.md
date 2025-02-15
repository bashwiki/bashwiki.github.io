# [리눅스] Bash hostname 사용법

## Overview
`hostname` komutu, bir sistemin ağdaki adını görüntülemek veya değiştirmek için kullanılır. Bu komut, özellikle sunucular ve ağ cihazları için kritik öneme sahiptir, çünkü sistemin kimliğini belirler ve ağ üzerinde diğer cihazlarla iletişim kurarken kullanılır. `hostname`, hem geçici olarak (sistem yeniden başlatıldığında kaybolur) hem de kalıcı olarak (sistem yapılandırma dosyalarında değişiklik yaparak) ayarlanabilir.

## Usage
`hostname` komutunun temel sözdizimi aşağıdaki gibidir:

```bash
hostname [seçenekler] [yeni_hostname]
```

### Yaygın Seçenekler:
- `-a`, `--alias`: Sistem için tanımlı olan takma adı gösterir.
- `-d`, `--domain`: Sistem alan adını gösterir.
- `-f`, `--fqdn`: Tam nitelikli alan adını (FQDN) gösterir.
- `-i`, `--ip-address`: Sistem IP adresini gösterir.
- `-s`, `--short`: Kısa hostname'i gösterir.
- `--help`: Komut hakkında yardım bilgisi gösterir.
- `--version`: Komutun sürüm bilgilerini gösterir.

## Examples
### Örnek 1: Mevcut hostname'i görüntüleme
Mevcut hostname'i görmek için aşağıdaki komutu kullanabilirsiniz:

```bash
hostname
```

Bu komut, sistemin mevcut ağ adını terminalde gösterecektir.

### Örnek 2: Yeni bir hostname ayarlama
Sistemin hostname'ini değiştirmek için aşağıdaki komutu kullanabilirsiniz:

```bash
sudo hostname yeni_hostname
```

Bu komut, sistemin hostname'ini "yeni_hostname" olarak ayarlayacaktır. Ancak, bu değişiklik geçici olacak ve sistem yeniden başlatıldığında kaybolacaktır.

## Tips
- Kalıcı bir değişiklik yapmak istiyorsanız, `/etc/hostname` dosyasını düzenlemeniz ve yeni hostname'i buraya eklemeniz gerekmektedir. Ardından, sistemi yeniden başlatmalısınız.
- Ağ üzerindeki diğer cihazlarla uyumlu olabilmesi için hostname'iniz kısa ve anlamlı olmalıdır.
- `hostname` komutunu kullanmadan önce, sistemdeki mevcut hostname'i kontrol etmek iyi bir uygulamadır, böylece gereksiz değişikliklerden kaçınabilirsiniz.