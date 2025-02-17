# [Linux] Bash mv Kullanımı: Dosya ve dizin taşıma veya yeniden adlandırma

## Overview
`mv` komutu, dosyaları veya dizinleri taşımak veya yeniden adlandırmak için kullanılır. Bu komut, dosya sisteminde bir dosyanın yerini değiştirmek veya dosyanın adını değiştirmek için oldukça kullanışlıdır.

## Usage
Temel sözdizimi aşağıdaki gibidir:

```bash
mv [options] [arguments]
```

## Common Options
- `-i`: Hedef dosya mevcutsa, üzerine yazmadan önce kullanıcıdan onay ister.
- `-u`: Hedef dosya mevcutsa ve kaynak dosya daha yeni ise, dosyayı taşır.
- `-v`: Taşıma işlemi sırasında hangi dosyaların taşındığını gösterir.
- `-n`: Hedef dosya mevcutsa, üzerine yazmaz.

## Common Examples
Aşağıda `mv` komutunun bazı yaygın kullanım örnekleri bulunmaktadır:

### 1. Dosya Taşıma
Bir dosyayı başka bir dizine taşımak için:

```bash
mv dosya.txt /hedef/dizin/
```

### 2. Dosya Yeniden Adlandırma
Bir dosyanın adını değiştirmek için:

```bash
mv eski_ad.txt yeni_ad.txt
```

### 3. Dizin Taşıma
Bir dizini başka bir konuma taşımak için:

```bash
mv /kaynak/dizin/ /hedef/dizin/
```

### 4. Kullanıcı Onayı ile Taşıma
Mevcut dosyaların üzerine yazmadan önce onay almak için:

```bash
mv -i dosya.txt /hedef/dizin/
```

### 5. Taşıma İşlemi Detaylarını Görüntüleme
Taşıma işlemi sırasında hangi dosyaların taşındığını görmek için:

```bash
mv -v dosya.txt /hedef/dizin/
```

## Tips
- Taşıma işlemi yapmadan önce dosyaların yedeğini almak iyi bir uygulamadır.
- `-i` seçeneğini kullanarak yanlışlıkla dosyaların üzerine yazma riskini azaltabilirsiniz.
- Dizinleri taşırken, dizin yapısını korumak için dikkatli olun; yanlış bir taşıma işlemi dosya kaybına yol açabilir.