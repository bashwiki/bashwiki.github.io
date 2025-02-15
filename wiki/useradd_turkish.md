# [리눅스] Bash useradd 사용법

## Overview
`useradd` komutu, Linux ve Unix tabanlı işletim sistemlerinde yeni kullanıcı hesapları oluşturmak için kullanılır. Bu komut, sistem yöneticilerinin kullanıcıları yönetmesine olanak tanır ve yeni bir kullanıcı oluştururken gerekli ayarları yapar. Kullanıcı adı, ev dizini, kabuk gibi bilgileri belirleyerek yeni bir kullanıcı hesabı oluşturulmasını sağlar.

## Usage
`useradd` komutunun temel sözdizimi aşağıdaki gibidir:

```bash
useradd [seçenekler] kullanıcı_adı
```

### Yaygın Seçenekler
- `-m`: Kullanıcı için ev dizini oluşturur.
- `-s`: Kullanıcının varsayılan kabuğunu belirtir (örneğin, `/bin/bash`).
- `-G`: Kullanıcıyı belirtilen gruplara ekler.
- `-d`: Kullanıcının ev dizinini belirtir.
- `-r`: Sistem kullanıcısı oluşturur (genellikle sistem hizmetleri için kullanılır).

## Examples
### Örnek 1: Basit Kullanıcı Oluşturma
Aşağıdaki komut, "yeni_kullanici" adında bir kullanıcı oluşturur ve varsayılan ayarlarla bir ev dizini oluşturur:

```bash
sudo useradd -m yeni_kullanici
```

### Örnek 2: Belirli Bir Kabuk ve Ev Dizinine Sahip Kullanıcı Oluşturma
Aşağıdaki komut, "geliştirici" adında bir kullanıcı oluşturur, ev dizinini `/home/geliştirici` olarak ayarlar ve varsayılan kabuk olarak `/bin/bash` kullanır:

```bash
sudo useradd -m -s /bin/bash -d /home/geliştirici geliştirici
```

## Tips
- Kullanıcı oluşturduktan sonra, `passwd` komutunu kullanarak kullanıcıya bir şifre atamayı unutmayın.
- Kullanıcıları gruplara eklemek için `-G` seçeneğini kullanarak daha iyi bir erişim yönetimi sağlayabilirsiniz.
- Kullanıcı oluşturma işlemlerini otomatikleştirmek için bir betik yazmayı düşünebilirsiniz, böylece birden fazla kullanıcıyı aynı anda oluşturabilirsiniz.
- Kullanıcı bilgilerini kontrol etmek için `/etc/passwd` dosyasını inceleyebilirsiniz.