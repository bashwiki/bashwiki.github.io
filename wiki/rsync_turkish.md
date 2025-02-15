# [리눅스] Bash rsync 사용법

## Overview
`rsync`, dosya ve dizinleri yerel veya uzak sistemler arasında senkronize etmek için kullanılan bir komut satırı aracıdır. Özellikle büyük dosya transferlerinde verimlilik sağlamak için tasarlanmıştır. `rsync`, yalnızca değişen veya yeni dosyaları kopyalayarak zaman ve bant genişliği tasarrufu sağlar. Ayrıca, dosya izinleri, zaman damgaları ve sembolik bağlantılar gibi dosya özelliklerini de korur.

## Usage
Temel `rsync` komutunun sözdizimi şu şekildedir:

```bash
rsync [seçenekler] kaynak hedef
```

### Yaygın Seçenekler
- `-a`: Arşiv modu; dosya izinleri, zaman damgaları ve sembolik bağlantılar dahil olmak üzere tüm dosya özelliklerini korur.
- `-v`: Ayrıntılı çıktı; işlem sırasında hangi dosyaların kopyalandığını gösterir.
- `-z`: Verileri sıkıştırarak transfer eder; bu, ağ üzerinden transfer edilen dosyaların boyutunu azaltır.
- `-r`: Alt dizinleri de kopyalar; bu seçenek, dizinleri ve alt dizinlerini kopyalamak için kullanılır.
- `--delete`: Hedef dizinde, kaynak dizinde olmayan dosyaları siler; bu, iki dizinin tam olarak senkronize olmasını sağlar.

## Examples
### Örnek 1: Yerel Dosyaları Senkronize Etme
Aşağıdaki komut, `kaynak_dizin` içindeki tüm dosyaları `hedef_dizin`e senkronize eder:

```bash
rsync -av kaynak_dizin/ hedef_dizin/
```

### Örnek 2: Uzak Sunucuya Dosya Gönderme
Aşağıdaki komut, yerel `dosya.txt` dosyasını `kullanici@sunucu:/hedef_dizin/` adresine kopyalar:

```bash
rsync -avz dosya.txt kullanici@sunucu:/hedef_dizin/
```

## Tips
- `rsync` kullanırken, kaynak ve hedef dizinlerin sonuna `/` eklemeyi unutmayın. Bu, `rsync`'in yalnızca içeriği kopyalamasını sağlar.
- Büyük dosya transferleri yaparken, `-z` seçeneğini kullanarak veri sıkıştırmasını etkinleştirmek, bant genişliği tasarrufu sağlar.
- `--dry-run` seçeneği ile işlemin ne olacağını önceden görebilir, bu sayede yanlışlık yapma riskini azaltabilirsiniz. Örneğin:

```bash
rsync -av --dry-run kaynak_dizin/ hedef_dizin/
```

Bu komut, dosyaların hangi dosyaların kopyalanacağını gösterir, ancak gerçek bir transfer gerçekleştirmez.