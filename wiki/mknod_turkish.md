# [리눅스] Bash mknod 사용법

## Overview
`mknod` komutu, Unix ve Linux sistemlerinde özel dosyalar oluşturmak için kullanılır. Bu özel dosyalar genellikle karakter veya blok cihazlarıdır. `mknod`, sistem düzeyinde dosya sistemine yeni cihaz dosyaları eklemek için kullanılır ve bu dosyalar, işletim sisteminin donanım bileşenleriyle etkileşimde bulunmasına olanak tanır.

## Usage
`mknod` komutunun temel sözdizimi şu şekildedir:

```bash
mknod [seçenekler] dosya_adı tür [major minor]
```

### Ortak Seçenekler
- `-m, --mode`: Oluşturulan dosyanın izinlerini ayarlamak için kullanılır. Örneğin, `-m 666` ile dosya izinleri ayarlanabilir.
- `-Z, --context`: SELinux güvenlik bağlamını ayarlamak için kullanılır.

### Türler
- `c`: Karakter cihaz dosyası.
- `b`: Blok cihaz dosyası.

`major` ve `minor` numaraları, cihazın türüne göre belirlenir ve genellikle sistemin donanım yapılandırmasına bağlıdır.

## Examples
### Örnek 1: Karakter Cihaz Dosyası Oluşturma
Aşağıdaki komut, bir karakter cihaz dosyası oluşturur:

```bash
mknod /dev/mychar c 200 0
```
Bu komut, `mychar` adında bir karakter cihaz dosyası oluşturur. Burada `200` major numarası, `0` ise minor numarasıdır.

### Örnek 2: Blok Cihaz Dosyası Oluşturma
Aşağıdaki komut, bir blok cihaz dosyası oluşturur:

```bash
mknod /dev/myblock b 100 1
```
Bu komut, `myblock` adında bir blok cihaz dosyası oluşturur. Burada `100` major numarası, `1` ise minor numarasıdır.

## Tips
- `mknod` komutunu kullanmadan önce, cihaz numaralarının doğru olduğundan emin olun. Yanlış numaralar, cihazın düzgün çalışmamasına neden olabilir.
- Özel dosyalar oluştururken, uygun izinleri ayarlamak için `-m` seçeneğini kullanmayı unutmayın.
- `mknod` komutunu kullanmak için genellikle yönetici (root) yetkilerine sahip olmanız gerekir. Bu nedenle, komutu `sudo` ile çalıştırmayı düşünün.
- Cihaz dosyalarını oluşturduktan sonra, bunları test etmek için uygun araçları kullanarak doğrulayın.