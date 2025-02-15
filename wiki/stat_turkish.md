# [리눅스] Bash stat 사용법

## Overview
`stat` komutu, bir dosyanın veya dizinin dosya sistemindeki durumunu ve özelliklerini gösterir. Bu komut, dosyanın boyutu, oluşturulma tarihi, son erişim tarihi, izinler ve diğer önemli bilgileri içeren ayrıntılı bir çıktı sağlar. Geliştiriciler ve sistem yöneticileri için dosya yönetimi ve analizinde oldukça yararlıdır.

## Usage
`stat` komutunun temel sözdizimi şu şekildedir:

```bash
stat [seçenekler] [dosya_adı]
```

### Yaygın Seçenekler
- `-c` veya `--format`: Çıktıyı özel bir formatta gösterir. Format belirteçleri kullanarak çıktıyı özelleştirebilirsiniz.
- `-f` veya `--file-system`: Dosya sisteminin durumunu gösterir.
- `--help`: Komutun kullanımına dair yardım bilgilerini gösterir.
- `--version`: `stat` komutunun sürüm bilgilerini gösterir.

## Examples
### Örnek 1: Basit Kullanım
Aşağıdaki komut, `example.txt` dosyasının durumunu gösterir:

```bash
stat example.txt
```

Bu komut, dosyanın boyutu, izinleri, oluşturulma tarihi ve diğer bilgileri içeren bir çıktı verecektir.

### Örnek 2: Özel Format Kullanımı
Aşağıdaki komut, sadece dosyanın boyutunu ve son erişim tarihini gösterecek şekilde çıktıyı özelleştirir:

```bash
stat -c "Boyut: %s bytes, Son Erişim: %y" example.txt
```

Bu komut, `example.txt` dosyasının boyutunu ve son erişim tarihini belirttiğiniz formatta gösterir.

## Tips
- `stat` komutunu sıkça kullandığınız dosyalar için bir alias oluşturabilirsiniz. Örneğin, `alias s='stat -c "%s bytes, %y"'` komutunu kullanarak `s example.txt` şeklinde hızlı bir şekilde dosya bilgilerini alabilirsiniz.
- Dosya sisteminin durumunu kontrol etmek için `stat -f` seçeneğini kullanarak daha geniş bir perspektif elde edebilirsiniz.
- Çıktıyı bir dosyaya yönlendirmek için `>` operatörünü kullanarak sonuçları kaydedebilirsiniz. Örneğin: `stat example.txt > example_stat.txt`.