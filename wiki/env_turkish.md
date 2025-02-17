# [Linux] Bash env Kullanımı: Ortam Değişkenlerini Yönetme

## Genel Bakış
`env` komutu, ortam değişkenlerini görüntülemek veya yeni bir ortam değişkeni ile bir komut çalıştırmak için kullanılır. Bu komut, belirli bir ortamda çalıştırılacak komutları tanımlamak için oldukça yararlıdır.

## Kullanım
Temel sözdizimi aşağıdaki gibidir:

```bash
env [seçenekler] [argümanlar]
```

## Yaygın Seçenekler
- `-i`: Yeni bir ortam oluşturur ve mevcut ortam değişkenlerini kullanmaz.
- `-u`: Belirtilen ortam değişkenini kaldırır.
- `VAR=değer`: Yeni bir ortam değişkeni tanımlar ve belirtilen komutu bu değişkenle çalıştırır.

## Yaygın Örnekler

1. Tüm ortam değişkenlerini görüntüleme:
   ```bash
   env
   ```

2. Belirli bir ortam değişkenini kaldırma:
   ```bash
   env -u PATH command
   ```

3. Yeni bir ortam değişkeni ile bir komut çalıştırma:
   ```bash
   env MY_VAR=hello bash -c 'echo $MY_VAR'
   ```

4. Yeni bir ortam oluşturarak bir komut çalıştırma:
   ```bash
   env -i bash -c 'echo $HOME'
   ```

## İpuçları
- `env` komutunu, bir komutun hangi ortam değişkenleri ile çalıştığını test etmek için kullanabilirsiniz.
- Ortam değişkenlerini temiz bir şekilde yönetmek için `-i` seçeneğini kullanarak yeni bir ortam oluşturmayı düşünebilirsiniz.
- `env` komutunu, betiklerinizde belirli bir ortamda çalıştırmak istediğiniz komutlar için kullanarak daha kontrollü bir çalışma ortamı sağlayabilirsiniz.