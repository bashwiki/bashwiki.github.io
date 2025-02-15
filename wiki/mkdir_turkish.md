# [리눅스] Bash mkdir 사용법

## Genel Bakış
`mkdir` (make directory), Linux ve Unix benzeri işletim sistemlerinde yeni dizinler (kataloglar) oluşturmak için kullanılan bir komuttur. Bu komut, dosya sisteminde belirli bir hiyerarşi oluşturmak ve düzen sağlamak amacıyla yeni dizinler yaratmak için temel bir araçtır.

## Kullanım
`mkdir` komutunun temel sözdizimi aşağıdaki gibidir:

```bash
mkdir [seçenekler] dizin_adı
```

### Yaygın Seçenekler
- `-p`: Belirtilen dizin yolundaki eksik olan üst dizinleri de oluşturur. Örneğin, `mkdir -p /a/b/c` komutu, `/a` ve `/a/b` dizinleri yoksa bunları da oluşturur.
- `-v`: Oluşturulan dizinlerin adını ekrana yazdırır. Bu, hangi dizinlerin oluşturulduğunu görmek için faydalıdır.

## Örnekler
### Örnek 1: Basit Dizin Oluşturma
Aşağıdaki komut, "yeni_dizin" adında bir dizin oluşturur:

```bash
mkdir yeni_dizin
```

### Örnek 2: Üst Dizinlerle Birlikte Dizin Oluşturma
Aşağıdaki komut, eksik olan üst dizinleri de oluşturarak "a/b/c" dizin yolunu oluşturur:

```bash
mkdir -p a/b/c
```

## İpuçları
- Dizin adlarında boşluk veya özel karakter kullanıyorsanız, dizin adını tırnak içinde yazmayı unutmayın. Örneğin: `mkdir "yeni dizin"`.
- Birden fazla dizin oluşturmak için dizin adlarını boşlukla ayırarak yazabilirsiniz. Örneğin: `mkdir dizin1 dizin2 dizin3`.
- Dizin oluşturma işlemi sırasında hata almamak için, dizin adlarının geçerli ve izinlerinizin yeterli olduğundan emin olun.