# [리눅스] Bash chmod 사용법

## Overview
`chmod` (change mode) komutu, Unix ve Linux tabanlı işletim sistemlerinde dosya ve dizinlerin erişim izinlerini değiştirmek için kullanılır. Bu komut, kullanıcıların dosyalara veya dizinlere kimlerin erişebileceğini ve bu erişimlerin ne tür işlemlerle sınırlı olduğunu belirlemelerine olanak tanır. `chmod`, dosya sahipleri, gruplar ve diğer kullanıcılar için okuma, yazma ve çalıştırma izinlerini ayarlamak amacıyla kullanılır.

## Usage
Temel `chmod` sözdizimi şu şekildedir:

```bash
chmod [seçenekler] izinler dosya_adı
```

### Yaygın Seçenekler
- `u`: Dosya sahibi (user)
- `g`: Dosya grubuna ait kullanıcılar (group)
- `o`: Diğer kullanıcılar (others)
- `a`: Tüm kullanıcılar (all)
- `r`: Okuma izni (read)
- `w`: Yazma izni (write)
- `x`: Çalıştırma izni (execute)

İzinleri ayarlamak için iki ana yöntem vardır:
1. **Sembolik Notasyon**: İzinleri `+`, `-`, `=` operatörleri ile ayarlamak.
2. **Sayısal Notasyon**: İzinleri 3 basamaklı bir sayı ile belirtmek (örneğin, 755).

## Examples
### Örnek 1: Sembolik Notasyon Kullanarak İzin Verme
Aşağıdaki komut, `myfile.txt` dosyasına tüm kullanıcılara okuma ve çalıştırma izni verir:

```bash
chmod a+rx myfile.txt
```

### Örnek 2: Sayısal Notasyon Kullanarak İzin Ayarlama
Aşağıdaki komut, `myfolder` dizinine sahibi için tam izin (okuma, yazma, çalıştırma), grup için okuma ve çalıştırma, diğer kullanıcılar için ise sadece okuma izni verir:

```bash
chmod 755 myfolder
```

## Tips
- İzinleri ayarlarken dikkatli olun; yanlış izinler, dosyalarınıza veya sisteminize zarar verebilir.
- `ls -l` komutunu kullanarak dosya ve dizinlerin mevcut izinlerini kontrol edebilirsiniz.
- İzinleri değiştirmeden önce dosyanın yedeğini almak iyi bir uygulamadır.
- `chmod` komutunu kullanırken, hangi kullanıcı grubunun izinlerini değiştirdiğinizi net bir şekilde belirleyin.