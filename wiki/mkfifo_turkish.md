# [리눅스] Bash mkfifo 사용법

## Genel Bakış
`mkfifo`, Unix ve Linux işletim sistemlerinde kullanılan bir komuttur. Bu komut, "named pipe" (isimli boru) oluşturmak için kullanılır. İsimli borular, süreçler arasında veri iletimi sağlamak için kullanılır ve bu süreçlerin birbirleriyle senkronize bir şekilde iletişim kurmasına olanak tanır. `mkfifo` komutu, bir dosya sistemi nesnesi olarak bir isimli boru oluşturur, böylece diğer süreçler bu boruya veri yazabilir veya bu borudan veri okuyabilir.

## Kullanım
`mkfifo` komutunun temel sözdizimi şu şekildedir:

```bash
mkfifo [seçenekler] FIFO_ADI
```

### Yaygın Seçenekler
- `-m, --mode=MODE`: Oluşturulan FIFO'nun izinlerini belirler. Örneğin, `-m 0666` ile herkesin okuma ve yazma iznine sahip olmasını sağlayabilirsiniz.

## Örnekler
### Örnek 1: Basit FIFO Oluşturma
Aşağıdaki komut, "myfifo" adında bir isimli boru oluşturur:

```bash
mkfifo myfifo
```

Bu komut çalıştırıldığında, "myfifo" adında bir dosya oluşturulur. Diğer süreçler bu boruya veri yazabilir veya bu borudan veri okuyabilir.

### Örnek 2: FIFO Üzerinden Veri İletimi
Aşağıdaki örnekte, bir terminalde veri yazmak ve diğer bir terminalde bu veriyi okumak için `myfifo` borusunu kullanacağız.

1. Bir terminalde, `myfifo`'ya veri yazmak için:

    ```bash
    echo "Merhaba, FIFO!" > myfifo
    ```

2. Diğer bir terminalde, `myfifo`'dan veri okumak için:

    ```bash
    cat myfifo
    ```

Bu iki komut çalıştırıldığında, ilk terminalde yazılan "Merhaba, FIFO!" mesajı, ikinci terminalde görüntülenecektir.

## İpuçları
- FIFO'lar, birden fazla süreç arasında veri iletimi sağlamak için oldukça kullanışlıdır. Ancak, bir süreç FIFO'ya veri yazarken diğer bir süreç bu veriyi okumazsa, yazma işlemi bloklanır. Bu nedenle, FIFO'ları kullanırken süreçlerin senkronizasyonuna dikkat etmek önemlidir.
- `mkfifo` ile oluşturduğunuz FIFO dosyalarının izinlerini kontrol etmek için `ls -l` komutunu kullanabilirsiniz. Bu, hangi kullanıcıların bu FIFO'ya erişim iznine sahip olduğunu görmenizi sağlar.
- FIFO'lar, geçici veri iletimi için idealdir, ancak kalıcı veri saklama gereksinimleriniz varsa, dosya sisteminde normal dosyalar kullanmayı düşünmelisiniz.