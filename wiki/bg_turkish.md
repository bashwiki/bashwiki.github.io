# [리눅스] Bash bg 사용법

## Overview
`bg` komutu, Bash kabuğunda arka planda çalışan bir işlemi başlatmak için kullanılır. Bu komut, bir işlemi duraklatıp (suspend) arka planda çalıştırarak, terminalde başka komutlar girmenize olanak tanır. Genellikle, bir işlemi durdurduktan sonra (örneğin `Ctrl + Z` ile) bu işlemi arka plana almak için kullanılır.

## Usage
Temel sözdizimi şu şekildedir:

```bash
bg [job_spec]
```

- `job_spec`: Arka plana almak istediğiniz işin tanımıdır. Bu, işin numarası veya işin adı olabilir. Eğer belirtilmezse, en son duraklatılan iş arka plana alınır.

### Ortak Seçenekler
- `job_spec`: İş numarasını belirtirken, `%` sembolü ile işin numarasını kullanabilirsiniz. Örneğin, `%1` ilk iş anlamına gelir.

## Examples

### Örnek 1: Bir işlemi duraklatıp arka plana almak
Bir işlemi başlatın ve duraklatın:

```bash
sleep 100
```

Bu komutu duraklatmak için `Ctrl + Z` tuşlarına basın. Ardından, işlemi arka plana almak için:

```bash
bg
```

Bu komut, duraklatılan `sleep` işlemini arka planda çalıştırmaya başlar.

### Örnek 2: Belirli bir işlemi arka plana almak
Eğer birden fazla işiniz varsa ve belirli bir iş numarasını arka plana almak istiyorsanız:

```bash
bg %1
```

Bu komut, birinci iş numarasına sahip duraklatılmış işlemi arka plana alır.

## Tips
- `jobs` komutunu kullanarak mevcut işlerinizi listeleyebilir ve hangi işlerin duraklatıldığını görebilirsiniz.
- Arka planda çalışan bir işlemi durdurmak için `fg` komutunu kullanarak işlemi ön plana alabilirsiniz.
- `bg` komutunu kullanmadan önce işlemin duraklatıldığından emin olun; aksi takdirde, hata alabilirsiniz.