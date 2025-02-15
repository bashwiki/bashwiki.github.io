# [리눅스] Bash bunzip2 사용법

## Overview
`bunzip2`, Bzip2 sıkıştırma algoritması ile sıkıştırılmış dosyaları açmak için kullanılan bir komut satırı aracıdır. Bu komut, genellikle `.bz2` uzantılı dosyaları açmak için kullanılır ve dosyaların boyutunu küçültmek için sıkıştırma işlemi yapılmış verileri geri yükler. `bunzip2`, dosyaları açarken orijinal dosyayı geri yükler ve sıkıştırılmış dosyayı siler.

## Usage
Temel kullanım sözdizimi şu şekildedir:

```bash
bunzip2 [seçenekler] dosya.bz2
```

### Yaygın Seçenekler
- `-k`, `--keep`: Sıkıştırılmış dosyayı açtıktan sonra orijinal dosyayı korur.
- `-f`, `--force`: Var olan dosyaların üzerine yazmak için zorlar.
- `-v`, `--verbose`: İşlem sırasında daha fazla bilgi gösterir.

## Examples
### Örnek 1: Basit Kullanım
Aşağıdaki komut, `example.bz2` dosyasını açar ve sıkıştırılmış dosyayı siler:

```bash
bunzip2 example.bz2
```

### Örnek 2: Dosyayı Koruyarak Açma
Aşağıdaki komut, `example.bz2` dosyasını açar ve orijinal dosyayı korur:

```bash
bunzip2 -k example.bz2
```

## Tips
- Sıkıştırılmış dosyalarla çalışırken, dosyaların yedeğini almak iyi bir uygulamadır. Özellikle önemli dosyalar üzerinde işlem yapmadan önce yedek almak, veri kaybını önleyebilir.
- `bunzip2` komutunu kullanmadan önce dosyanın gerçekten `.bz2` uzantısına sahip olduğundan emin olun, aksi takdirde beklenmeyen sonuçlar alabilirsiniz.
- `-v` seçeneği ile işlem sırasında daha fazla bilgi alarak, işlemin ne kadar sürdüğünü ve hangi dosyaların açıldığını takip edebilirsiniz.