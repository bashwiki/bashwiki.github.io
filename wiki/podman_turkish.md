# [리눅스] Bash podman 사용법

## Overview
Podman, konteyner yönetimi için kullanılan bir araçtır. Docker ile benzer bir işlevsellik sunar ancak Podman, daemon tabanlı bir mimariye sahip değildir. Bu, kullanıcıların konteynerleri doğrudan komut satırından yönetmelerine olanak tanır. Podman, konteynerleri oluşturma, çalıştırma, durdurma ve silme gibi işlemleri gerçekleştirmek için kullanılır. Ayrıca, Podman, konteynerlerinizi gruplamak için "pod" kavramını kullanarak çoklu konteyner uygulamalarını yönetmeyi kolaylaştırır.

## Usage
Podman komutunun temel sözdizimi aşağıdaki gibidir:

```bash
podman [OPTIONS] COMMAND [ARG...]
```

### Yaygın Seçenekler
- `--help`: Komut hakkında yardım almanızı sağlar.
- `--version`: Podman sürümünü gösterir.
- `-d`, `--detach`: Konteyneri arka planda çalıştırır.
- `--name`: Konteynere özel bir isim atar.
- `-p`, `--publish`: Konteynerin portunu dışarıya açar.

## Examples
### Örnek 1: Basit bir konteyner çalıştırma
Aşağıdaki komut, "nginx" görüntüsünden bir konteyner oluşturur ve çalıştırır:

```bash
podman run -d --name my-nginx -p 8080:80 nginx
```
Bu komut, `my-nginx` adında bir konteyner oluşturur ve 8080 portunu 80 portuna yönlendirir.

### Örnek 2: Çalışan konteynerleri listeleme
Aşağıdaki komut, sistemdeki tüm çalışan konteynerleri listeler:

```bash
podman ps
```

## Tips
- Podman ile çalışırken, konteynerlerinizi yönetmek için `podman ps`, `podman stop`, `podman rm` gibi komutları kullanarak düzenli bir şekilde konteynerlerinizi kontrol edin.
- Konteynerlerinizi isimlendirmek, yönetimi kolaylaştırır. Her konteynere anlamlı bir isim vermeyi unutmayın.
- Podman ile çalışırken, güvenlik için konteynerlerinizi en son güncellemelerle güncel tutmaya özen gösterin.