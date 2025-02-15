# [리눅스] Bash e2fsck 사용법

## Overview
`e2fsck`, Linux işletim sistemlerinde kullanılan bir dosya sistemi kontrol aracıdır. Özellikle ext2, ext3 ve ext4 dosya sistemleri için tasarlanmıştır. Bu komut, dosya sistemindeki hataları tespit etmek ve düzeltmek için kullanılır. Disk hatalarını gidermek, dosya sisteminin bütünlüğünü sağlamak ve veri kaybını önlemek amacıyla düzenli olarak çalıştırılması önerilir.

## Usage
`e2fsck` komutunun temel sözdizimi aşağıdaki gibidir:

```bash
e2fsck [seçenekler] <dosya_sistemi>
```

### Yaygın Seçenekler
- `-p`: Hataları otomatik olarak düzeltir. Kullanıcıdan onay istemez.
- `-f`: Dosya sistemini zorla kontrol eder, her zaman kontrol işlemi yapar.
- `-n`: Hataları düzeltmeden sadece kontrol eder. Değişiklik yapmaz.
- `-y`: Tüm hataları otomatik olarak düzeltir, kullanıcıdan onay istemez.

## Examples
### Örnek 1: Dosya Sistemini Kontrol Etme
Aşağıdaki komut, `/dev/sda1` dosya sistemini kontrol eder ve hataları düzeltmeye çalışır:

```bash
sudo e2fsck /dev/sda1
```

### Örnek 2: Otomatik Düzeltme ile Kontrol Etme
Aşağıdaki komut, `/dev/sda1` dosya sistemini kontrol eder ve bulunan hataları otomatik olarak düzeltir:

```bash
sudo e2fsck -p /dev/sda1
```

## Tips
- `e2fsck` komutunu çalıştırmadan önce dosya sisteminin montajlı olmadığından emin olun. Montajlı bir dosya sisteminde çalıştırmak, veri kaybına neden olabilir.
- Düzenli aralıklarla dosya sisteminizi kontrol etmek, olası hataların önüne geçmek için iyi bir uygulamadır.
- Eğer dosya sisteminizde ciddi hatalar varsa, yedekleme yapmayı unutmayın. `e2fsck` bazı durumlarda veri kaybına yol açabilir.