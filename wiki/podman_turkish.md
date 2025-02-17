# [Linux] Bash podman Kullanımı: Konteynerleri yönetmek için bir araç

## Overview
Podman, konteynerleri yönetmek için kullanılan bir komut satırı aracıdır. Docker'a benzer bir işlevsellik sunar, ancak daemon gerektirmeden çalışır. Bu, kullanıcıların konteynerleri daha güvenli ve izole bir şekilde yönetmelerine olanak tanır.

## Usage
Podman komutunun temel sözdizimi aşağıdaki gibidir:

```bash
podman [options] [arguments]
```

## Common Options
- `run`: Yeni bir konteyner başlatır.
- `ps`: Çalışan konteynerlerin listesini gösterir.
- `stop`: Belirtilen konteyneri durdurur.
- `rm`: Durdurulmuş bir konteyneri siler.
- `images`: Mevcut görüntülerin listesini gösterir.

## Common Examples
Aşağıda, podman komutunun bazı yaygın kullanım örnekleri bulunmaktadır:

### 1. Yeni bir konteyner başlatma
```bash
podman run -d --name my_container nginx
```
Bu komut, arka planda (`-d` seçeneği ile) `nginx` görüntüsünden yeni bir konteyner başlatır ve ona `my_container` adını verir.

### 2. Çalışan konteynerleri listeleme
```bash
podman ps
```
Bu komut, o anda çalışan tüm konteynerlerin listesini gösterir.

### 3. Konteyner durdurma
```bash
podman stop my_container
```
Bu komut, `my_container` adındaki konteyneri durdurur.

### 4. Durdurulmuş bir konteyneri silme
```bash
podman rm my_container
```
Bu komut, durdurulmuş olan `my_container` konteynerini siler.

### 5. Mevcut görüntüleri listeleme
```bash
podman images
```
Bu komut, sistemde mevcut olan tüm görüntülerin listesini gösterir.

## Tips
- Podman ile çalışırken, konteynerlerinizi düzenli olarak güncellemeyi unutmayın.
- Konteynerlerinizi isimlendirmek, yönetimi kolaylaştırır.
- Podman, kullanıcı izinlerini daha iyi yönetmek için root olmayan kullanıcılar için tasarlanmıştır; bu nedenle, güvenlik açısından avantaj sağlar.