# [리눅스] Bash pkill 사용법

## Genel Bakış
`pkill`, Linux ve Unix benzeri işletim sistemlerinde çalışan bir komuttur. Bu komut, belirli bir isimle eşleşen süreçleri sonlandırmak için kullanılır. `pkill`, süreçlerin PID'lerini (Process ID) bilmeden, sadece süreç adını kullanarak bu süreçleri durdurma yeteneği sağlar. Bu, sistem yöneticileri ve geliştiriciler için süreç yönetimini kolaylaştırır.

## Kullanım
`pkill` komutunun temel sözdizimi şu şekildedir:

```
pkill [seçenekler] <süreç_adı>
```

### Yaygın Seçenekler
- `-f`: Süreç adının tam komut satırıyla eşleşmesini sağlar.
- `-n`: En son başlatılan süreci sonlandırır.
- `-o`: En eski başlatılan süreci sonlandırır.
- `-signal`: Hangi sinyalin gönderileceğini belirtir. Örneğin, `-9` sinyali, süreci zorla sonlandırmak için kullanılır.

## Örnekler
### Örnek 1: Belirli bir süreç adını kullanarak süreci sonlandırma
Aşağıdaki komut, "firefox" adındaki tüm süreçleri sonlandırır:

```bash
pkill firefox
```

### Örnek 2: Tam komut satırıyla eşleşen süreçleri sonlandırma
Aşağıdaki komut, "python script.py" komutuyla başlatılan süreçleri sonlandırır:

```bash
pkill -f "python script.py"
```

## İpuçları
- `pkill` komutunu kullanmadan önce, hangi süreçlerin etkileneceğini görmek için `pgrep` komutunu kullanarak süreçleri listelemek iyi bir uygulamadır.
- Süreçleri sonlandırırken dikkatli olun; yanlışlıkla önemli sistem süreçlerini sonlandırmak sistem kararlılığını etkileyebilir.
- Gerekirse, `-n` veya `-o` seçeneklerini kullanarak sadece en son veya en eski süreçleri hedefleyebilirsiniz. Bu, daha kontrollü bir süreç sonlandırma sağlar.