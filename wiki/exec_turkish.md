# [리눅스] Bash exec 사용법

## Overview
`exec` komutu, mevcut shell'in yerini başka bir programla değiştirmek için kullanılır. Bu komut, yeni bir işlem başlatır ve mevcut shell sürecini sonlandırır. `exec`, genellikle bir script içinde başka bir programı çalıştırmak ve scriptin geri kalan kısmını atlamak için kullanılır. Bu sayede, yeni program çalıştığında mevcut shell süreci kapatılır ve sistem kaynakları daha verimli bir şekilde kullanılır.

## Usage
Temel sözdizimi şu şekildedir:

```bash
exec [seçenekler] komut [argümanlar]
```

### Yaygın Seçenekler
- `-a`: Belirtilen komutun alternatif bir isimle çalıştırılmasını sağlar.
- `-l`: Yeni bir login shell başlatır.
- `-p`: Yeni bir işlem oluştururken mevcut ortamı korur.

## Examples
### Örnek 1: Basit bir program çalıştırma
Aşağıdaki komut, mevcut shell sürecini `bash` ile değiştirir:

```bash
exec bash
```

Bu komut çalıştırıldığında, mevcut shell kapanır ve yeni bir `bash` shell başlatılır.

### Örnek 2: Bir script içinde `exec` kullanma
Bir script içinde başka bir program çalıştırmak için `exec` kullanabilirsiniz:

```bash
#!/bin/bash
echo "Bu mesajı göreceksiniz."
exec ls -l
echo "Bu mesajı göremezsiniz."
```

Yukarıdaki script çalıştırıldığında, `ls -l` komutu çalıştırılır ve scriptin geri kalan kısmı atlanır.

## Tips
- `exec` komutunu kullanırken dikkatli olun, çünkü mevcut shell sürecini kapatır ve geri dönmek mümkün olmayabilir.
- `exec` ile çalıştırılan programın çıktısını yönlendirmek için `>` veya `>>` gibi yönlendirme operatörlerini kullanabilirsiniz.
- `exec` komutunu, shell scriptlerinizde performansı artırmak için kullanabilirsiniz, çünkü yeni bir shell başlatmak yerine mevcut shell'i değiştirmiş olursunuz.