# [리눅스] Bash 7z 사용법

## Overview
`7z`, 7-Zip arşivleme yazılımının komut satırı sürümüdür. Bu komut, dosyaları sıkıştırmak, arşivlemek ve açmak için kullanılır. `7z`, yüksek sıkıştırma oranları ve çeşitli dosya formatlarını desteklemesi ile bilinir. Genellikle büyük dosyaların veya klasörlerin depolanması ve taşınması için idealdir.

## Usage
Temel `7z` komutunun sözdizimi şu şekildedir:

```bash
7z [seçenekler] [işlem] [arşiv dosyası] [dosyalar]
```

### Yaygın Seçenekler
- `a`: Arşiv oluşturur ve dosyaları ekler.
- `x`: Arşivi çıkarır.
- `l`: Arşiv içeriğini listeler.
- `d`: Arşivden dosyaları siler.
- `t`: Arşivin bütünlüğünü test eder.

## Examples

### Örnek 1: Dosya Sıkıştırma
Aşağıdaki komut, `dosya.txt` adlı dosyayı `arşiv.7z` adlı bir arşiv dosyasına sıkıştırır:

```bash
7z a arşiv.7z dosya.txt
```

### Örnek 2: Arşivden Dosya Çıkarma
Aşağıdaki komut, `arşiv.7z` adlı arşiv dosyasını çıkarır:

```bash
7z x arşiv.7z
```

## Tips
- Sıkıştırma oranını artırmak için `-mx=9` seçeneğini kullanabilirsiniz. Bu, en yüksek sıkıştırma seviyesini ayarlar. Örneğin:

```bash
7z a -mx=9 arşiv.7z dosya.txt
```

- Arşiv içeriğini listelemek için `l` seçeneğini kullanarak arşivdeki dosyaları hızlıca görebilirsiniz:

```bash
7z l arşiv.7z
```

- Büyük dosyalarla çalışırken, işlem süresini ve sistem kaynaklarını göz önünde bulundurun. Gereksiz dosyaları arşivden çıkarmak veya silmek, yer tasarrufu sağlar.