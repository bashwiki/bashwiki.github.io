# [Linux] Bash tune2fs Kullanımı: Dosya sistemini ayarlamak için bir araç

## Overview
`tune2fs` komutu, Linux işletim sistemlerinde ext2, ext3 ve ext4 dosya sistemlerinin parametrelerini değiştirmek için kullanılır. Bu komut, dosya sisteminin performansını ve güvenliğini artırmak amacıyla çeşitli ayarların yapılmasına olanak tanır.

## Usage
Temel sözdizimi şu şekildedir:

```bash
tune2fs [seçenekler] [argümanlar]
```

## Common Options
- `-c <numara>`: Dosya sisteminin maksimum dosya sayısını ayarlar.
- `-i <süre>`: Dosya sisteminin kontrol aralığını belirler.
- `-m <yüzde>`: Kullanıcı alanının maksimum yüzdesini ayarlar.
- `-o <seçenekler>`: Dosya sistemi seçeneklerini ayarlamak için kullanılır.
- `-L <etiket>`: Dosya sistemine bir etiket atar.

## Common Examples
Aşağıda, `tune2fs` komutunun bazı yaygın kullanımları bulunmaktadır:

### 1. Dosya sisteminin maksimum dosya sayısını ayarlama
```bash
tune2fs -c 10000 /dev/sda1
```

### 2. Dosya sistemi kontrol aralığını değiştirme
```bash
tune2fs -i 2w /dev/sda1
```

### 3. Kullanıcı alanının maksimum yüzdesini ayarlama
```bash
tune2fs -m 5 /dev/sda1
```

### 4. Dosya sistemine etiket atama
```bash
tune2fs -L mylabel /dev/sda1
```

## Tips
- `tune2fs` komutunu kullanmadan önce dosya sisteminin yedeklemesini almayı unutmayın.
- Komutu çalıştırmadan önce dosya sisteminin montaj durumunu kontrol edin; montajda olan bir dosya sistemi üzerinde değişiklik yapmaktan kaçının.
- Değişikliklerin etkili olabilmesi için dosya sisteminin yeniden monte edilmesi gerekebilir.