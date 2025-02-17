# [Linux] Bash dig Kullanımı: DNS sorgulama aracı

## Genel Bakış
`dig` (Domain Information Groper), DNS (Domain Name System) sorguları yapmak için kullanılan bir komut satırı aracıdır. Bu komut, bir alan adının IP adresini, DNS kayıtlarını ve diğer bilgileri sorgulamak için yaygın olarak kullanılır.

## Kullanım
Temel sözdizimi aşağıdaki gibidir:
```bash
dig [seçenekler] [argümanlar]
```

## Yaygın Seçenekler
- `@sunucu`: Sorgunun gönderileceği DNS sunucusunu belirtir.
- `-t tür`: Sorgulamak istediğiniz DNS kayıt türünü belirler (örneğin, A, AAAA, MX).
- `+short`: Sadece kısa bir çıktı almak için kullanılır.
- `-x`: Ters DNS sorgusu yapmak için kullanılır.

## Yaygın Örnekler
Aşağıda `dig` komutunun bazı pratik örnekleri bulunmaktadır:

### 1. Basit bir DNS sorgusu
Bir alan adının IP adresini sorgulamak için:
```bash
dig example.com
```

### 2. Belirli bir DNS kayıt türünü sorgulama
Bir alan adının MX (Mail Exchange) kayıtlarını sorgulamak için:
```bash
dig -t MX example.com
```

### 3. Kısa çıktı almak
Sadece IP adresini görmek için:
```bash
dig +short example.com
```

### 4. Ters DNS sorgusu
Bir IP adresinin alan adını sorgulamak için:
```bash
dig -x 93.184.216.34
```

### 5. Belirli bir DNS sunucusunu kullanma
Sorguyu belirli bir DNS sunucusu üzerinden yapmak için:
```bash
dig @8.8.8.8 example.com
```

## İpuçları
- `dig` komutunu kullanmadan önce, hangi DNS kayıt türlerini sorgulamak istediğinizi belirleyin.
- Çıktıyı daha iyi anlamak için `+trace` seçeneğini ekleyerek sorgu sürecini takip edebilirsiniz.
- Sık kullanılan DNS sunucularını (örneğin, Google DNS: 8.8.8.8) kullanarak daha hızlı sonuçlar alabilirsiniz.