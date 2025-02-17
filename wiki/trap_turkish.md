# [Linux] Bash trap Kullanımı: Sinyal yakalama ve işleme

## Overview
`trap` komutu, bir Bash betiği çalışırken belirli sinyalleri veya olayları yakalamak ve bunlara yanıt vermek için kullanılır. Bu, betiğin belirli bir durumda düzgün bir şekilde sonlanmasını veya belirli bir işlemi gerçekleştirmesini sağlar.

## Usage
Temel sözdizimi aşağıdaki gibidir:

```bash
trap [options] [commands] [signals]
```

## Common Options
- `-l`: Tüm sinyalleri listelemek için kullanılır.
- `-p`: Mevcut `trap` ayarlarını yazdırır.
- `-n`: Sinyal yakalamayı devre dışı bırakır.

## Common Examples

### Örnek 1: Sinyal Yakalama
Bir betik çalışırken `SIGINT` (Ctrl+C) sinyalini yakalamak için:

```bash
trap 'echo "Sinyal yakalandı!"' SIGINT
```

### Örnek 2: Betik Sonlanırken Temizlik Yapma
Betik sona erdiğinde geçici dosyaları silmek için:

```bash
trap 'rm -f /tmp/mytempfile' EXIT
```

### Örnek 3: Birden Fazla Sinyali Yakalama
Hem `SIGINT` hem de `SIGTERM` sinyallerini yakalamak için:

```bash
trap 'echo "Sinyal yakalandı!"' SIGINT SIGTERM
```

## Tips
- `trap` komutunu kullanırken, her zaman hangi sinyalleri yakalamak istediğinizi net bir şekilde belirleyin.
- Betiğinizin sonlanma durumunda temizlik işlemleri yapmak için `EXIT` sinyalini kullanmayı unutmayın.
- Sinyal yakalama işlemlerinin karmaşık hale gelmemesi için, mümkün olduğunca basit ve anlaşılır komutlar yazmaya özen gösterin.