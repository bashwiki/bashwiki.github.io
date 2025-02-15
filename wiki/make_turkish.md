# [리눅스] Bash make 사용법

## Overview
`make`, yazılım geliştirme sürecinde kullanılan bir otomasyon aracıdır. Genellikle C veya C++ gibi derleme dillerinde yazılmış projelerin derlenmesi ve yönetilmesi için kullanılır. `make`, bir proje için gerekli olan dosyaları ve bağımlılıkları tanımlayan bir "Makefile" dosyasını okuyarak, yalnızca değişen dosyaları derleyerek zaman kazandırır ve derleme sürecini otomatikleştirir.

## Usage
Temel `make` komutunun sözdizimi şu şekildedir:

```bash
make [seçenekler] [hedef]
```

### Yaygın Seçenekler
- `-f, --file=FILE`: Kullanılacak Makefile dosyasını belirtir. Varsayılan olarak "Makefile" veya "makefile" dosyası kullanılır.
- `-j, --jobs=N`: Aynı anda çalıştırılacak görev sayısını belirtir. Bu, derleme sürecini hızlandırabilir.
- `-k, --keep-going`: Hatalı hedefler olsa bile diğer hedeflerin derlenmesine devam eder.
- `-n, --just-print`: Gerçek derleme işlemi yapmadan, hangi komutların çalıştırılacağını gösterir.

## Examples
### Örnek 1: Basit Bir Projeyi Derlemek
Aşağıdaki komut, mevcut dizindeki "Makefile" dosyasını kullanarak projeyi derler.

```bash
make
```

### Örnek 2: Belirli Bir Hedefi Derlemek
Eğer "clean" adında bir hedefiniz varsa, bu hedefi derlemek için aşağıdaki komutu kullanabilirsiniz:

```bash
make clean
```

Bu komut, genellikle geçici dosyaları silmek için kullanılır.

## Tips
- **Makefile Düzenleme**: Makefile dosyanızı düzenlerken, bağımlılıkları doğru bir şekilde tanımlamak, derleme sürecinin düzgün çalışması için kritik öneme sahiptir.
- **Hedefleri Kullanma**: Projenizde farklı hedefler tanımlayarak, belirli görevleri kolayca yönetebilirsiniz. Örneğin, "install", "test" gibi hedefler eklemek, projeyi daha modüler hale getirir.
- **Otomatik Bağımlılık Yönetimi**: `make` kullanırken, dosya değişikliklerini izlemek için otomatik bağımlılık yönetimi özelliklerini kullanmayı unutmayın. Bu, yalnızca gerekli dosyaların yeniden derlenmesini sağlar.

Bu bilgilerle `make` komutunu daha etkili bir şekilde kullanabilir ve yazılım projelerinizi daha verimli bir şekilde yönetebilirsiniz.