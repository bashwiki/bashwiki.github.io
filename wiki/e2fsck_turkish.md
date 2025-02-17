# [Linux] Bash e2fsck Kullanımı: Dosya sistemini kontrol etme ve onarma

## Genel Bakış
e2fsck, Linux tabanlı dosya sistemlerinde kullanılan bir komuttur. Bu komut, dosya sisteminin tutarlılığını kontrol eder ve gerektiğinde onarır. Genellikle, dosya sisteminde bir hata meydana geldiğinde veya sistem düzgün bir şekilde kapatılmadığında kullanılır.

## Kullanım
Temel sözdizimi aşağıdaki gibidir:

```
e2fsck [seçenekler] [argümanlar]
```

## Yaygın Seçenekler
- `-p`: Hızlı bir kontrol yapar ve otomatik onarımlar gerçekleştirir.
- `-f`: Dosya sistemini zorla kontrol eder, hata ayıklama için kullanışlıdır.
- `-n`: Onarım yapmadan sadece kontrol eder, değişiklik yapmaz.
- `-y`: Tüm onarım isteklerini otomatik olarak "evet" olarak yanıtlar.

## Yaygın Örnekler
Aşağıda e2fsck komutunun bazı pratik örnekleri bulunmaktadır:

1. **Basit Kontrol**: Bir dosya sistemini kontrol etmek için.
   ```bash
   e2fsck /dev/sda1
   ```

2. **Otomatik Onarım**: Hataları otomatik olarak onarmak için.
   ```bash
   e2fsck -p /dev/sda1
   ```

3. **Zorla Kontrol**: Dosya sistemini zorla kontrol etmek için.
   ```bash
   e2fsck -f /dev/sda1
   ```

4. **Sadece Kontrol**: Değişiklik yapmadan dosya sistemini kontrol etmek için.
   ```bash
   e2fsck -n /dev/sda1
   ```

5. **Tüm Onarımları Kabul Et**: Tüm onarım isteklerini otomatik olarak kabul etmek için.
   ```bash
   e2fsck -y /dev/sda1
   ```

## İpuçları
- e2fsck komutunu kullanmadan önce dosya sisteminin montajda olmadığından emin olun; aksi takdirde, veri kaybı yaşanabilir.
- Düzenli olarak dosya sisteminizi kontrol etmek, olası sorunları önceden tespit etmenize yardımcı olur.
- Eğer büyük bir dosya sisteminde çalışıyorsanız, işlemin tamamlanması zaman alabilir; bu nedenle sabırlı olun.