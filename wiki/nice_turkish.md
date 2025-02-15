# [리눅스] Bash nice 사용법

## Overview
`nice` komutu, Unix ve Unix benzeri işletim sistemlerinde, bir işlemin CPU zaman payını ayarlamak için kullanılır. Bu komut, bir işlemin önceliğini değiştirmeye yarar; böylece daha yüksek veya daha düşük öncelikli işlemler arasında CPU kaynaklarının nasıl dağıtılacağını kontrol edebilirsiniz. `nice`, sistemin genel performansını optimize etmeye yardımcı olur, özellikle de kaynak yoğun işlemler çalıştırıldığında.

## Usage
Temel `nice` komutunun sözdizimi şu şekildedir:

```bash
nice [seviye] [komut]
```

- **seviye**: İşlemin önceliğini belirten bir tam sayıdır. Bu değer -20 ile 19 arasında olabilir. -20 en yüksek önceliği, 19 ise en düşük önceliği temsil eder. Varsayılan değer 0'dır.
- **komut**: Önceliği ayarlanacak olan çalıştırılacak komuttur.

### Yaygın Seçenekler
- `-n, --adjustment`: Öncelik seviyesini ayarlamak için kullanılır. Bu seçenek ile `seviye` değerini belirtebilirsiniz.
- `-h, --help`: `nice` komutunun kullanımına dair yardım bilgilerini gösterir.
- `-V, --version`: `nice` komutunun sürüm bilgisini gösterir.

## Examples
### Örnek 1: Varsayılan öncelikle bir komut çalıştırma
Aşağıdaki komut, varsayılan öncelikle `my_script.sh` adlı bir betiği çalıştırır:

```bash
nice ./my_script.sh
```

### Örnek 2: Düşük öncelikle bir komut çalıştırma
Aşağıdaki komut, `my_script.sh` betiğini 10 öncelik seviyesinde çalıştırır:

```bash
nice -n 10 ./my_script.sh
```

Bu durumda, `my_script.sh` betiği, diğer işlemlerle kıyaslandığında daha düşük bir öncelik alır ve sistem kaynaklarını daha az kullanır.

## Tips
- `nice` komutunu kullanırken, yüksek öncelikli işlemlerin sistem performansını olumsuz etkileyebileceğini unutmayın. Bu nedenle, öncelik ayarlamalarını dikkatli yapmalısınız.
- Eğer bir işlemi daha yüksek öncelikle çalıştırmak istiyorsanız, `nice` yerine `renice` komutunu kullanarak mevcut bir işlemin önceliğini değiştirebilirsiniz.
- `nice` komutunu arka planda çalışan işlemler için kullanmak, sistemin yanıt verme süresini artırabilir. Özellikle uzun süreli çalışan işlemlerde bu yaklaşım faydalı olabilir.