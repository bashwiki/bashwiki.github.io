# [리눅스] Bash history 사용법

## Overview
`history` komutu, Bash kabuğunda daha önce çalıştırılan komutların bir listesini görüntülemek için kullanılır. Bu komut, kullanıcıların geçmişteki komutlarını hızlı bir şekilde gözden geçirmesine ve gerektiğinde tekrar kullanmasına olanak tanır. `history`, özellikle sık kullanılan komutları hatırlamak veya tekrar çalıştırmak isteyen mühendisler ve geliştiriciler için oldukça faydalıdır.

## Usage
Temel `history` komutunun sözdizimi şu şekildedir:

```bash
history [n]
```

Burada `n`, görüntülemek istediğiniz komut sayısını belirtir. Eğer `n` verilmezse, tüm geçmiş komutları gösterir. Ayrıca, bazı yaygın seçenekler şunlardır:

- `-c`: Geçmişi temizler.
- `-d offset`: Belirtilen offset'teki komutu geçmişten siler.

## Examples
### Örnek 1: Tüm Geçmişi Görüntüleme
Tüm geçmiş komutlarını görüntülemek için `history` komutunu şu şekilde kullanabilirsiniz:

```bash
history
```

Bu komut, geçmişte çalıştırdığınız tüm komutları numaralandırarak listeleyecektir.

### Örnek 2: Son 5 Komutu Görüntüleme
Son 5 komutu görüntülemek için `n` parametresini kullanabilirsiniz:

```bash
history 5
```

Bu komut, yalnızca en son çalıştırdığınız 5 komutu gösterecektir.

## Tips
- Geçmişteki komutları hızlı bir şekilde tekrar çalıştırmak için, komut numarasını kullanarak `!n` şeklinde bir komut yazabilirsiniz. Örneğin, `!100` yazarsanız, geçmişteki 100 numaralı komut tekrar çalıştırılır.
- Geçmişi temizlemek için `history -c` komutunu kullanarak tüm geçmişinizi silebilirsiniz. Ancak, bu işlemi yapmadan önce dikkatli olun, çünkü bu işlem geri alınamaz.
- Geçmiş komutlarınızı daha iyi yönetmek için, `.bash_history` dosyasını inceleyebilir veya düzenleyebilirsiniz. Bu dosya, geçmiş komutlarınızı saklar ve gerektiğinde erişim sağlar.