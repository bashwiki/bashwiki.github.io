# [Linux] Bash lsblk Kullanımı: Disk ve Bölüm Bilgilerini Listeleme

## Overview
`lsblk` komutu, sistemdeki blok aygıtlarını (diskler, bölümler, vb.) listelemek için kullanılır. Bu komut, aygıtların yapısını ve özelliklerini görsel olarak sunarak kullanıcıların disk yönetimini kolaylaştırır.

## Usage
Temel kullanım sözdizimi aşağıdaki gibidir:

```bash
lsblk [options] [arguments]
```

## Common Options
- `-a` veya `--all`: Tüm aygıtları, boş olanlar da dahil olmak üzere gösterir.
- `-f` veya `--fs`: Dosya sistemi bilgilerini gösterir.
- `-l` veya `--list`: Liste formatında çıktı verir.
- `-o` veya `--output`: Görüntülenecek sütunları belirler.
- `-p` veya `--paths`: Aygıtların tam yollarını gösterir.

## Common Examples
Aşağıda `lsblk` komutunun bazı yaygın kullanım örnekleri bulunmaktadır:

### 1. Tüm blok aygıtlarını listeleme
```bash
lsblk
```

### 2. Dosya sistemi bilgileri ile listeleme
```bash
lsblk -f
```

### 3. Liste formatında çıktı alma
```bash
lsblk -l
```

### 4. Belirli sütunları görüntüleme
```bash
lsblk -o NAME,SIZE,TYPE,MOUNTPOINT
```

### 5. Tüm aygıtları, boş olanlar dahil gösterme
```bash
lsblk -a
```

## Tips
- `lsblk` çıktısını daha okunabilir hale getirmek için `column` komutunu kullanabilirsiniz:
  ```bash
  lsblk | column -t
  ```
- Disklerinizi düzenli olarak kontrol etmek için `lsblk` komutunu bir betik içinde kullanabilirsiniz.
- Çıktıyı bir dosyaya yönlendirmek için `>` operatörünü kullanarak bilgileri kaydedebilirsiniz:
  ```bash
  lsblk > disk_bilgileri.txt
  ``` 

Bu bilgilerle `lsblk` komutunu etkili bir şekilde kullanarak sisteminizdeki disk ve bölüm bilgilerini kolayca yönetebilirsiniz.