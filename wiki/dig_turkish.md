# [리눅스] Bash dig 사용법

## Overview
`dig` (Domain Information Groper), DNS (Domain Name System) sorguları yapmak için kullanılan bir komut satırı aracıdır. İnternet üzerindeki alan adlarının IP adreslerini, DNS kayıtlarını ve diğer DNS bilgilerini sorgulamak için yaygın olarak kullanılır. Geliştiriciler ve sistem yöneticileri için DNS sorunlarını teşhis etmek ve ağ yapılandırmalarını doğrulamak amacıyla oldukça faydalıdır.

## Usage
`dig` komutunun temel sözdizimi aşağıdaki gibidir:

```
dig [@sunucu] [alan_adı] [seçenekler]
```

- `@sunucu`: (isteğe bağlı) Sorgunun gönderileceği DNS sunucusunu belirtir. Eğer belirtilmezse, sistemin varsayılan DNS sunucusu kullanılır.
- `alan_adı`: Sorgulamak istediğiniz alan adıdır.
- `seçenekler`: (isteğe bağlı) Sorgu türünü veya diğer parametreleri belirlemek için kullanılabilecek çeşitli seçeneklerdir.

### Yaygın Seçenekler
- `A`: IPv4 adresi sorgulamak için kullanılır.
- `AAAA`: IPv6 adresi sorgulamak için kullanılır.
- `MX`: Mail exchange (posta değişim) kayıtlarını sorgulamak için kullanılır.
- `NS`: Alan adının ad sunucularını sorgulamak için kullanılır.
- `CNAME`: Alan adının takma adlarını sorgulamak için kullanılır.

## Examples
### Örnek 1: Basit bir A kaydı sorgulama
Aşağıdaki komut, `example.com` alan adının IPv4 adresini sorgular:

```bash
dig example.com A
```

### Örnek 2: Belirli bir DNS sunucusunu kullanarak MX kaydı sorgulama
Aşağıdaki komut, Google'ın DNS sunucusunu kullanarak `example.com` alan adının mail exchange kayıtlarını sorgular:

```bash
dig @8.8.8.8 example.com MX
```

## Tips
- `+short` seçeneğini ekleyerek daha kısa ve okunabilir bir çıktı alabilirsiniz. Örneğin:

```bash
dig example.com +short
```

- Sorgu sonuçlarını daha iyi anlamak için `+trace` seçeneğini kullanarak DNS sorgusunun nasıl işlendiğini adım adım görebilirsiniz.
- `dig` çıktısını bir dosyaya yönlendirmek için `>` operatörünü kullanabilirsiniz. Örneğin:

```bash
dig example.com > sonuc.txt
```

- DNS önbelleğini temizlemek veya güncellemek için `dig` komutunu sık sık kullanarak DNS kayıtlarındaki değişiklikleri hızlıca kontrol edebilirsiniz.