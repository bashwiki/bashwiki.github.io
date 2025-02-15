# [리눅스] Bash blkid 사용법

## Overview
`blkid` komutu, Linux sistemlerinde blok aygıtlarının (diskler, bölümler vb.) kimlik bilgilerini görüntülemek için kullanılır. Bu komut, aygıtların dosya sistemleri, UUID'leri (Evrensel Benzersiz Tanımlayıcılar) ve diğer önemli bilgileri hakkında bilgi sağlar. Genellikle sistem yöneticileri ve geliştiriciler, disk yapılandırmalarını kontrol etmek ve dosya sistemlerini yönetmek için bu komutu kullanır.

## Usage
`blkid` komutunun temel sözdizimi aşağıdaki gibidir:

```bash
blkid [seçenekler] [aygıt]
```

### Yaygın Seçenekler
- `-o, --output`: Çıktı formatını belirler. Örneğin, `value`, `full`, `list` gibi değerler alabilir.
- `-s, --match-tag`: Belirli bir etikete (örneğin, UUID veya LABEL) göre filtreleme yapar.
- `-p, --probe`: Aygıtın dosya sistemini tanımlamak için probe işlemi yapar.
- `-c, --cache`: Önbellek dosyasını kullanarak daha hızlı sonuçlar almanızı sağlar.

## Examples
### Örnek 1: Tüm blok aygıtlarını listeleme
Aşağıdaki komut, sistemdeki tüm blok aygıtlarının kimlik bilgilerini listeler:

```bash
blkid
```

Bu komut, her bir aygıt için UUID, dosya sistemi türü ve diğer bilgileri gösterir.

### Örnek 2: Belirli bir aygıtın bilgilerini görüntüleme
Aşağıdaki komut, `/dev/sda1` aygıtının bilgilerini görüntüler:

```bash
blkid /dev/sda1
```

Bu komut, yalnızca belirtilen aygıtın kimlik bilgilerini döndürür.

## Tips
- `blkid` komutunu çalıştırmadan önce, sistemdeki aygıtların güncel olduğundan emin olun. Bunun için `lsblk` veya `fdisk -l` gibi komutları kullanabilirsiniz.
- Çıktıyı daha okunabilir hale getirmek için `grep` veya `awk` gibi araçlarla birleştirebilirsiniz. Örneğin, yalnızca UUID'leri listelemek için:

```bash
blkid | grep UUID
```
- `blkid` komutunu root yetkileriyle çalıştırmak, bazı aygıtlara erişim sağlamak için gerekebilir. Bu durumda `sudo` kullanmayı unutmayın.