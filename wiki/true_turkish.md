# [리눅스] Bash true 사용법

## Overview
`true` komutu, her zaman başarılı bir çıkış durumu (exit status) döndüren basit bir Bash komutudur. Temel amacı, bir komutun başarılı bir şekilde çalıştığını belirtmektir. Genellikle, koşullu ifadelerde veya döngülerde bir "do nothing" (hiçbir şey yapma) komutu olarak kullanılır. `true`, bir komut dosyasında veya bir betikte belirli bir koşulun her zaman doğru olduğu durumlarda yararlıdır.

## Usage
`true` komutunun temel sözdizimi oldukça basittir:

```bash
true
```

Bu komut, herhangi bir seçenek veya argüman almaz. Çalıştırıldığında, çıkış durumu 0 (başarılı) olarak döner.

## Examples
### Örnek 1: Basit Kullanım
Aşağıdaki komut, `true` komutunu çalıştırır ve çıkış durumunu kontrol eder:

```bash
true
echo $?
```

Bu komut çalıştırıldığında, `echo $?` ifadesi 0 değerini döndürecektir, bu da `true` komutunun başarılı bir şekilde çalıştığını gösterir.

### Örnek 2: Koşullu İfade ile Kullanım
`true` komutunu bir koşul ifadesinde kullanarak, belirli bir durumda hiçbir şey yapmamak için kullanabilirsiniz:

```bash
if true; then
    echo "Bu her zaman çalışır."
fi
```

Bu komut çalıştırıldığında, "Bu her zaman çalışır." mesajı ekrana yazdırılacaktır.

## Tips
- `true` komutunu, bir komut dosyasında veya betikte belirli bir koşulun her zaman doğru olduğu durumlarda kullanarak, kodunuzu daha okunabilir hale getirebilirsiniz.
- `true` komutunu, bir döngü içinde koşul olarak kullanarak sonsuz döngüler oluşturabilirsiniz, ancak dikkatli olun; bu, sistem kaynaklarını tüketebilir.
- `true` komutu, test veya hata ayıklama sırasında geçici olarak bir komutun yerini almak için de kullanılabilir.