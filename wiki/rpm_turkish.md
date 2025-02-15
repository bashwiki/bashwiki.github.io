# [리눅스] Bash rpm 사용법

## Overview
`rpm` (Red Hat Package Manager), Red Hat tabanlı sistemlerde kullanılan bir paket yönetim aracıdır. RPM, yazılım paketlerini kurmak, kaldırmak, güncellemek ve sorgulamak için kullanılır. RPM paketleri, yazılımın bağımlılıklarını ve dosya konumlarını içeren bir yapıda sunulur, bu sayede sistem yöneticileri ve geliştiriciler, yazılımları kolayca yönetebilir.

## Usage
Temel `rpm` komutunun sözdizimi aşağıdaki gibidir:

```bash
rpm [seçenekler] [paket]
```

### Yaygın Seçenekler
- `-i`: Yeni bir RPM paketi kurar.
- `-e`: Kurulu bir RPM paketini kaldırır.
- `-U`: Mevcut bir paketi günceller veya yeni bir paket kurar.
- `-q`: Kurulu bir paketi sorgular.
- `-l`: Belirtilen paketin dosyalarını listeler.
- `--help`: Komut hakkında yardım bilgisi gösterir.

## Examples
### Örnek 1: RPM Paketi Kurma
Aşağıdaki komut, `example.rpm` adlı bir RPM paketini kurar:

```bash
rpm -i example.rpm
```

### Örnek 2: Kurulu Paketi Sorgulama
Aşağıdaki komut, `example` adlı kurulu paketin bilgilerini sorgular:

```bash
rpm -q example
```

## Tips
- RPM paketlerini kurmadan önce, bağımlılıkların karşılandığından emin olun. Bağımlılık sorunları, kurulum sırasında hatalara yol açabilir.
- `rpm` komutunu kullanırken, genellikle `sudo` ile çalıştırmak gerekebilir, çünkü paket yönetimi sistem düzeyinde değişiklikler yapar.
- Paketlerin güncel olup olmadığını kontrol etmek için `rpm -q --changelog paket_adı` komutunu kullanarak değişiklik günlüklerini inceleyebilirsiniz.
- `rpm` ile çalışırken, `--nodeps` seçeneğini kullanarak bağımlılık kontrolünü atlayabilirsiniz, ancak bu genellikle önerilmez.