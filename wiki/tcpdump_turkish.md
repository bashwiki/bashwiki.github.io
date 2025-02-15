# [리눅스] Bash tcpdump 사용법

## Overview
`tcpdump`, ağ trafiğini izlemek ve analiz etmek için kullanılan bir komut satırı aracıdır. Genellikle ağ yöneticileri ve geliştiriciler tarafından, ağ üzerindeki veri paketlerini yakalamak ve incelemek amacıyla kullanılır. `tcpdump`, belirli bir ağ arayüzü üzerinden geçen verileri filtreleyerek, kullanıcıların ağ trafiği hakkında detaylı bilgi edinmelerine olanak tanır.

## Usage
`tcpdump` komutunun temel sözdizimi aşağıdaki gibidir:

```bash
tcpdump [seçenekler] [filtreler]
```

### Yaygın Seçenekler
- `-i <arayüz>`: Hangi ağ arayüzünün izleneceğini belirtir. Örneğin, `-i eth0`.
- `-n`: IP adreslerini ve port numaralarını sayısal olarak gösterir, isim çözümlemesi yapmaz.
- `-c <sayı>`: Belirtilen sayıda paket yakaladıktan sonra durur.
- `-w <dosya>`: Yakalanan paketleri bir dosyaya yazmak için kullanılır.
- `-r <dosya>`: Önceden kaydedilmiş bir dosyadan paketleri okumak için kullanılır.

## Examples
### Örnek 1: Temel Kullanım
Ağ arayüzü üzerinden geçen tüm paketleri izlemek için aşağıdaki komutu kullanabilirsiniz:

```bash
tcpdump -i eth0
```

### Örnek 2: Belirli Bir Portu İzleme
Sadece 80 numaralı port üzerinden geçen HTTP trafiğini izlemek için:

```bash
tcpdump -i eth0 port 80
```

## Tips
- `tcpdump` kullanırken, ağ trafiğinin yoğunluğuna dikkat edin; çok fazla paket kaydetmek, sistem kaynaklarını tüketebilir.
- Yakalanan verileri analiz etmek için `-w` seçeneği ile bir dosyaya kaydedebilir ve daha sonra `-r` seçeneği ile bu dosyayı inceleyebilirsiniz.
- Ağ trafiğini izlerken gizliliğe dikkat edin; kişisel verilerin yakalanması yasal sorunlara yol açabilir.
- `tcpdump` ile birlikte `grep` gibi araçları kullanarak belirli paketleri filtrelemek, analiz sürecini kolaylaştırabilir.