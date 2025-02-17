# [Linux] Bash nslookup Kullanımı: Alan adı sorgulama aracı

## Overview
`nslookup`, alan adı sistemini (DNS) sorgulamak için kullanılan bir komuttur. Bu komut, bir alan adının IP adresini veya bir IP adresinin alan adını bulmak için kullanılır. Ağ yöneticileri ve kullanıcılar, DNS ile ilgili sorunları teşhis etmek için bu aracı sıklıkla kullanır.

## Usage
Temel kullanım sözdizimi aşağıdaki gibidir:

```
nslookup [seçenekler] [argümanlar]
```

## Common Options
- `-type=TYPE`: Sorgulamak istediğiniz DNS kaynağının türünü belirtir (örneğin, A, MX, CNAME).
- `-timeout=TIME`: Sorgu zaman aşımını ayarlamak için kullanılır.
- `-retry=COUNT`: Yeniden deneme sayısını ayarlamak için kullanılır.
- `server`: Belirli bir DNS sunucusunu sorgulamak için kullanılır.

## Common Examples
Aşağıda `nslookup` komutunun bazı yaygın kullanım örnekleri bulunmaktadır:

### 1. Bir alan adının IP adresini bulma
```
nslookup example.com
```

### 2. Belirli bir DNS sunucusunu kullanarak sorgulama
```
nslookup example.com 8.8.8.8
```

### 3. MX kayıtlarını sorgulama
```
nslookup -type=MX example.com
```

### 4. CNAME kayıtlarını sorgulama
```
nslookup -type=CNAME www.example.com
```

## Tips
- `nslookup` komutunu kullanırken, doğru DNS sunucusunu seçmek sorunları daha hızlı çözmenize yardımcı olabilir.
- Sorgu sonuçlarını daha iyi anlamak için, farklı kayıt türlerini denemekten çekinmeyin.
- Eğer bir alan adıyla ilgili sorun yaşıyorsanız, `nslookup` ile sorgulama yaparak DNS yapılandırmanızı kontrol edin.