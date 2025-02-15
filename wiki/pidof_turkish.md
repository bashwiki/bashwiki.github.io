# [리눅스] Bash pidof 사용법

## Overview
`pidof` komutu, Linux işletim sistemlerinde belirli bir programın veya işlemin PID'lerini (Process ID) bulmak için kullanılır. Bu komut, bir veya daha fazla çalışmakta olan işlemin kimliğini belirlemek için oldukça yararlıdır. Genellikle, bir uygulamanın çalışıp çalışmadığını kontrol etmek veya belirli bir işlemi hedeflemek için kullanılır.

## Usage
`pidof` komutunun temel sözdizimi aşağıdaki gibidir:

```bash
pidof [seçenekler] <program_adı>
```

### Yaygın Seçenekler
- `-o <pid>`: Belirtilen PID'yi hariç tutar.
- `-s`: Sadece ilk bulunan PID'yi döndürür.
- `-c`: PID'lerin yanı sıra, işlem adını da gösterir.

## Examples
### Örnek 1: Basit Kullanım
Belirli bir programın PID'lerini bulmak için `pidof` komutunu kullanabilirsiniz. Örneğin, `bash` işleminin PID'lerini bulmak için:

```bash
pidof bash
```

Bu komut, sistemde çalışan tüm `bash` işlemlerinin PID'lerini döndürecektir.

### Örnek 2: Sadece İlk PID'yi Alma
Eğer sadece ilk bulunan PID'yi almak istiyorsanız `-s` seçeneğini kullanabilirsiniz:

```bash
pidof -s bash
```

Bu komut, yalnızca ilk `bash` işleminin PID'sini döndürecektir.

## Tips
- `pidof` komutunu, bir işlemin çalışıp çalışmadığını kontrol etmek için bir betikte kullanabilirsiniz. Örneğin, bir işlem çalışmıyorsa başlatmak için bir koşul oluşturabilirsiniz.
- PID'leri kullanarak işlemleri sonlandırmak için `kill` komutunu `pidof` ile birleştirebilirsiniz. Örneğin, `bash` işlemini sonlandırmak için:

```bash
kill $(pidof bash)
```

Bu, sistemdeki tüm `bash` işlemlerini sonlandıracaktır.