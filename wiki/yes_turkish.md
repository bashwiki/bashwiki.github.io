# [리눅스] Bash yes 사용법

## Overview
`yes` komutu, belirli bir metni sürekli olarak ekrana yazdırmak için kullanılan basit bir Bash komutudur. Genellikle, bir komutun veya programın otomatik olarak "evet" (yes) yanıtını alması gerektiği durumlarda kullanılır. Bu, etkileşimli komutları otomatikleştirmek için faydalıdır.

## Usage
`yes` komutunun temel sözdizimi şu şekildedir:

```bash
yes [METİN]
```

- **METİN**: Ekrana yazdırılacak metni belirtir. Eğer bir metin verilmezse, `yes` varsayılan olarak "y" harfini sürekli olarak yazdırır.

### Common Options
`yes` komutunun kendine özgü seçenekleri yoktur; ancak, genellikle diğer komutlarla birlikte kullanılır. Örneğin, bir komutun otomatik olarak "evet" yanıtı alması için `yes` komutunu bir boru (pipe) ile bağlayabilirsiniz.

## Examples
### Örnek 1: Varsayılan "y" Yanıtı
Aşağıdaki komut, sürekli olarak "y" yazdırır:

```bash
yes
```

### Örnek 2: Özel Metin Yazdırma
Aşağıdaki komut, "Devam etmek istiyor musunuz?" metnini sürekli olarak yazdırır:

```bash
yes "Devam etmek istiyor musunuz?"
```

Bu komut, "Devam etmek istiyor musunuz?" ifadesini sürekli olarak ekrana basacaktır.

### Örnek 3: Komutlarla Birlikte Kullanma
`yes` komutunu, bir komutun otomatik olarak "evet" yanıtını alması için kullanabilirsiniz:

```bash
yes | rm -i dosya.txt
```

Bu komut, `rm -i` komutunun etkileşimli olarak dosyayı silme isteğine otomatik olarak "evet" yanıtı verir.

## Tips
- `yes` komutunu kullanırken dikkatli olun; çünkü otomatik "evet" yanıtı vermek, istenmeyen veri kaybına veya sistem değişikliklerine yol açabilir.
- `yes` komutunu uzun süre çalıştırmak, sistem kaynaklarını tüketebilir. Gereksiz yere çalıştırmaktan kaçının.
- `yes` komutunu, test senaryolarında veya otomasyon süreçlerinde kullanmak, etkileşimli yanıtları hızlandırabilir.