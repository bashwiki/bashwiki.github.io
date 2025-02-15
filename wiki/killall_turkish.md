# [리눅스] Bash killall 사용법

## Overview
`killall` komutu, belirtilen bir süreç adını kullanarak sistemdeki tüm eşleşen süreçleri sonlandırmak için kullanılır. Bu komut, özellikle birden fazla örneği çalışan bir uygulamayı kapatmak istediğinizde oldukça faydalıdır. `killall`, süreçleri adlarına göre hedef alarak işlem yönetimini kolaylaştırır.

## Usage
`killall` komutunun temel sözdizimi aşağıdaki gibidir:

```bash
killall [seçenekler] süreç_adı
```

### Yaygın Seçenekler:
- `-9`: Bu seçenek, süreçleri zorla sonlandırmak için kullanılır. Normalde bir süreç, sonlandırılmadan önce temizleme işlemleri yapar, ancak `-9` ile bu işlemler atlanır.
- `-u kullanıcı_adı`: Belirtilen kullanıcıya ait süreçleri sonlandırmak için kullanılır.
- `-q`: Hata mesajlarını bastırmak için kullanılır. Eğer süreç bulunamazsa, bu seçenek ile hata mesajı gösterilmez.

## Examples
### Örnek 1: Belirli bir süreç adını sonlandırma
Aşağıdaki komut, "firefox" adındaki tüm süreçleri sonlandırır:

```bash
killall firefox
```

### Örnek 2: Zorla bir süreci sonlandırma
Eğer "myapp" adlı bir uygulama normal yollarla kapanmıyorsa, aşağıdaki komut ile zorla kapatabilirsiniz:

```bash
killall -9 myapp
```

## Tips
- `killall` komutunu kullanmadan önce, hangi süreçlerin çalıştığını görmek için `ps` veya `top` komutlarını kullanarak süreç listesini kontrol etmek iyi bir uygulamadır.
- Süreç adlarını tam olarak yazmak önemlidir; yanlış bir ad kullanmak, beklenmeyen süreçlerin kapatılmasına neden olabilir.
- Eğer yalnızca belirli bir kullanıcıya ait süreçleri sonlandırmak istiyorsanız, `-u` seçeneğini kullanarak hedefinizi daraltabilirsiniz.