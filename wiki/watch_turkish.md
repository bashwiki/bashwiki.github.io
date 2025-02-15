# [리눅스] Bash watch 사용법

## Overview
`watch` komutu, belirli bir komutu belirli aralıklarla çalıştırarak çıktısını sürekli olarak güncelleyerek görüntülemeye yarar. Bu, özellikle sistem durumunu izlemek veya bir komutun çıktısındaki değişiklikleri takip etmek için oldukça kullanışlıdır. Örneğin, bir dosyanın boyutunu veya bir sistem kaynağının kullanımını izlemek için kullanılabilir.

## Usage
`watch` komutunun temel sözdizimi şu şekildedir:

```bash
watch [seçenekler] komut
```

### Yaygın Seçenekler
- `-n, --interval <saniye>`: Komutun ne sıklıkla (saniye cinsinden) çalıştırılacağını belirler. Varsayılan değer 2 saniyedir.
- `-d, --differences`: Çıktıda değişiklikleri vurgular. Bu seçenek, çıktının hangi kısımlarının değiştiğini kolayca görmenizi sağlar.
- `-t, --no-title`: Başlık satırını gizler. Bu, yalnızca komutun çıktısını görmek istediğinizde yararlıdır.

## Examples
### Örnek 1: Sistem Bellek Kullanımını İzleme
Aşağıdaki komut, her 2 saniyede bir sistemin bellek kullanımını gösterir:

```bash
watch free -h
```

### Örnek 2: Bir Dosyanın Boyutunu İzleme
Belirli bir dosyanın boyutunu izlemek için şu komutu kullanabilirsiniz:

```bash
watch -n 5 ls -lh /path/to/dosya
```
Bu komut, her 5 saniyede bir belirtilen dosyanın boyutunu güncelleyerek gösterir.

## Tips
- `watch` komutunu kullanırken, sık sık güncellenen verileri izlemek için `-d` seçeneğini kullanarak değişiklikleri vurgulamak, dikkatli olmanıza yardımcı olabilir.
- Uzun süreli izleme işlemleri için, `-n` seçeneği ile aralık sürelerini ayarlamak, sistem kaynaklarınızı daha verimli kullanmanıza yardımcı olur.
- `watch` komutunu, diğer komutlarla birleştirerek daha karmaşık izleme senaryoları oluşturabilirsiniz. Örneğin, `grep` ile belirli bir çıktıyı filtreleyebilirsiniz.