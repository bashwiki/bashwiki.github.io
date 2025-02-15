# [리눅스] Bash rar 사용법

## Overview
`rar`, RAR dosyalarını oluşturmak, açmak ve yönetmek için kullanılan bir komut satırı aracıdır. RAR, yüksek sıkıştırma oranları sunan bir dosya sıkıştırma formatıdır. `rar` komutu, kullanıcıların dosyaları sıkıştırmasına, arşivlemesine ve gerektiğinde bu arşivleri açmasına olanak tanır. Genellikle büyük dosyaların veya klasörlerin depolanması ve taşınması için kullanılır.

## Usage
`rar` komutunun temel sözdizimi aşağıdaki gibidir:

```
rar [seçenekler] [işlem] [arşiv adı] [dosya/dosya yolu]
```

### Yaygın Seçenekler
- `a`: Yeni bir arşiv oluşturur ve belirtilen dosyaları ekler.
- `x`: Belirtilen arşivden dosyaları çıkarır.
- `t`: Arşivin içeriğini test eder.
- `v`: Ayrıntılı çıktı sağlar.
- `r`: Klasörleri ve alt klasörleri de dahil ederek dosyaları ekler.

## Examples
### Örnek 1: Yeni bir RAR arşivi oluşturma
Aşağıdaki komut, `belgeler` klasöründeki tüm dosyaları `arşiv.rar` adlı bir RAR arşivine ekler:

```bash
rar a arşiv.rar belgeler/*
```

### Örnek 2: RAR arşivinden dosyaları çıkarma
Aşağıdaki komut, `arşiv.rar` adlı RAR arşivinden tüm dosyaları mevcut dizine çıkarır:

```bash
rar x arşiv.rar
```

## Tips
- RAR arşivleri oluştururken, sıkıştırma oranını artırmak için `-m5` seçeneğini kullanabilirsiniz. Bu, en yüksek sıkıştırma seviyesini sağlar.
- Arşivlerinizi şifrelemek için `-p` seçeneğini kullanarak bir şifre belirleyebilirsiniz. Örneğin: `rar a -pşifrem arşiv.rar belgeler/*`.
- RAR arşivlerini düzenli olarak test etmek, dosya bütünlüğünü sağlamak için iyi bir uygulamadır. Bunu yapmak için `rar t arşiv.rar` komutunu kullanabilirsiniz.