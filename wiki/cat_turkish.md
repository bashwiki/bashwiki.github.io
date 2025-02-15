# [리눅스] Bash cat 사용법

## Overview
`cat` komutu, Unix ve Linux sistemlerinde dosyaların içeriğini görüntülemek, birleştirmek veya yeni dosyalar oluşturmak için kullanılan bir komuttur. Adı "concatenate" kelimesinin kısaltmasıdır. Genellikle metin dosyalarını okuma ve birleştirme amacıyla kullanılır.

## Usage
`cat` komutunun temel sözdizimi aşağıdaki gibidir:

```bash
cat [seçenekler] [dosya_adı...]
```

### Yaygın Seçenekler:
- `-n`: Satır numaralarını gösterir.
- `-b`: Boş olmayan satırları numaralandırır.
- `-E`: Satır sonlarını `$` ile gösterir.
- `-s`: Ardışık boş satırları birleştirir.

## Examples
### Örnek 1: Bir dosyanın içeriğini görüntüleme
Aşağıdaki komut, `dosya.txt` adlı dosyanın içeriğini terminalde görüntüler:

```bash
cat dosya.txt
```

### Örnek 2: Birden fazla dosyayı birleştirme
İki dosyanın içeriğini birleştirip yeni bir dosya oluşturmak için:

```bash
cat dosya1.txt dosya2.txt > birlesik_dosya.txt
```

Bu komut, `dosya1.txt` ve `dosya2.txt` dosyalarının içeriğini alır ve `birlesik_dosya.txt` adlı yeni bir dosyaya yazar.

## Tips
- `cat` komutunu büyük dosyalarla kullanırken, dosya içeriği terminalde kaybolabilir. Bunun yerine `less` veya `more` komutları ile birlikte kullanmak daha iyi bir deneyim sağlayabilir.
- `cat` komutunu, dosya içeriğini hızlıca kontrol etmek için kullanırken, `-n` seçeneği ile satır numaralarını görüntülemek, hangi satırda olduğunuzu takip etmenize yardımcı olabilir.
- Dosyaları birleştirirken, dosya sırasına dikkat edin; ilk dosya önce, ikinci dosya sonra yazılacaktır.