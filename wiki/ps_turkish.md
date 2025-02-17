# [Linux] Bash ps Kullanımı: Çalışan süreçleri görüntüleme

## Overview
`ps` komutu, sistemde çalışan süreçlerin durumunu görüntülemek için kullanılır. Bu komut, kullanıcıların hangi işlemlerin çalıştığını, bu işlemlerin PID'lerini (Process ID), CPU ve bellek kullanımını ve daha fazlasını görmelerine olanak tanır.

## Usage
Temel sözdizimi aşağıdaki gibidir:
```bash
ps [options] [arguments]
```

## Common Options
- `-e`: Tüm süreçleri gösterir.
- `-f`: Tam formatta süreç bilgilerini gösterir.
- `-u [kullanıcı]`: Belirtilen kullanıcıya ait süreçleri listeler.
- `-aux`: Tüm kullanıcıların süreçlerini ayrıntılı bir şekilde gösterir.
- `--sort`: Çıktıyı belirtilen kritere göre sıralar.

## Common Examples
Aşağıda `ps` komutunun bazı yaygın kullanım örnekleri bulunmaktadır:

- Tüm süreçleri görüntülemek için:
    ```bash
    ps -e
    ```

- Ayrıntılı süreç bilgilerini görmek için:
    ```bash
    ps -ef
    ```

- Belirli bir kullanıcıya ait süreçleri listelemek için:
    ```bash
    ps -u username
    ```

- Tüm kullanıcıların süreçlerini ayrıntılı olarak görüntülemek için:
    ```bash
    ps aux
    ```

- Çıktıyı CPU kullanımına göre sıralamak için:
    ```bash
    ps aux --sort=-%cpu
    ```

## Tips
- `ps` komutunu `grep` ile birleştirerek belirli bir süreci bulabilirsiniz. Örneğin:
    ```bash
    ps aux | grep process_name
    ```

- `top` komutunu kullanarak gerçek zamanlı süreç izleme yapabilirsiniz. `ps` komutu, anlık bir görüntü sağlarken, `top` sürekli güncellenen bir görünüm sunar.

- `man ps` komutunu kullanarak `ps` komutunun tüm seçenekleri ve kullanımı hakkında daha fazla bilgi alabilirsiniz.