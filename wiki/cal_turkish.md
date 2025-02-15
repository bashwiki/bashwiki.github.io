# [리눅스] Bash cal 사용법

## Overview
`cal` komutu, belirli bir ay veya yıl için takvim görüntülemek amacıyla kullanılan bir Bash komutudur. Kullanıcıların tarihleri hızlı bir şekilde görselleştirmesine olanak tanır. Bu komut, özellikle tarih ve zaman ile çalışan mühendisler ve geliştiriciler için faydalıdır.

## Usage
`cal` komutunun temel sözdizimi aşağıdaki gibidir:

```bash
cal [ay] [yıl]
```

### Ortak Seçenekler
- `-m`: Ayları baştan sona kadar yan yana gösterir.
- `-3`: Mevcut ayın yanı sıra bir önceki ve bir sonraki ayı da gösterir.
- `-y`: Belirtilen yılı takvim olarak gösterir.
- `-j`: Yılın gün numaralarını gösterir.

## Examples
### Örnek 1: Mevcut Ayın Takvimi
Mevcut ayın takvimini görüntülemek için sadece `cal` komutunu kullanabilirsiniz:

```bash
cal
```

### Örnek 2: Belirli Bir Ay ve Yılın Takvimi
Örneğin, 2023 yılının Ekim ayının takvimini görüntülemek için:

```bash
cal 10 2023
```

### Örnek 3: Üç Aylık Görüntüleme
Mevcut ayın yanı sıra bir önceki ve bir sonraki ayı göstermek için:

```bash
cal -3
```

## Tips
- `cal` komutunu sık kullananlar için, belirli bir ay veya yıl için takvim görüntülemek üzere bir alias oluşturmak faydalı olabilir.
- Takvim çıktısını daha iyi görmek için çıktıyı bir dosyaya yönlendirebilir veya `less` gibi bir sayfalayıcı ile görüntüleyebilirsiniz. Örneğin:

```bash
cal | less
```

- `cal` komutunu, tarih hesaplamaları veya zaman yönetimi uygulamalarında kullanarak, belirli tarihler arasındaki gün sayısını bulmak için bir temel olarak kullanabilirsiniz.