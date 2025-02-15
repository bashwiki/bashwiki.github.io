# [리눅스] Bash tail 사용법

## Overview
`tail` komutu, bir dosyanın son kısmını görüntülemek için kullanılan bir Bash komutudur. Genellikle log dosyalarını izlemek veya büyük metin dosyalarının son kısımlarını hızlıca kontrol etmek için kullanılır. Varsayılan olarak, `tail` komutu bir dosyanın son 10 satırını gösterir, ancak bu sayı kullanıcı tarafından değiştirilebilir.

## Usage
`tail` komutunun temel sözdizimi şu şekildedir:

```bash
tail [seçenekler] [dosya_adı]
```

### Yaygın Seçenekler
- `-n [sayı]`: Gösterilecek satır sayısını belirtir. Örneğin, `-n 20` son 20 satırı gösterir.
- `-f`: Dosya sürekli olarak izlenir ve yeni eklenen satırlar anında görüntülenir. Bu, log dosyalarını gerçek zamanlı olarak takip etmek için kullanışlıdır.
- `-c [sayı]`: Dosyanın sonundan itibaren belirtilen byte sayısını gösterir.

## Examples
### Örnek 1: Son 10 Satırı Görüntüleme
Aşağıdaki komut, `example.log` dosyasının son 10 satırını görüntüler:

```bash
tail example.log
```

### Örnek 2: Log Dosyasını Gerçek Zamanlı İzleme
Aşağıdaki komut, `server.log` dosyasını izler ve dosyaya yeni eklenen satırları anında gösterir:

```bash
tail -f server.log
```

## Tips
- Log dosyalarını izlerken `-f` seçeneğini kullanarak, dosyaya yeni satırlar eklendikçe anında güncellemeleri görebilirsiniz.
- `-n` seçeneği ile belirli bir satır sayısını görüntülemek, büyük dosyalarla çalışırken zaman kazandırabilir.
- `tail` komutunu diğer komutlarla birleştirerek daha karmaşık işlemler gerçekleştirebilirsiniz. Örneğin, `tail -n 50 example.log | grep "ERROR"` komutu, son 50 satırda "ERROR" kelimesini arar.