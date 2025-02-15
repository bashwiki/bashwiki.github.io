# [리눅스] Bash ss 사용법

## Overview
`ss` (socket statistics) komutu, Linux sistemlerinde ağ bağlantılarını ve soket durumlarını görüntülemek için kullanılan bir araçtır. `ss`, özellikle TCP, UDP ve diğer soket türleri hakkında detaylı bilgi sağlar. `netstat` komutuna benzer, ancak daha hızlı ve daha ayrıntılı bilgiler sunar. Ağ bağlantılarının durumu, dinleme portları ve soketlerin istatistikleri hakkında bilgi edinmek için kullanılır.

## Usage
`ss` komutunun temel sözdizimi şu şekildedir:

```bash
ss [OPTIONS]
```

### Yaygın Seçenekler
- `-t`: TCP bağlantılarını gösterir.
- `-u`: UDP bağlantılarını gösterir.
- `-l`: Dinleme durumundaki soketleri listeler.
- `-p`: Soketlerin hangi süreçler tarafından kullanıldığını gösterir.
- `-n`: Adres ve port numaralarını sayısal olarak gösterir, isim çözümlemesi yapmaz.

## Examples
### Örnek 1: Tüm TCP Bağlantılarını Listeleme
Aşağıdaki komut, sistemdeki tüm TCP bağlantılarını gösterir:

```bash
ss -t
```

### Örnek 2: Dinleme Durumundaki Soketleri Görüntüleme
Dinleme durumundaki soketleri görüntülemek için şu komutu kullanabilirsiniz:

```bash
ss -l
```

Bu komut, dinleme durumundaki tüm soketleri listeler.

## Tips
- `ss` komutunu kullanırken, `-n` seçeneği ile adres ve port numaralarını sayısal olarak görüntülemek, daha hızlı sonuç almanızı sağlar.
- Ağ sorunlarını teşhis etmek için `ss -t -p` komutunu kullanarak hangi süreçlerin hangi bağlantıları kullandığını görebilirsiniz.
- `ss` komutunun çıktısını daha okunabilir hale getirmek için `grep` veya `less` gibi araçlarla birleştirebilirsiniz. Örneğin:

```bash
ss -t | grep ESTAB
```

Bu komut, yalnızca kurulu (ESTABLISHED) TCP bağlantılarını gösterir.