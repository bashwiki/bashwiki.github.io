# [Linux] Bash tcpdump Kullanımı: Ağ trafiğini analiz etme aracı

## Overview
tcpdump, ağ trafiğini yakalamak ve analiz etmek için kullanılan bir komut satırı aracıdır. Ağ üzerinde geçen paketleri inceleyerek, ağ sorunlarını teşhis etme ve güvenlik analizleri yapma imkanı sunar.

## Usage
tcpdump komutunun temel sözdizimi aşağıdaki gibidir:

```bash
tcpdump [options] [arguments]
```

## Common Options
- `-i <interface>`: Hangi ağ arayüzünün kullanılacağını belirtir.
- `-n`: IP adreslerini ve port numaralarını sayısal olarak gösterir, DNS çözümlemesi yapmaz.
- `-v`: Daha ayrıntılı çıktı verir. Birden fazla `-v` kullanarak daha fazla ayrıntı elde edilebilir.
- `-c <count>`: Belirtilen sayıda paketi yakaladıktan sonra tcpdump'ı durdurur.
- `-w <file>`: Yakalanan paketleri belirtilen dosyaya yazar.

## Common Examples
Aşağıda tcpdump komutunun bazı yaygın kullanım örnekleri bulunmaktadır:

### 1. Tüm ağ trafiğini yakalamak
```bash
tcpdump -i eth0
```

### 2. Belirli bir IP adresine ait trafiği yakalamak
```bash
tcpdump -i eth0 host 192.168.1.1
```

### 3. Belirli bir port üzerindeki trafiği yakalamak
```bash
tcpdump -i eth0 port 80
```

### 4. Yakalanan paketleri bir dosyaya yazmak
```bash
tcpdump -i eth0 -w capture.pcap
```

### 5. Yakalanan paketleri sayısal olarak göstermek
```bash
tcpdump -i eth0 -n
```

## Tips
- tcpdump kullanırken, yalnızca gerekli verileri yakalamak için filtreleme yapmayı unutmayın. Bu, daha yönetilebilir bir çıktı sağlar.
- Ağ trafiğini analiz etmeden önce, hangi arayüzü kullanacağınızı belirleyin. `ifconfig` veya `ip a` komutları ile mevcut arayüzleri kontrol edebilirsiniz.
- Yakalanan verileri analiz etmek için Wireshark gibi grafiksel araçlarla birlikte kullanmak, daha derinlemesine analiz yapmanıza yardımcı olabilir.