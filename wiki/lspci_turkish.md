# [리눅스] Bash lspci 사용법

## Overview
`lspci`, Linux işletim sistemlerinde kullanılan bir komuttur ve sistemdeki PCI (Peripheral Component Interconnect) aygıtlarını listelemek için kullanılır. Bu komut, bilgisayar donanımının yapılandırmasını anlamak ve aygıtların özelliklerini incelemek amacıyla mühendisler ve geliştiriciler tarafından sıklıkla tercih edilir. `lspci`, sistemdeki tüm PCI aygıtlarının kimlik bilgilerini ve özelliklerini gösterir.

## Usage
`lspci` komutunun temel sözdizimi aşağıdaki gibidir:

```bash
lspci [seçenekler]
```

### Yaygın Seçenekler
- `-v`: Daha ayrıntılı bilgi gösterir.
- `-vv`: Çok daha ayrıntılı bilgi sağlar.
- `-k`: Aygıt sürücülerinin hangi sürücü tarafından kullanıldığını gösterir.
- `-n`: Aygıtların PCI kimlik numaralarını gösterir.
- `-s [bölüm]`: Belirtilen bölümdeki aygıtı listelemek için kullanılır.

## Examples
### Örnek 1: Tüm PCI Aygıtlarını Listeleme
Aşağıdaki komut, sistemdeki tüm PCI aygıtlarını listeleyecektir:

```bash
lspci
```

### Örnek 2: Ayrıntılı Bilgi Gösterme
Aşağıdaki komut, PCI aygıtları hakkında daha ayrıntılı bilgi almak için kullanılabilir:

```bash
lspci -v
```

## Tips
- `lspci` çıktısını daha okunabilir hale getirmek için `less` komutunu kullanabilirsiniz. Örneğin:

```bash
lspci | less
```

- Eğer belirli bir aygıt hakkında bilgi almak istiyorsanız, `-s` seçeneğini kullanarak o aygıtın bölüm numarasını belirtebilirsiniz. Bu, çıktıyı daha hedefli hale getirir.
- `lspci` komutunu kullanmadan önce, sistemde gerekli izinlerin olduğundan emin olun; bazı durumlarda, kök (root) erişimi gerekebilir.