# [리눅스] Bash shift 사용법

## Overview
`shift` komutu, Bash betiklerinde kullanılan bir komuttur ve pozisyonel parametreleri sola kaydırmak için kullanılır. Bu, bir betikteki argümanları yönetmek ve işlemek için oldukça yararlıdır. `shift` komutu, pozisyonel parametrelerin sırasını değiştirerek, ilk parametreyi kaldırır ve geri kalan parametreleri bir sola kaydırır. Bu, özellikle döngülerde veya argümanları sırayla işlemek istediğiniz durumlarda faydalıdır.

## Usage
Temel kullanım şekli aşağıdaki gibidir:

```bash
shift [n]
```

Burada `n`, kaç pozisyonel parametrenin kaydırılacağını belirtir. Eğer `n` belirtilmezse, varsayılan olarak 1 kabul edilir. Örneğin, `shift` komutunu çağırdığınızda, `$1` parametresi kaybolur ve `$2` artık `$1` olur.

### Örnekler
1. **Basit Kullanım**:
   Aşağıdaki örnekte, bir betik içinde `shift` komutunun nasıl kullanılacağını görebilirsiniz:

   ```bash
   #!/bin/bash
   echo "İlk parametre: $1"
   echo "İkinci parametre: $2"
   shift
   echo "Shift sonrası ilk parametre: $1"
   echo "Shift sonrası ikinci parametre: $2"
   ```

   Bu betik çalıştırıldığında, ilk iki parametreyi ekrana yazdırır, ardından `shift` komutu ile ilk parametreyi kaydırır.

2. **Birden Fazla Kaydırma**:
   Aşağıdaki örnekte, birden fazla pozisyonel parametreyi kaydırmayı gösterir:

   ```bash
   #!/bin/bash
   echo "Parametreler: $@"
   shift 2
   echo "İki kaydırma sonrası parametreler: $@"
   ```

   Bu betik, başlangıçta tüm parametreleri yazdırır ve ardından iki pozisyonel parametreyi kaydırır.

## Tips
- `shift` komutunu kullanırken, kaydırma işlemi sonrasında pozisyonel parametrelerin sayısını kontrol etmek önemlidir. Eğer kaydırdığınızdan daha fazla parametre varsa, `$1` ve diğerleri boş kalabilir.
- `shift` komutunu döngüler içinde kullanırken dikkatli olun; her döngüde kaydırma yapıldığında, parametrelerin sayısı azalır ve bu, döngünün beklenmedik bir şekilde sona ermesine neden olabilir.
- `shift` komutunu kullanmadan önce, pozisyonel parametrelerin sayısını kontrol etmek için `"$#"` değişkenini kullanabilirsiniz. Bu, kaç tane parametre olduğunu gösterir ve kaydırma işlemi yapmadan önce bir kontrol mekanizması oluşturmanıza yardımcı olur.