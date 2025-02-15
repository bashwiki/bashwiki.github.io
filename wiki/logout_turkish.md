# [리눅스] Bash logout 사용법

## Overview
`logout` komutu, bir kullanıcı oturumunu sonlandırmak için kullanılan bir Bash komutudur. Genellikle bir terminal oturumunu kapatmak istediğinizde veya bir shell oturumundan çıkmak istediğinizde kullanılır. Bu komut, özellikle bir kullanıcı shell oturumunu kapatmak için tasarlanmıştır ve genellikle bir oturum açma işlemi sırasında kullanılan shell'lerde (örneğin, login shell) etkilidir.

## Usage
Temel kullanım şekli oldukça basittir. `logout` komutunu terminalde yazmanız yeterlidir:

```bash
logout
```

Bu komut, mevcut oturumu kapatır ve kullanıcıyı shell'den çıkarır. `logout` komutu, genellikle bir login shell'de kullanılmalıdır; aksi takdirde, "logout" hatası alabilirsiniz.

## Examples
### Örnek 1: Basit Oturum Kapatma
Bir terminal penceresinde, oturumu kapatmak için aşağıdaki komutu yazabilirsiniz:

```bash
logout
```

Bu komut, mevcut oturumu kapatacak ve terminal penceresini kapatacaktır.

### Örnek 2: Oturum Kapatma ile Script Kullanımı
Eğer bir script içinde oturumu kapatmak istiyorsanız, `logout` komutunu şu şekilde kullanabilirsiniz:

```bash
#!/bin/bash
echo "Oturum kapatılıyor..."
logout
```

Bu script çalıştırıldığında, "Oturum kapatılıyor..." mesajını gösterir ve ardından oturumu kapatır.

## Tips
- `logout` komutunu kullanmadan önce, kaydedilmemiş işlerinizi kaydettiğinizden emin olun. Oturum kapatıldığında, açık olan tüm işlemler sonlanacaktır.
- `logout` komutunu yalnızca login shell'lerde kullanmaya dikkat edin. Eğer bir non-login shell'de kullanırsanız, hata mesajı alabilirsiniz.
- Terminal oturumlarınızı yönetmek için `exit` komutunu da kullanabilirsiniz; ancak `logout`, özellikle login shell'lerde daha uygun bir seçimdir.