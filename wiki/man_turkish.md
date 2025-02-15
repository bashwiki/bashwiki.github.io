# [리눅스] Bash man 사용법

## Overview
`man` komutu, Linux ve Unix benzeri işletim sistemlerinde kullanılan bir komuttur. Bu komut, kullanıcıların sistemdeki komutlar, sistem çağrıları, dosya formatları ve diğer önemli konular hakkında bilgi almasını sağlar. `man`, "manual" kelimesinin kısaltmasıdır ve genellikle bir komutun nasıl kullanılacağına dair detaylı belgeleri görüntülemek için kullanılır.

## Usage
`man` komutunun temel kullanımı oldukça basittir. Aşağıda temel sözdizimi ve yaygın seçenekler verilmiştir:

### Temel Sözdizimi
```
man [seçenekler] [komut]
```

### Yaygın Seçenekler
- `-k`: Anahtar kelime ile arama yapar. Belirtilen anahtar kelime ile ilgili tüm `man` sayfalarını listeler.
- `-f`: Belirtilen komutun kısa bir açıklamasını gösterir.
- `-a`: Belirtilen komut için tüm `man` sayfalarını sırayla görüntüler.

## Examples
### Örnek 1: Bir Komutun Manuel Sayfasını Görüntüleme
Aşağıdaki komut, `ls` komutunun manuel sayfasını görüntüler:
```bash
man ls
```

### Örnek 2: Anahtar Kelime ile Arama
Aşağıdaki komut, "copy" anahtar kelimesi ile ilgili tüm `man` sayfalarını listeler:
```bash
man -k copy
```

## Tips
- `man` sayfalarını gezmek için yön tuşlarını kullanabilir veya `Space` tuşu ile sayfayı aşağı kaydırabilirsiniz. `q` tuşuna basarak çıkabilirsiniz.
- `man` sayfalarında daha fazla bilgi bulmak için, sayfanın üst kısmında genellikle "SEE ALSO" bölümü bulunur. Bu bölümde ilgili diğer komutlar hakkında bilgi alabilirsiniz.
- `man` sayfalarını daha iyi anlamak için, belirli bir komutun argümanları ve seçenekleri hakkında bilgi almayı unutmayın. Bu, komutları etkili bir şekilde kullanmanıza yardımcı olacaktır.