# [리눅스] Bash shopt 사용법

## Overview
`shopt`, Bash kabuğunda kullanılan bir komuttur ve "shell options" (kabuk seçenekleri) anlamına gelir. Bu komut, Bash kabuğunun davranışını değiştirmek için kullanılabilen çeşitli seçenekleri etkinleştirmek veya devre dışı bırakmak amacıyla kullanılır. `shopt`, kullanıcıların kabuk ortamlarını özelleştirmelerine ve belirli özellikleri açıp kapatmalarına olanak tanır.

## Usage
`shopt` komutunun temel sözdizimi aşağıdaki gibidir:

```bash
shopt [options] [option_name]
```

### Yaygın Seçenekler
- `-s` veya `--set`: Belirtilen seçeneği etkinleştirir.
- `-u` veya `--unset`: Belirtilen seçeneği devre dışı bırakır.
- `-p` veya `--print`: Tüm mevcut seçenekleri ve durumlarını listelemek için kullanılır.

## Examples
### Örnek 1: Seçenekleri Listeleme
Aşağıdaki komut, mevcut tüm `shopt` seçeneklerini ve durumlarını listeleyecektir:

```bash
shopt
```

### Örnek 2: Bir Seçeneği Etkinleştirme
Aşağıdaki komut, `cdspell` seçeneğini etkinleştirir. Bu seçenek, yanlış yazılmış `cd` komutlarını düzeltmek için kullanılır:

```bash
shopt -s cdspell
```

## Tips
- `shopt` komutunu kullanmadan önce mevcut seçeneklerinizi kontrol etmek, hangi seçeneklerin etkin olduğunu anlamanıza yardımcı olur.
- Özellikle sık kullandığınız seçenekleri `.bashrc` dosyanıza ekleyerek her oturumda otomatik olarak etkinleştirebilirsiniz.
- `shopt` ile etkinleştirilen seçeneklerin bazıları, kabuğun davranışını önemli ölçüde değiştirebilir, bu nedenle dikkatli kullanmak önemlidir.