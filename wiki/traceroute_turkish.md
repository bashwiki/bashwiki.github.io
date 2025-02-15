# [리눅스] Bash traceroute 사용법

## Genel Bakış
`traceroute`, bir ağ üzerindeki veri paketlerinin bir hedefe ulaşırken geçtiği yolları izlemek için kullanılan bir komuttur. Bu komut, bir IP adresine veya alan adına giden yol üzerindeki her bir yönlendiriciyi (router) gösterir. Ağ bağlantı sorunlarını teşhis etmek ve ağın performansını analiz etmek için oldukça yararlıdır.

## Kullanım
Temel `traceroute` komutunun sözdizimi şu şekildedir:

```bash
traceroute [seçenekler] hedef
```

### Yaygın Seçenekler
- `-m <sayı>`: Maksimum sıçrama sayısını belirler. Varsayılan değer genellikle 30'dur.
- `-p <port>`: Hedefe ulaşmak için kullanılacak UDP portunu belirtir. Varsayılan olarak 33434 portu kullanılır.
- `-n`: IP adreslerini çözümlemeden doğrudan kullanır. Bu, sorgu süresini kısaltabilir.
- `-w <saniye>`: Her bir sıçrama için zaman aşımını ayarlar. Varsayılan değer genellikle 5 saniyedir.

## Örnekler
### Örnek 1: Temel Kullanım
Aşağıdaki komut, `example.com` adresine giden yol üzerindeki yönlendiricileri gösterir:

```bash
traceroute example.com
```

### Örnek 2: Maksimum Sıçrama Sayısını Belirleme
Aşağıdaki komut, `example.com` adresine giden yol üzerindeki maksimum 15 sıçramayı gösterir:

```bash
traceroute -m 15 example.com
```

## İpuçları
- `traceroute` komutunu kullanmadan önce, ağ bağlantınızın aktif olduğundan emin olun.
- Ağ sorunlarını teşhis ederken, `-n` seçeneğini kullanarak IP adreslerini doğrudan görmek, zaman kazandırabilir.
- Farklı portlar kullanarak (örneğin, `-p 80` ile) belirli hizmetlerin (HTTP gibi) durumunu kontrol edebilirsiniz.
- Eğer `traceroute` komutu sisteminizde yüklü değilse, genellikle `traceroute` paketini yükleyerek erişebilirsiniz. Örneğin, Debian tabanlı sistemlerde `sudo apt install traceroute` komutunu kullanabilirsiniz.